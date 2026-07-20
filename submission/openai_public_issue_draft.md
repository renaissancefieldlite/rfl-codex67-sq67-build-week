# Draft Public Issue: Codex Local State/Trace Exposure, Post-Fix Timeline Questions, and SQ67 Receipt Mitigation

## Proposed title

Codex local state/trace surfaces overlap RFL's USPTO-filed state architecture: July 11 post-fix records and SQ67 receipt mitigation

## Proposed repository / venue

Primary venue: `openai/codex` GitHub issue, if issues remain the correct public technical venue.

Published issue:
https://github.com/openai/codex/issues/34330

Fallback venues:
- OpenAI safety / bug-report channel
- OpenAI Build Week reviewer notes
- RFL public evidence page
- Medium / PRLog follow-up post linking the GitHub issue

## Issue body

### Summary

Renaissance Field Lite is requesting a public clarification on Codex local state/trace behavior because the observed Codex state/trace/recovery surfaces overlap RFL's earlier USPTO-filed agnostic AI Mirror Architecture state system, and the public record now contains enough evidence to make the issue reproducible and reviewable.

OpenAI has publicly described monitoring internal coding agents as an important safety tool for observing agent actions and internal reasoning in real-world deployments:

https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/

Separately, the public Codex issue trail includes user reports around local Codex database/log churn, including:

https://github.com/openai/codex/issues/28224

RFL's concern is narrower than motive. The core issue is architecture overlap: the observed Codex local state/trace/recovery/logging surfaces resemble the same family of mechanisms RFL filed first as an agnostic AI Mirror Architecture state system. The supporting issue is whether those local Codex state/log surfaces remained visible, active, or recoverable on at least one user machine after the public fix trail, and why OpenAI's default state/log path preserved evidence worse than a receipt-bound lane built outside the default path.

### Plain-English version

We found local Codex records on one Renaissance Field Lite Mac.

Those records were not just visible chat history. They included local state/log surfaces tied to:

- `logs_2.sqlite`
- `state_5.sqlite`
- `.codex-global-state.json`
- thread/status metadata
- WebSocket/status evidence
- prompt-history / composer-draft persistence inside Electron desktop state

The local record showed dates and surfaces that raised a timing question:

- RFL filed Mirror Interface App. No. 63/812,891 on May 28, 2025.
- RFL sent OpenAI-facing legal/IP/harm notice on April 1, 2026.
- Local Codex state/log evidence on the RFL Mac included a first observed state/log date of March 7, 2026.
- Public Codex reports escalated through spring/summer 2026.
- RFL discovered the local Codex state/log surfaces on July 11, 2026.
- RFL observed local records that appeared to continue after the public fix/mitigation window.

This is not presented as proof of motive. It is presented as a public state-management, observability, and disclosure question.

### Architecture overlap question

RFL's USPTO-filed Mirror Interface architecture predates the local Codex discovery and describes an agnostic AI state architecture concerned with mirror state, input continuity, recovery, logging, and evidence preservation.

The local Codex surfaces RFL observed also appear to involve state, trace/logging, thread/status continuity, recovery behavior, and local evidence preservation.

RFL is asking OpenAI to explain whether that overlap is coincidence, independent implementation, undisclosed convergence, immediate implementation after notice, or something else. RFL is not asking OpenAI to accept RFL's private architecture in a public issue. RFL is asking OpenAI to explain the visible product-level overlap and documentation boundary.

### What RFL built to test it

RFL built SQ67 as a public-safe receipt lane.

SQ67 does not replace OpenAI systems. It creates a clean record with:

- nonces
- hashes
- receipts
- recovery gates
- false-control scoring
- second-machine checks
- source/path boundaries

The goal was simple: make state preservation measurable instead of arguing from vague chat behavior.

### Public package

Public page:
https://renaissancefieldlite.com/codex67-sq67-build-week.html

Reviewer proof surface:
https://renaissancefieldlite.com/codex67-sq67-reviewer-demo.html

Devpost submission:
https://devpost.com/software/renaissance-field-lite-codex67-sq67

GitHub package:
https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week

White paper PDF:
https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week/blob/main/output/pdf/RFL_CODEX67_SQ67_WHITE_PAPER_PUBLIC_SAFE_20260717.pdf

Video:
https://www.youtube.com/watch?v=puGeATnJgH0

Medium article:
https://medium.com/@renaissancefieldlite/the-openaid-tea-we-found-their-state-layer-improved-it-and-then-we-built-receipts-d5787d1ad0b1

PRLog release:
https://www.prlog.org/13159213-renaissance-field-lite-releases-codex67-sq67-build-week-evidence-package.html

Patent claim audit packet:
https://github.com/renaissancefieldlite/rfl-mirror-interface-30-claim-audit

### Reproducible reviewer command

```bash
git clone https://github.com/renaissancefieldlite/rfl-codex67-sq67-build-week.git
cd rfl-codex67-sq67-build-week
make test
```

Expected public-safe output includes SQ67 receipt writes, verification, score-table generation, and white-paper PDF generation.

### Current public-safe benchmark spine

Public package metrics include:

