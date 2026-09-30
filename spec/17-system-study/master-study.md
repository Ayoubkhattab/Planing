---
id: SYS-STUDY-MASTER
type: master-index
title: "Master Study — فهرس إعادة البناء الهندسي الديناميكي للنظام (Dynamic Engineering System Reconstruction)"
status: DRAFT
generated_by: Claude (Dynamic Engineering System Reconstruction, Phase 6)
generated_at: '2026-09-29'
updated_at: '2026-09-30'
notes: >
  هذا الملف فهرس فقط — لا يكرر محتوى أي ملف آخر. كل رقم/جدول/اكتشاف تفصيلي موجود في مصدره
  المرتبط أدناه. عند التعارض بين هذا الفهرس وملف مصدر، الملف المصدر هو المرجع الصحيح دائمًا.
  أُعيدت هيكلته في Phase 3.6 إلى الأقسام الـ21 المتفق عليها.
---

# Master Study — فهرس النظام الكامل

## 0. ما هذا المستند ولمن

نقطة الدخول الوحيدة لكل ما أُنتِج في "إعادة البناء الهندسي الديناميكي" (Dynamic Engineering System Reconstruction) لمستودع `spec/` (705 ملفًا مصدريًا). يُستخدَم للتنقل، لا للقراءة الخطية الكاملة — كل قسم يلخّص في أسطر قليلة ويحيل إلى ملفه المصدر الكامل.

**منهجية العمل (مُطبَّقة عبر كل الملفات):** كل حقيقة مُصنَّفة صراحة كـ **Explicit** (موجودة حرفيًا في المصدر)، **Derived** (استنتاج منطقي من عدة مصادر)، **Inferred** (تخمين معقول بلا تأكيد مباشر)، **Missing** (مرجع بلا تعريف)، **Conflict** (تعارض بين مصدرين)، أو **Needs Review** (يحتاج قرارًا بشريًا). لا معلومة اختُرعت بلا تصنيف.

**ملفات الدراسة:**

| المرحلة | الملف | الغرض |
|---|---|---|
| Phase 1 | [00-inventory.md](00-inventory.md) | جرد الـ705 ملف: front-matter، إحصاءات حسب المجلد/BC/النوع/الحالة |
| Phase 2 | [01-entity-index.md](01-entity-index.md) | فهرس 3999+ كيان فريد مع مكان التعريف وعدد الاستشهادات |
| Phase 2 | [02-relationship-index.md](02-relationship-index.md) | العلاقات المصنَّفة يدويًا (§3–§19) + السلاسل الكاملة لكل Aggregate مولَّدة آليًا (§21) |
| Phase 2 | [03-data-quality.md](03-data-quality.md) | كيانات متعددة التعريف، يتيمة (944)، مراجع بلا تعريف (90 → 6 فئات RD-* حقيقية) |
| Phase 3 | bc01 … bc08 (§21 أدناه) | دراسة كل Bounded Context بقالب موحَّد من 21 قسمًا |
| Phase 4 | [04-cross-cutting.md](04-cross-cutting.md) | الأنماط العابرة: أمن، بيانات، واجهات، جودة، تتبّعية |
| Phase 5 | [05-conflicts.md](05-conflicts.md) | سجل التعارضات (5: 2 مُغلَقة، 3 مفتوحة) |
| Phase 6 | هذا الملف | الفهرس الأعلى |
| أدوات | `_build/` | `phase2_extract.ps1`/`phase2_report.ps1` (Phase 2)، `build_relationships.py` (§21 من ملف العلاقات) |

## 1. نظرة عامة على النظام (System Overview)

منصة مؤسسية متعددة المستأجرين لإدارة دورة حياة المعلومات والمعرفة والعمليات: تربط المعلومات الجغرافية والزمنية والوثائقية والتشغيلية بالأحداث والمصادر والأدلة، وتتتبّع القرار من دليله حتى تنفيذه وأثره. [Explicit — `01-business/system-definition.md` §1–§2]

| البُعد | القيمة | المصدر |
|---|---|---|
| أولويات السنة الأولى | OUT-02 الفهم السياقي ← OUT-04 دعم القرار ← OUT-05 التنفيذ المنسق | `01-business/outcomes.md` |
| الإصدارات | R1: SLC-01..08، SLC-11، SLC-12a · R2: SLC-09، 10، 12، 14، 15، 16 · R3: SLC-17، 18، 19 | `14-slices/slices.md` |
| نطاق التصميم | 50,000 مستخدم / 5,000 متزامن / 100 مستأجر؛ مسار نمو 10× | `07-quality/scale-envelope.md` |
| البيئة | محايدة، خط الأساس معزول عن الإنترنت (air-gapped) | `system-definition.md` §5 |
| الواجهات واللغة | ويب متجاوب + تطبيق ميداني؛ عربية أساسية + إنجليزية | `system-definition.md` §5 |
| مبادئ حاكمة | SR-00 Scale-Ready not Scale-First؛ البساطة التشغيلية قيد ملزم؛ التصميم للحالة القانونية الأشد | `system-definition.md` §6 |
| حالة البوابات | G0–G5 PASS · G6 R1 READY (delegated) بانتظار تصديق المالك | `16-reports/SESSION-W9.md` |

