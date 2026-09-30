---
id: SESSION-SLC19
type: session-report
wave: W4–W7 (SLC-19, Release 3)
date: 2026-09-29
basis: V6§21.3
---

# SESSION REPORT — SLC-19 Training, Competency & Exercises (R3) — third and last R3 slice

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review **and** the R2 pilot review (RSK-028 — and, like SLC-17, unlike SLC-18, this slice's real technical exposure to that risk is narrow: its dependencies on SLC-03/SLC-09/SLC-12 are each a single generic reference field, not shared contention infrastructure; see `14-slices/SLC-19/readiness.md`).

| Output (computed) | Count |
|---|---|
| Aggregates: Scenario, Exercise, Simulation (BC05) | 3 · 7 invariants |
| Commands / queries / events | 15 / 7 / 17 |
| OpenAPI | 22 operations — validated |
| Hand-written acceptance scenarios | 10 · 5 properties |
| Cross-slice corrections | CR-63 (AGG-KNOWLEDGE-OBJECT, SLC-12 — guard text and REQ-KNW-002 statement only; payload schema unchanged) — applied and regenerated; round-trip verified (guard text and requirement statement only; OpenAPI, AsyncAPI, errors and acceptance state machines otherwise byte-identical) |

## Key design points
1. **Highest reuse among the three R3 slices, confirmed rather than assumed:** `01-business/release-3-scope.md` §2 predicted this before design started. Design confirmed it exactly: DOM-18's six named elements (Competency, Training, Qualification, Certification, Readiness, Eligibility) needed **zero** new aggregates and **zero** corrections to SLC-03 or SLC-09 — both `AGG-QUALIFICATION-RECORD` and `AGG-ROLE-REQUIREMENT` already had generic-enough fields (`evidence:urn`, `code:string`) before this slice existed.
2. **Three aggregates, not a reduction — but earned, not assumed:** `01-business/release-3-scope.md` §4 (R3-Q4) named Exercise/Scenario/Simulation as three new aggregates before design started, unlike SLC-17 and SLC-18, whose own scope notes listed larger element counts later reduced during actual design (DOM-17: 8 → 2; DOM-16: 6 → 2). This session re-examined R3-Q4's premise rather than accepting it — the conclusion is that the three-way split is structurally justified on its own terms: Scenario is a reusable reference definition (own lifecycle, independent of any one exercise's timing); Exercise is a coordination/scheduling aggregate; Simulation is an execution aggregate with an append-only operational history. This is the same shape as SLC-18's Logistics Request/Shipment split, applied here for the same reason, not merely inherited from the scope note. No fourth aggregate for Evaluation — it is an internal entity of Simulation, same pattern as `Statement` inside `AGG-KNOWLEDGE-OBJECT` or `Requirement` inside `AGG-ROLE-REQUIREMENT`.
3. **Exercise never decides its own ending — Simulation does (reusing CR-62's pattern on a brand-new pair, not extending an existing one):** `AGG-EXERCISE` has no human command for COMPLETED or ABORTED. Both are `SYS:` transitions driven exclusively by `AGG-SIMULATION`'s own `EVT-SIM-COMPLETED`/`EVT-SIM-ABORTED` (INV-EXR-02) — visible in the full state × command matrix, which has no human-triggered cell for either terminal state. Because both aggregates are new in this slice, this reuse needed no correction (CR) at all — the linked-creation and outcome-delegation pattern from CR-62/SLC-18 was simply repeated on a fresh pair of aggregates, not applied by extending an old one.
4. **A simulation never certifies attendance without assessment:** `CMD-SIM-COMPLETE` requires at least one recorded evaluation per participant listed on the linked exercise (INV-SIM-02, `EVALUATION_MISSING` otherwise) — no state hides an unevaluated participant, mirroring SLC-18's "no state hides a shortfall" principle for delivery quantity.
5. **The one correction this slice needed, and how small it was (CR-63):** `AGG-KNOWLEDGE-OBJECT`'s lesson-drafting guard restricted terminal sources to `{task, plan, incident}` (`REQ-KNW-002`). A completed Simulation is a fourth legitimate terminal source for an After Action Review (R3-Q5's reuse decision). The payload field (`source:urn`) was already untyped — CR-63 broadens only the guard text and `REQ-KNW-002`'s statement, exactly the same minimal footprint as CR-62.
6. **No auto-retry after an aborted exercise (found during design, not left implicit):** once IN_PROGRESS, an exercise cannot be cancelled — it resolves to COMPLETED or ABORTED only, driven by its simulation. Covering a training gap after an abort requires an explicit new `CMD-EXR-PLAN`; this is an intentional simplification (A17), the same choice SLC-18 made for undelivered partial-shipment quantity, not an oversight (FM-S19-01).

## Housekeeping
Property ids for this slice start at P-175 (P-170..174 belong to SLC-18).

## Gates
R1: G6 RATIFIED (2026-09-27) · R2: all 6 slices DESIGN COMPLETE, G6 held (RSK-027) · SLC-17: DESIGN COMPLETE, G6 held (RSK-028) · SLC-18: DESIGN COMPLETE, G6 held (RSK-028) · **SLC-19 DESIGN COMPLETE** — G6 held (RSK-028; portfolio-level hold, though this slice's own technical exposure to it is the narrowest of the three R3 slices — see `14-slices/SLC-19/readiness.md`).

## Next recommended session
**R3 is now fully designed** (SLC-17, SLC-18, SLC-19 all DESIGN COMPLETE). No further R3 slice design remains. The next recommended session is **R1 and R2 pilot review** — the gate every R3 slice's G6 is held behind (RSK-027, RSK-028) — followed by G6 ratification for R2 and R3 once that evidence exists. Until a pilot review is actually run, no further detailed design should proceed; this matches `01-business/release-3-scope.md` §3's original timing caution, which the project owner has so far overridden slice-by-slice rather than lifted wholesale.
