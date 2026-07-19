# Reviewer Code Map

This repository is a public-safe evaluator package. It contains enough code to inspect and run the SQ67 receipt pattern, but it does not publish protected production implementation or raw private evidence.

Live reviewer proof surface:

```text
https://renaissancefieldlite.com/codex67-sq67-reviewer-demo.html
```

## Public Code To Inspect

| File | Purpose |
| --- | --- |
| `scripts/sq67_demo.py` | Creates a local SQLite receipt ledger, writes deterministic receipt rows, verifies hash chains, exports JSONL, and recovers by nonce. |
| `scripts/score_receipts.py` | Scores public-safe benchmark rows by lane: exact recovery, evidence preservation, false recovery, control rejection, latency, and token totals. |
| `scripts/build_whitepaper_pdf.py` | Builds the public-safe white paper PDF from `docs/whitepaper.md`. |
| `Makefile` | Provides the shortest judge path: `make test`. |
| `docs/public_make_test_receipt_2026-07-18.md` | Stores the exact transcript from the public verifier run. |
| `docs/provisional_claim_audit/` | Public-safe 30-claim patent audit packet: source hashes, claim-theme matrix, FIG. 1-FIG. 15 overlap map, and protected-material boundaries. |

## One-Command Review

```sh
make test
```

Supported platforms:

- macOS
- Linux
- Windows with WSL, Git Bash, or PowerShell running Python 3.10+

No API key, hosted account, plugin install, private credential, or rebuild of the protected system is required for public judging.

Expected:

- three demo receipts written
- receipt chain verification returns `OK`
- benchmark scorer prints lane-level preservation rates
- white paper PDF rebuilds locally

## What Is Not Public Code

The following are protected and are not included in the public repository:

- raw `state_5.sqlite`
- raw `logs_2.sqlite`
- raw `.codex-global-state.json`
- raw private prompts
- account identifiers
- private thread IDs
- tokens, cookies, bearer strings, auth headers
- machine-bound backend identifiers
- full private payload bodies
- protected production implementation details

Protected implementation code, raw evidence, and licensing-grade integrations are available only under NDA, licensing review, or another protected review process with Renaissance Field Lite.
