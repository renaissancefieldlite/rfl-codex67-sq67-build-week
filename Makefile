.PHONY: demo verify score test clean

DB := examples/output/sq67_demo.sqlite

demo:
	python3 scripts/sq67_demo.py demo --db $(DB)

verify:
	python3 scripts/sq67_demo.py verify --db $(DB)

score:
	python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv

test: demo verify score

clean:
	find examples/output -type f -delete 2>/dev/null || true
	rmdir examples/output 2>/dev/null || true

