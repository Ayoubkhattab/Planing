---
id: CONSISTENCY-R1
type: consistency-report
wave: W9
status: FINAL (delegated)
basis: V5§110, V6§16
---

# Consistency Report — Release 1

فحص آلي شامل عبر كل ملفات الحزمة (`w9_check`)، لا عينة.

| الفحص | الحكم | الدليل |
|---|---|---|
| Requirements ↔ Business | PASS | 114/114 REQ → capability → outcome → BRQ (RTM-R1) |
| Business ↔ Domain | PASS | 14 capabilities → 26 domains → 8 BCs; R1 slices cover all R1 capabilities |
| Domain ↔ Information | PASS | 54 aggregates; 48+ business objects single-owned (SL-01 = 0) |
| Information ↔ API | PASS | 16 ADRs approved; all 54 aggregates have contracts; commands missing in OpenAPI: 0 (after CR-55) |
| API ↔ Events | PASS | all domain events present in AsyncAPI; each with partition key and consumers |
| Events ↔ State machines | PASS | every transition emits one event (SL-03/04); complete matrices (SL-05) for all aggregates |
| State machines ↔ Acceptance | PASS | every aggregate has a generated state-machine acceptance file |
| Commands ↔ Policies | PASS | every command has a policy decision table entry |
| Security ↔ Architecture | PASS | label source for 54/54 aggregates (SL-29); trust boundaries; per-slice threat models; non-inference properties |
| Performance ↔ Architecture | PASS (model) | workloads → technology decisions (TD-*) → performance test strategy; values estimated until pilot |
| Quality ↔ Verification | PASS | 74/74 QAS mapped to verification (after CR-56) |
| AI ↔ Security | PASS (R2 scope) | autonomy matrix, AIL ≤ 2 in R1; AI slice in R2 |
| Registers | PASS with conditions | unknowns open: [['UNK-002', 'partially_closed_non_blocking_for_design'], ['UNK-012', 'partially_closed_non_blocking_for_design']] (non-blocking for design); open questions: 0; corrections not applied: 0 of 58 |
| Everything ↔ Traceability | PASS | SL-20: 0 real dangling references |

## ما كشفه الفحص الشامل وصُحح في W9
| الرقم | المشكلة | التصحيح |
|---|---|---|
| CR-55 | `CMD-RUN-SUBMIT` غائب عن OpenAPI: أمرا إنشاء على نفس المسار، والمولّد كتب أحدهما فوق الآخر بصمت | مسار مستقل لإعادة الإنتاج؛ المولّد يفشل الآن عند أي تصادم مسارات؛ فُحصت كل الشرائح |
| CR-56 | 19 من 74 سيناريو جودة بلا مرجع تحقق | مصفوفة تحقق الجودة تغطي الـ 74 |
| CR-06 | تصحيح قديم بقي بحالة PROPOSED رغم تطبيقه في SLC-03 | الحالة صُححت |
| CR-57 | قابلية إعادة الإنتاج: عقود الشرائح الأولى وُلدت بإصدارات أقدم من المولّد، وإثراءات 6 شرائح طُبقت يدوياً | نُقلت كل الإثراءات إلى بيانات المصدر؛ أُعيد توليد كل الشرائح؛ اختبار ذهاب وإياب كامل: 0 ملفات مختلفة |

## المخاطر المفتوحة ذات الأثر العالي (كلها بتخفيف)
RSK-001, RSK-002, RSK-003, RSK-007, RSK-008, RSK-010, RSK-013, RSK-018, RSK-020, RSK-025, RSK-026 — التفاصيل في `00-governance/registers/risks.md`.
