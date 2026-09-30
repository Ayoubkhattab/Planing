---
id: G6-SLC-03
type: slice-readiness
title: Slice Readiness — SLC-03 Task Lifecycle (G6-SLC)
wave: W7
slice: SLC-03
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, depends_on: [G6-SLC-01]}
---

# G6-SLC-03 — Task Lifecycle (+ Task Types, Qualifications & Eligibility)

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

| الشرط | الحالة |
|---|---|
| SLC-01 READY | ✓ |
| البنود الأحد عشر | ✓ |
| الفحص | 0 مخالفات — 33 أمراً، 36 حدثاً، 6 استعلامات، 3 مصفوفات كاملة |
| OpenAPI (BC04 32 + BC05 7 عملية) | valid؛ 6 أوامر موسومة `x-offline-capable` |
| القبول | 86 انتقالاً + 306 رفضاً (مولدة) + 22 سيناريو + 9 خصائص |
| Threat model / FMEA | 6 تهديدات (كلها L متبقية) / 4 أنماط فشل |
| التتبع | 11 متطلباً، 0 بلا اختبار |
| الأسئلة المفتوحة OQ-031..033 | **مغلقة** (SPEC-TASK-RULES §1) |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-TASK | ✓ 9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-TASK-TYPE | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-QUALIFICATION-RECORD | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| COMPLETED | آلي عند الاعتماد إن كانت كل المعايير آلية ومستوفاة؛ وإلا بأمر إكمال مع إقرارات |
| CLOSED | يدوي، أو آلي بعد 7 أيام بلا متابعات مفتوحة |
| انتهاء المهلة | تصعيد افتراضياً؛ EXPIRED فقط إن أعلن النوع expires_on_due |
| الرفض | نهائي؛ إعادة المحاولة مهمة متابعة جديدة |
| التعليق | علم متعامد لا حالة (CR-46) |
| الإسناد | لمستخدم واحد؛ تصريح ≥ تصنيف المهمة؛ أهلية مفحوصة وقت الإسناد؛ fail-closed |
| المعايير | مجمّدة من ASSIGNED |
| الأوامر دون اتصال | ACCEPT، START، BLOCK، RESUME، ADD-RESULT-ITEM، SUBMIT فقط |
| زمن التصعيد | ≤ 60 ث بعد الموعد |
