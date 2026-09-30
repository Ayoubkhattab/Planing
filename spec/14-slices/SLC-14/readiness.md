---
id: G6-SLC-14
type: slice-readiness
title: Slice Readiness — SLC-14 Collection Requirements & Planning (R2)
wave: W7
slice: SLC-14
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {depends_on: [G6-SLC-02, G6-SLC-03, G6-SLC-11]}
---

# SLC-14 — Collection Requirements & Planning

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 2 / 6 |
| الفحص | 0 مخالفات — 14 أمراً، 16 حدثاً، 4 استعلامات |
| OpenAPI | 18 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 8 + 4 خصائص |
| التتبع | 3 متطلبات، 0 بلا اختبار |
| تغيير عابر | SLC-03: plan_ref يقبل خطة جمع (CR-59) — أُعيد التوليد |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-COLLECTION-REQUIREMENT | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-COLLECTION-PLAN | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| EEIs | إلزامية؛ كل منها يعرّف ما يُعد إجابة (أنواع، سمات، أساليب، كميات) |
| المطابقة | الملاحظات المعتمدة فقط؛ داخل المنطقة والنافذة |
| التحقق | يُحسب لكل مشاهد على ما يراه؛ لا إشارة لما يُخفى |
| الانتهاء | بتاريخ الاستحقاق فقط |
| التكليف | مهمة لكل نشاط عند التفعيل؛ plan_ref = خطة الجمع |
