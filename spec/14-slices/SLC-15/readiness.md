---
id: G6-SLC-15
type: slice-readiness
title: Slice Readiness — SLC-15 Coordination & Correlation/Fusion (R2)
wave: W7
slice: SLC-15
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {depends_on: [G6-SLC-04, G6-SLC-08]}
---

# SLC-15 — Coordination Cases & Correlation/Fusion

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 3 / 10 |
| الفحص | 0 مخالفات — 17 أمراً، 19 حدثاً، 4 استعلامات |
| OpenAPI | 21 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 8 + 5 خصائص |
| التتبع | 4 متطلبات، 0 بلا اختبار |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-COORDINATION-CASE | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CORRELATION-PROPOSAL | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CORRELATION-RULE | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| نطاق التنسيق | داخل المستأجر فقط؛ بين المستأجرين عبر توزيع المنتجات |
| إجراءات تتطلب سلطة الغير | مقفلة حتى قرار مسجل عبر طلب قرار (SLC-08) |
| الربط | دلاء geohash6 × 10 دقائق؛ مصدران مستقلان على الأقل |
| قبول الربط | بشري دائماً؛ الآثار عبر أوامر المالك |
| الدمج | موقع موزون بعكس التباين؛ زمن بالتقاطع؛ النوع بالأغلبية والتعادل = نزاع |
| تفعيل القواعد | دقة الاقتراحات ≥ 70 % على مجموعة موسومة (يعاير بعد Pilot) |
