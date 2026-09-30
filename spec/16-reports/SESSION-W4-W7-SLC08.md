---
id: SESSION-SLC08
type: session-report
wave: W4–W7 (SLC-08)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-08 Decision → Plan → Version → Baseline → Tasks

**Result:** **G6-SLC-08 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates: Decision Request, Decision, Plan, Plan Version, Outcome Tracker | 5 · 17 invariants (corrected; first stated 20) |
| Commands / queries / events | 24 / 9 / 33 |
| Specification: decision basis ("what was known"), change classification (major/minor), deterministic task synchronization, outcome progress as-known-at | 1 |
| OpenAPI (33 ops; plan content schemas) — validated · AsyncAPI (33) · errors (27) · logical model (10 tables) | — |
| Acceptance: 120 generated + 22 scenarios · 7 properties | — |
| Threats 6 · failure modes 3 · observability 6 · quality scenarios +2 | — |

## Key design points
1. **Decision basis is queryable.** For any decision: the authority chain valid at recording time, the pinned versions of cited assessments, and the key claims as known at that instant — side by side with what is known now. This is OUT-04 made operational.
2. **Plan identity vs plan versions.** CR-29 is now fully closed: the 14 components of the original plan live in immutable versions; exactly one baseline at a time.
3. **Major/minor is computed, not argued.** BRL-005 becomes a deterministic classification at submission; major changes need a new approved version.
4. **Task synchronization is a deterministic diff** keyed by stable activity ids — idempotent, ≤ 60 s for 500 activities, respects frozen criteria of assigned tasks by superseding instead of editing.
5. **Outcome progress is bitemporal,** so past progress reports can be reproduced exactly.

## Quality note
The OpenAPI validator caught a generator defect (numeric payload fields unsupported) — fixed and recorded as CR-48; earlier slices were checked and unaffected. This is the value of validating generated contracts rather than trusting them.

## Registers
CR-29 fully applied · CR-48 added · HAP-09 evidence: SLC-08 · glossary +3.

## Gates
G0–G3 PASS · **G6-SLC-01..08 READY** · G6 release BLOCKED (remaining R1: SLC-11 offline sync, SLC-12a retention & legal hold)

## Next recommended session
**SLC-11 — Offline field capture & synchronization** (implements ADR-P09 and the offline contracts already fixed by SLC-02 and SLC-03), then **SLC-12a** (retention, legal hold, disposition), then **W8**.
