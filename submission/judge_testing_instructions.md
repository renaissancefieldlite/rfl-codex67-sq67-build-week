# Judge Testing Instructions

## Requirements

- Python 3.10 or newer
- No external Python packages required

## Supported Platforms

- macOS
- Linux
- Windows with WSL, Git Bash, or PowerShell running Python 3.10+

SQLite is used through Python standard library `sqlite3`. No hosted account, API key, plugin install, or private credential is required for the public evaluator harness.

## Demo / Sandbox

Judges can inspect the hosted public-safe proof surface without rebuilding anything:

```text
https://renaissancefieldlite.com/codex67-sq67-reviewer-demo.html
```

They can also run the local harness with:

```sh
git clone https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week.git
cd rfl-codex67-sq67-build-week
make test
```

## Run The Demo

From the repository root:

```sh
python3 scripts/sq67_demo.py demo --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py verify --db examples/output/sq67_demo.sqlite
python3 scripts/sq67_demo.py recover --db examples/output/sq67_demo.sqlite --nonce SQ67_PUBLIC_DEMO_A002
python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv
```

## Expected Output

The first command should report:

```text
OK wrote 3 receipts to examples/output/sq67_demo.sqlite
```

The verification command should report:

```text
OK
```

The recovery command should return a JSON receipt for `SQ67_PUBLIC_DEMO_A002`.

The score command should print a CSV summary of public-safe benchmark rows.

The expected public packet includes these rows:

```text
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
```

## What To Look For

- deterministic SHA256 receipt hashes
- chained receipt hashes
- recoverable nonce rows
- lane-level evidence preservation rates
- clean public boundaries around what is and is not proven
- a fresh-clone test path that does not require private RFL machine state

## Code Access Boundary

The code in this repository is the public-safe evaluator harness.

Protected production code, raw private state evidence, unredacted logs, private prompts, and licensing-grade integration details are available only under NDA, licensing review, or another protected review process with Renaissance Field Lite.

For Devpost Session ID review, use the public-safe Tornado reproduction task described in `submission/tornado_public_safe_codex_session_prompt.md`.
