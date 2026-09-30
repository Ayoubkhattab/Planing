---
id: G6-SLC-12a
type: slice-readiness
title: Slice Readiness — SLC-12a Retention, Legal Hold, Disposition, Erasure (G6-SLC)
wave: W7
slice: SLC-12a
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, depends_on: [G6-SLC-01, G6-SLC-02, G6-SLC-03]}
---

# G6-SLC-12a — Retention, Legal Hold, Disposition & Erasure

## الحكم: **READY FOR IMPLEMENTATION (delegated)** — مع شرط قانوني قائم
**الشرط:** UNK-002 (الولاية القانونية الفعلية) يجب أن يُؤكد قبل G8 (الإنتاج): فترات الاحتفاظ الفعلية والأسس القانونية تُملأ في جدول الاحتفاظ عند تهيئة كل مستأجر. الآليات هنا مستقلة عن القيم.

| الشرط | الحالة |
|---|---|
| SLC-01، 02، 03 READY | ✓ |
| البنود الأحد عشر (4 Aggregates) | ✓ |
| الفحص | 0 مخالفات — 15 أمراً، 25 حدثاً، 5 استعلامات |
| OpenAPI (20 عملية؛ RetentionRule وHoldScopeItem وHoldCheck) | valid |
| القبول | 14 + 59 (مولدة) + 14 سيناريو + 5 خصائص |
| Threat model / FMEA | 5 تهديدات (كلها L) / 3 أنماط فشل |
| التتبع | 3 متطلبات، 0 بلا اختبار |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-RETENTION-SCHEDULE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-LEGAL-HOLD | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-DISPOSITION-RUN | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-ERASURE-REQUEST | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| وحدة الإتلاف | مفتاح لكل (فئة سجلات × شهر المحفز) |
| المحو | مفتاح لكل صاحب بيانات؛ حقائق التدقيق بمرجع مستعار |
| المجمّد داخل حاوية تُتلف | يُعاد لفه بمفتاح التجميد قبل الإتلاف |
| بوابة الاستعادة | إعادة تطبيق سجل الإتلاف قبل تشغيل أي خدمة؛ نسخ مخزن المفاتيح ≤ 35 يوماً |
| الاعتمادات | الجدول والإتلاف والمحو وفك التجميد: شخصان مختلفان دائماً |
| تقصير الاحتفاظ | غير رجعي إلا بقرار قانوني صريح |
