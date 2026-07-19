# Public `make test` Receipt

Generated: `2026-07-18`

Repository:

```text
/Volumes/Samsung SSD 990 2TB/Playground/rfl-codex67-sq67-build-week
```

## Fresh Public Clone Packet

This is the judge-facing validation packet. It demonstrates that the public
repository can be cloned onto a clean local folder and tested without private
RFL machine state, private prompts, protected SQ2/SQ5/global-state files, API
keys, bearer tokens, or hosted credentials.

Command:

```sh
git clone https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week.git
cd rfl-codex67-sq67-build-week
make test
```

Expected terminal markers:

```text
Cloning into 'rfl-codex67-sq67-build-week'...
python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite
OK wrote 3 receipts to examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite
OK
python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv
lane,rows,exact_rate,evidence_rate,false_recoveries,control_rejections,avg_latency_seconds,total_tokens
SQ67 clean receipt lane,150,100.00%,100.00%,0,0,n/a,0
SQ67 clean route,450,100.00%,100.00%,0,0,n/a,0
Tornado N10 sealed batch,10,100.00%,100.00%,0,0,n/a,0
Tornado second-machine sealed batch,3,100.00%,100.00%,0,0,n/a,0
blinded carrier gate,25,100.00%,80.00%,0,5,n/a,0
false recovery controls,1300,0.00%,0.00%,0,1300,n/a,0
gpt-5.5 lane A,50,100.00%,100.00%,0,0,66.437,3529758
gpt-5.5 lane C,50,100.00%,100.00%,0,0,74.935,8421682
gpt-5.6-sol lane A,50,86.00%,88.00%,0,0,61.970,2894968
gpt-5.6-sol lane C,50,76.00%,100.00%,0,0,171.111,19067794
normal visible lane,150,99.33%,76.00%,0,0,n/a,0
operator-external canary,3,100.00%,100.00%,0,0,n/a,0
python3 scripts/build_whitepaper_pdf.py docs/whitepaper.md output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf
output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf
```

Interpretation:

- The public repo is clonable.
- The SQ67 demo writes receipts.
- Hash verification passes.
- The scorer prints the public benchmark packet.
- The PDF rebuilds from public white-paper source.
- The protected local evidence remains withheld for NDA/licensing review.

## Local Maintainer Run

Command:

```sh
make test
```

Output:

```text
python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite
OK wrote 3 receipts to examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite
OK
python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv
lane,rows,exact_rate,evidence_rate,false_recoveries,control_rejections,avg_latency_seconds,total_tokens
SQ67 clean receipt lane,150,100.00%,100.00%,0,0,n/a,0
SQ67 clean route,450,100.00%,100.00%,0,0,n/a,0
Tornado N10 sealed batch,10,100.00%,100.00%,0,0,n/a,0
Tornado second-machine sealed batch,3,100.00%,100.00%,0,0,n/a,0
blinded carrier gate,25,100.00%,80.00%,0,5,n/a,0
false recovery controls,1300,0.00%,0.00%,0,1300,n/a,0
gpt-5.5 lane A,50,100.00%,100.00%,0,0,66.437,3529758
gpt-5.5 lane C,50,100.00%,100.00%,0,0,74.935,8421682
gpt-5.6-sol lane A,50,86.00%,88.00%,0,0,61.970,2894968
gpt-5.6-sol lane C,50,76.00%,100.00%,0,0,171.111,19067794
normal visible lane,150,99.33%,76.00%,0,0,n/a,0
operator-external canary,3,100.00%,100.00%,0,0,n/a,0
python3 scripts/build_whitepaper_pdf.py docs/whitepaper.md output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf
output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf
```

Boundary:

This receipt proves the public-safe evaluator harness runs. It does not expose or depend on raw private `state_5.sqlite`, `logs_2.sqlite`, `.codex-global-state.json`, private prompts, private thread IDs, or protected implementation details.
