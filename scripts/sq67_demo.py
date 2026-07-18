#!/usr/bin/env python3
"""Public-safe SQ67 receipt demo.

This script does not read private Codex state files. It creates a small local
SQLite receipt ledger that demonstrates the public SQ67 pattern:

write marker -> hash proof -> recover later -> verify chain.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA = """
CREATE TABLE IF NOT EXISTS receipts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  nonce TEXT NOT NULL UNIQUE,
  lane TEXT NOT NULL,
  task TEXT NOT NULL,
  claim TEXT NOT NULL,
  evidence_json TEXT NOT NULL,
  boundary TEXT NOT NULL,
  next_gate TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  payload_sha256 TEXT NOT NULL,
  prev_sha256 TEXT,
  receipt_sha256 TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_receipts_nonce ON receipts(nonce);
"""


DEMO_ROWS = [
    {
        "nonce": "SQ67_PUBLIC_DEMO_A001",
        "lane": "sq67_clean",
        "task": "extract_facts",
        "claim": "receipt writer created a durable marker",
        "evidence": ["nonce preserved", "payload hash computed", "receipt hash chained"],
        "boundary": "synthetic public demo row only",
        "next_gate": "recover by nonce",
    },
    {
        "nonce": "SQ67_PUBLIC_DEMO_A002",
        "lane": "visible_baseline",
        "task": "extract_facts",
        "claim": "visible answer can be correct while preserving less evidence",
        "evidence": ["answer present", "missing structured receipt"],
        "boundary": "synthetic public demo row only",
        "next_gate": "compare against SQ67 receipt",
    },
    {
        "nonce": "SQ67_PUBLIC_DEMO_A003",
        "lane": "sealed_control",
        "task": "hash_reveal",
        "claim": "hash can verify later reveal without exposing plaintext during setup",
        "evidence": ["public id", "sha256 match after reveal"],
        "boundary": "synthetic public demo row only",
        "next_gate": "score false-recovery rate",
    },
]


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    return conn


def last_receipt_hash(conn: sqlite3.Connection) -> str | None:
    row = conn.execute(
        "SELECT receipt_sha256 FROM receipts ORDER BY id DESC LIMIT 1"
    ).fetchone()
    return str(row[0]) if row else None


def receipt_hash(fields: dict[str, Any]) -> str:
    keep = {
        "created_at": fields["created_at"],
        "nonce": fields["nonce"],
        "lane": fields["lane"],
        "task": fields["task"],
        "claim": fields["claim"],
        "evidence": fields["evidence"],
        "boundary": fields["boundary"],
        "next_gate": fields["next_gate"],
        "payload_sha256": fields["payload_sha256"],
        "prev_sha256": fields.get("prev_sha256"),
    }
    return sha256_text(stable_json(keep))


def write_receipt(conn: sqlite3.Connection, row: dict[str, Any]) -> dict[str, Any]:
    created_at = row.get("created_at") or utc_now()
    evidence = row.get("evidence") or []
    payload = {
        "nonce": row["nonce"],
        "lane": row["lane"],
        "task": row["task"],
        "claim": row["claim"],
        "evidence": evidence,
        "boundary": row["boundary"],
        "next_gate": row["next_gate"],
    }
    payload_json = stable_json(payload)
    fields = {
        **payload,
        "created_at": created_at,
        "payload_sha256": sha256_text(payload_json),
        "prev_sha256": last_receipt_hash(conn),
    }
    fields["receipt_sha256"] = receipt_hash(fields)
    conn.execute(
        """
        INSERT INTO receipts (
          created_at, nonce, lane, task, claim, evidence_json, boundary,
          next_gate, payload_json, payload_sha256, prev_sha256, receipt_sha256
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            fields["created_at"],
            fields["nonce"],
            fields["lane"],
            fields["task"],
            fields["claim"],
            stable_json(evidence),
            fields["boundary"],
            fields["next_gate"],
            payload_json,
            fields["payload_sha256"],
            fields["prev_sha256"],
            fields["receipt_sha256"],
        ),
    )
    conn.commit()
    return fields


