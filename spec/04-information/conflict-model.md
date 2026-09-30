---
id: CONFLICT-MODEL
type: information-model
title: Conflict Model
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-INF-025, REQ-OFF-004], rules: [BRL-002]}
---

# Conflict Model

## Conflict
```text
Conflict
  id, urn, subject_ref, predicate
  claim_refs[]          ≥ 2
  temporal_scope        overlap of the claims' valid intervals
  spatial_scope?        for geometric conflicts
  detected_by           rule code | user | sync (ADR-P09)
  status                OPEN → UNDER_REVIEW → RESOLVED | ACCEPTED_AS_CONFLICT ; any → SUPERSEDED
  resolution            {preferred_claim_ref?, rationale, decided_by, decided_at}
  security              = highest classification among its claims
```

## قواعد الكشف (RD-CONFLICT-RULES)
| القاعدة | الشرط |
|---|---|
| CF-01 single-value mismatch | predicate أحادي، فترات valid متداخلة، قيم مختلفة بعد التطبيع |
| CF-02 numeric tolerance | فرق يتجاوز تسامح الـ predicate |
| CF-03 spatial | مسافة بين هندستين > مجموع الدقتين × معامل الـ predicate |
| CF-04 temporal impossibility | حدث ينتهي قبل أن يبدأ، أو كيان في مكانين متباعدين بسرعة مستحيلة |
| CF-05 sync | أمر ميداني مغير للحالة على نسخة قديمة (ADR-P09) — **يُمثل بـ AGG-SYNC-CONFLICT في BC07، لا بـ Conflict هنا** (CR-49، SPEC-FIELD-SYNC §5) |

## القواعد
- الكشف **يفتح** تعارضاً ولا يغير أي ادعاء.
- `RESOLVED` يحدد ادعاءً مفضلاً للعرض؛ الادعاءات الأخرى تبقى بحالتها.
- `ACCEPTED_AS_CONFLICT`: التعارض حقيقي ويُعرض للمستخدمين كما هو (مثلاً روايتان متنافستان).
- ادعاء جديد يغير الحالة يجعل التعارض `SUPERSEDED` وقد يفتح تعارضاً جديداً.
- المستخدم الذي لا يملك صلاحية أحد الادعاءين لا يرى التعارض كتعارض؛ يرى فقط ما يحق له (A21).
