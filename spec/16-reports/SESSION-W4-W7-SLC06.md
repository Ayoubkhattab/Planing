---
id: SESSION-SLC06
type: session-report
wave: W4–W7 (SLC-06)
date: 2026-09-24
basis: V6§21.3
---

# SESSION REPORT — SLC-06 Situation, Alerts, Notifications & COP

**Result:** **G6-SLC-06 READY FOR IMPLEMENTATION (delegated).**

## Produced
| Output | Count |
|---|---|
| Aggregates: Situation, Alert Rule, Alert (BC03); Subscription, Notification (BC04) | 5 · 15 invariants (corrected; first stated 17) |
| Commands / queries / events | 22 / 8 / 30 |
| Component spec: membership criteria semantics, alert evaluation, COP, secured tiles (scope hash + data version), notification delivery incl. air-gapped push | 1 |
| OpenAPI (30 ops; criteria, alert-condition and vector-tile schemas) — validated · AsyncAPI (30) · errors (25) · logical model (10 tables) | — |
| Acceptance: 85 generated + 23 scenarios · 6 properties | — |
| Threats 7 · failure modes 5 · observability 7 · quality scenarios +3 | — |

## Key design points
1. **Two evaluators:** critical alerts are evaluated directly on the ingestion stream (≤ 5 s), independent of membership recomputation (≤ 10 s).
2. **All-or-nothing alert delivery:** users not cleared for an alert's label receive nothing — no redacted "something happened" alert that would itself leak.
3. **Tiles keyed by security scope and data version:** same-scope users share cache; different scopes never do; revocation changes the key, so stale tiles cannot be served.
4. **Reproducible membership:** every membership change records the definition version and causing event.
5. **Active rules are immutable,** and activation requires a 24-hour dry run showing expected alert volume — no silent suppression.
6. **Notifications carry references and safe templates only**, are re-checked at delivery, and — in an air-gapped deployment — use an internal push channel with polling fallback (new W8 input, RSK-023).

## Registers
RSK-023 added · HAP-09 evidence: SLC-06 · glossary +2 · W8 inputs +3.

## Gates
G0–G3 PASS · **G6-SLC-01..06 READY** · G6 release BLOCKED (remaining R1: SLC-07, 08, 11, 12a)

## Next recommended session
**SLC-07 — Analysis Case → Run → Finding → Assessment** (reproducibility and lineage of analytical work).
