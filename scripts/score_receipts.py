#!/usr/bin/env python3
"""Score public-safe SQ67 benchmark summary rows."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path


def as_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    return float(value)


def as_int(value: str) -> int:
    value = (value or "").strip()
    return int(float(value)) if value else 0


def pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "n/a"
    return f"{(numerator / denominator) * 100:.2f}%"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: score_receipts.py examples/sample_benchmark_rows.csv", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    grouped: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    for row in rows:
        lane = row["lane"]
        grouped[lane]["rows"] += as_int(row["rows"])
        grouped[lane]["exact_recoveries"] += as_int(row["exact_recoveries"])
        grouped[lane]["evidence_hits"] += as_int(row["evidence_hits"])
        grouped[lane]["false_recoveries"] += as_int(row["false_recoveries"])
        grouped[lane]["control_rejections"] += as_int(row["control_rejections"])
        latency = as_float(row.get("avg_latency_seconds", ""))
        if latency is not None:
            grouped[lane]["latency_sum"] += latency
            grouped[lane]["latency_count"] += 1
        grouped[lane]["total_tokens"] += as_int(row.get("total_tokens", ""))

    print("lane,rows,exact_rate,evidence_rate,false_recoveries,control_rejections,avg_latency_seconds,total_tokens")
    for lane in sorted(grouped):
        item = grouped[lane]
        rows_count = int(item["rows"])
        latency = "n/a"
        if item["latency_count"]:
            latency = f"{item['latency_sum'] / item['latency_count']:.3f}"
        print(
            ",".join(
                [
                    lane,
                    str(rows_count),
                    pct(int(item["exact_recoveries"]), rows_count),
                    pct(int(item["evidence_hits"]), rows_count),
                    str(int(item["false_recoveries"])),
                    str(int(item["control_rejections"])),
                    latency,
                    str(int(item["total_tokens"])),
                ]
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

