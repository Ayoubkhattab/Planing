---
id: ADR-P03
type: adr
title: Importance Tiers
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-007
corrects:
- CR-10
verified_by:
- FIT-06
---

# ADR-P03: Importance Tiers

## Context and Problem
كلمة 'مهم' تحكم BRL-001/002/009/015 ومبادئ Provenance دون تعريف؛ تحدد حجم النظام وأداءه.

## Considered Options
1. T1 Evidential / T2 Governed / T3 Operational / T4 Ephemeral — لكل سمة
2. مستوى واحد لكل الكائن
3. تطبيق النموذج الكامل على كل شيء

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1 (مستويات لكل سمة).

## W1 Input (delegated answers)
Q12 → الخيار 1 — يُعتمد رسمياً في W3.

## Decision Outcome
**Importance tiers per attribute** — see `04-information/importance-tiers.md`.
- **T1 Evidential:** claim-based, bitemporal, source required, evidence optional, full confidence, conflict detection.
- **T2 Governed:** immutable versions, approval where defined, audit, effective time.
- **T3 Operational:** current value + audit record of change.
- **T4 Ephemeral:** no audit.

## Rationale
W1 Q12; avoids 'maximum rigor everywhere' anti-pattern.

## Consequences
- ✅ Rigor where decisions depend on it
- ✅ Simple CRUD where it does not
- ⚠️ Tier must be declared per attribute (enforced by SL-10)

## Impact
- **performance:** T3/T4 unaffected by claim overhead

## Verified By
FIT-06

## Previously Blocked By
UNK-007
