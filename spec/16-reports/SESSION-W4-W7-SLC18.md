---
id: SESSION-SLC18
type: session-report
wave: W4–W7 (SLC-18, Release 3)
date: 2026-09-27
basis: V6§21.3
---

# SESSION REPORT — SLC-18 Logistics & Supply (R3) — second R3 slice

**Result:** **DESIGN COMPLETE.** G6 held until the R1 pilot review **and** the R2 pilot review (RSK-028 — and, unlike SLC-17, this slice's actual technical dependency (SLC-09) really is R2, unmeasured; see `14-slices/SLC-18/readiness.md`).

| Output (computed) | Count |
|---|---|
| Aggregates: Logistics Request, Shipment (BC05) | 2 · 9 invariants |
| Commands / queries / events | 10 / 5 / 15 |
| OpenAPI | 15 operations — validated |
| Hand-written acceptance scenarios | 9 · 5 properties |
| Cross-slice corrections | CR-62 (AGG-ALLOCATION, SLC-09) — applied and regenerated; round-trip verified (guard text only, payload schema unchanged) |

## Key design points
1. **Two aggregates, not six:** DOM-16 names Inventory, Shipment, Movement, Supply, Storage and Logistics Request, but only Logistics Request and Shipment get new aggregates — the same reduction pattern SLC-17 applied to DOM-17's eight named elements. Inventory and Storage are AGG-RESOURCE-POOL (SLC-09) unmodified, scoped by item type and location; Movement is an append-only `MovementEvent` history inside Shipment, not its own identity; Supply is the name for the capability the two aggregates jointly provide, not a third entity.
2. **No second allocation engine (R3-Q3):** every quantity commitment — logistics or otherwise — goes through the one AGG-ALLOCATION and its capacity ledger. The only correction needed was CR-62: broadening `CMD-ALC-REQUEST`'s guard text so `target` may reference a Logistics Request as a third alternative to task/activity. The payload field (`target!:urn`) was already generic, so this was a one-line prose correction, not a schema change — confirmed by regenerating SLC-09's contracts and diffing byte-for-byte against the committed files (only the two guard-text lines changed; OpenAPI, AsyncAPI, errors and acceptance state machines were identical).
3. **A Logistics Request never approves itself:** it has no approval command of its own. Every REQUESTED → APPROVED/PENDING_APPROVAL/REJECTED transition is a `SYS:` transition driven by its linked Allocation's own events (EVT-ALC-COMMITTED/-APPROVAL-REQUIRED/-REJECTED) — full delegation to an already-approved mechanism, not a duplicated one, and fully visible in the state × command matrix (SL-05), not a hidden side effect.
4. **Delivery is never rounded up:** `delivered_quantity` is a required, explicit field at `CMD-SHP-DELIVER`. A Logistics Request reaches FULFILLED only when it equals the requested quantity; anything less — including a total loss reported via `CMD-SHP-REPORT-LOST` — resolves to PARTIALLY_FULFILLED. Consumption on the linked Allocation is recorded only from a confirmed shipment outcome, never speculatively at dispatch (INV-LGR-05).
5. **Departure re-checks capacity, not just creation:** `CMD-SHP-PLAN` and `CMD-SHP-DEPART` both require the linked Allocation still COMMITTED for at least the shipped quantity at that instant (INV-SHP-03), closing the race where a request is cancelled concurrently with shipment planning (FM-S18-02).
6. **Found during design, not left for later (FM-S18-01):** logistics requests and task/plan allocations now compete for the same pools and the same priority/time ordering window. No new contention rule was introduced — the same levers SLC-09 already exposes (priority, pre-emption, per-tenant pool configuration) apply directly — but this is a real, not hypothetical, new load on infrastructure sized only from SLC-09's own unmeasured estimates.

## Housekeeping
Property ids for this slice start at P-170 (P-165..169 belong to SLC-17).

## Gates
R1: G6 RATIFIED (2026-09-27) · R2: all 6 slices DESIGN COMPLETE, G6 held (RSK-027) · SLC-17: DESIGN COMPLETE, G6 held (RSK-028) · **SLC-18 DESIGN COMPLETE** — G6 held (RSK-028; this slice's own technical dependency, SLC-09, is genuinely R2 and unmeasured, unlike SLC-17's R1-only actual dependency).

## Next recommended session
**SLC-19 — Training, Competency & Exercises** (CAP-08.05, DOM-18+19, BC05) — the last R3 slice; extends SLC-03's Qualification Record and SLC-09's Role Requirement, and stores After Action Review as an SLC-12 Knowledge Object (highest reuse among the three R3 slices per `01-business/release-3-scope.md` §2).