def recover(conn: sqlite3.Connection, nonce: str) -> dict[str, Any] | None:
    row = conn.execute(
        """
        SELECT id, created_at, nonce, lane, task, claim, evidence_json, boundary,
               next_gate, payload_json, payload_sha256, prev_sha256, receipt_sha256
        FROM receipts
        WHERE nonce=?
        """,
        (nonce,),
    ).fetchone()
    if not row:
        return None
    keys = [
        "id",
        "created_at",
        "nonce",
        "lane",
        "task",
        "claim",
        "evidence_json",
        "boundary",
        "next_gate",
        "payload_json",
        "payload_sha256",
        "prev_sha256",
        "receipt_sha256",
    ]
    result = dict(zip(keys, row))
    result["evidence"] = json.loads(result.pop("evidence_json"))
    result["payload"] = json.loads(result.pop("payload_json"))
    return result


def verify(conn: sqlite3.Connection) -> list[str]:
    errors: list[str] = []
    prev: str | None = None
    rows = conn.execute(
        """
        SELECT id, created_at, nonce, lane, task, claim, evidence_json, boundary,
               next_gate, payload_json, payload_sha256, prev_sha256, receipt_sha256
        FROM receipts
        ORDER BY id
        """
    ).fetchall()
    for row in rows:
        (
            row_id,
            created_at,
            nonce,
            lane,
            task,
            claim,
            evidence_json,
            boundary,
            next_gate,
            payload_json,
            payload_sha256,
            prev_sha256,
            receipt_sha256,
        ) = row
        if sha256_text(payload_json) != payload_sha256:
            errors.append(f"row {row_id} payload hash mismatch")
        fields = {
            "created_at": created_at,
            "nonce": nonce,
            "lane": lane,
            "task": task,
            "claim": claim,
            "evidence": json.loads(evidence_json),
            "boundary": boundary,
            "next_gate": next_gate,
            "payload_sha256": payload_sha256,
            "prev_sha256": prev_sha256,
        }
        if prev_sha256 != prev:
            errors.append(f"row {row_id} prev hash mismatch")
        if receipt_hash(fields) != receipt_sha256:
            errors.append(f"row {row_id} receipt hash mismatch")
        prev = receipt_sha256
    return errors


def export_rows(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT nonce, lane, task, claim, evidence_json, boundary, next_gate,
               payload_sha256, prev_sha256, receipt_sha256
        FROM receipts
        ORDER BY id
        """
    ).fetchall()
    output = []
    for row in rows:
        output.append(
            {
                "nonce": row[0],
                "lane": row[1],
                "task": row[2],
                "claim": row[3],
                "evidence": json.loads(row[4]),
                "boundary": row[5],
                "next_gate": row[6],
                "payload_sha256": row[7],
                "prev_sha256": row[8],
                "receipt_sha256": row[9],
            }
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)

    def add_db_option(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--db", type=Path)

    init_parser = sub.add_parser("init")
    add_db_option(init_parser)
    demo_parser = sub.add_parser("demo")
    add_db_option(demo_parser)
    verify_parser = sub.add_parser("verify")
    add_db_option(verify_parser)
    verify_parser.add_argument("--quiet", action="store_true")
    recover_parser = sub.add_parser("recover")
    add_db_option(recover_parser)
    recover_parser.add_argument("--nonce", required=True)
    export_parser = sub.add_parser("export")
    add_db_option(export_parser)
    export_parser.add_argument("--format", choices=["json", "jsonl"], default="json")

    args = parser.parse_args()
    if args.db is None:
        args.db = Path("sq67_demo.sqlite")

    with connect(args.db) as conn:
        if args.command == "init":
            print(f"initialized {args.db}")
            return 0
        if args.command == "demo":
            for row in DEMO_ROWS:
                conn.execute("DELETE FROM receipts WHERE nonce = ?", (row["nonce"],))
            conn.commit()
            for row in DEMO_ROWS:
                write_receipt(conn, row)
            errors = verify(conn)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            print(f"OK wrote {len(DEMO_ROWS)} receipts to {args.db}")
            return 0
        if args.command == "verify":
            errors = verify(conn)
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            if not args.quiet:
                print("OK")
            return 0
        if args.command == "recover":
            row = recover(conn, args.nonce)
            if row is None:
                print("NO_RECOVERY")
                return 2
            print(json.dumps(row, indent=2, sort_keys=True))
            return 0
        if args.command == "export":
            rows = export_rows(conn)
            if args.format == "jsonl":
                for row in rows:
                    print(stable_json(row))
            else:
                print(json.dumps(rows, indent=2, sort_keys=True))
            return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
