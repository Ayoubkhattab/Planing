---
id: PROP-SLC12A
type: property-spec
title: Property-Based Invariant Specifications — SLC-12a
wave: W6
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-12a

| ID | الخاصية |
|---|---|
| P-121 | لا سجل مشمول بتجميد نشط يصبح غير مقروء بسبب إتلاف أو محو |
| P-122 | بعد إتلاف مفتاح K: لأي تسلسل استعادات لاحق (بأي نسخة احتياطية)، K غير قابل للاستخدام بعد بوابة الاستعادة |
| P-123 | كل حاوية مُتلفة: كل سجلاتها تجاوزت الاحتفاظ وفق الجدول الساري عند الاعتماد |
| P-124 | لكل فئة سجلات في الجدول النشط قاعدة واحدة بالضبط |
| P-125 | التجميد لا يمنع أبداً إنشاء إصدار جديد |
