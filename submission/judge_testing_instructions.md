# Judge Testing Instructions

## Requirements

- Python 3.10 or newer
- No external Python packages required

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

## What To Look For

- deterministic SHA256 receipt hashes
- chained receipt hashes
- recoverable nonce rows
- lane-level evidence preservation rates
- clean public boundaries around what is and is not proven

