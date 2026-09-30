---
id: PROP-SLC04
type: property-spec
title: Property-Based Invariant Specifications — SLC-04
wave: W6
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-04

| ID | الخاصية |
|---|---|
| P-41 | لا عملية دمج أو فصل تغير `subject_urn` أو أي حقل في أي ادعاء |
| P-42 | بعد أي تسلسل match/split: `split(match(x))` يعيد `resolve` لكل كيان إلى ما كان عليه قبل الدمج (مع الادعاءات الجديدة على موضوعها الأصلي) |
| P-43 | لا عنقود حالي يحتوي زوجاً مرتبطاً بـ NOT_A_MATCH حالي |
| P-44 | identity_clusters = المكونات المتصلة لروابط MATCH الحالية (مطابقة كاملة بعد كل خطوة) |
| P-45 | canonical = أصغر ULID في العنقود دائماً |
| P-46 | لكل (عنقود، سمة، نافذة): ≤ 1 تعارض غير نهائي |
| P-47 | تشغيل كاشف التعارضات مرتين متتاليتين على نفس الحالة لا ينتج أحداثاً في المرة الثانية |
| P-48 | لأي مستخدم: التعارضات المرئية ⊆ التعارضات التي يرى ≥ 2 من أعضائها المتعارضين |