## 2. نظرة عامة على المعمارية (Architecture Overview)

نموذج **الخلية (cell)**: كل خلية مجموعة Kubernetes مستقلة بخدماتها الحالة، وتخدم مستأجرًا مخصصًا/سياديًا أو عدة مستأجرين مشتركين بنفس الكود. [Explicit — `12-solution/cell-architecture.md`]

| الطبقة | المكوّنات | القرار |
|---|---|---|
| العملاء | Web (React + MapLibre)، تطبيق ميداني (React Native + SQLCipher) | TD-16 |
| الحافة | DU-01 Edge gateway / BFF (SecurityContext، rate limits) | `12-solution/deployment-units.md` |
| وحدات النشر | DU-02..DU-13 عديمة الحالة؛ كل BC في وحدة أو أكثر (BC04+BC05 معًا في DU-08) | `12-solution/c4-containers.md` |
| البيانات | PostgreSQL 16 + PostGIS (schema لكل سياق)، OpenSearch، Valkey، S3 + Object Lock | TD-01، TD-02، TD-11، TD-06 |
| الرسائل | Kafka KRaft لكل خلية + transactional outbox عبر CDC (Debezium) | TD-04 |
| الأمن | Keycloak (OIDC/SAML/SCIM)، OPA (Rego، bundles موقَّعة)، OpenBao + HSM | TD-09، TD-08، TD-07 |
| المنصة | RKE2، Argo CD، Zarf للتثبيت المعزول، Harbor + cosign | TD-05، TD-17 |
| الذكاء الاصطناعي | vLLM على GPU pool لكل خلية، نماذج مفتوحة الأوزان | TD-18، TD-19 |
| اللغات | TypeScript/Node.js للخدمات، Python للتحليل | TD-15 |

قرارات الإلغاء أو العكس المراقَبة في Pilot (مثلًا فصل عنقود BC02 عند > 70 % كتابة) في `16-reports/EVOLUTION-ROADMAP.md`. ملخص الـ19 قرارًا تقنيًا: `12-solution/technology-decisions.md`.

## 3. خريطة الـBounded Contexts

| BC | العنوان | Aggregates | أبرز اكتشاف واحد | الملف |
|---|---|---|---|---|
| BC01 | الأساس (Tenant/Org/Person/User/Role/Device/HR-Sync/Authority/Clearance) | 11 | تصحيحان رجعيان (THR-S16-02 مضاف، THR-S01-05/06 محذوف لصالح BC08) | [bc01-foundation.md](bc01-foundation.md) |
| BC02 | نواة المعلومات (Entity/Claim/Evidence/Source/ER-Case/Conflict...) | 18 | نمط CMD-*-RECLASSIFY عبر 7 aggregates، حل جزء من CONFLICT-01 | [bc02-information-core.md](bc02-information-core.md) |
| BC03 | الوعي بالموقف والتحليل | 9 | CR-29 "لا Aggregate إله" — فصل خماسي متعمَّد لخط أنابيب التحليل | [bc03-situational-awareness.md](bc03-situational-awareness.md) |
| BC04 | التخطيط والتنفيذ | 12 | BRL-003 مطبَّقة حرفيًا مرتين (فردي/بين-منظمات)؛ AGG-TASK الأعقد (15 حالة) | [bc04-planning-execution.md](bc04-planning-execution.md) |
| BC05 | الموارد واللوجستيات والجاهزية (أكبر BC من حيث المتطلبات: 45) | 13 | مصدر 5 من 6 فجوات RD-*؛ نمط CR-62 مكرَّر 3 مرات | [bc05-resources-readiness.md](bc05-resources-readiness.md) |
| BC06 | المعرفة والمنتجات والذاكرة المؤسسية (أصغر BC) | 6 | فصل صريح Knowledge/Truth (CR-33)؛ اعتماد SLC-12a على BC08 أُغلِق لاحقًا | [bc06-knowledge-products.md](bc06-knowledge-products.md) |
| BC07 | التكامل والذكاء الاصطناعي والاكتشاف (أكبر BC من حيث الشرائح: 5) | 13 | INV-AIR-02 — أول دفاع صريح ضد Prompt Injection في المنصة | [bc07-integration-ai-discovery.md](bc07-integration-ai-discovery.md) |
| BC08 | الحوكمة والأمن ودورة حياة البيانات | 7 | إغلاق CONFLICT-01/OQ-034 نهائيًا (CR-65)؛ أعلى كثافة SoD في الدراسة | [bc08-governance-security.md](bc08-governance-security.md) |

**الإجمالي: 89 aggregate عبر 8 Bounded Contexts.** خريطة السياقات الأصلية (علاقات upstream/downstream): `03-domain/context-map.md`؛ اختبار الحدود: `03-domain/bc-boundary-test.md`.

## 4. خريطة القدرات التجارية (Business Capability Map)

عدد المتطلبات من حقل `capability` في `requirements.md` [Explicit]؛ الـBCs المنفِّذة من `traces.satisfies` في ملفات الـAggregates [Derived]. المجموع 210.

