---
id: PROP-SLC19
type: property-spec
title: Property-Based Invariant Specifications — SLC-19
wave: W6
slice: SLC-19
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
---

# Property-Based Invariants — SLC-19

| ID | الخاصية |
|---|---|
| P-175 | أي تمرين يُخطَّط له يُشير حصراً إلى سيناريو ACTIVE وقت الإنشاء، ويُجمَّد هذا المرجع (رقم الإصدار) بلا تغيير طوال حياة التمرين مهما تعدَّلت نسخ السيناريو لاحقاً |
| P-176 | أي انتقال IN_PROGRESS→COMPLETED أو IN_PROGRESS→ABORTED لتمرين مصدره حصراً حدث من المحاكاة المرتبطة به، لا أمر بشري مباشر |
| P-177 | نقاط تسليم الحقن ضمن أي محاكاة متزايدة زمنياً بصرامة دوماً (append-only، بلا فجوات أو تعديل) |
| P-178 | أي محاكاة تصل COMPLETED فقط إذا كان لكل مشارك في التمرين المرتبط بها تقييم واحد مسجَّل على الأقل |
| P-179 | المقيِّم في أي تقييم مسجَّل لا يساوي أبداً المشارك المقيَّم نفسه |
