---
id: G6-SLC-16
type: slice-readiness
title: Slice Readiness — SLC-16 Enterprise Integrations (R2)
wave: W7
slice: SLC-16
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review (RSK-027) and tenant systems known (UNK-021)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {depends_on: [G6-SLC-01, G6-SLC-02, G6-SLC-06, G6-SLC-09]}
---

# SLC-16 — Enterprise Integrations

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1، وتعريف أنظمة المستأجر الفعلية (UNK-021) لبناء المحولات

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 4 / 12 |
| الفحص | 0 مخالفات — 18 أمراً، 25 حدثاً، 4 استعلامات |
| OpenAPI | 22 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 11 + 4 خصائص |
| التتبع | 4 متطلبات، 0 بلا اختبار |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-INTEGRATION-CONNECTION | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SENSOR-STREAM | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-HR-SYNC-PROPOSAL | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-CAP-MESSAGE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| اتجاه التكامل | وارد فقط لـ ERP/HRIS/DMS/CMMS؛ الصادر الوحيد CAP |
| HRIS | مقترحات فقط؛ المغادرة تُصعَّد بعد 14 يوماً؛ SCIM يبقى المسار الفوري |
| DMS | تصنيف عبر جدول مقابلة؛ غير المطابق = أعلى مستوى افتراضي |
| CMMS | نظام سجل التنفيذ؛ المنصة تعكس الحالة بأوامر مراقبة |
| الحساسات | دفعات ≤ 1,000؛ الجودة تعلّم ولا تحذف |
| CAP الصادر | مستوى إصدار خارجي لكل مستأجر؛ قالب فقط؛ شخصان |
| الاتصالات | قاعدة سماح واحدة لكل اتصال باعتماد شخص ثان |