| القدرة | العنوان | متطلبات | BCs المنفِّذة |
|---|---|---|---|
| CAP-01 | إدارة المؤسسة والوصول | 15 | BC01، BC08 |
| CAP-02 | جمع المعلومات | 20 | BC02، BC07، BC04، BC01 |
| CAP-03 | إدارة المعلومات | 22 | BC02، BC03، BC07 |
| CAP-04 | التحليل والتقييم | 10 | BC02، BC03 |
| CAP-05 | الوعي بالموقف | 7 | BC03 |
| CAP-06 | إدارة القرار | 6 | BC04 |
| CAP-07 | التخطيط والتنفيذ | 14 | BC04، BC01 |
| CAP-08 | الموارد والجاهزية | 45 | BC05 |
| CAP-09 | المخاطر والطوارئ | 16 | BC04 |
| CAP-10 | الاتصال والمنتجات | 8 | BC06، BC03، BC04 |
| CAP-11 | المعرفة والذاكرة المؤسسية | 9 | BC06، BC08 |
| CAP-12 | المساعدة بالذكاء الاصطناعي | 14 | BC07 |
| CAP-13 | الحوكمة والأمن والامتثال | 10 | BC08، BC01، BC02 |
| CAP-14 | تشغيل المنصة | 14 | BC01 (معظم REQ-PLT-* بلا Aggregate — متطلبات منصة لا نموذج مجال) |

القدرات الفرعية الكاملة: `01-business/capabilities.md`. نمط "Capability الظاهرة ≠ BC المنفِّذ" (BC08 منفِّذ مشترك لقدرات واجهتها في BC01/BC06): [04-cross-cutting.md §6.5](04-cross-cutting.md).

## 5. خريطة الميزات (Feature Map)

**[Missing في المصدر]** — لا توجد طبقة Features في `spec/` (لا كيان `FEAT-*`، و`capabilities.md` ينتقل من Capability مباشرة إلى Use Case). لذلك تبدأ كل سلسلة في هذه الدراسة من CAP ثم UC. أقرب بديل عملي هو **الـUse Cases (85)** مجمَّعة حسب القدرة: `02-requirements/use-cases.md`، وكتالوج كل BC في §5 من ملفه. هذا مُسجَّل صراحة في كل ملف BC قبل قسم Actors.

## 6. الفاعلون (Actors)

15 فاعلًا (ACT-01..15) في خمس مجموعات أصحاب مصلحة [Explicit — `01-business/stakeholders.md`]:

| المجموعة | الفاعلون |
|---|---|
| SH-01 القيادة | Executive، Manager |
| SH-02 العمليات | Planner، Operator، Field User، Resource Manager، Logistics User، Risk Manager، Training Manager |
| SH-03 التحليل والمعرفة | Analyst، Knowledge Manager |
| SH-04 الحوكمة | Archivist، Security Officer، Auditor |
| SH-05 الإدارة | Administrator |

إضافة إلى فاعلين نظاميين يظهرون في جداول الأوامر: `system (workload identity)`، المجدول (`SYS:`)، والمحوّلات. **فجوة معروفة [Missing في المصدر]:** كثير من حالات الاستخدام مسودات `actors: TBD` (BC03، BC04، BC06، BC07)؛ الفاعلون في §3 من ملفات تلك الـBCs مُشتقون [Derived] من جداول الأوامر والسياسات.

## 7. مسارات العمل الرئيسية (Major Workflows)

سبعة تيارات قيمة [Explicit — `01-business/value-streams.md`]؛ ربطها بالـBCs [Derived] من القدرات والشرائح:

| التيار | المسار | BCs الرئيسية | الإصدار |
|---|---|---|---|
| VS01 | Information → Understanding | BC02، BC07 (جمع/استيراد)، BC03 | R1 |
| VS02 | Understanding → Decision | BC03 (تحليل)، BC04 (قرار) | R1 |
| VS03 | Decision → Execution | BC04 (خطة/مهمة)، BC05 (تخصيص/أهلية) | R1–R2 |
| VS04 | Risk → Resilience | BC04 (AGG-RISK، AGG-INCIDENT) | R3 (SLC-17) |
| VS05 | Capability → Readiness | BC05 (تأهيل، تدريب، تمارين) | R2–R3 (SLC-09، SLC-19) |
| VS06 | Experience → Knowledge | BC06 (دروس، معرفة) | R2 (SLC-12) |
| VS07 | Record → Institutional Memory | BC06 (أرشيف)، BC08 (احتفاظ، تجميد، إتلاف) | R1 (SLC-12a) + R2 |

العمليات التفصيلية (BP-*): `01-business/processes.md`. مثال سلسلة كاملة من القدرة حتى المستهلك (Authority Grant): [02-relationship-index.md §21.4](02-relationship-index.md).

## 8. الاعتماديات بين الـBCs (Cross-BC Dependencies)

