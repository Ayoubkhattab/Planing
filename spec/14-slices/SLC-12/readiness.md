---
id: G6-SLC-12
type: slice-readiness
title: Slice Readiness — SLC-12 Products, Knowledge, Archive & Reconstruction (R2)
wave: W7
slice: SLC-12
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {depends_on: [G6-SLC-07, G6-SLC-08, G6-SLC-12a]}
---

# SLC-12 — Products, Knowledge & Lessons, Archive, Historical Reconstruction

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1 (RSK-027)

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 6 / 19 |
| الفحص | 0 مخالفات — 29 أمراً، 42 حدثاً، 8 استعلامات |
| OpenAPI | 37 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 16 |
| التتبع | 12 متطلباً، 0 بلا اختبار |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-PRODUCT-TEMPLATE | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-PRODUCT | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-DISTRIBUTION | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-KNOWLEDGE-OBJECT | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ARCHIVE-PACKAGE | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-RECONSTRUCTION | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| ربط بيانات القوالب | استعلامات منصة معلنة فقط، تُنفذ بصلاحيات المؤلف |
| المحتوى فوق تسمية المنتج | يُستبعد دون أي أثر مرئي؛ يُسجل للتدقيق فقط |
| تثبيت بيانات المنتج | known_at = لحظة التوليد |
| العلامة المائية | مرئية + غير مرئية لكل نسخة |
| الحزم الأرشيفية | BagIt + بيانات حفظ على نمط PREMIS؛ الأصل + تمثيل حفظ؛ WORM؛ فحص سنوي |
| طبقات الاسترجاع | warm ≤ دقيقة؛ cold ≤ 24 ساعة |
| إعادة البناء | بصلاحيات الطالب؛ كل عنصر موسوم؛ حتمية |
| المعرفة السياساتية | لا تغير الصلاحيات أبداً |
