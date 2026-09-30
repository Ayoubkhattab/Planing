---
id: SESSION-SLC11
type: session-report
wave: W4–W7 (SLC-11)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-11 Offline Field Capture & Synchronization

**Result:** **G6-SLC-11 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates: Field Device (BC01); Preload Package, Sync Session, Sync Conflict (BC07) | 4 · 14 invariants (corrected; first stated 15) |
| Commands / queries / events | 16 / 5 / 25 |
| Specification: device-side rules, handshake with clock-offset measurement, ordered signed batches, apply rules (append-only vs state-changing), delta download, conflicts, performance | 1 |
| OpenAPI (21 ops; CommandEnvelope and SyncDelta schemas) — validated · AsyncAPI (25) · errors (24) · logical model (server + device) | — |
| Acceptance: 88 generated + 17 scenarios · 6 properties over random interruption points | — |
| Threats 6 · failure modes 4 · observability 7 · quality scenarios +2 | — |

## Key design points
1. **Sync sends intentions, not state.** Every offline action is a signed command replayed through the owner context's API with the user's authority — owner guards and policies still decide.
2. **No loss, no duplicates, no last-write-wins,** whatever the interruption pattern (P-111..P-114): contiguous signed sequences, client command ids, client-generated ULIDs for new objects, and version checks for state changes.
3. **Honest time:** record time is server receipt; device time is kept and corrected by a measured clock offset; large skew is flagged.
4. **Lost devices are neutralised:** key revoked at once, wipe on first contact, and any command dated after the loss goes to human review.
5. **Capture outlives reading:** after the offline limit, users can still record observations, but preloaded (possibly sensitive, possibly stale) data can no longer be opened.
6. **Two kinds of conflict, kept apart (CR-49):** stale state-changing commands become sync conflicts in BC07; disagreements in content from synced observations still flow into BC02's claims conflict engine.

## Cross-slice change
CR-50: SLC-02 creation commands accept a client-generated id; SLC-02 contracts regenerated and re-validated, and the SLC-04 change to the resolved-entity query was carried into the SLC-02 source data so regeneration does not lose it.

## Gates
G0–G3 PASS · **G6-SLC-01..08, SLC-11 READY** · G6 release BLOCKED (remaining R1: SLC-12a)

## Next recommended session
**SLC-12a — Retention, legal hold, disposition and erasure** (R1 portion), then **W8 — Solution & technology decisions** from the collected W8 inputs, then **W9 — Baseline consolidation (G6 for R1)**.