- **خريطة الاعتماد المختصرة** (من/إلى/نوع الرابط): [04-cross-cutting.md §7](04-cross-cutting.md).
- **مستهلكو الأحداث العابرون** (أحداث يذكر مستهلكوها BC آخر صراحةً — 31 حدثًا، معظمها من BC08 نحو كل الـPEPs): [02-relationship-index.md §21.3](02-relationship-index.md).
- **العلاقات المصنَّفة** (`depends_on`، `feeds`، `mitigates`...) واكتشافات كل BC: [02-relationship-index.md §3–§19](02-relationship-index.md).
- **أقوى اعتمادين:** كل BC ← BC08 (قرار PDP يحتاج مخططًا وسياسة فعّالين)؛ BC03/BC04 ← BC05 (الأهلية والتخصيص، fail-closed عند تعطل BC05 — THR-S03-04).

## 9. معمارية الأمن (Security Architecture)

| العنصر | الملخص | التفصيل |
|---|---|---|
| خطوط الأساس | PB-01..14، صفر قابل للتجاوز من المستأجر عدا PB-06 | [04-cross-cutting.md §2.1](04-cross-cutting.md) |
| التخويل | PEP في كل وحدة يطلب قرار PDP (OPA) ويطبق `allowed_scope` قبل القراءة (SL-09، ADR-P06) | `08-security/authorization-model.md` |
| الإفصاح الصفري | المحجوب يُعامَل كأنه غير موجود، لا "access denied" | [04-cross-cutting.md §2.2](04-cross-cutting.md) |
| فصل المهام | كثافته ترتفع مع عدم قابلية العملية للعكس (BC08 الأعلى) | [04-cross-cutting.md §2.3](04-cross-cutting.md) |
| التصنيف | مخطط تصنيف (BC08) + تصريح المستخدم (BC01) + إعادة تصنيف الكائن (BC02) | `08-security/classification-scheme.md` |
| التشفير والإتلاف | تشفير مغلَّف عبر OpenBao + HSM؛ Crypto-shredding للإتلاف والمحو | `08-security/key-hierarchy-and-disposition.md` |
| إبطال الصلاحيات | `EVT-SEC-VERSION-INCREMENTED` من BC01/BC08 يُبطل كل ذاكرات PEP | [04-cross-cutting.md §2.5](04-cross-cutting.md) |
| التهديدات | 114 تهديدًا (STRIDE + OWASP LLM)، 5 مخاطر متبقية M مقبولة صراحة، صفر H | [04-cross-cutting.md §2.4](04-cross-cutting.md) |
| الذكاء الاصطناعي | PB-12..14؛ INV-AIR-02 ضد Prompt Injection؛ AIL ≤ 3 | `10-ai/autonomy-matrix.md` |

حدود الثقة: `08-security/trust-boundaries.md`؛ التدقيق: `08-security/audit-architecture.md`.

## 10. معمارية البيانات (Data Architecture)

- **التخزين:** PostgreSQL + PostGIS بـschema لكل سياق وعنقود لكل خلية (TD-01)؛ الإسقاطات للبحث في OpenSearch (TD-02)؛ لا قاعدة رسوم بيانية في R1 (TD-03).
- **نمط الحفظ الموحَّد:** كل الـ89 Aggregate: `If-Match` + `Idempotency-Key` + State/History/Outbox/AuditOutbox في معاملة واحدة (FIT-04) — [04-cross-cutting.md §3.1](04-cross-cutting.md).
- **نموذج المعلومات:** نواة الادعاء/الدليل، الثقة، التعارض، الأصل والسلالة، النموذج الزمني الثنائي، المكاني — `04-information/*` (claim-evidence-model، temporal-model، provenance-lineage...).
- **البيانات الشخصية:** 4 Aggregates بـ`personal_data: true` (AGG-PERSON، AGG-HR-SYNC-PROPOSAL في BC01؛ AGG-QUALIFICATION-RECORD في BC05؛ AGG-ERASURE-REQUEST في BC08). نطاق المحو مقابل BC05 مفتوح (CONFLICT-04).
- **دورة الحياة:** جداول الاحتفاظ، التجميد القانوني، الإتلاف، المحو — BC08 (SLC-12a).
- **النموذج المنطقي لكل شريحة:** `06-data/logical-model/slc-NN.md`.
- **فجوة:** 6 فئات RD-* مُستشهَد بها وغير معرَّفة في `04-information/reference-data.md` (CONFLICT-03).

## 11. معمارية الواجهات (API Architecture)

- **العقود:** 28 ملف OpenAPI، و19 ملف أخطاء، في `05-contracts/` (موزعة حسب المجال والشريحة، مثل `openapi-foundation-slc01.md`).
- **الأوامر:** 477 أمرًا، كل منها `POST /api/v1/<area>/<resource>[/{id}/actions/<verb>]` بـ`Idempotency-Key` إلزامي و`If-Match` لغير الإنشاء — مصدرها جداول `03-domain/contexts/BC*/commands-slcNN.md`.
- **الاستعلامات:** 133 استعلامًا (117 مرتبطة بـAggregate + 16 عابرة مثل QRY-PDP-DECIDE وQRY-SRCH-QUERY)؛ كلها عبر PEP/PDP قبل القراءة، والقوائم بمؤشر لا offset — [04-cross-cutting.md §4.1](04-cross-cutting.md).
- **الأخطاء الموحَّدة:** `VERSION_CONFLICT` (409)، `IDEMPOTENCY_KEY_REUSED` (422)، `SEGREGATION_OF_DUTIES`، `{AGGREGATE}_INVALID_STATE_TRANSITION` — [04-cross-cutting.md §4.2](04-cross-cutting.md).
- **واجهات الحافة:** BFF لكل عميل عبر DU-01؛ OGC API Features/Tiles للجغرافيا (TD-10، ADR-P12).

