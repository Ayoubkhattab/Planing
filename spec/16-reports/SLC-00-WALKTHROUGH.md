---
id: SLC-00-WALKTHROUGH
type: conceptual-validation
title: SLC-00 Conceptual End-to-End Walkthrough (end of W3)
wave: W3
status: DRAFT
basis: V6§11.1, V5§117
---

# SLC-00 — Conceptual Walkthrough

**السيناريو:** مراقب ميداني يرصد انسداد طريق بسبب سيول؛ المعلومة تمر بالنموذج كله حتى الأرشفة.

| # | الخطوة | المالك | الأمر / الاستعلام | الحدث | الصلاحية | الأزمنة | الدليل / المصدر | النتيجة |
|---|---|---|---|---|---|---|---|---|
| 1 | تسجيل ملاحظة دون اتصال مع صورة | BC02 | RecordObservation (offline queue) | ObservationRecorded | Field User + preload scope | observed_at (جهاز) + clock_offset؛ recorded_from عند المزامنة | Source = المراقب؛ Evidence = الصورة (hash) | ✓ |
| 2 | اشتقاق ادعاء: الطريق R12 مغلق | BC02 | AssertClaim (derived) | ClaimAsserted | Analyst أو قاعدة | valid_from = event_time التقديري | Claim ← Observation (lineage) | ✓ |
| 3 | تعارض مع ادعاء سابق "R12 مفتوح" من نظام المرور | BC02 | (rule CF-01) | ConflictDetected | — | valid متداخلة | ادعاءان بمصدرين | ✓ |
| 4 | مطابقة "R12" مع "طريق الساحل" من مصدر آخر | BC02 | ProposeMatch → DecideMatch | EntitiesLinked | Analyst | SameAsLink record time | ER case + evidence | ✓ |
| 5 | الموقف "سيول المنطقة الشرقية" يضم الطريق | BC03 | (membership rule) | SituationChanged | — | ≤ 10 ث (QAS-PERF-006) | يشير لكيانات BC02 | ✓ |
| 6 | تنبيه حرج لمشتركي الموقف | BC03 → BC04 | RaiseAlert → Notify | AlertRaised | مشترك مصرح فقط؛ الإشعار مرجع | ≤ 5 ث | قاعدة التنبيه | ✓ |
| 7 | تحليل أثر الإغلاق على الوصول | BC03 | ExecuteAnalysisRun (job) | AnalysisRunCompleted | Analyst | الإدخالات بـ known_at | lineage للمدخلات بإصدار | ✓ |
| 8 | تقييم: "مرجح جداً" انقطاع قرية X | BC03 | PublishAssessment | AssessmentPublished | Analysis lead | إصدار ثابت | findings + evidence + احتمال تقديري | ✓ |
| 9 | طلب قرار وخيارات | BC04 | CreateDecisionRequest | DecisionRequested | Manager | — | مرجع التقييم (URN + version) | ✓ |
| 10 | القرار بفتح مسار بديل | BC04 | RecordDecision | DecisionRecorded | **AuthorityCheck (BC01)** | effective_from | روابط التقييم والأدلة | ✓ |
| 11 | خطة بإصدار وخط أساس | BC04 | CreatePlan → ApprovePlan | PlanBaselined | Planner يُعد، Manager يعتمد (SoD) | effective | رابط القرار | ✓ |
| 12 | مهمة + إسناد لفريق | BC04 | CreateTask → AssignTask | TaskAssigned | **EligibilityCheck (BC05)** | — | رابط الخطة | ✓ |
| 13 | تخصيص معدة | BC05 | AllocateResource | ResourceAllocated | Resource Manager | — | رابط المهمة | **R2** — في R1 يُسجل المورد كنص في المهمة |
| 14 | التنفيذ والإكمال | BC04 | Submit → Approve → Complete | TaskCompleted | المعتمد ≠ المنفذ | — | نتيجة + ملاحظة جديدة (عودة للخطوة 1) | ✓ |
| 15 | قياس نتيجة الخطة | BC04 | RecordOutcomeMeasurement | OutcomeMeasured | Planner | — | — | ✓ |
| 16 | درس مستفاد | BC06 | CaptureLesson | LessonCaptured | — | — | — | **R2** |
| 17 | احتفاظ وأرشفة | BC08 / BC06 | ApplyRetention | — | Archivist | — | — | الاحتفاظ ✓ R1؛ الأرشفة R2 |
| 18 | مراجعة القرار لاحقاً: ماذا كان معروفاً؟ | BC02/BC04 | QueryState(known_at = decision.recorded_at) | — | Auditor | As-Known-At | — | ✓ |

## ما كشفه المرور
1. **الخطوة 13:** R1 يربط المهام بالموارد نصاً فقط. مقبول مرحلياً، لكن يُسجل كدين معرفي (DEBT-001) حتى SLC-09.
2. **الخطوة 6:** التنبيه يعبر من BC03 إلى BC04 (الإشعارات). يحتاج عقداً: `AlertRaised` → Notification service. مضاف لقائمة عقود W6.
3. **الخطوة 18:** مراجعة القرار تتطلب أن يحتفظ القرار بـ `recorded_at` دقيق وبمراجع التقييمات **بإصدار**. مؤكد في REQ-DEC-003 والنموذج الزمني.
4. **لا فجوة ملكية:** كل خطوة لها مالك وعقد.
