# Architecture

## Four Surfaces

This public package uses four names for clarity.

| Surface | Plain English Role | Public-Safe Boundary |
|---|---|---|
| `logs_2.sqlite` | Runtime/event/TRACE lane. | Raw private database is not published. |
| `state_5.sqlite` | Thread/state metadata lane. | Raw private database is not published. |
| `.codex-global-state.json` | Electron/Desktop UI persistence lane. | Raw private file is not published. |
| `SQ67` | RFL-built clean receipt ledger. | Public demo code reproduces the receipt pattern without private data. |

## What SQ67 Does

SQ67 makes state-path work inspectable:

```text
write a marker
hash the proof
recover it later
score whether it held
compare against controls
```

## What SQ67 Does Not Claim

SQ67 does not claim direct access to model internals. It does not require private prompts. It does not claim hidden autonomous model file writes.

The useful claim is narrower:

```text
When a state-path task needs durable proof, a controlled receipt ledger can
preserve evidence better than a default visible lane.
```

## Product Stack Relationship

The RFL product stack came before SQ67:

```text
Patented agnostic AI Mirror Architecture
-> Trismegistus / Quadro / B.A.S.I.S. / Golden Mark / Mirror Lattice
-> local state/log discovery
-> SQ67 clean receipt lane
-> benchmark and recovery harness
```