## 12. معمارية الأحداث (Event Architecture)

- **الحجم:** 584 حدث مجال مرتبطًا بـAggregate، **كل حدث له منتِج ومستهلك مُعلَن** (صفر بلا مستهلك) — [02-relationship-index.md §21.1](02-relationship-index.md).
- **النقل:** Outbox في نفس المعاملة ← CDC (Debezium) ← Kafka KRaft لكل خلية؛ topic عالي الأولوية لأحداث الأمن (TD-04).
- **مفتاح التقسيم:** `tenant_id + aggregate.id` في كل كتالوج أحداث (ترتيب مضمون لكل Aggregate).
- **الأحداث الأمنية:** كل حدث "يؤثر أمنيًا" يُطلق `EVT-SEC-VERSION-INCREMENTED` المستهلَك من Security-version service وذاكرات PEP.
- **العقود:** 19 ملف AsyncAPI (`05-contracts/asyncapi-slcNN.md`).
- **كتالوجات الأحداث:** `03-domain/contexts/BC*/events-slcNN.md`؛ ربط كل أمر بحدثه ومستهلكيه: [02-relationship-index.md §21](02-relationship-index.md).

## 13. معمارية التكامل (Integration Architecture)

- **إطار المحوّلات الموحَّد:** AGG-ADAPTER (BC07) + AGG-IMPORT-BATCH (BC02)؛ كل ادعاء مستورَد يحمل مصدر المحوّل وموثوقيته ولا يصبح حقيقة آليًا (BRL-013، THR-S02-01).
- **R1:** الهوية (Keycloak/SCIM)، GIS، الطقس. **R2 (SLC-16):** ERP، HRIS (مقترحات فقط تنتظر موافقة — AGG-HR-SYNC-PROPOSAL)، DMS، الحساسات، CAP للتنبيهات الصادرة.
- **المزامنة الميدانية:** بروتوكول offline بـ`base_version` + `client_command_id` + توقيع الجهاز (SLC-11) — `03-domain/contexts/BC07/field-sync-protocol.md`.
- **الجغرافيا:** OGC API، WMS/WFS للاستيراد، GeoJSON/GeoPackage/COG (TD-10، `04-information/spatial-model.md` §6).
- **فهرس المواصفات:** `11-integration/README.md`.

## 14. تتبّعية المتطلبات (Requirements Traceability)

| المقياس | القيمة | المصدر |
|---|---|---|
| متطلبات النظام | **210** (R1 114 · R2 51 · R3 45) | `02-requirements/requirements.md` |
| متطلبات يلبيها Aggregate واحد على الأقل | 173 (تداخل فعلي بين BCs: 11) | [04-cross-cutting.md §6.2](04-cross-cutting.md) |
| متطلبات لا يلبيها أي Aggregate | 37 (معظمها منصة/جودة أو OQ-034 أو R3) | [02-relationship-index.md §21.2](02-relationship-index.md) |
| تتبّع R1 (OUT → BRQ → REQ → slice → verification) | 114/114 | `15-traceability/rtm-r1.md` |
| تتبّع R2 | — | `15-traceability/rtm-r2.md` |
| السلسلة الكاملة لكل Aggregate | 89/89 | [02-relationship-index.md §21](02-relationship-index.md) |
| فجوات REQ → UC حقيقية | BC04، BC05، BC07 | CONFLICT-05 |

**تنبيه [Explicit، Needs Review]:** رأس `system_requirements` في `requirements.md` يقول `_181 items_` بينما الملف يحوي 210 — رأس قديم في المصدر، انظر §17 والبند 5 في §20.3.

## 15. نماذج الحالات على مستوى النظام (System-wide State Models)

- **89 آلة حالات** (واحدة لكل Aggregate)، **420 حالة** إجمالًا، بمتوسط 4.7 حالة لكل Aggregate. [Derived — عدّ آلي من ملفات الـAggregates]
- **الأعقد:** AGG-TASK (15 حالة، 5 نهائية)، ثم AGG-PRODUCT (9)، AGG-AI-REQUEST وAGG-LOGISTICS-REQUEST وAGG-ER-CASE (8 لكل منها).
- **SL-05:** مصفوفة الحالات × الأوامر كاملة في كل Aggregate (لا خلية فارغة).
- **SL-06:** PASS في 85، وEXEMPT مُعلَّل في 4 (ORGANIZATION، ENTITY، REALWORLD-EVENT، RELATIONSHIP — تُحفَظ للتاريخ فحالتها الأخيرة قابلة للعكس عمدًا)، صفر FAIL — [04-cross-cutting.md §5](04-cross-cutting.md).
- **ملف اختبار قبول لكل آلة:** 89/89 في `13-verification/acceptance/SLC-NN/*-state-machine.md`.
- جداول الانتقالات لكل Aggregate: §6 من ملف الـBC، والمصدر في `03-domain/contexts/BC*/aggregates/`.

