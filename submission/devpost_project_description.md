# Devpost Project Description Draft

## Title

Renaissance Field Lite Codex67 / SQ67

## Tagline

A Codex-built receipt, recovery, and benchmark harness for making agent state-path behavior measurable.

## Category

Developer Tools

## What We Built

RFL built SQ67, a public-safe receipt lane for Codex workflows. SQ67 writes a marker, hashes the proof, recovers it later, and scores whether the state-path evidence held.

RFL also added a public-safe 30-claim patent audit packet that maps the May 28, 2025 Mirror Interface priority anchor and later non-provisional support spine to the Codex/SQ67 state-path evidence without exposing private implementation files.

This is part of a larger RFL Codex-built product stack: Trismegistus, Quadro, B.A.S.I.S., Golden Mark, Mirror Lattice, and SQ67.

## Why It Matters

Codex work can produce useful outputs while leaving weak or messy evidence trails. SQ67 turns that into a measurable loop: receipts, hashes, recovery gates, controls, and second-machine checks.

## How Codex Was Used

Codex helped build the product stack, run the state-path tests, generate and inspect receipts, compare lanes, package videos, and assemble this public-safe repository.

## How GPT-5.6 Was Used

GPT-5.6-sol was included in the C57/C58 model-gate comparison harness. The result was useful because it made model behavior measurable under the same evidence-preservation tests, including stability boundaries and timeouts.

## Results

- SQ67 clean receipt lane: 150 / 150 evidence rows preserved.
- Normal visible lane: 114 / 150 evidence rows preserved.
- Earlier clean route: 450 / 450 recoveries.
- Controls: 0 / 1300 false recoveries.
- H09 Tornado second-machine sealed batch: 10 / 10 hashes matched, zero plaintext hits.

## Demo Video

YouTube URL: https://www.youtube.com/watch?v=s1YJU8eL2es

## Public Paper / Repository

- Public repository: https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week
- Reviewer proof surface: https://renaissancefieldlite.com/codex67-sq67-reviewer-demo.html
- White paper PDF: https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week/blob/main/output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf
- 30-claim patent audit packet: https://github.com/renaissancefieldlite/rfl-mirror-interface-30-claim-audit
- Zenodo DOI record: https://doi.org/10.5281/zenodo.21417649

## Code Access / Licensing Boundary

The public repository includes runnable public-safe code for judges to inspect:

- SQ67 SQLite receipt demo
- SHA256 receipt verification
- nonce recovery
- lane scoring
- PDF rebuild script
- public-safe 30-claim patent audit packet

Protected implementation code, raw state evidence, private prompts, unredacted logs, and licensing-grade integration material are available only under NDA, licensing review, or another protected review process with Renaissance Field Lite.

## Installation / Testing Instructions

Supported platforms:

- macOS
- Linux
- Windows with WSL, Git Bash, or PowerShell running Python 3.10+

No API key, hosted account, plugin install, private credential, or rebuild of the protected system is required for public judging.

Hosted demo / sandbox surface:

https://renaissancefieldlite.com/codex67-sq67-reviewer-demo.html

Local test:

```sh
git clone https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week.git
cd rfl-codex67-sq67-build-week
make test
```

Expected validation packet:

```text
OK wrote 3 receipts to examples/output/sq67_demo.sqlite
OK
SQ67 clean receipt lane,150,100.00%,100.00%,0,0,n/a,0
SQ67 clean route,450,100.00%,100.00%,0,0,n/a,0
Tornado N10 sealed batch,10,100.00%,100.00%,0,0,n/a,0
false recovery controls,1300,0.00%,0.00%,0,1300,n/a,0
gpt-5.5 lane C,50,100.00%,100.00%,0,0,74.935,8421682
gpt-5.6-sol lane C,50,76.00%,100.00%,0,0,171.111,19067794
normal visible lane,150,99.33%,76.00%,0,0,n/a,0
```

If `make` is unavailable:

```sh
python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py recover --db examples/output/sq67_demo.sqlite --nonce SQ67_PUBLIC_DEMO_A002
python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv
```

## Feedback Session

Codex `/feedback` session ID: `TBD`

Session ID plan: use a fresh public-safe Tornado PC reproduction task, not the private RFL Mac build thread.

## Boundary

This package proves a repeatable state-path test harness and measured evidence-preservation lift. It does not rely on exposing private prompts or claiming direct access to model internals.
