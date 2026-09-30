---
id: PROP-SLC18
type: property-spec
title: Property-Based Invariant Specifications — SLC-18
wave: W6
slice: SLC-18
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---

# Property-Based Invariants — SLC-18

| ID | الخاصية |
|---|---|
| P-170 | كل انتقال REQUESTED→APPROVED/PENDING_APPROVAL/REJECTED لطلب إمداد مصدره حصراً حدث من التخصيص المرتبط به (SLC-09)، لا أمر بشري مباشر |
| P-171 | delivered_quantity عند CMD-SHP-DELIVER وdamaged_quantity عند CMD-SHP-REPORT-DAMAGE لا تتجاوزان planned_quantity أبداً |
| P-172 | طلب الإمداد يصبح FULFILLED إذا وفقط إذا كانت delivered_quantity لشحنته المرتبطة تساوي الكمية المطلوبة؛ أي نقصان ينتج PARTIALLY_FULFILLED |
| P-173 | نقاط تتبع أي شحنة متزايدة زمنياً بصرامة دوماً (append-only، بلا فجوات أو تعديل) |
| P-174 | لا يُسجَّل CMD-ALC-RECORD-CONSUMPTION على تخصيص مرتبط بطلب إمداد قبل وصول شحنته إلى حالة نهائية (DELIVERED أو DAMAGED أو LOST) |