## 16. التعارضات (Conflicts)

| # | التعارض | الحالة |
|---|---|---|
| CONFLICT-01 | ملكية REQ-GOV-004 (BC08 مقابل BC01) | CLOSED (CR-64، CR-65) |
| CONFLICT-02 | نمط "الشريحة ≠ Bounded Context" (3 حالات سوء إسناد تهديدات) | CLOSED |
| CONFLICT-03 | 6 فئات RD-* مُستشهَد بها وغير معرَّفة | **OPEN** |
| CONFLICT-04 | نطاق AGG-ERASURE-REQUEST لا يشمل BC05 رغم `personal_data: true` | **OPEN** |
| CONFLICT-05 | فجوات تغطية REQ → UC حقيقية (BC04، BC05، BC07) | **OPEN** |

التفاصيل والمرشحون الذين فُحصوا ولم يُثبَتوا كتعارض: [05-conflicts.md](05-conflicts.md).

## 17. المعلومات الناقصة (Missing Information)

| البند | التصنيف | أين |
|---|---|---|
| طبقة Features غير موجودة في المصادر | Missing في المصدر | §5 أعلاه |
| حالات استخدام مسودات `actors: TBD` (UC-010..024، 030..046، 060..065، 070..074، 050..055) | Missing في المصدر | §20 من ملفات BC03/04/05/06/07 |
| 6 فئات RD-* بلا تعريف | Missing | CONFLICT-03 |
| جولة تحقق سطرًا بسطر لملفات acceptance وعقود OpenAPI/AsyncAPI (قُرئت بالاسم والعدد فقط في معظم الـBCs) | Missing verification pass | §20 من كل ملف BC |
| رأس `requirements.md` يقول 181 والمحتوى 210 | خلل في المصدر، Needs Review | [04-cross-cutting.md §6.2](04-cross-cutting.md) |
| `system-definition.md` §4 و`slices.md` ما زالا يعرّفان R3 كشريحة واحدة SLC-13 (`g6_slc: NOT_STARTED`)، بينما R3 فُكِّك فعليًا إلى SLC-17/18/19 بملفات تصميم كاملة | خلل في المصدر (غير محدَّث)، Needs Review | `14-slices/slices.md`، `01-business/release-3-scope.md` |
| `EVOLUTION-ROADMAP.md` يقول "لا تصميم تفصيلي بدأ" لـR3، بينما SLC-17/18/19 لها عقود ونماذج تهديد وقبول | خلل في المصدر (غير محدَّث)، Needs Review | `16-reports/EVOLUTION-ROADMAP.md` |
| الولاية القانونية الفعلية (UNK-002) والميزانية (UNK-012) | Unknown، غير حاجب للتصميم | `00-governance/registers/unknowns.md` |
| "الاتصالات الموسعة" في R3 غير مُفكَّكة (UNK-022) | Unknown | `01-business/release-3-scope.md` |

## 18. المخاطر (Risks)

- **سجل المخاطر:** 28 خطرًا (RSK-001..028): 25 مفتوحًا، 2 مخفَّفان، 1 مغلق. الوحيد المفتوح بتقدير H/H هو **RSK-001** (نطاق 26 مجالًا للإصدار الأول) — `00-governance/registers/risks.md`.
- **المخاطر الأمنية المتبقية:** 5 تهديدات بمخاطرة متبقية M مقبولة صراحة (THR-S01-04، THR-S01-11، THR-S10-04، THR-S05-08، THR-S12-P2)، صفر H — [04-cross-cutting.md §2.4](04-cross-cutting.md).
- **مخاطر المعمارية ومحفّزات العكس:** `16-reports/ARCHITECTURE-REVIEW-R1.md`، `ARCHITECTURE-REVIEW-R2.md`، و`EVOLUTION-ROADMAP.md` (محفّزات Pilot).
- **الفشل والتدهور:** FMEA لكل شريحة `09-reliability/fmea-slcNN.md`؛ الاستمرارية والتعافي `09-reliability/dr-and-continuity.md`.
- **الدَّين التقني:** `00-governance/registers/technical-debt.md`.

## 19. حالة التحقق (Verification Status)

| المستوى | الحالة | المصدر |
|---|---|---|
| ملف قبول لكل آلة حالات | 89/89 (مطابقة بالاسم مع `traces.state_machine`) | [02-relationship-index.md §21.1](02-relationship-index.md) |
| قراءة ملفات القبول سطرًا بسطر مقابل جداول الانتقالات | **لم تُنفَّذ** إلا في BC01 وملف واحد في BC06 | §20 من كل ملف BC |
| سيناريوهات الجودة بطريقة تحقق | 74/74 | `15-traceability/quality-verification-matrix.md` |
| Fitness functions | 19 (FIT-01..19) | `13-verification/fitness-functions.md` |
| خصائص الثوابت لكل شريحة | 19 ملفًا | `13-verification/invariant-properties-slcNN.md` |
| قواعد فحص المواصفات (SL-*) | مطبَّقة آليًا عبر الأدوات المضمَّنة | `13-verification/spec-lint-rules.md`، `13-verification/tooling/` |
| التحقق التنفيذي (أداء، DR، اختراق تحت الحمل) | خارج مرحلة الدراسة — شروط G8 | `16-reports/IMPLEMENTATION-READINESS-R1.md` |

