---
id: G6-SLC-08
type: slice-readiness
title: Slice Readiness — SLC-08 Decision → Plan → Baseline → Tasks (G6-SLC)
wave: W7
slice: SLC-08
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {approval: HAP-09, depends_on: [G6-SLC-01, G6-SLC-03, G6-SLC-07]}
---

# G6-SLC-08 — Decision → Plan → Version → Baseline → Tasks

## الحكم: **READY FOR IMPLEMENTATION (delegated)**

| الشرط | الحالة |
|---|---|
| SLC-01، 03، 07 READY | ✓ |
| البنود الأحد عشر (5 Aggregates) | ✓ |
| الفحص | 0 مخالفات — 24 أمراً، 33 حدثاً، 9 استعلامات |
| OpenAPI (33 عملية؛ مخططات Objective وOutcome وPhase وActivity وMilestone وDependency وCitation) | valid — المدقق كشف نوع `number` غير مدعوم في المولّد، صُحح |
| القبول | 27 + 93 (مولدة) + 22 سيناريو + 7 خصائص |
| Threat model / FMEA | 6 تهديدات (كلها L) / 3 أنماط فشل |
| التتبع | 11 متطلباً، 0 بلا اختبار |
| CR-29 للخطة | **مغلق** — هوية الخطة منفصلة عن إصداراتها؛ 7 أنواع مكونات داخلية (SL-24) |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-DECISION-REQUEST | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-DECISION | ✓ 4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-PLAN | ✓ 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-PLAN-VERSION | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-OUTCOME-TRACKER | ✓ 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| طلب القرار | ≥ خياران (أحدهما "لا إجراء") و≥ استشهاد واحد قبل الفتح |
| القرار | فحص السلطة وقت التسجيل وحفظ لقطة السلسلة؛ استشهاد إلزامي؛ أثر رجعي ≤ ساعة |
| إلغاء القرار | لسلطة أعلى لنفس النوع؛ الخطط المنفذة تُعلَّم للمراجعة ولا تتغير تلقائياً |
| الخطة | هوية بلا محتوى؛ المحتوى في إصدارات؛ ACTIVE عند أول خط أساس |
| تصنيف التغيير | آلي عند التقديم (major / minor) حسب جدول SPEC-PLAN §2 |
| مزامنة المهام | فرق حتمي بمعرفات أنشطة ثابتة، idempotent، ≤ 60 ث لـ 500 نشاط |
| معايير مهمة مسندة تغيرت | إحلال بمهمة جديدة (لا تعديل للمجمّد) |
| إكمال الخطة | كل المهام نهائية + كل نتيجة لها قياس واحد على الأقل |
