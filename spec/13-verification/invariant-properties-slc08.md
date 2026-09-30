---
id: PROP-SLC08
type: property-spec
title: Property-Based Invariant Specifications — SLC-08
wave: W6
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-08

| ID | الخاصية |
|---|---|
| P-81 | لكل خطة: ≤ 1 إصدار BASELINED؛ ACTIVE ⇔ يوجد واحد بالضبط |
| P-82 | sync(v1→v2) مرتين = sync(v1→v2) مرة واحدة |
| P-83 | بعد sync(v1→v2): لكل نشاط task_generating في v2 مهمة غير نهائية واحدة بالضبط؛ لا مهمة غير نهائية لنشاط غير موجود في v2 |
| P-84 | محتوى أي إصدار BASELINED أو SUPERSEDED لا يتغير |
| P-85 | كل قرار RECORDED: AuthorityCheck(decider, type, scope, recorded_at) = true (يعاد التحقق من التاريخ) |
| P-86 | basis(D) لا يتغير بعد أي عمليات لاحقة على البيانات |
| P-87 | progress(T, K) لا يتغير بإضافة قياسات مسجلة بعد K |