## 20. الاكتمال الإجمالي (Overall Completeness)

### 20.1 حالة المراحل

| المرحلة | الحالة |
|---|---|
| Phase 1 — الجرد | ✅ CLOSED |
| Phase 2 — فهرس الكيانات والعلاقات وجودة البيانات | ✅ CLOSED (السلاسل الكاملة أُضيفت آليًا في Phase 3.6) |
| Phase 3 — إعادة بناء الـBCs | ✅ **مكتملة هيكليًا**: الثمانية بقالب 21 قسمًا. **حالة المحتوى:** 2 مغلقة أو شبه مغلقة، 6 مفتوحة ببنود قرار بشري أو تحقق (انظر 20.2) |
| Phase 3.5 — رفع عمق BC02–BC07 لمستوى BC01 | ✅ CLOSED |
| Phase 3.6 — تدقيق آلي للأرقام وتوليد السلاسل وإعادة هيكلة هذا الفهرس | ✅ CLOSED |
| Phase 4 — الأنماط العابرة | ✅ CLOSED (صُحِّح في 3.5 و3.6) |
| Phase 5 — التعارضات | ✅ CLOSED كسجل (3 تعارضات مفتوحة بانتظار قرار) |
| Phase 6 — هذا الفهرس | ✅ CLOSED |

### 20.2 حالة كل BC (من §21 في ملفه)

| BC | الحالة | ما يبقيها مفتوحة |
|---|---|---|
| BC01 | OPEN | تأكيد بشري لـCR-64/CR-65 (البند 3 أدناه) |
| BC02 | CLOSED هيكليًا وأمنيًا | جولات تحقق تكميلية (acceptance، OpenAPI) |
| BC03 | OPEN جزئيًا | فحص `openapi-operations-slc06.md`؛ هل يستحق REQ-SIT-006/REQ-ANL-008 سؤالًا مفتوحًا مثل OQ-034 |
| BC04 | OPEN | CONFLICT-05 (CAP-09 بلا UC)؛ RD-HAZARD-CATEGORIES (CONFLICT-03) |
| BC05 | OPEN | CONFLICT-03، CONFLICT-04، CONFLICT-05 |
| BC06 | CLOSED جزئيًا | بندان إجرائيان (تحقق acceptance، سؤال SoD لتعديل قالب نشط) |
| BC07 | OPEN | `actors: TBD` لـUC-070..074؛ سؤال مفتوح مماثل لـOQ-034 لعمليات الحوكمة الداخلية |
| BC08 | OPEN جزئيًا | تحقق Verification/Acceptance سطرًا بسطر |

### 20.3 ما يحتاج قرارًا بشريًا الآن (كل البنود المفتوحة في مكان واحد)

| # | البند | الملف المرجعي | نوع القرار |
|---|---|---|---|
| 1 | فجوة RD-* الست: استنباط من الاستخدام أم ورشة عمل مخصَّصة؟ | [05-conflicts.md §4](05-conflicts.md) | سياسة بيانات مرجعية |
| 2 | نطاق AGG-ERASURE-REQUEST: هل يشمل BC05 (Qualification-Record) أم استبعاد متعمَّد؟ | [05-conflicts.md §5](05-conflicts.md) | مراجعة نطاق أمن/خصوصية |
| 3 | CR-64/CR-65 (UC-089 + traces.satisfies الجديد): تأكيد بشري نهائي على التصنيف | `corrections.md` (CR-64 status: `APPLIED_IN_SPEC` معلَّق تأكيدًا) | اعتماد حوكمة |
| 4 | CONFLICT-05: فجوات REQ → UC — BC04 (REQ-RCM-001..016)، BC05 (REQ-LOG-*/REQ-TRX-*)، BC07 (MODEL-VERSION، EVAL-SUITE، PROJECTION-VERSION) — تسجيلها كـOQ رسمية تمهيدًا لكتابة UCs، أم تأكيد أنها عمل مؤجَّل (BC05 تحديدًا R3)؟ | [05-conflicts.md §6](05-conflicts.md) | فتح OQ جديدة أو تأكيد تأجيل |
| 5 | تصحيح رأس `requirements.md` (`_181 items_` ← 210) عبر CR جديد، لأن الملف ضمن خط الأساس | [04-cross-cutting.md §6.2](04-cross-cutting.md) | CR تحريري |
| 6 | تحديث `system-definition.md` §4 و`slices.md` (SLC-13 ← SLC-17/18/19) و`EVOLUTION-ROADMAP.md` (حالة تصميم R3) | §17 أعلاه | CR تحريري |

**لا بنود أخرى معلَّقة في نطاق الدراسة الثمانية BCs** خلاف البنود الستة أعلاه — كل تصحيح رجعي آخر (THR-S06، THR-S16-02، THR-S01-05/06، أعداد BC01، SL-06، التداخل) طُبِّق بالكامل.

