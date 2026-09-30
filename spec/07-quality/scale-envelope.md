---
id: SCALE-ENVELOPE
type: quality
title: Design Scale Envelope & Scale-Ready Principles
wave: W1
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Design Scale Envelope & Scale-Ready Principles

**principle:** SR-00 Scale-Ready, not Scale-First: كل مكوّن له مسار توسع مصمم ومختبر، لكن لا يُنشر تعقيد قبل أن يثبت القياس حاجته.

## envelope

_10 items_

| dimension | pilot | design | growth_path |
|---|---|---|---|
| users_total | 500 | 50000 | 500000 |
| users_concurrent | 100 | 5000 | 50000 |
| tenants | 1-3 | 100 | 1000+ (cells) |
| events_per_second_sustained | 100 | 5000 | partitioned scale-out |
| events_per_second_burst | TBD | 50000 | backpressure + buffering |
| operational_structured_data | TBD | 10 TB | partition / cell |
| object_storage | TBD | PB-class | object store scale-out |
| entities_and_claims | TBD | 1e8 | partition by tenant |
| observations | TBD | 1e9 | time + tenant partitioning |
| offline_duration | 72h | 7d | — |

**rule:** كل مكوّن يثبت 10× نطاق Pilot دون تغيير معماري؛ إعادة المعايرة إذا تجاوز الواقع 50% من نطاق التصميم

## scale_ready_principles

_12 items_

| id | rule |
|---|---|
| SR-01 | طبقات الحوسبة عديمة الحالة (stateless) وقابلة للتوسع الأفقي |
| SR-02 | tenant_id جزء من مفتاح التقسيم لكل بيانات؛ لا استعلام يعبر المستأجرين |
| SR-03 | كل حدث له مفتاح تقسيم (aggregate id) يضمن الترتيب محلياً ويسمح بالتوازي |
| SR-04 | كل الإسقاطات قابلة لإعادة البناء والتجزئة |
| SR-05 | الملفات الكبيرة في Object Storage فقط، وليس في قاعدة البيانات التشغيلية |
| SR-06 | العمليات الثقيلة (Raster، OCR، AI Batch، Reconstruction) غير متزامنة عبر Jobs |
| SR-07 | حصص (Quotas) وحدود معدل لكل مستأجر لمنع تأثير المستأجر المزعج |
| SR-08 | بيانات السلاسل الزمنية الكبيرة (ملاحظات، قياسات) مقسمة زمنياً ومستأجرياً مع سياسة تقادم (hot/warm/cold) |
| SR-09 | نمط الخلايا (Cells): المستأجر الكبير أو السيادي في خلية مستقلة بنفس الكود |
| SR-10 | لا مكوّن جديد (بحث، رسم، ناقل أحداث مخصص) قبل أن يثبت القياس حاجته — ADR-P05 |
| SR-11 | التحليلات معزولة عن التشغيل ولا تنافسه على الموارد |
| SR-12 | كل واجهة تدعم Pagination بالمؤشر (cursor)، لا بالإزاحة، للجداول الكبيرة |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
principle: 'SR-00 Scale-Ready, not Scale-First: كل مكوّن له مسار توسع مصمم ومختبر، لكن لا يُنشر تعقيد قبل أن يثبت القياس حاجته.'
envelope:
- dimension: users_total
  pilot: 500
  design: 50000
  growth_path: 500000
- dimension: users_concurrent
  pilot: 100
  design: 5000
  growth_path: 50000
- dimension: tenants
  pilot: 1-3
  design: 100
  growth_path: 1000+ (cells)
- dimension: events_per_second_sustained
  pilot: 100
  design: 5000
  growth_path: partitioned scale-out
- dimension: events_per_second_burst
  pilot: TBD
  design: 50000
  growth_path: backpressure + buffering
- dimension: operational_structured_data
  pilot: TBD
  design: 10 TB
  growth_path: partition / cell
- dimension: object_storage
  pilot: TBD
  design: PB-class
  growth_path: object store scale-out
- dimension: entities_and_claims
  pilot: TBD
  design: 1e8
  growth_path: partition by tenant
- dimension: observations
  pilot: TBD
  design: 1e9
  growth_path: time + tenant partitioning
- dimension: offline_duration
  pilot: 72h
  design: 7d
  growth_path: null
rule: كل مكوّن يثبت 10× نطاق Pilot دون تغيير معماري؛ إعادة المعايرة إذا تجاوز الواقع 50% من نطاق التصميم
scale_ready_principles:
- id: SR-01
  rule: طبقات الحوسبة عديمة الحالة (stateless) وقابلة للتوسع الأفقي
- id: SR-02
  rule: tenant_id جزء من مفتاح التقسيم لكل بيانات؛ لا استعلام يعبر المستأجرين
- id: SR-03
  rule: كل حدث له مفتاح تقسيم (aggregate id) يضمن الترتيب محلياً ويسمح بالتوازي
- id: SR-04
  rule: كل الإسقاطات قابلة لإعادة البناء والتجزئة
- id: SR-05
  rule: الملفات الكبيرة في Object Storage فقط، وليس في قاعدة البيانات التشغيلية
- id: SR-06
  rule: العمليات الثقيلة (Raster، OCR، AI Batch، Reconstruction) غير متزامنة عبر Jobs
- id: SR-07
  rule: حصص (Quotas) وحدود معدل لكل مستأجر لمنع تأثير المستأجر المزعج
- id: SR-08
  rule: بيانات السلاسل الزمنية الكبيرة (ملاحظات، قياسات) مقسمة زمنياً ومستأجرياً مع سياسة تقادم (hot/warm/cold)
- id: SR-09
  rule: 'نمط الخلايا (Cells): المستأجر الكبير أو السيادي في خلية مستقلة بنفس الكود'
- id: SR-10
  rule: لا مكوّن جديد (بحث، رسم، ناقل أحداث مخصص) قبل أن يثبت القياس حاجته — ADR-P05
- id: SR-11
  rule: التحليلات معزولة عن التشغيل ولا تنافسه على الموارد
- id: SR-12
  rule: كل واجهة تدعم Pagination بالمؤشر (cursor)، لا بالإزاحة، للجداول الكبيرة
```

</details>