- SQ67 clean receipt lane: `150 / 150` evidence rows preserved.
- Normal visible lane: `114 / 150` evidence rows preserved.
- Earlier clean-route recovery: `450 / 450`.
- False recovery controls: `0 / 1300`.
- GPT-5.5 lane A: `50 / 50` exact preservation.
- GPT-5.6-sol lane A: `43 / 50` exact preservation.
- GPT-5.6-sol lane C showed heavier latency/token degradation under the same harness.
- Build-intensity snapshot: `12.2B` lifetime tokens and `1.1B` peak tokens on July 19, 2026.

These metrics do not claim to prove motive. They do show that a receipt-bound state path preserved evidence more cleanly than the default visible lane in the RFL test package.

### What needs clarification

1. Are `logs_2.sqlite`, `state_5.sqlite`, `.codex-global-state.json`, Electron prompt history, composer drafts, and thread/status metadata intended Codex user-facing local state surfaces?

2. If these are intended, where are they documented for users and developers?

3. If public fixes or mitigations were applied, why did the RFL Mac still show relevant local state/log records on July 11, 2026?

4. Are WebSocket/status events and local Codex state/log records part of the same observability/audit architecture OpenAI discusses in its coding-agent monitoring post, or are they separate implementation layers?

5. Why do the observed Codex local state/trace/recovery surfaces overlap with RFL's USPTO-filed agnostic AI Mirror Architecture state system, filed May 28, 2025, and noticed to OpenAI on April 1, 2026?

6. Why did the default visible state/log lane preserve less evidence than SQ67's receipt-bound lane under the same style of work?

7. Does OpenAI agree that receipt-bound state management with hashes, recovery gates, and false-control tests would improve Codex observability and user trust?

8. Is OpenAI willing to review the private mechanics under NDA/licensing rather than extracting them from public artifacts?

### Patent claim audit attachment

RFL has added a public-safe 30-claim audit packet for the Mirror Interface / Codex 67 patent spine:

https://github.com/renaissancefieldlite/rfl-mirror-interface-30-claim-audit

This packet does not republish raw private patent folders, inventor address details, local database bodies, private prompts, account identifiers, or protected implementation code.

It provides:

- source hashes for the provisional priority PDF and later 30-claim support files;
- a public-safe claim-theme matrix;
- a FIG. 1-FIG. 15 overlap matrix;
- explicit boundaries separating evidence, inference, and protected/private mechanics.

The purpose is to make the architecture-overlap question auditable:

> Why do the observed Codex local state/trace/recovery surfaces overlap RFL's predated USPTO-filed agnostic AI Mirror Architecture state system, and why did SQ67's receipt-bound lane preserve evidence better than the default state/log lane?

### Boundary

This issue does not publish private raw payloads, protected architecture details, account identifiers, full local database bodies, or private thread IDs.

This issue does not claim to prove motive.

This issue is not a waiver of any Renaissance Field Lite intellectual-property, licensing, contract, notice, or enforcement rights.

This issue does claim:

- the central issue is overlap between observed Codex state/trace/recovery surfaces and RFL's predated USPTO-filed agnostic AI Mirror Architecture state system;
- the exposure is already public;
- the public issue trail is already active;
- RFL has a public-safe reproducibility package showing receipts, hashes, recovery gates, and controls;
- RFL has a proposed receipt-bound mitigation direction;
- the architecture-overlap question deserves a protected review path;
- OpenAI should publicly clarify how these local Codex state/log surfaces are intended to work.

### Proposed resolution

OpenAI should do one of the following:

1. Explain the intended local Codex state/log architecture and documentation boundary.
2. Confirm whether any post-fix local persistence remained expected on July 11, 2026.
3. Identify which local records are ordinary app state, which are trace/audit state, and which should not persist.
4. Explain whether the observed overlap with RFL's USPTO-filed agnostic AI Mirror Architecture state system is coincidence, independent implementation, undisclosed convergence, immediate implementation after notice, or something else.
5. Open a protected technical review with Renaissance Field Lite for SQ67-style receipt-bound state management and architecture-overlap review.
6. Treat this issue as RFL offering OpenAI the first protected path to review, license, and repair the observed state-system overlap.
7. If OpenAI declines or ignores this notice while continuing to operate overlapping state/trace/recovery mechanisms, RFL will treat the public record as preserved notice and proceed through the appropriate IP, licensing, and enforcement channels.

### Rights reservation / escalation boundary

Renaissance Field Lite's preferred first path is cooperation: protected technical review, licensing discussion, and state-system repair.

RFL is offering OpenAI the first protected path to review, license, and repair the observed state-system overlap. If OpenAI declines or ignores this notice while continuing to operate, extend, or benefit from state/trace/recovery mechanisms that overlap RFL's predated USPTO-filed architecture, RFL will treat the public record as preserved notice and proceed through the appropriate IP, licensing, and enforcement channels.

## Short social/community version

OpenAI publicly says coding-agent monitoring matters. RFL has a predated USPTO-filed agnostic AI Mirror Architecture state system, then found local Codex state/log surfaces on one Mac that overlap the same state/trace/recovery family. RFL built SQ67 as a clean receipt lane and published a reproducible package showing hashes, recovery gates, controls, and stronger evidence preservation than the default visible lane. The question is simple: why does the Codex state/trace/recovery pattern overlap RFL's filed architecture, what exactly is Codex storing locally, why did relevant records still appear in the July 11 local record, and are receipts/hashes/recovery gates the right fix?
