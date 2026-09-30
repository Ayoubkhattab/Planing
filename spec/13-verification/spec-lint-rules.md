---
id: LINT
type: spec-lint-rules
title: Spec Lint Rules
wave: W0
tier: T0
owner_role: Orchestrator
status: DRAFT
approved_by: null
approved_at: null
consumers:
- W7
- W9
---

# Spec Lint Rules

## rules

_29 items_

| id | rule | severity |
|---|---|---|
| SL-01 | كل BO له مالك واحد بالضبط | ERROR |
| SL-02 | كل CMD مرتبط بـ AGG وPOL | ERROR |
| SL-03 | كل CMD يغير الحالة ينتج EVT | ERROR |
| SL-04 | كل انتقال له CMD/trigger وحدث وشرط | ERROR |
| SL-05 | جدول حالات × أوامر كامل | ERROR |
| SL-06 | كل حالة غير نهائية تصل لحالة نهائية | ERROR |
| SL-07 | كل EVT له مخطط بإصدار ومستهلك | ERROR |
| SL-08 | كل API يرتبط بـ CMD أو QRY | ERROR |
| SL-09 | كل QRY يحدد الصلاحية ونطاق الاسترجاع | ERROR |
| SL-10 | كل BO T1 يحدد الأزمنة والدليل والثقة | ERROR |
| SL-11 | created_at/updated_at ليست زمن عمل | ERROR |
| SL-12 | كل سمة مكانية تحدد CRS والدقة | ERROR |
| SL-13 | لا قراءة عبر السياقات إلا بعقد معلن | ERROR |
| SL-14 | كل Projection تحدد مصدرها وإعادة بنائها وتأخرها وصلاحيتها | ERROR |
| SL-15 | كل REQ له acceptance_criteria وverification_method | ERROR |
| SL-16 | كل QAS بأولوية H له مقياس أو TBD بمالك | ERROR |
| SL-17 | كل THR بأثر H له ضابط أو قبول | ERROR |
| SL-18 | كل FM بشدة H له تعافٍ واختبار | ERROR |
| SL-19 | لا APPROVED دون approved_by وapproved_at | ERROR |
| SL-20 | كل معرّف في traces موجود | ERROR |
| SL-21 | كل عملية AI لها AIL | ERROR |
| SL-22 | UNK مفتوح يحجب الشريحة يمنع G6-SLC | ERROR |
| SL-23 | لا مخرج بلا مستهلك | WARNING |
| SL-24 | Aggregate بأكثر من 7 كيانات يحتاج تبريراً | WARNING |
| SL-25 | لا تقنية في W1–W7 دون ADR | WARNING |
| SL-26 | كل مصطلح في glossary.md | WARNING |
| SL-27 | حدث التكامل منفصل عن الحدث الداخلي | WARNING |
| SL-28 | السياسات fail-closed عند فشل المحرك | ERROR |
| SL-29 | كل Aggregate له مصدر تسمية في LABEL-DERIVATION (صريح / مشتق / إداري) | ERROR |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
rules:
- id: SL-01
  rule: كل BO له مالك واحد بالضبط
  severity: ERROR
- id: SL-02
  rule: كل CMD مرتبط بـ AGG وPOL
  severity: ERROR
- id: SL-03
  rule: كل CMD يغير الحالة ينتج EVT
  severity: ERROR
- id: SL-04
  rule: كل انتقال له CMD/trigger وحدث وشرط
  severity: ERROR
- id: SL-05
  rule: جدول حالات × أوامر كامل
  severity: ERROR
- id: SL-06
  rule: كل حالة غير نهائية تصل لحالة نهائية
  severity: ERROR
- id: SL-07
  rule: كل EVT له مخطط بإصدار ومستهلك
  severity: ERROR
- id: SL-08
  rule: كل API يرتبط بـ CMD أو QRY
  severity: ERROR
- id: SL-09
  rule: كل QRY يحدد الصلاحية ونطاق الاسترجاع
  severity: ERROR
- id: SL-10
  rule: كل BO T1 يحدد الأزمنة والدليل والثقة
  severity: ERROR
- id: SL-11
  rule: created_at/updated_at ليست زمن عمل
  severity: ERROR
- id: SL-12
  rule: كل سمة مكانية تحدد CRS والدقة
  severity: ERROR
- id: SL-13
  rule: لا قراءة عبر السياقات إلا بعقد معلن
  severity: ERROR
- id: SL-14
  rule: كل Projection تحدد مصدرها وإعادة بنائها وتأخرها وصلاحيتها
  severity: ERROR
- id: SL-15
  rule: كل REQ له acceptance_criteria وverification_method
  severity: ERROR
- id: SL-16
  rule: كل QAS بأولوية H له مقياس أو TBD بمالك
  severity: ERROR
- id: SL-17
  rule: كل THR بأثر H له ضابط أو قبول
  severity: ERROR
- id: SL-18
  rule: كل FM بشدة H له تعافٍ واختبار
  severity: ERROR
- id: SL-19
  rule: لا APPROVED دون approved_by وapproved_at
  severity: ERROR
- id: SL-20
  rule: كل معرّف في traces موجود
  severity: ERROR
- id: SL-21
  rule: كل عملية AI لها AIL
  severity: ERROR
- id: SL-22
  rule: UNK مفتوح يحجب الشريحة يمنع G6-SLC
  severity: ERROR
- id: SL-23
  rule: لا مخرج بلا مستهلك
  severity: WARNING
- id: SL-24
  rule: Aggregate بأكثر من 7 كيانات يحتاج تبريراً
  severity: WARNING
- id: SL-25
  rule: لا تقنية في W1–W7 دون ADR
  severity: WARNING
- id: SL-26
  rule: كل مصطلح في glossary.md
  severity: WARNING
- id: SL-27
  rule: حدث التكامل منفصل عن الحدث الداخلي
  severity: WARNING
- id: SL-28
  rule: السياسات fail-closed عند فشل المحرك
  severity: ERROR
- id: SL-29
  rule: كل Aggregate له مصدر تسمية في LABEL-DERIVATION (صريح / مشتق / إداري)
  severity: ERROR
```

</details>
