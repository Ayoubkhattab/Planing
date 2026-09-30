---
id: PROP-SLC03
type: property-spec
title: Property-Based Invariant Specifications — SLC-03
wave: W6
slice: SLC-03
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Property-Based Invariants — SLC-03

| ID | الخاصية |
|---|---|
| P-31 | COMPLETED ⇒ كل المعايير satisfied (عند زمن الانتقال) |
| P-32 | لا مهمة تصل COMPLETED دون أن تمر بـ APPROVED |
| P-33 | suspended = true ⇒ لا تغيير حالة إلا UNSUSPEND أو CANCEL |
| P-34 | رسم الاعتماديات لا دوري بعد أي تسلسل EDIT/MARK-READY |
| P-35 | لكل مهمة في ASSIGNED فما بعد: snapshot الأهلية ∈ {ELIGIBLE, CONDITIONALLY_ELIGIBLE} وتصريح المسند ≥ التصنيف عند الإسناد |
| P-36 | المعتمد ≠ المسند إليه (مع SoD مفعل) |
| P-37 | المعايير لا تتغير بعد ASSIGNED |
| P-38 | إعادة تشغيل تسلسل أوامر دون اتصال بنفس client_command_id لا تغير الحالة مرة ثانية |
| P-39 | EligibilityCheck(at) مطابق لمرجع مستقل من تاريخ سجلات التأهيل لكل at |
