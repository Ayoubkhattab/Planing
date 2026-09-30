---
id: PROP-SLC02
type: property-spec
title: Property-Based Invariant Specifications — SLC-02
wave: W6
slice: SLC-02
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-02

P-01..P-04 و P-14 من SLC-01 تنطبق على كل Aggregate هنا. خصائص إضافية لمكتبة الادعاءات (LIB-CLAIMS-KERNEL):

| ID | الخاصية |
|---|---|
| P-21 | لأي تسلسل عمليات: لكل ClaimKey، فترات record للسجلات "الجارية لنفس القيمة المنطقية" لا تتداخل |
| P-22 | `resolve(T, K)` لا يتغير بعد أي عملية لاحقة زمنها > K (الماضي المعروف ثابت) |
| P-23 | `resolve(T, now)` بعد `correct` يساوي قيمة التصحيح لكل T في فترة البديل |
| P-24 | إزالة ادعاءات غير مرئية من المدخل ≡ تطبيق visibility (نفس الناتج) |
| P-25 | لا خانة `status = SINGLE` لقيمتين غير متوافقتين دون حل تعارض معروف عند K |
| P-26 | جدول current = إسقاط `record.to = ∞` من التاريخ (مطابقة كاملة بعد كل خطوة) |
| P-27 | التعميم المكاني حتمي ولا يحسّن الدقة أبداً (`accuracy_m` الناتج ≥ الأصلي) |
| P-28 | عدد الملاحظات بعد إعادة إرسال أي دفعة = عددها بعد الإرسال الأول |
