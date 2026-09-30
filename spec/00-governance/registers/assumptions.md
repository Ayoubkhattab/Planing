---
id: REG-ASM
type: register
title: Assumption Register
wave: W0
tier: T3
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers: []
---

# Assumption Register

## assumptions

_10 items_

| id | statement | source | epistemic | validation_needed | status | note |
|---|---|---|---|---|---|---|
| ASM-001 | PostgreSQL/PostGIS يكفي كمصدر حقيقة لكل الأعباء التشغيلية | PRJ§21, §50 | ASSUMED (implicit in PRJ) | WL-01, WL-03, ADR-P05 | confirmed_for_design | TD-01: PostgreSQL operational store for all contexts |
| ASM-002 | Multi-Tenancy مطلوب | PRJ§6 | ASSUMED (implicit in PRJ) | UNK-004, UNK-018 | confirmed_by_delegated_decision | Q6 |
| ASM-003 | الواجهات الثلاث مطلوبة في الإصدار الأول | PRJ§47, §75 | ASSUMED (implicit in PRJ) | UNK-020, HAP-02 | rejected | R1 = web + mobile; desktop deferred (Q10) |
| ASM-004 | المستخدمون عرب أساساً | INF من لغة PRJ | ASSUMED (implicit in PRJ) | UNK-011 | confirmed_by_delegated_decision | Q15 |
| ASM-005 | فريق قادر على تشغيل حزمة متعددة القواعد | PRJ§77 | ASSUMED (implicit in PRJ) | UNK-012 | open | ops capacity for 8 stateful services — RSK-026 |
| ASM-006 | ناقل أحداث مخصص مطلوب | PRJ§77 | ASSUMED (implicit in PRJ) | WL-06 | confirmed_by_evidence | TD-04 (WL-06a) |
| ASM-007 | قاعدة رسم مخصصة مطلوبة | PRJ§77 | ASSUMED (implicit in PRJ) | WL-08 | rejected | TD-03: no graph DB in R1 |
| ASM-008 | فريق تشغيل صغير في البداية؛ البساطة التشغيلية قيد ملزم | Q22 | ASSUMED (planning) | حجم الفريق الفعلي | adopted_for_design | — |
| ASM-009 | فريق هندسي واحد 6–10 مهندسين في R1، قابل للتوسع إلى 8 فرق | Q30 | ASSUMED (planning) | UNK-012 | adopted_for_design | — |
| ASM-010 | أرقام نطاق التصميم (Q7, Q11) أهداف تصميم لا توقعات طلب | Q7,Q11 | DECISION (design target) | قياس فعلي في Pilot؛ إعادة المعايرة إن تجاوز الواقع 50% من النطاق | adopted_for_design | — |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
assumptions:
- id: ASM-001
  statement: PostgreSQL/PostGIS يكفي كمصدر حقيقة لكل الأعباء التشغيلية
  source: PRJ§21, §50
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: WL-01, WL-03, ADR-P05
  status: confirmed_for_design
  note: 'TD-01: PostgreSQL operational store for all contexts'
- id: ASM-002
  statement: Multi-Tenancy مطلوب
  source: PRJ§6
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: UNK-004, UNK-018
  status: confirmed_by_delegated_decision
  note: Q6
- id: ASM-003
  statement: الواجهات الثلاث مطلوبة في الإصدار الأول
  source: PRJ§47, §75
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: UNK-020, HAP-02
  status: rejected
  note: R1 = web + mobile; desktop deferred (Q10)
- id: ASM-004
  statement: المستخدمون عرب أساساً
  source: INF من لغة PRJ
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: UNK-011
  status: confirmed_by_delegated_decision
  note: Q15
- id: ASM-005
  statement: فريق قادر على تشغيل حزمة متعددة القواعد
  source: PRJ§77
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: UNK-012
  status: open
  note: ops capacity for 8 stateful services — RSK-026
- id: ASM-006
  statement: ناقل أحداث مخصص مطلوب
  source: PRJ§77
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: WL-06
  status: confirmed_by_evidence
  note: TD-04 (WL-06a)
- id: ASM-007
  statement: قاعدة رسم مخصصة مطلوبة
  source: PRJ§77
  epistemic: ASSUMED (implicit in PRJ)
  validation_needed: WL-08
  status: rejected
  note: 'TD-03: no graph DB in R1'
- id: ASM-008
  statement: فريق تشغيل صغير في البداية؛ البساطة التشغيلية قيد ملزم
  source: Q22
  epistemic: ASSUMED (planning)
  validation_needed: حجم الفريق الفعلي
  status: adopted_for_design
- id: ASM-009
  statement: فريق هندسي واحد 6–10 مهندسين في R1، قابل للتوسع إلى 8 فرق
  source: Q30
  epistemic: ASSUMED (planning)
  validation_needed: UNK-012
  status: adopted_for_design
- id: ASM-010
  statement: أرقام نطاق التصميم (Q7, Q11) أهداف تصميم لا توقعات طلب
  source: Q7,Q11
  epistemic: DECISION (design target)
  validation_needed: قياس فعلي في Pilot؛ إعادة المعايرة إن تجاوز الواقع 50% من النطاق
  status: adopted_for_design
```

</details>
