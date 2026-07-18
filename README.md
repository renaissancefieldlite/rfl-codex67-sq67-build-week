# Renaissance Field Lite Codex67 / SQ67

Codex helped Renaissance Field Lite build a product stack. Then we used Codex to build a receipt system for making agent state-path behavior easier to inspect, reproduce, and score.

SQ67 is the receipt book: write a marker, hash the proof, recover it later, and score whether it held.

## What This Is

This repository is the public-safe Build Week package for the Renaissance Field Lite Codex67 / SQ67 work.

It contains:

- a public-safe white paper
- a local SQLite receipt demo
- scoring scripts
- redacted sample benchmark rows
- Devpost and reviewer instructions
- video receipt metadata

It does not contain raw private state logs, private prompts, account identifiers, tokens, cookies, bearer strings, or machine-bound backend identifiers.

## The Plain English Finding

RFL found local Codex state and trace surfaces on one RFL Mac. The default lane was noisy and weak as an evidence surface. RFL built SQ67 as a clean receipt lane and measured better preservation with hashes, controls, recovery gates, and second-machine checks.

The narrow public claim is this:

> SQ67 proves a repeatable state-path testing harness and measurable evidence-preservation lift. It does not require exposing private prompts or claiming direct access to model internals.

## Product Stack Context

This is not a one-prompt demo. The RFL product stack includes:

- Trismegistus
- Quadro
- B.A.S.I.S.
- Golden Mark
- Golden Field Lite
- Mirror Lattice
- SQ67

Important nuance:

> The patented agnostic AI Mirror Architecture workflow built the stack. SQ67 came later as the clean receipt and recovery layer for measuring state-path behavior.

## Repository Layout

```text
.
├── README.md
├── LICENSE
├── PATENT_NOTICE.md
├── docs/
│   ├── whitepaper.md
│   ├── timeline.md
│   ├── architecture.md
│   ├── benchmark_summary.md
│   ├── openai_questions.md
│   ├── redaction_statement.md
│   ├── public_record_links.md
│   └── video_receipt.md
├── examples/
│   ├── sample_receipts.jsonl
│   └── sample_benchmark_rows.csv
├── scripts/
│   ├── sq67_demo.py
│   └── score_receipts.py
├── submission/
│   ├── devpost_project_description.md
│   └── judge_testing_instructions.md
└── video/
    └── README.md
```

## Quick Start

Run the receipt demo with only Python standard library:

```sh
make test
```

Or run each step directly:

```sh
python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py export --db examples/output/sq67_demo.sqlite --format jsonl
```

Score the sample benchmark rows:

```sh
python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv
```

Expected result:

- the demo writes three chained SQ67-style receipts
- verification returns `OK`
- the benchmark scorer prints lane-level recovery and evidence preservation rates

## Key Results Carried Into This Public Package

- SQ67 clean receipt lane: `150 / 150` evidence rows preserved.
- Normal visible lane: `114 / 150` evidence rows preserved.
- Clean lane kept `36` more proof rows on the same kind of work.
- Earlier clean route: `450 / 450` recoveries.
- Controls: `0 / 1300` false recoveries.
- H07 sealed canary: `3 / 3` hashes matched, zero plaintext hits.
- H08D Tornado second-machine sealed batch: `3 / 3` hashes matched, zero plaintext hits.
- H09 Tornado N10 sealed batch: `10 / 10` hashes matched, zero plaintext hits.

## Boundaries

This repo supports:

- repeatable receipt writing
- hash verification
- public-safe benchmark scoring
- evidence-preservation comparison
- reviewer-facing documentation

This repo does not prove:

- motive
- human reading of private material
- direct hidden-internal readability
- hidden autonomous model access
- a legal conclusion of IP theft

Those are separate questions. The repo preserves the technical record and asks OpenAI to answer the implementation/documentation gap.

## Build Week Status

Public package status: repo-ready.

Pending before final Devpost submission:

- public YouTube URL
- `/feedback` Codex session ID
- final category selection
- final review of public visibility and redaction
