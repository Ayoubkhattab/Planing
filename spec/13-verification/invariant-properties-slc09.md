---
id: PROP-SLC09
type: property-spec
title: Property-Based Invariant Specifications — SLC-09
wave: W6
slice: SLC-09
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-09

| ID | الخاصية |
|---|---|
| P-91 | لكل مجمع وساعة: Σ الكميات الملتزمة ≤ السعة، تحت أي تسلسل متزامن من الطلبات والإفراجات والاستباقات |
| P-92 | دفتر السعة = مجموع التخصيصات الملتزمة (مطابقة كاملة بعد كل خطوة) |
| P-93 | لا حجزان نشطان ولا تعيينان نشطان متداخلان لنفس الأصل |
| P-94 | available(asset, w) = false عند وجود أي مانع من §4، وtrue عند غياب كل الموانع |
| P-95 | سلسلة الحيازة بلا فجوات |
| P-96 | readiness(t) مطابق لمرجع مستقل من تاريخ السجلات لكل t |
