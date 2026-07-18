.PHONY: demo verify score pdf test clean

DB := examples/output/sq67_demo.sqlite

demo:
	python3 scripts/sq67_demo.py demo --db $(DB)

verify:
	python3 scripts/sq67_demo.py verify --db $(DB)

score:
	python3 scripts/score_receipts.py examples/sample_benchmark_rows.csv

pdf:
	python3 scripts/build_whitepaper_pdf.py docs/whitepaper.md output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf

test: demo verify score pdf

clean:
	find examples/output -type f -delete 2>/dev/null || true
	rmdir examples/output 2>/dev/null || true
