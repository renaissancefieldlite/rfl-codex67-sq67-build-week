# Tornado Public-Safe Codex Session Prompt

Use this in a fresh Codex task on the Tornado PC only. Do not use the private RFL Mac build thread as the Devpost Session ID.

After the task completes, run `/feedback` in that Tornado task and copy the Session ID into Devpost.

```text
OPENAI CODEX BUILD WEEK PUBLIC-SAFE REVIEW THREAD

Project:
Renaissance Field Lite Codex67 / SQ67

Public repository:
https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week

Public demo video:
https://www.youtube.com/watch?v=s1YJU8eL2es

Public page:
https://renaissancefieldlite.com/codex67-sq67-build-week.html

Goal:
Verify the public-safe repository as an evaluator would. Do not use private Mac files, raw state databases, private prompts, browser session stores, account identifiers, tokens, or hidden local context.

Steps:
1. Clone or open the public repository.
2. Read `README.md`, `docs/reviewer_code_map.md`, and `submission/judge_testing_instructions.md`.
3. Run `make test`.
4. If `make` is unavailable, run:
   - `python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite`
   - `python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite`
   - `python3 scripts/sq67_demo.py recover --db examples/output/sq67_demo.sqlite --nonce SQ67_PUBLIC_DEMO_A002`
   - `python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv`
5. Summarize:
   - files inspected
   - commands run
   - whether verification passed
   - what the public repo proves
   - what remains protected under NDA/licensing review

Boundary:
This is a public-safe reproduction thread for Devpost review. It is not the private build thread and it should not disclose raw private state/log evidence.
```

