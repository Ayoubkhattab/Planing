---
id: SYS-STUDY-RELATIONSHIP-INDEX
type: relationship-index
title: Phase 2 — Typed Relationship Index
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 2)
generated_at: '2026-09-29'
notes: >
  This file does NOT duplicate the raw co-reference graph — that graph already
  exists as the defined_in / ext_ref_count / ext_files columns in
  01-entity-index.md, and re-deriving it here would create a second source of
  truth for the same data. This file is for the layer 01-entity-index.md
  cannot express: TYPED, directional, semantically-judged relationships
  (depends_on, enables, mitigates, triggers, ...), which require reading and
  understanding content, not just grep. It grows incrementally during Phase 3
  (one BC at a time) rather than being generated in one pass.
---

# Phase 2 — Typed Relationship Index

## 1. الفرق بين هذا الملف و`01-entity-index.md`

| | `01-entity-index.md` | `02-relationship-index.md` (هذا الملف) |
|---|---|---|
| **كيف يُبنى** | آليًا بالكامل (regex عبر 705 ملف) | يدويًا/تدريجيًا أثناء التعمّق في كل BC |
| **يجيب** | أين عُرِّف X؟ من يذكر X؟ (كم مرة) | **ما نوع** العلاقة بين X وY، ولماذا؟ |
| **مثال** | `QRY-AUT-CHECK` → مذكور في 8 ملفات | `QRY-AUT-CHECK` **--mitigates-->** `THR-S01-03` |
| **تصنيف المعرفة** | Explicit فقط (مطابقة نص حرفية) | Explicit / Derived / Inferred (يحتاج حكمًا) |

**القاعدة العملية:** إذا كان السؤال "أين يظهر هذا المعرّف؟" → الجواب في `01-entity-index.md` عمود `ext_files`. إذا كان السؤال "لماذا هذان العنصران مرتبطان، وبأي اتجاه؟" → الجواب هنا.

## 2. قاموس أنواع العلاقات (يُستخدم كمرجع موحّد لكل BC لاحقًا)

`depends_on` · `enables` · `feeds` · `consumes` · `produces` · `triggers` · `authorizes` · `constrains` · `mitigates` · `controls` (SoD) · `validates` · `extends` · `related_to` · `duplicate_of` · `similar_to` (غير مؤكد الدمج) · `contains` · `belongs_to`

كل علاقة جديدة يكتشفها أي BC تُضاف هنا فور اكتشافها، مع الإشارة إليها كنوع جديد إن لم تكن في القائمة (Dynamic Discovery Rule).

## 3. علاقات مؤكدة حتى الآن (Seed — من عمل BC01 السابق)

هذه العلاقات استُخرجت فعليًا (وليست افتراضية) أثناء التوسعة العميقة لميزتي Authority Grant وClearance، قبل بدء Phase 2 رسميًا. أُدرجها هنا كنقطة بداية لأنها Explicit ومُتحقَّق منها بالفعل:

| From | Relationship | To | النوع | Evidence |
|---|---|---|---|---|
| CAP-01.03 | `contains` | UC-082, UC-083 | Explicit | capabilities.md, use-cases.md |
| UC-082 / UC-083 | `realizes` | AGG-AUTHORITY-GRANT | Derived | لا سرد UC صريح، مُشتق من جدول الانتقالات |
| CMD-AUT-DELEGATE | `constrains_by` | INV-AUT-01, INV-AUT-02, INV-AUT-03 | Explicit | AGG-AUTHORITY-GRANT.md |
| QRY-AUT-CHECK | `mitigates` | THR-S01-03 (Delegation chain amplifies authority) | Explicit | threat-model-slc01.md |
| CMD-CLR-APPROVE | `controls` (Segregation of Duties) | — | Explicit | policies-slc01.md#POL-CLR-APPROVE |
| INV-CLR-02/03 | `mitigates` | THR-S01-04 (Security Officer grants own/colluding clearance) | Explicit | threat-model-slc01.md |
| AGG-AUTHORITY-GRANT | `feeds` | BRL-003 (business decision requires authority) | Explicit | business-rules.md |
| BRL-003 | `enables` | CAP-06 (إدارة القرار) | Derived | ربط منطقي، لا رابط مباشر بملف واحد |
| AGG-CLEARANCE | `depends_on` | AGG-CLASSIFICATION-SCHEME (BC08) | Explicit | "level and compartments exist in ACTIVE scheme" — AGG-CLEARANCE.md guard |
| UC-089 (جديدة، CR-64) | `realizes` | AGG-CLEARANCE (جانب المستخدم) | Explicit (بعد التصحيح) | CR-64 |
| UC-085 | `realizes` | AGG-CLASSIFICATION-SCHEME (جانب الكائن/المخطط) | Explicit | traces.satisfies |
| AGG-AUTHORITY-GRANT | `similar_to` (ليست duplicate) | AGG-CLEARANCE | Derived | نفس نمط state machine، أبعاد مختلفة تمامًا (من يقرر vs من يرى) |

