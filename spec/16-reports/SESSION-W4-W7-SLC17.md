---
id: SESSION-SLC17
type: session-report
wave: W4–W7 (SLC-17, Release 3)
date: 2026-09-27
basis: V6§21.3
---

# SESSION REPORT — SLC-17 Risk & Contingency (R3) — first R3 slice

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review **and** the R2 pilot review (RSK-028 — stricter than R2's own RSK-027, as agreed for all of R3 in `release-3-scope.md` §3).

| Output (computed) | Count |
|---|---|
| Aggregates: Risk, Incident (BC04) | 2 · 10 invariants |
| Commands / queries / events | 15 / 5 / 17 |
| OpenAPI | 20 operations — validated |
| Hand-written acceptance scenarios | 10 · 5 properties |
| Cross-slice corrections | CR-60 (AGG-PLAN, SLC-08), CR-61 (AGG-TASK, SLC-03) — both applied and regenerated |

## Key design points
1. **Two aggregates, not six:** DOM-17 names Risk, Hazard, Incident, Emergency, Crisis, Response, Recovery and Continuity, but only Risk and Incident get new aggregates. Hazard is reference data (RD-HAZARD-CATEGORIES, same pattern as R2-Q1); Emergency/Crisis are severity levels on the same Incident, not separate identities; Response reuses Task (SLC-03); Continuity reuses Plan (SLC-08); Recovery is a computed query over the two, never a stored state.
2. **Reuse required two real cross-slice corrections, not just documentation:** AGG-PLAN gained `plan_kind` (OPERATIONS/CONTINGENCY) and an optional `triggered_by` (CR-60); AGG-TASK gained `incident_ref` as a third alternative to `plan_ref`/`ad_hoc_reason` (CR-61). Both regenerated cleanly; round-trip re-verified at 0 differences across all 17 slices afterward.
3. **Severity only moves one authorized step at a time:** escalation only increases severity, de-escalation is a distinct authorized command that decreases by at most one level, and every change is kept in an append-only SeverityHistory — no silent severity drift.
4. **Contingency activation is never a side effect:** escalating an incident's severity, by itself, never creates or activates a Plan. Only `CMD-INC-ACTIVATE-CONTINGENCY` does, and it needs its own authorization — the same Silent-Pre-emption lesson SLC-09 already established, reapplied here deliberately.
5. **A linked Risk never changes state automatically:** an Incident can reference the Risk it materialized from, and a closed Risk can record which Incident materialized it, but neither aggregate's lifecycle is ever driven by the other's commands.
6. **Found during design, not left for later (FM-S17-02):** closing an Incident does not require its linked contingency Plan to be closed too — recovery work may legitimately outlast incident closure. This is a recorded design trade-off (documented in the FMEA), not a gap.

## Housekeeping
Property ids for this slice start at P-165 (P-161..164 belong to SLC-16, the last R2 slice).

## Gates
R1: G6 RATIFIED (2026-09-27) · R2: all 6 slices DESIGN COMPLETE, G6 held (RSK-027) · **SLC-17 DESIGN COMPLETE** — G6 held (RSK-028, R1 **and** R2 pilot review required — stricter than the rest of R3's own default because it is the first R3 slice reviewed under that rule).

## Next recommended session
**SLC-18 — Logistics & Supply** (CAP-08.03, DOM-16, BC05) — depends on SLC-09's asset/resource model directly, so it is the slice where RSK-028's R2-dependency actually bites.
