---
id: PROP-SLC06
type: property-spec
title: Property-Based Invariant Specifications — SLC-06
wave: W6
slice: SLC-06
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-06

| ID | الخاصية |
|---|---|
| P-61 | عضوية الموقف عند t = دالة (نسخة التعريف الفعالة عند t، حالة الكائنات عند t) — إعادة الحساب من التاريخ تعطي نفس السجل |
| P-62 | ≤ 1 تنبيه غير نهائي لكل (قاعدة، موضوع) داخل نافذة التكرار |
| P-63 | مجموعة مستلمي أي تنبيه ⊆ المشتركين المصرح لهم بتسمية التنبيه |
| P-64 | picture_U(S ∪ H) = picture_U(S) و tile_U(S ∪ H) = tile_U(S) لأي أعضاء مخفيين H (عدم الاستدلال) |
| P-65 | لا حمولة دفع تحتوي نصاً خارج قائمة القوالب الآمنة |
| P-66 | لا إشعار في حالة SENT لمستلم فقد الصلاحية قبل لحظة الإرسال |