## 4. اكتشاف عابر للـBC ظهر أثناء Phase 2 الآلي (يحتاج تصنيف علاقة رسمي في Phase 3)

من `03-data-quality.md` §3: ست فئات بيانات مرجعية (`RD-HAZARD-CATEGORIES`, `RD-LOGISTICS-ITEM-TYPES`, `RD-ASSET-TYPES`, `RD-RESOURCE-TYPES`, `RD-EXERCISE-TYPES`, `RD-CONDITION-GRADES`) **يعتمد عليها BC04/BC05 صراحة** (`depends_on` من عدة aggregates) لكنها **غير معرَّفة فعليًا** في `04-information/reference-data.md` (المصدر المفترض لكل RD-*). هذه علاقة `depends_on` حقيقية لكن **طرفها الثاني مفقود [Missing]** — ستُسجَّل رسميًا في `conflicts.md` عند الوصول لـBC04/BC05 في Phase 3، لا هنا.

## 5. BC01 — علاقات إضافية مؤكَّدة (اكتمال Phase 3 لـBC01)

| From | Relationship | To | Evidence |
|---|---|---|---|
| AGG-TENANT (decommission) | `depends_on` | BC08 (legal hold query) | AGG-TENANT.md guard |
| UC-085 (Manage Classification Scheme) | `realizes` | BC08 (AGG-CLASSIFICATION-SCHEME) | تأكيد سابق |
| UC-086 (Manage Access Policy) | `realizes` | BC08 (AGG-POLICY-SET) | تحقّق مباشر من وجود الملف في BC08 |
| UC-088 (Request & Approve Security Exception) | `realizes` | BC08 (AGG-SECURITY-EXCEPTION) | تحقّق مباشر من وجود الملف في BC08 |
| AGG-ROLE-ASSIGNMENT | `enables` | BC04 (SoD لاعتماد الخطة/المهمة، REQ-OPS-005/009) | traces.satisfies + REQ statements |
| AGG-HR-SYNC-PROPOSAL | `mitigates` | THR-S01-01 (SCIM يمنح أدوارًا مباشرة) | AGG-HR-SYNC-PROPOSAL.md + threat-model-slc01.md |
| QRY-AUT-CHECK | `mitigates` | THR-S01-03 (تسلسل تفويض يضخّم السلطة) | مؤكَّد سابقًا |
| INV-CLR-02/03 | `mitigates` | THR-S01-04 (تواطؤ ضباط أمن) | threat-model-slc01.md |

**نمط مكتشَف عابر لأكثر من علاقة واحدة:** ثلاث حالات استخدام على الأقل في نطاق UC-080..089 (UC-085, UC-086, UC-088) تُنفَّذ فعليًا عبر BC08 لا BC01، رغم ظهورها في نفس الكتالوج المتقاطع. هذا يستدعي عند بدء دراسة BC08 التحقق من وجود ازدواجية أو تكامل حقيقي مع ما وثّقناه هنا.

## 7. BC02 — اكتشاف مهم يُعيد فتح CONFLICT-01/OQ-034 بنطاق أوسع

أثناء دراسة BC02، وُجد أن **7 من 18 aggregate** (ENTITY, RELATIONSHIP, REALWORLD-EVENT, CLAIM, EVIDENCE, OBSERVATION, SOURCE) تحمل جميعًا أمر `CMD-*-RECLASSIFY` بنفس الحارس الحرفي: *"authority per tenant policy (**REQ-GOV-004**); new version; bumps object security_version"*.

**الأثر:** REQ-GOV-004 ليست مسؤولية aggregate أو BC واحد (كما افترضنا في CONFLICT-01 الأصلي بين BC01/BC08) — بل **نمط أمر مُكرَّر عبر عشرات الـaggregates في كل الـBCs على الأرجح**. هذا يعني:
- `use_cases` الصحيح لـREQ-GOV-004 في requirements.md قد يحتاج إعادة صياغة جذرية: ليس UC-085 أو UC-089 فقط، بل **كل واجهة "إعادة تصنيف" عبر كل الـBCs**.
- هذا **يوسّع نطاق OQ-034/CR-64** إلى ما هو أبعد من BC01 — القرار البشري النهائي بشأنها يجب أن يُؤجَّل حتى تُفحص بقية الـBCs (BC03..BC08) ويُعرف حجم النمط الكامل.

