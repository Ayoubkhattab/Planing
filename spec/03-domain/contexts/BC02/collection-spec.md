---
id: SPEC-COLLECTION
type: component-specification
title: Collection Requirements — EEIs, Matching Engine, Viewer-Scoped Fulfilment, Tasking
wave: W4
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {requirements: [REQ-COL-001, REQ-COL-002, REQ-COL-003], quality: [QAS-COL-001], corrects: [CR-59], value_stream: VS01, recalibrate_after_pilot: true}
---

# Collection Requirements

## 1. عناصر المعلومات الأساسية (EEI)
كل متطلب جمع يُفكك إلى EEIs؛ كل EEI يحدد ما يعتبر إجابة: أنواع كيانات، سمات (predicates)، أساليب رصد، كميات قابلة للقياس. المتطلب بلا EEI لا يُقدَّم (REQ-COL-001).

## 2. محرك المطابقة (REQ-COL-003)
```text
on EVT-OBS-VALIDATED(o):
  for each APPROVED requirement r with area ∩ location(o) ≠ ∅ and window ∋ observed_at(o):     -- spatial index of active requirement areas
     for each EEI e of r:
        if method(o) ∈ e.observation_methods
           or ∃ derived claim c of o with predicate ∈ e.predicates / subject type ∈ e.entity_types
           or ∃ measurement m of o with quantity ∈ e.quantities:
              link (r, e, o) with lineage → EVT-CRQ-FULFILMENT-UPDATED
```
- الروابط تُسجل دائماً (بهوية نظام)؛ **الحساب المعروض يجري لكل مشاهد** على الروابط التي يرى ملاحظاتها.
- `fulfilment(r, viewer) = ANSWERED` إذا كان لكل EEI رابط مرئي، `PARTIAL` إذا كان لبعضها، وإلا `OPEN`.
- لا يعرض المتطلب عدد الروابط غير المرئية ولا وجودها (A21)؛ الانتهاء EXPIRED يعتمد على التاريخ فقط.

## 3. من الخطة إلى المهام (REQ-COL-002، CR-59)
- تفعيل خطة الجمع ينشئ مهمة ميدانية لكل نشاط عبر SLC-03 بنوع مهمة النشاط، و`plan_ref` = خطة الجمع (المرجع يقبل خطة عمليات أو خطة جمع).
- المهام الميدانية تدعم العمل دون اتصال (SLC-11)؛ الملاحظات الناتجة تُعتمد ثم تُطابق تلقائياً (§2).
- اكتمال كل مهام النشاطات يكمل الخطة.

## 4. لوحة الجمع
عرض مكاني للمتطلبات النشطة حسب الأولوية والموعد والتحقق (كما يراه المشاهد)، لتوجيه المخططين إلى الفجوات.
