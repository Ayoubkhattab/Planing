---
id: SYS-STUDY-MASTER
type: master-index
title: "Master Study — فهرس إعادة البناء الهندسي الديناميكي للنظام (Dynamic Engineering System Reconstruction)"
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 6)
generated_at: '2026-09-29'
notes: >
  هذا الملف فهرس فقط — لا يكرر محتوى أي ملف آخر. كل رقم/جدول/اكتشاف تفصيلي موجود في مصدره
  المرتبط أدناه. عند التعارض بين هذا الفهرس وملف مصدر، الملف المصدر هو المرجع الصحيح دائمًا.
---

# Master Study — فهرس النظام الكامل

## 0. ما هذا المستند ولمن

نقطة الدخول الوحيدة لكل ما أُنتِج في "إعادة البناء الهندسي الديناميكي" (Dynamic Engineering System Reconstruction) لمستودع `spec/` (705 ملفًا مصدريًا). يُستخدَم للتنقل، لا للقراءة الخطية الكاملة — كل قسم يحيل إلى ملفه المصدر الكامل.

**منهجية العمل (مُطبَّقة عبر كل الملفات):** كل حقيقة مُصنَّفة صراحة كـ **Explicit** (موجودة حرفيًا في المصدر)، **Derived** (استنتاج منطقي من عدة مصادر)، **Inferred** (تخمين معقول بلا تأكيد مباشر)، **Missing** (مرجع بلا تعريف)، **Conflict** (تعارض بين مصدرين)، أو **Needs Review** (يحتاج قرارًا بشريًا). لا معلومة اختُرعت بلا تصنيف.

## 1. المراحل (Phases) — بالترتيب

| المرحلة | الملف | الحالة | الوصف |
|---|---|---|---|
| Phase 1 | [00-inventory.md](00-inventory.md) | ✅ CLOSED | جرد كامل لكل الـ705 ملف: front-matter، إحصاءات حسب المجلد/BC/النوع/الحالة |
| Phase 2 | [01-entity-index.md](01-entity-index.md) | ✅ CLOSED | فهرس 3999+ كيان فريد (REQ/UC/AGG/CMD/EVT/QRY/POL/INV/BRL/ADR/THR/CR/OQ...) مع مكان التعريف وعدد الاستشهادات |
| Phase 2 | [02-relationship-index.md](02-relationship-index.md) | ✅ CLOSED (Phase 3) | الرسم البياني الدلالي للعلاقات المصنَّفة (depends_on/enables/mitigates/...)؛ يحوي أيضًا سجل اكتشافات Phase 3 التراكمية بالترتيب الزمني (§3–§19) |
| Phase 2 | [03-data-quality.md](03-data-quality.md) | ✅ CLOSED | كيانات متعددة التعريف، كيانات يتيمة (944)، مرشحو RD-* غير معرَّفين (90→6 فئات حقيقية) |
| Phase 3 | bc01–bc08 (أدناه) | ✅ CLOSED (كل الثمانية) | دراسة هندسية كاملة لكل Bounded Context |
| Phase 4 | [04-cross-cutting.md](04-cross-cutting.md) | ✅ CLOSED | الأنماط العابرة لكل الـBCs: أمن، بيانات، واجهات، جودة، تتبّعية |
| Phase 5 | [05-conflicts.md](05-conflicts.md) | ✅ CLOSED (كسجل، مُحدَّث بعد Phase 3.5) | 5 تعارضات: 2 مُغلَقة (CR مرجعي)، 3 مفتوحة (تحتاج قرارًا بشريًا) |
| Phase 6 | هذا الملف | ✅ CLOSED | الفهرس الأعلى |

## 2. الـBounded Contexts الثمانية

| BC | العنوان | Aggregates | أبرز اكتشاف واحد | الملف |
|---|---|---|---|---|
| BC01 | الأساس (Tenant/Org/Person/User/Role/Device/HR-Sync/Authority/Clearance) | 11 | تصحيحان رجعيان (THR-S16-02 مضاف، THR-S01-05/06 محذوف لصالح BC08) | [bc01-foundation.md](bc01-foundation.md) |
| BC02 | نواة المعلومات (Entity/Claim/Evidence/Source/ER-Case/Conflict...) | 18 | نمط CMD-*-RECLASSIFY عبر 7 aggregates، حل جزء من CONFLICT-01 | [bc02-information-core.md](bc02-information-core.md) |
| BC03 | الوعي بالموقف والتحليل | 9 | CR-29 "لا Aggregate إله" — فصل خماسي متعمَّد لخط أنابيب التحليل | [bc03-situational-awareness.md](bc03-situational-awareness.md) |
| BC04 | التخطيط والتنفيذ (أكبر BC من حيث المتطلبات) | 12 | BRL-003 مطبَّقة حرفيًا مرتين (فردي/بين-منظمات)؛ AGG-TASK الأعقد (15 حالة) | [bc04-planning-execution.md](bc04-planning-execution.md) |
| BC05 | الموارد واللوجستيات والجاهزية (أكبر BC من حيث المتطلبات: 45) | 13 | مصدر 5 من 6 فجوات RD-*؛ نمط CR-62 مكرَّر 3 مرات | [bc05-resources-readiness.md](bc05-resources-readiness.md) |
| BC06 | المعرفة والمنتجات والذاكرة المؤسسية (أصغر BC: 6 aggregates) | 6 | فصل صريح Knowledge/Truth (CR-33)؛ اعتماد SLC-12a على BC08 أُغلِق لاحقًا | [bc06-knowledge-products.md](bc06-knowledge-products.md) |
| BC07 | التكامل والذكاء الاصطناعي والاكتشاف (أكبر BC من حيث الشرائح: 5) | 13 | INV-AIR-02 — أول دفاع صريح ضد Prompt Injection في المنصة | [bc07-integration-ai-discovery.md](bc07-integration-ai-discovery.md) |
| BC08 | الحوكمة والأمن ودورة حياة البيانات (آخر BC) | 7 | إغلاق CONFLICT-01/OQ-034 نهائيًا (CR-65)؛ أعلى كثافة SoD في الدراسة | [bc08-governance-security.md](bc08-governance-security.md) |