**لم أُعدِّل CR-64/OQ-034 بهذا بعد** — أسجّله هنا أولًا لأن القرار يمسّ نطاقًا يتجاوز صلاحية "قرار بشأن ميزة واحدة"؛ يحتاج تجميع الأدلة من كل الـBCs أولًا (Source Closure الحقيقي لهذه المسألة تحديدًا).

## 9. BC03 — اكتملت من أول جولة (بلا اكتشافات جديدة تمس CONFLICT-01)

BC03 (الوعي بالموقف + التحليل، 9 aggregates) أُغلقت هيكليًا وأمنيًا في جولة واحدة بتطبيق درس §7/§10 (فصل الشريحة عن BC). لا أوامر RECLASSIFY بنمط REQ-GOV-004 المكتشف في BC02 ظهرت هنا بنفس الكثافة (AGG-SITUATION فقط يحمل CMD-SIT-RECLASSIFY، وAGG-ANALYSIS-CASE يحمل CMD-ACS-RECLASSIFY) — يُضاف إلى قائمة الأدلة المتراكمة لصالح فرضية "RECLASSIFY نمط عابر لكل BC" دون تغيير القرار المعلَّق.

## 11. BC04 — اكتملت، مع تصحيح رجعي على BC03

BC04 (12 aggregate: Decision/Plan/Task/Risk/Incident/Coordination/Notification/Subscription، أكبر BC حتى الآن) اكتملت هيكليًا وأمنيًا. **اكتشاف أثناء هذه الجولة أدّى لتصحيح `bc03-situational-awareness.md` رجعيًا:** THR-S06-02 وTHR-S06-07 (ملف "threat-model-slc06.md") تخصان AGG-NOTIFICATION/AGG-SUBSCRIPTION (BC04) لا BC03 كما نُسِب أول مرة — نفس نمط AGG-ADAPTER (BC02→BC07) وTHR-S15-01/02 (BC02→BC04، مُؤكَّد نهائيًا هنا). أيضًا BRL-003 (لا قرار بلا سلطة) ظهرت مطبَّقة **حرفيًا مرتين**: AGG-DECISION (بين الأفراد) وAGG-COORDINATION-CASE (بين المنظمات) — نفس القاعدة التجارية، تطبيقان هندسيان مستقلان.

**تأكيد إضافي على فجوة RD-HAZARD-CATEGORIES:** AGG-RISK وAGG-INCIDENT كلاهما يستشهد بها كحارس إلزامي مباشر — من المصدر، لا استنتاجًا.

## 13. BC05 — اكتملت (بلا تصحيحات رجعية)

BC05 (13 aggregate: Asset/Allocation/Logistics/Shipment/Exercise/Simulation...) اكتملت. **تأكيد رابع متراكم لفجوة RD-*** — BC05 وحدها استشهدت بـ5 من 6 فئات مرجعية مفقودة من Phase 2. **نمط CR-62 (الإنشاء المرتبط بنفس المعاملة) مؤكَّد الآن كـنمط تصميم متكرر عمدًا** (3 حالات: Logistics→Allocation، Logistics→Shipment، Exercise→Simulation) لا حالة استثنائية واحدة.

## 15. BC06 — اكتملت (اعتماد معلَّق واحد على BC08)

BC06 (6 aggregates: Product/Template/Distribution/Knowledge-Object/Archive/Reconstruction، شريحة SLC-12 واحدة). **نمط "الإفصاح الصفري" (لا كشف لوجود شيء محجوب) مؤكَّد للمرة الرابعة** عبر BCs مختلفة (BC01 PB-01، BC03 INV-ALR-02، BC06 INV-DST-01/INV-REC-03) — مبدأ تصميمي مركزي للمنصة كلها. اعتماد صريح غير محلول: `AGG-ARCHIVE-PACKAGE` على "SLC-12a" (يُرجَّح BC08) — يُترَك معلَّقًا حتى BC08.

## 17. BC07 — اكتملت (أكبر BC من حيث الشرائح؛ تصحيحان رجعيان)

