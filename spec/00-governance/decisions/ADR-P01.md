---
id: ADR-P01
type: adr
title: Temporal Model
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-007
- UNK-015
corrects:
- CR-04
- CR-25
verified_by:
- QAS-TMP-001
- FIT-05
---

# ADR-P01: Temporal Model

## Context and Problem
خمسة أزمنة معرّفة في PRJ§3.5 و§22، لكن Envelope (PRJ§11) لا يمثل Event Time ولا Effective Time، وRecord Time لحظة لا فترة؛ وسؤال As-Of (PRJ§103) غامض.

## Considered Options
1. ثنائي الزمن كامل (فترة Valid + فترة Record) لكائنات T1، مع Event/Observation/Effective كسمات حسب النوع
2. زمن أحادي (Valid) + جدول إصدارات مؤرخ
3. Event Sourcing وإعادة البناء من الأحداث

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1 لـ T1 والخيار 2 لـ T2 — لأنه وحده يجيب عن 'ماذا كنا نعرف في تاريخ X' دون إعادة تشغيل الأحداث.

## W1 Input (delegated answers)
Q13 → الخيار 1 (T1) — يُعتمد رسمياً في W3.

## Decision Outcome
**Option 1 — Bitemporal for T1, versioned valid-time for T2.**
- T1 claims carry two half-open intervals in UTC with microsecond precision: `valid = [valid_from, valid_to)` and `record = [recorded_from, recorded_to)`. Open ends are explicit `null` meaning +∞.
- `recorded_from/recorded_to` are assigned **only by the server**. Clients never set record time.
- Semantic times are attributes on the types that need them: `event_time` (interval + precision), `observed_at` (instant), `effective_from/effective_to` (decisions, plans, policies).
- Temporal precision is first-class: `precision ∈ {instant, second, minute, hour, day, month, year, decade, unknown}` plus optional `uncertainty` bounds.
- T2 objects keep immutable versions; each version has `effective_from/to` and a server-assigned `recorded_at`.
- Query semantics: `AS OF VALID t` and `AS KNOWN AT k`; defaults: both = now.
- Reconstruction results are labeled `RECORDED | RECONSTRUCTED | INFERRED | UNKNOWN` (CR-25).

## Rationale
W1 Q13 requires both 'what was true at t' and 'what did we know at k'. Only option 1 answers the second directly without replaying events.

## Consequences
- ✅ Decision audits can reproduce exactly what was known at decision time
- ✅ Corrections never destroy history
- ✅ Fuzzy historical dates are representable
- ⚠️ Every T1 query needs temporal predicates (mitigated: 'current' views materialized)
- ⚠️ Storage grows with corrections (mitigated: tiered storage SR-08)

## Impact
- **performance:** current-state views materialized; as-of queries on indexed intervals
- **storage:** ~1.2–2× T1 volume (estimate, INF)
- **migration:** legacy data imported with record_from = import time and valid time from source when known

## Verified By
QAS-TMP-001, FIT-05

## Previously Blocked By
UNK-007, UNK-015
