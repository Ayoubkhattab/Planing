---
id: SESSION-SLC16
type: session-report
wave: W4–W7 (SLC-16, Release 2)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-16 Enterprise Integrations (R2) — last R2 slice

**Result:** **DESIGN COMPLETE** (G6 held until the R1 pilot review and the tenants' actual systems are known — UNK-021).

| Output (computed) | Count |
|---|---|
| Aggregates: Integration Connection, Sensor Stream (BC07); HR Sync Proposal (BC01); CAP Message (BC03) | 4 · 12 invariants |
| Commands / queries / events | 18 / 4 / 25 |
| OpenAPI | 22 operations — validated |
| Hand-written acceptance scenarios | 11 · 4 properties |

## Key design points
1. **Sources, never sinks:** ERP, HRIS, DMS and CMMS only feed the platform through adapters, as claims with source reliability; conflicts open conflicts, nothing is overwritten; no writes back in R2.
2. **HR changes are proposals:** moves and departures propose role changes for an administrator; departures escalate; account disablement via SCIM stays immediate.
3. **One path out:** CAP 1.2 messages built from a reviewed template, capped by the tenant's external release level, released by a second person.
4. **Every connection is a firewall decision:** one allow-list entry per connection, approved by another person; suspension closes it at once.
5. **Sensors at design rate:** streams feed observation batches with idempotency; quality rules annotate readings rather than dropping them.

## Found and fixed during the slice
A hand-written scenario expected outbound ERP connections to be rejected at registration, while the guard sat on activation — aligned by moving the rule to registration in the source data and regenerating.

## R2 status
All six R2 slices are DESIGN COMPLETE: SLC-09, 12, 10, 14, 15, 16.

## Next recommended session
**R2 baseline consolidation** (W9-style): global consistency and coverage checks for R2, anti-pattern and architecture review, R2 traceability, Engineering Baseline R2 (design), and the list of conditions tied to the R1 pilot.
