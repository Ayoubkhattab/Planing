---
id: ATAM-SLC18
type: architecture-review
title: ATAM-lite Review — SLC-18
wave: W7
slice: SLC-18
status: DRAFT
---

# ATAM-lite — SLC-18

**المفاضلات:** إعادة استخدام AGG-RESOURCE-POOL/AGG-ALLOCATION الكاملة للمخزون بدل محرك تخصيص ثانٍ توفّر كوداً ومنطق تنافس مُختبَراً مسبقاً، مقابل حِمل معرفي أعلى على من يقرأ عقد Allocation لأول مرة (يحتاج فهم أن `target` قد يشير لآن إلى Task أو Activity أو Logistics Request — CR-62). ربط AGG-LOGISTICS-REQUEST بحالته عبر أحداث نظامية من AGG-ALLOCATION بدل أمر تصريح مباشر يبسّط منع الازدواج لكنه يجعل تتبّع "لماذا صار الطلب APPROVED" يتطلب تتبّع الحدث المصدر في تخصيص آخر — قرار مقصود، موثَّق في SPEC-LOGISTICS §3 وليس أثراً جانبياً صامتاً. عدم وجود Aggregate مستقل للمخزون (Inventory) أو الموقع (Storage) أو الحركة (Movement) يقلل عدد الكيانات الجديدة إلى اثنين فقط (Logistics Request، Shipment) مقابل تسمية أقل "حرفية" مقارنة بعناصر DOM-16 الستة الأصلية — نفس نمط SLC-17 مع DOM-17. أعلى مخاطرة معمارية فعلية هنا (خلافاً لـ SLC-17) هي أن SLC-18 تعتمد مباشرة على SLC-09 (R2) غير المقاس، لا على R1 المُصادَق عليه فقط — موثَّقة صراحة في `03-domain/contexts/BC05/logistics-spec.md` §8 وفي `14-slices/SLC-18/readiness.md`، لا مخفية.