### 20.4 أرقام رئيسية (كل رقم مرتبط بمصدره)

- **705** ملف مصدري ([00-inventory.md](00-inventory.md))
- **3999+** كيان فريد مفهرَس ([01-entity-index.md](01-entity-index.md))
- **210** متطلبًا (173 يلبيها Aggregate، تداخل فعلي 11 — [04-cross-cutting.md §6.2](04-cross-cutting.md))
- **89** aggregate عبر 8 BCs، **صفر استثناء** من نمط If-Match + Idempotency-Key + State/History/Outbox/AuditOutbox ([04-cross-cutting.md §3.1](04-cross-cutting.md))
- **477** أمرًا، **584** حدثًا، **133** استعلامًا ([02-relationship-index.md §21.1](02-relationship-index.md))
- **114** تهديدًا موثَّقًا (STRIDE) بعد كل التصحيحات الرجعية، بما فيها إعادة العدّ الدقيقة في Phase 3.5 (كانت مُقدَّرة بـ"~121" قبل ذلك) ([04-cross-cutting.md §2.4](04-cross-cutting.md))
- **14** Platform Baseline (PB-01..14)، صفر قابل للتجاوز من المستأجر عدا PB-06 ([04-cross-cutting.md §2.1](04-cross-cutting.md))
- **65** تصحيحًا مُطبَّقًا على المصادر (CR-01..CR-65، `spec/00-governance/registers/corrections.md`)
- **5** تعارضات مُكتشَفة أثناء البناء (آخرها CONFLICT-05 أثناء Phase 3.5): 2 مُغلَقة، 3 مفتوحة ([05-conflicts.md](05-conflicts.md))

## 21. روابط دراسات الـBCs التفصيلية

كل ملف BC يتبع نفس القالب (مستوى مبسّط + مستوى هندسي): 1 الهوية · 2 المعنى التجاري (+ ملاحظة Features) · 3 Actors · 4 Requirements · 5 Use Cases · 6 Aggregates والحالات · 7 Commands · 8 Queries · 9 Events · 10 Business Rules/Invariants · 11 Policies · 12 Security & Threats · 13 Data & APIs · 14 Integrations · 15 Verification · 16 Dependencies · 17 Cross-BC · 18 Traceability · 19 Conflicts · 20 Missing Information · 21 Completeness Status.

| BC | الدراسة التفصيلية | السلاسل المولَّدة |
|---|---|---|
| BC01 | [bc01-foundation.md](bc01-foundation.md) | [02-relationship-index.md §21.4](02-relationship-index.md) |
| BC02 | [bc02-information-core.md](bc02-information-core.md) | [§21.5](02-relationship-index.md) |
| BC03 | [bc03-situational-awareness.md](bc03-situational-awareness.md) | [§21.6](02-relationship-index.md) |
| BC04 | [bc04-planning-execution.md](bc04-planning-execution.md) | [§21.7](02-relationship-index.md) |
| BC05 | [bc05-resources-readiness.md](bc05-resources-readiness.md) | [§21.8](02-relationship-index.md) |
| BC06 | [bc06-knowledge-products.md](bc06-knowledge-products.md) | [§21.9](02-relationship-index.md) |
| BC07 | [bc07-integration-ai-discovery.md](bc07-integration-ai-discovery.md) | [§21.10](02-relationship-index.md) |
| BC08 | [bc08-governance-security.md](bc08-governance-security.md) | [§21.11](02-relationship-index.md) |

---

## ملحق أ — ما هو خارج نطاق هذه الدراسة عمدًا

- تفاصيل العقود التقنية الكاملة (OpenAPI/AsyncAPI schemas الحرفية) — مُشار إليها بالمسار فقط في كل ملف BC، لا مُستنسَخة.
- ملفات `06-data/logical-model/*`، `07-quality/*`، `09-reliability/*`، `13-verification/*` بالتفصيل الكامل — استُهلِكت مفاهيميًا (SL-05/06/09، FIT-04) في [04-cross-cutting.md §5](04-cross-cutting.md) دون نسخ محتواها.
- أي عمل تنفيذي (كود، بنية تحتية فعلية) — هذه دراسة نموذج المجال (domain model) والمواصفات فقط.

## ملحق ب — كيف تُحدَّث هذه الدراسة مستقبلاً

1. أي تعديل على ملف مصدر في `spec/` (خارج `17-system-study/`) يُقابَله فحص: هل يمس رقمًا أو جدولاً هنا؟ إن كان كذلك، حدِّث ملف الـBC أو `04-cross-cutting.md` أو `05-conflicts.md` المعني مباشرة.
2. أعِد توليد السلاسل: `python3 spec/17-system-study/_build/build_relationships.py` — يعيد كتابة §21 من [02-relationship-index.md](02-relationship-index.md) فقط، ويكشف أي فرق في أعداد الأوامر والأحداث والاستعلامات مقابل ملفات الـBC.
3. سجِّل كل تصحيح لخطأ سابق في مصدر كـCR جديد في `corrections.md`، لا تعديلاً صامتًا؛ والأخطاء الداخلية في ملفات الدراسة تُصحَّح في مكانها مع ملاحظة "تصحيح [Phase X]".
