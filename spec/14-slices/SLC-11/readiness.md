---
id: G6-SLC-11
type: slice-readiness
title: Slice Readiness — SLC-11 Offline Field Capture & Sync (G6-SLC)
wave: W7
slice: SLC-11
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, depends_on: [G6-SLC-01, G6-SLC-02, G6-SLC-03]}
---

# G6-SLC-11 — Offline Field Capture & Synchronization

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

| الشرط | الحالة |
|---|---|
| SLC-01، 02، 03 READY | ✓ (عقود الأوامر الميدانية ثُبتت فيها مسبقاً) |
| البنود الأحد عشر (4 Aggregates) | ✓ |
| الفحص | 0 مخالفات — 16 أمراً، 25 حدثاً، 5 استعلامات |
| OpenAPI (BC01 8 + BC07 13 عملية؛ CommandEnvelope وSyncDelta) | valid |
| القبول | 19 + 69 (مولدة) + 17 سيناريو + 6 خصائص (نقاط انقطاع عشوائية) |
| Threat model / FMEA | 6 تهديدات (1 متبقٍ M مقبول) / 4 أنماط فشل |
| التتبع | 6 متطلبات، 0 بلا اختبار |
| تغيير عابر للشرائح | SLC-02: أوامر الإنشاء تقبل client_id (CR-50) — أُعيد توليد عقود SLC-02 وتحقق منها |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-DEVICE | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-PRELOAD-PACKAGE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SYNC-SESSION | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-SYNC-CONFLICT | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| الأجهزة | ≤ 3 نشطة لكل مستخدم؛ تسجيل بشهادة جهاز أو امتثال MDM |
| مستوى البيانات دون اتصال | افتراضياً INTERNAL كحد أقصى (قابل للتهيئة لكل مستأجر) |
| ما بعد 72 ساعة | الالتقاط يستمر، وقراءة البيانات المحملة تتوقف |
| الدفعات | ≤ 200 أمر، تسلسل متصل، توقيع لكل أمر، سلسلة hash |
| المعرّفات | ULID يولده الجهاز للكائنات الجديدة |
| الجهاز المفقود | إلغاء المفتاح فوراً، مسح عند أول اتصال، لا تطبيق لأي أمر بعد وقت الفقد |
| تعارضات المزامنة | كائن مستقل في BC07 (لا في محرك تعارض الادعاءات) |
