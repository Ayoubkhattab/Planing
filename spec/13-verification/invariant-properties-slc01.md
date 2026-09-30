---
id: PROP-SLC01
type: property-spec
title: Property-Based Invariant Specifications — SLC-01
wave: W6
slice: SLC-01
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-01

يُولَّد تسلسل عشوائي من الأوامر (صالحة وغير صالحة، بفاعلين متعددين وأزمنة متقدمة)، ثم يُتحقق بعد كل خطوة من الخصائص التالية.

| ID | الخاصية | Aggregate |
|---|---|---|
| P-01 | الحالة ∈ states دائماً؛ لا انتقال خارج مصفوفة SM | الكل |
| P-02 | لا أمر يغير حالة نهائية | الكل |
| P-03 | version يزيد بـ 1 بالضبط لكل أمر مقبول، ولا يتغير لأمر مرفوض | الكل |
| P-04 | عدد الأحداث في outbox = عدد الأوامر المقبولة = عدد سجلات audit_outbox للأوامر | الكل |
| P-05 | شجرة الوحدات تبقى شجرة (جذر واحد، لا دورات) | ORGANIZATION |
| P-06 | لكل مستخدم ≤ 1 clearance غير نهائي | CLEARANCE |
| P-07 | لكل منحة مفوضة: scope ⊆ parent، limits ≤ parent، period ⊆ parent، depth ≤ 2 | AUTHORITY-GRANT |
| P-08 | AuthorityCheck(t) مطابق لمرجع مستقل (oracle) يحسب الفعالية من التاريخ لكل t | AUTHORITY-GRANT |
| P-09 | لا مستخدم لديه دوران متعارضان فعالان معاً | ROLE-ASSIGNMENT |
| P-10 | ACTIVE user ⇒ identities ≥ 1 ∧ tenant ACTIVE | USER |
| P-11 | لكل مستأجر: نسخة ACTIVE واحدة بالضبط من scheme ومن policy set | SCHEME, POLICY-SET |
| P-12 | ACTIVE exception ⇒ 2 موافقين متمايزين ≠ المقدم ∧ المدة ≤ 30 يوماً | SECURITY-EXCEPTION |
| P-13 | أي حدث security-affecting ⇒ security_version للموضوعات المتأثرة يزيد | USER, RAS, CLR, AUT, ROL, CLS, POL |
| P-14 | إعادة إرسال نفس Idempotency-Key بنفس الحمولة ⇒ نفس النتيجة دون أثر إضافي | الكل |
