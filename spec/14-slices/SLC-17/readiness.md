---
id: G6-SLC-17
type: slice-readiness
title: Slice Readiness — SLC-17 Risk & Contingency (R3)
wave: W7
slice: SLC-17
status: DESIGN_COMPLETE — G6 HELD until R1 pilot review AND R2 pilot review (RSK-028, stricter than RSK-027)
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
traces: {depends_on: [G6-SLC-03, G6-SLC-08]}
---

# SLC-17 — Risk & Contingency

## الحكم: **DESIGN COMPLETE** — G6 محجوز حتى مراجعة Pilot R1 **و** R2 (RSK-028)

| الشرط | الحالة (محسوب) |
|---|---|
| Aggregates / ثوابت | 2 / 10 |
| الفحص | 0 مخالفات — 15 أمراً، 17 حدثاً، 5 استعلامات |
| OpenAPI | 20 عملية — valid |
| سيناريوهات مكتوبة يدوياً | 10 + 5 خصائص |
| التتبع | 16 متطلباً، 0 بلا اختبار |
| تصحيحات عابرة للشرائح | CR-60 (SLC-08 Plan)، CR-61 (SLC-03 Task) — كلاهما مطبَّق ومُعاد توليده؛ اختبار ذهاب وإياب 0 فرق |

| Aggregate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | الحكم |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AGG-RISK | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |
| AGG-INCIDENT | ✓ 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **PASS** |

## قرارات مفوضة
| القرار | القيمة |
|---|---|
| فئات الخطر | كتالوج مرجعي RD-HAZARD-CATEGORIES لكل مستأجر (نمط R2-Q1)؛ لا فئات مثبَّتة |
| Emergency/Crisis | ليست Aggregates منفصلة؛ خطورة (severity) متصاعدة على AGG-INCIDENT نفسه |
| الاستمرارية | لا Aggregate جديد؛ AGG-PLAN بامتداد plan_kind=CONTINGENCY (CR-60، R3-Q2) |
| التعافي | محسوب لا مخزَّن؛ استعلام على مهام الخطة المرتبطة (R3-Q4) |
| تفعيل الاستمرارية | أمر صريح دائماً، ليس أثراً تلقائياً للتصعيد (INV-INC-03) |
| SLA الاستجابة | إشاري، موسوم لإعادة الاشتقاق بعد Pilot R1 وR2 (RSK-028)، لا التزام |

## ملاحظة صريحة حول شرط "R1 وR2 معاً" (RSK-028)
اعتماديات SLC-17 التقنية الفعلية (`G6-SLC-03`، `G6-SLC-08`) كلاهما من R1 المُصادَق عليه بالفعل — لا اعتماد بنيوي مباشر على BC05 (R2). هذا يجعل SLC-17 أقل تعرضاً لمخاطرة RSK-028 من SLC-18/19 (اللتين تعتمدان مباشرة على BC05 المصمَّم في SLC-09/R2). مع ذلك، تبقى هذه الشريحة خاضعة لقرار المحفظة الشامل في `release-3-scope.md` §3 (لا G6 لأي شريحة R3 قبل مراجعة R1 وR2 معاً) — قرار اتُّخذ على مستوى R3 ككل، لا شريحة بشريحة، وتغييره يحتاج تحديثاً صريحاً لذلك الملف لا استثناءً هنا.
