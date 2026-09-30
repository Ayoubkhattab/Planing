---
id: G6-SLC-04
type: slice-readiness
title: Slice Readiness — SLC-04 Conflict & Entity Resolution (G6-SLC)
wave: W7
slice: SLC-04
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, depends_on: [G6-SLC-01, G6-SLC-02]}
---

# G6-SLC-04 — Conflict Management & Entity Resolution

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

| الشرط | الحالة |
|---|---|
| SLC-01 و SLC-02 READY | ✓ |
| البنود الأحد عشر لكل Aggregate | ✓ |
| الفحص (SL-02..SL-09, SL-24) | 0 مخالفات — 19 أمراً، 23 حدثاً، 6 استعلامات، 3 مصفوفات كاملة، كل الحالات تصل لنهاية |
| OpenAPI (25 عملية) | valid |
| القبول | 21 انتقالاً + 98 رفضاً (مولدة) + 20 سيناريو + 8 خصائص |
| Threat model / FMEA | 7 تهديدات (كلها L متبقية) / 4 أنماط فشل |
| التتبع | 6 متطلبات، 0 بلا اختبار |
| مجهولات حاجبة | 0 |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-CONFLICT | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ER-CASE | ✓ 6 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-MATCH-RULESET | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| الدمج الآلي | ممنوع دائماً؛ الآلة تقترح فقط |
| حجم العنقود | > 50 عضواً يتطلب مراجعاً ثانياً |
| الفصل | مقدم الطلب ≠ المنفذ |
| حل التعارض | المراجع ≠ صاحب الادعاء المفضل |
| مرشحون لكل كيان | ≤ 10 لكل تشغيل |
| تفعيل قواعد المطابقة | استدعاء ≥ 95 %، دقة ≥ 60 % على مجموعة موسومة عربية/إنجليزية |
| أزمنة | كشف التعارض ≤ 30 ث، ظهور المرشحين ≤ 60 ث (p95) |
| تغيير عابر للشرائح | مكتبة LIB-CLAIMS-KERNEL §7: الحل عبر العناقيد؛ QRY-ENT-RESOLVED يعيد canonical_urn |

## ترتيب البناء
1. same_as_links + identity_clusters + امتداد المكتبة (§7) مع P-41..P-45.
2. ER Case + Match Ruleset + مولّد المرشحين + مجموعة التقييم.
3. Conflict + محرك الكشف (P-46, P-47).