BC07 (13 aggregate: Adapter/Connection/Sensor/AI-*/Projection/Sync-*/Preload، 5 شرائح) اكتملت. **حسمت توزيع SLC-16 نهائيًا** بعد أن كان جزئيًا: BC01(1: HRIS) + BC03(1: Outbound CAP) + BC07(3: DMS/Connections/Sensors) = 5/5. **صححت رجعيًا `bc01-foundation.md`** (أضافت THR-S16-02 المفقود لـAGG-HR-SYNC-PROPOSAL). Platform Baselines أصبحت مكتملة: **PB-01..14** (01-07 BC01، 08-11 BC02، 12-14 BC07/AI). اكتُشف مبدأ أمني جديد خاص بالـLLM: "البيانات المسترجَعة لا يمكنها رفع الصلاحية أو توسيع النطاق أبدًا" (INV-AIR-02) — دفاع مباشر ضد Prompt Injection.

## 19. BC08 — اكتملت (آخر BC في Phase 3؛ يُغلق CONFLICT-01/OQ-034 نهائيًا)

BC08 (7 aggregates: Classification-Scheme/Policy-Set/Security-Exception (SLC-01، مشتركة مع BC01) + Retention-Schedule/Legal-Hold/Disposition-Run/Erasure-Request (SLC-12a، خالصة)) اكتملت.

**تصحيح رجعي ثانٍ على BC01 (بعد THR-S16-02 في §17):** `THR-S01-05` (Policy set) و`THR-S01-06` (Security exception) في `threat-model-slc01.md` تخصان BC08 لا BC01 — نفس نمط "الشريحة ≠ BC" يتكرر للمرة الثالثة (بعد AGG-ADAPTER §10 وTHR-S06 §11). صُحِّح `bc01-foundation.md` (13→11 تهديدًا لـBC01؛ 71→58 سياسة أمر). كذلك 6 من 14 query_policies في `policies-slc01.md` تخص BC08.

**إغلاق CONFLICT-01/OQ-034/CR-64 نهائيًا عبر CR-65:** `AGG-CLASSIFICATION-SCHEME.md` لم يكن يُعلن `REQ-GOV-004` في `traces.satisfies` رغم أن `INV-CLS-04` هو آلية إنفاذه على مستوى المخطط. أُضيف الآن (CR-65). REQ-GOV-004 له الآن **ثلاث نقاط إنفاذ موثَّقة صراحة**: AGG-CLASSIFICATION-SCHEME (مستوى المخطط)، نمط CMD-*-RECLASSIFY عبر BC02+ (مستوى الكائن، §7)، AGG-CLEARANCE (مستوى تصريح المستخدم، BC01، CR-64). اكتشاف §7 حول "نطاق REQ-GOV-004 عبر كل الـBCs" يبقى موثَّقًا كملاحظة توسّع نمطي مشروعة، لكنه لم يعد يمنع إغلاق CONFLICT-01 نفسها — الثلاث نقاط الموثَّقة تغطي كل الزوايا التي أثارها النزاع الأصلي (كائن BC08 × مستخدم BC01).

**إغلاق اعتماد BC06→SLC-12a:** مؤكَّد أن `AGG-ARCHIVE-PACKAGE.CMD-ARC-DISPOSE` يعتمد على `AGG-DISPOSITION-RUN` (BC08) عبر آلية تدمير المفتاح المشتركة (ADR-P08, CR-51) — رابط ضمني [Derived]، لا رابط صريح بين ملفي الـaggregate. صُحِّح `bc06-knowledge-products.md` (§4.3/§7/§8: CLOSED جزئيًا → CLOSED).

**اكتشاف جديد:** BC08 يحمل أعلى كثافة قيود SoD في كل الدراسة (كل أمر تغييري تقريبًا يحمل قيد فصل مهام صريح) — منطقي بصفته "الحارس الأخير" لعمليات لا رجعة فيها (إتلاف، محو، تجميد قانوني). Crypto-shredding (تدمير مفتاح لا صف) هو الآلية الموحَّدة عبر AGG-DISPOSITION-RUN وAGG-ERASURE-REQUEST معًا.

## 20. حالة هذا الملف

`CLOSED (Phase 3)` — **BC01→BC08 اكتملت جميعًا.** كل التصحيحات الرجعية مُطبَّقة وموثَّقة (BC01 ×2، BC03 ×1، BC06 ×1). CONFLICT-01/OQ-034 مُغلَق نهائيًا (CR-65). الأعمال المتبقية على مستوى النظام كله (لا BC واحد): Phase 4 (`cross-cutting.md`)، Phase 5 (`conflicts.md` — توثيق رسمي لكل التعارضات المكتشفة بما فيها CONFLICT-01 كسجل تاريخي)، Phase 6 (`master-study.md` كفهرس أعلى بلا تكرار محتوى).
