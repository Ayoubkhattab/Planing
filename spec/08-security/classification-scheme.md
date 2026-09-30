---
id: CLASSIFICATION-SCHEME
type: security-model
title: Classification Scheme Model
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-GOV-001, REQ-GOV-002, REQ-GOV-003, REQ-GOV-004], decided_by: [ADR-P04, ADR-P06]}
---

# Classification Scheme Model

## 1. البنية (لكل مستأجر)
```text
ClassificationScheme (T2, versioned, effective time)
  levels[]        ordered: {code, rank, label_ar, label_en, requires_dedicated_cell: bool}
  compartments[]  {code, label, owner_authority}          unlimited
  caveats[]       {code, label, rule: releasable_to[] | not_releasable_to[]}
  audit_threshold level rank at/above which reads are audited (REQ-FND-015)
  default_level   for new objects when creator does not choose (never below creator's org default)

Label on an object  = {level, compartments[], caveats[]}
Clearance on subject = {max_level, compartments[], nationality/org attributes for caveats}
```

## 2. القاعدة (REQ-GOV-003)
```text
READ allowed ⇔ rank(clearance.max_level) ≥ rank(label.level)
             ∧ label.compartments ⊆ clearance.compartments
             ∧ every caveat rule satisfied by subject attributes
             ∧ tenant(subject) = tenant(object)
             ∧ policy (PDP) returns ALLOW | CONDITIONAL(satisfied) | REDACT
```

## 3. الافتراضي (يمكن للمستأجر تغييره عند التهيئة)
| rank | code | الاسم | خلية مخصصة |
|---|---|---|---|
| 0 | PUBLIC | عام | لا |
| 1 | INTERNAL | داخلي | لا |
| 2 | CONFIDENTIAL | سري | لا |
| 3 | SECRET | سري للغاية | **نعم** (ADR-P04) |

## 4. التركيب والاشتقاق
- الكائن المركب (تقييم، منتج، تعارض) يأخذ **أعلى** تصنيف ومجموع الأقسام من مكوناته، ما لم يُخفَّض بقرار موثق (REQ-GOV-004).
- التخفيض (downgrade) قرار T2 يتطلب سلطة ويُسجل كإصدار.
- الادعاء قد يكون أعلى من كيانه؛ الكيان لا يرث تصنيف ادعاءاته.
- هوية المصدر البشري: افتراضياً أعلى بدرجة من معلوماته (claim-evidence-model §4).
