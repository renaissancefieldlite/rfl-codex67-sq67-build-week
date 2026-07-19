# Redaction Statement

This repository is public-safe by design.

Excluded:

- raw `state_5.sqlite`
- raw `logs_2.sqlite`
- raw `.codex-global-state.json`
- raw private prompt dumps
- account identifiers
- private thread IDs
- tokens, cookies, bearer strings, and auth headers
- machine-bound backend identifiers
- full private payload bodies
- unredacted screenshots containing private UI details

Included:

- public-safe summaries
- counts
- dates
- public GitHub issue/PR references
- benchmark summaries
- synthetic sample receipts
- runnable demo code using local toy demo data only
- video checksum and media notes

Reviewers can request private raw evidence, protected implementation code, or licensing-grade integration material under an appropriate NDA, licensing review, or equivalent protected-review process with Renaissance Field Lite.