**الإجمالي: 89 aggregate عبر 8 Bounded Contexts، موثَّقة بالكامل.**

## 3. أرقام رئيسية (كل رقم مرتبط بمصدره — لا رقم بلا إحالة)

- **705** ملف مصدري ([00-inventory.md](00-inventory.md))
- **3999+** كيان فريد مفهرَس ([01-entity-index.md](01-entity-index.md))
- **181** متطلبًا مُعتمَدًا (202 حساب مباشر عبر BCs بسبب تداخل مقصود — [04-cross-cutting.md §6.2](04-cross-cutting.md))
- **89** aggregate عبر 8 BCs، **صفر استثناء** من نمط If-Match+Idempotency-Key+State/History/Outbox/AuditOutbox ([04-cross-cutting.md §3.1](04-cross-cutting.md))
- **114** تهديدًا موثَّقًا (STRIDE) بعد كل التصحيحات الرجعية، بما فيها إعادة العدّ الدقيقة في Phase 3.5 (كانت مُقدَّرة بـ"~121" قبل ذلك) ([04-cross-cutting.md §2.4](04-cross-cutting.md))
- **14** Platform Baseline (PB-01..14)، صفر قابل للتجاوز من المستأجر عدا PB-06 ([04-cross-cutting.md §2.1](04-cross-cutting.md))
- **65** تصحيحًا مُطبَّقًا (CR-01..CR-65، `spec/00-governance/registers/corrections.md`)
- **5** تعارضات مُكتشَفة أثناء البناء (آخرها CONFLICT-05 أثناء Phase 3.5): 2 مُغلَقة، 3 مفتوحة ([05-conflicts.md](05-conflicts.md))
- **6** فئات بيانات مرجعية (RD-*) مُستشهَد بها وغير معرَّفة — فجوة مفتوحة ([05-conflicts.md §4](05-conflicts.md))

## 4. ما يحتاج قرارًا بشريًا الآن (كل البنود المفتوحة في مكان واحد)

| # | البند | الملف المرجعي | نوع القرار |
|---|---|---|---|
| 1 | فجوة RD-* الست: استنباط من الاستخدام أم ورشة عمل مخصَّصة؟ | [05-conflicts.md §4](05-conflicts.md) | سياسة بيانات مرجعية |
| 2 | نطاق AGG-ERASURE-REQUEST: هل يشمل BC05 (Qualification-Record) أم استبعاد متعمَّد؟ | [05-conflicts.md §5](05-conflicts.md) | مراجعة نطاق أمن/خصوصية |
| 3 | CR-64/CR-65 (UC-089 + traces.satisfies الجديد): تأكيد بشري نهائي على التصنيف | `corrections.md` (CR-64 status: `APPLIED_IN_SPEC` معلَّق تأكيدًا) | اعتماد حوكمة |
| 4 | CONFLICT-05: فجوات تغطية Requirement→Use Case حقيقية — BC04 (REQ-RCM-001..016، 16 متطلبًا)، BC05 (REQ-LOG-*/REQ-TRX-*، 29 من 45)، BC07 (REQ-AI-*/REQ-SRC-004 وaggregates حوكمة داخلية، 10 من 23) — لكل حالة: تسجيلها كـOQ رسمية تمهيدًا لكتابة UCs، أم تأكيد أنها عمل مؤجَّل لدورة إصدار لاحقة (BC05 تحديدًا R3)؟ | [05-conflicts.md §6](05-conflicts.md) | فتح OQ جديدة أو تأكيد تأجيل |

**لا بنود أخرى معلَّقة في نطاق الدراسة الثمانية BCs** خلاف البنود الأربعة أعلاه — كل تصحيح رجعي آخر (THR-S06، THR-S16-02، THR-S01-05/06) طُبِّق بالكامل ولا يحتاج مراجعة إضافية.

## 5. ما هو خارج نطاق هذه الدراسة عمدًا

- تفاصيل العقود التقنية الكاملة (OpenAPI/AsyncAPI schemas الحرفية) — مُشار إليها بالمسار فقط في كل ملف BC، لا مُستنسَخة.
- ملفات `06-data/logical-model/*`، `07-quality/*`، `09-reliability/*`، `13-verification/*` بالتفصيل الكامل — استُهلِكت مفاهيميًا (SL-05/06/09، FIT-04) في [04-cross-cutting.md §5](04-cross-cutting.md) دون نسخ محتواها.
- أي عمل تنفيذي (كود، بنية تحتية فعلية) — هذه دراسة نموذج المجال (domain model) والمواصفات فقط.

## 6. كيف تُحدَّث هذه الدراسة مستقبلاً

أي تعديل على ملف مصدر في `spec/` (خارج `17-system-study/`) يجب أن يُقابَله فحص: هل يمس رقمًا أو جدولاً هنا؟ إن كان كذلك، حدِّث ملف الـBC أو `04-cross-cutting.md` أو `05-conflicts.md` المعني مباشرة، مع تسجيل التغيير كتصحيح جديد في `corrections.md` إن كان يصحح خطأ سابق، لا تعديلاً صامتًا.
