---
id: CONSISTENCY-R2
type: consistency-report
wave: R2 baseline consolidation
status: FINAL (delegated)
basis: V5§110, V6§16
---

# Consistency Report — Release 2

فحص آلي شامل عبر كل ملفات الحزمة الموحّدة (R1+R2)، بنفس أداة `w9_check` المضمّنة في `13-verification/tooling/`، لا عينة. الفحص أُعيد تشغيله على نسخة كاملة من الحزمة بعد استخراج الأدوات وإعادة توليد الشرائح الست عشرة (اختبار ذهاب وإياب: 0 ملفات مختلفة عن المولَّد).

| الفحص | الحكم | الدليل |
|---|---|---|
| Requirements ↔ Business | PASS | 165/165 REQ (114 R1 + 51 R2) → capability → outcome → BRQ (`rtm-r1.md` + `rtm-r2.md`) |
| Business ↔ Domain | PASS | 6 قدرات R2 جديدة (CAP-02.01، CAP-04.04، CAP-06.03، CAP-08.01/02، CAP-10.02، CAP-11.01/03، CAP-12.01..04) موزّعة على BC02, BC04, BC05, BC06, BC07؛ كل شريحة R2 تغطي قدراتها المعلنة في `release-2-scope.md` |
| Domain ↔ Information | PASS | 82 aggregate إجمالاً (54 R1 + 28 R2)؛ 0 orphan/missing aggregate files |
| Information ↔ API | PASS | commands_missing_in_openapi: 0؛ queries_missing_in_openapi: 0 (عبر كل الـ 82 aggregate) |
| API ↔ Events | PASS | events_missing_in_asyncapi: 0 |
| Events ↔ State machines | PASS | aggregates_without_acceptance: 0 |
| Commands ↔ Policies | PASS | commands_without_policy: 0 |
| Security ↔ Architecture | PASS | aggregates_without_label_source: 0/82؛ حدود ثقة جديدة لـ R2: TB-06 (محولات المؤسسة، SLC-16)، عزل GPU (SLC-10) |
| Performance ↔ Architecture | PASS (model) | كل قيمة رقمية R2 موسومة "تُعاد معايرتها بعد Pilot R1" (RSK-027)؛ لا قياس فعلي بعد |
| Quality ↔ Verification | PASS | qas_without_verification_reference: 0/89 (74 R1 + 15 R2) |
| AI ↔ Security | PASS (design) | AGG-AI-ROUTING لا يمكن أن يعبّر عن AIL 5 بالبنية؛ مسارات R2 ≤ AIL 3؛ الاسترجاع يعمل بهوية المستخدم مع LabelCheck (P-101) |
| Registers | PASS with conditions | unknowns_open: UNK-002, UNK-012 (غير حاجبة للتصميم، من R1)، **UNK-021 (جديد R2 — أنظمة المستأجرين الفعلية، لا يحجب الإطار)**؛ open_questions: 0؛ corrections_not_applied: 0/59 |
| Everything ↔ Traceability | PASS | requirements_untraced (R1، يجب أن يكون 0): **0**؛ requirements_untraced_R2_pending_slices: **0** — كل الـ51 متطلب R2 مربوط رغم أن G6 محجوز |

## ما كشفه الفحص الشامل بعد إضافة R2

لا مشكلة جديدة. الفحص الشامل نظيف منذ اندماج الشرائح الست (SLC-09, 10, 12, 14, 15, 16) لأن كل شريحة نُظّفت عبر `w9_check` قبل الانتقال للتالية (CR-58 عند SLC-10، CR-59 عند SLC-14 — كلاهما مُطبَّق، انظر `00-governance/registers/corrections.md`).

| البند | R1 (10 شرائح: 01–08, 11, 12a) | R2 (6 شرائح: 09, 10, 12, 14, 15, 16) | الإجمالي |
|---|---|---|---|
| Aggregates / invariants | 54 / 191 | 28 / 84 | 82 / 275 |
| Commands / events / queries | 293 / 357 / 83 | 144 / 179 / 33 | 437 / 536 / 116 |
| OpenAPI operations | 377 (16 ملفاً) | 177 (9 ملفات: `05-contracts/openapi-*-slc{09,10,12,14,15,16}.md`) | 554 (25 ملفاً) |
| Requirements traced | 114/114 | 51/51 | 165/165 |
| Quality scenarios verified | 74/74 | 15/15 | 89/89 |
| ADRs approved | 16/16 | 0 جديدة (لا حاجة؛ التقنيات الجديدة TD-18/19 مسجّلة تحت ADR-P05) | 16/16 |
| Corrections | 57 | +2 (CR-58, CR-59) | 59/59 مطبّقة |
| Deployment units | 13 | +3 (DU-14 Readiness، DU-15 Knowledge، DU-16 AI Serving — انظر `12-solution/deployment-units.md`؛ DU-08 تقلّصت إلى BC04 وحده) | 16 |
| المخاطر | 26 | +1 (RSK-027، M/M، مفتوحة بتخفيف) | 27 |

## المخاطر المفتوحة ذات الأثر العالي (كلها بتخفيف — بلا تغيير عن R1)
RSK-001, RSK-002, RSK-003, RSK-007, RSK-008, RSK-010, RSK-013, RSK-018, RSK-020, RSK-025, RSK-026 — التفاصيل في `00-governance/registers/risks.md`. RSK-027 (خاص بـ R2) أثره M وليس H، فلا يظهر في هذه القائمة، لكنه الشرط الحاكم لبوابة G6 لكل شرائح R2 (انظر `01-business/release-2-scope.md` §3).

## سلامة الحزمة (اختبار ذهاب وإياب)
أُعيد استخراج الأدوات الست (`md_io.py`, `slice_gen.py`, `slice_contracts.py`, `acc_gen.py`, `lint_md.py`, `w9_check.py`) من `spec-tooling.md`، وبيانات الشرائح الست عشرة من `slice-sources.md`، وأُعيد توليد كل الشرائح بترتيب `slice_gen ← slice_contracts ← acc_gen`. **الفرق مع الحزمة المسلَّمة: 0 ملف** لكل ما يُولَّد (aggregates، كتالوجات، OpenAPI/AsyncAPI/الأخطاء، ملفات القبول)؛ الفروق الوحيدة كانت في نهايات الأسطر (CRLF بيئة Windows) بلا أثر على المحتوى. الملفات الموجودة فقط في الحزمة المسلَّمة (context-map.md، ownership.md، domains.md، المواصفات النصية لكل شريحة، إلخ) هي وثائق مُحرَّرة يدوياً بحكم `spec-tooling.md` ولا يُتوقع أن يولّدها المولّد.
