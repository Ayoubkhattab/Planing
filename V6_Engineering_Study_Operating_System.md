# V6 — ENGINEERING STUDY OPERATING SYSTEM
## From Architecture Study to Programmable Specification

**المشروع:** Unified Geospatial Information, Intelligence, Knowledge, Planning & Operations Platform

**المصادر:**
- V5 — AI Multi-Agent Engineering Study, Architecture & Quality Operating System
- مستند المشروع الكامل (Architecture Blueprint)
- نتائج دراستين مستقلتين لمستند المشروع: مراجعة دقيقة، ثم دراسة وفق V5

**الحالة:** PROPOSED — تتطلب اعتماداً بشرياً قبل أن تصبح مرجعاً ملزماً.

---

# 0. كيف يُستخدم هذا الملف

هذا الملف هو المرجع التشغيلي الوحيد للدراسة الهندسية. يحل محل V5 ويحتفظ بكل مبادئه، ويضيف ما يلزم لتحويل الدراسة من وثائق معمارية إلى **مواصفة قابلة للبرمجة**.

يُستخدم بطريقتين:

1. **كـ Master Prompt لنظام وكلاء ذكاء اصطناعي.** يُحمَّل هذا الملف مع مستند المشروع ومستودع المواصفات الحالي، ويُطلب تنفيذ موجة واحدة (Wave) في كل جلسة، وفق بروتوكول القسم 21.
2. **كدليل لفريق بشري.** الموجات والقوالب ومعايير الجاهزية تنطبق كما هي على فريق هندسي تقليدي.

ترتيب القراءة المقترح: الأقسام 2 و3 و9 و10 و11 أولاً، فهي تحدد ما هو المطلوب ومتى يعتبر منجزاً.

---

# 1. ما الذي تغيّر عن V5

| المجال | V5 | V6 | السبب |
|---|---|---|---|
| تعريف النجاح | Engineering Baseline | **Programmable Specification** بمعيار قابل للفحص (القسم 2) | "Baseline" بلا معيار قبول يمكن أن يكون مجموعة وثائق غير قابلة للتنفيذ |
| وحدة الجاهزية | G6 للنظام كله | **G6 لكل شريحة (Slice)** + G6 للنواة | انتظار جاهزية 26 مجالاً معاً يعني عدم الوصول إليها أبداً |
| المخرجات | 113 مخرجاً بلا أولوية | **4 مستويات (T0–T3)** مرتبطة بالموجات والشرائح | ليس كل مخرج مطلوباً قبل أول سطر كود |
| صيغة المخرجات | غير محددة | **صيغ قابلة للقراءة آلياً** حيث يستهلكها برنامج (YAML، JSON Schema، OpenAPI، AsyncAPI، Gherkin) | المواصفة التي لا يمكن فحصها آلياً تنحرف بصمت |
| الاتساق | فحص يدوي (القسم 110) | **قواعد فحص آلية للمواصفة** (القسم 16) | الاتساق بين مئات المخرجات لا يُضمن يدوياً |
| المنهجيات | "ادرس X" | **تقنية معتمدة محددة لكل نشاط** (القسم 5) | تقليل التباين بين الوكلاء |
| متطلبات الجودة | قوائم خصائص | **Quality Attribute Scenarios** قابلة للقياس | "يجب أن يكون سريعاً" غير قابل للتحقق |
| المجهولات | سجل | سجل + **بنك أسئلة لأصحاب القرار** + نقاط اعتماد بشري إلزامية | المجهولات لا تُغلق بالتحليل بل بالسؤال |
| نتائج الدراسات السابقة | — | **30 تصحيحاً لخط الأساس** + **15 قراراً معمارياً مقترحاً** | إدماج ما اكتُشف من تناقضات وفجوات |
| اللغة | RTL وLocalization ضمن Accessibility | **اللغة العربية قرار معماري** يؤثر على مطابقة الكيانات والبحث | مطابقة الأسماء العربية مشكلة بيانات، لا مشكلة واجهة |
| التسمية | L0–L5 للوكلاء وللـ AI بنفس الرموز | **DAL** لصلاحيات وكلاء الدراسة، **AIL** لاستقلالية AI في المنتج | إزالة الالتباس |
| نهاية الملف | مبتورة في القسم 124 | مكتملة (القسم 22) | — |

---

# 2. تعريف النجاح: المواصفة القابلة للبرمجة

## 2.1 التعريف

> **Programmable Specification** هي مواصفة تسمح لمهندس — أو وكيل برمجة — بتنفيذ جزء من النظام **دون أن يتخذ أي قرار معماري أو قرار عمل بنفسه**، وتسمح لطرف ثالث بالتحقق آلياً من أن التنفيذ مطابق لها.

الاختبار العملي لأي مخرج:

```text
هل يستطيع منفّذ لا يعرف تاريخ المشروع أن يبني هذا الجزء
من المواصفة وحدها،
دون أن يسأل سؤالاً يغير السلوك أو البيانات أو الأمن،
وأن يعرف متى انتهى؟
```

إذا كانت الإجابة "لا"، فالمخرج غير جاهز، مهما كان طوله أو جودة صياغته.

## 2.2 ما يجعل Aggregate قابلاً للبرمجة

الـ Aggregate هو الوحدة الأساسية للتنفيذ. يعتبر قابلاً للبرمجة فقط إذا توفر له:

1. **الثوابت (Invariants)** مرقمة، كل منها جملة قابلة للتحويل إلى اختبار.
2. **جدول حالات كامل**: كل حالة × كل أمر → مسموح (مع الشرط والحدث) أو ممنوع (مع رمز الخطأ). لا توجد خلية فارغة.
3. **لكل أمر (Command)**: الفاعل، سياسة الصلاحية، الشروط المسبقة، مفتاح عدم التكرار (Idempotency)، الأحداث الناتجة، الأخطاء الممكنة.
4. **لكل حدث (Event)**: مخطط بيانات بإصدار (JSON Schema أو AsyncAPI)، ومن يستهلكه.
5. **النموذج المنطقي للبيانات**: الكائنات والعلاقات والقيود، دون اختيار محرك قاعدة البيانات إن لم يُحسم بعد.
6. **استراتيجية التزامن**: Optimistic Versioning أو غيرها، وسلوك التعارض.
7. **مستوى الأهمية (Tier)**: هل يحتاج Claims وProvenance وثنائية زمنية أم Versioning فقط (ADR-P03).
8. **عقد الواجهة**: OpenAPI للأوامر والاستعلامات.
9. **سيناريوهات القبول**: Gherkin، تغطي المسار الطبيعي وكل انتقال ممنوع وكل حالة صلاحية.
10. **سيناريوهات الجودة** المرتبطة به، بقيم محددة أو TBD مع مالك وموعد إغلاق.
11. **صفر مجهولات حرجة** مفتوحة تمس سلوكه.

## 2.3 ما لا يُعتبر دليلاً على الجاهزية

- طول الوثيقة أو عدد المخرجات.
- وجود علامة ✓ دون دليل ومعتمِد.
- مخططات بلا جداول انتقال أو عقود.
- موافقة وكلاء متعددين دون قرار بشري موثق (لا Majority Vote).

---

# 3. قيد المرحلة الحالية

يبقى قيد V5 كما هو: **لا Production Code، لا Infrastructure، لا Deployment، لا Credentials، لا بيانات أعمال مخترعة.**

**توضيح V6:** ملفات المواصفة بصيغ قابلة للقراءة آلياً — مثل YAML وJSON Schema وOpenAPI وAsyncAPI وملفات Gherkin ومخططات Mermaid — **ليست كوداً إنتاجياً**. هي مواصفات مسموحة، بل مطلوبة. كذلك "مستودع المواصفات" في القسم 8 حزمة وثائق، وليس مستودع كود.

يُسمح أيضاً بكتابة قواعد فحص المواصفة (القسم 16) كمواصفة، لا كأداة منفذة.

---

# 4. المسلّمات المعمارية

## 4.1 مسلّمات V5 (محتفظ بها كما هي)

| # | المسلّمة | الجوهر |
|---|---|---|
| A01 | Business Before Technology | Business → Requirements → Workloads → Constraints → Architecture → Technology |
| A02 | Semantics Before Schema | المعنى والمسؤولية والدورة قبل الجداول |
| A03 | Invariants Before CRUD | ما يجب أن يبقى صحيحاً، ومن يغيّره، وبأي شرط، وماذا يُسجَّل |
| A04 | Ownership Before Integration | مالك واحد لكل كائن، أو نموذج تعارض صريح |
| A05 | Entity ≠ Event | الكيان له هوية مستمرة، والحدث وقع في زمن |
| A06 | Evidence ≠ Truth | الدليل يدعم ادعاءً ولا يساويه |
| A07 | Projection ≠ Source of Truth | البحث والرسم والتحليلات إسقاطات قابلة لإعادة البناء |
| A08 | History Must Be Preserved | لا كتابة صامتة فوق المعلومات المهمة |
| A09 | Authorization Before Retrieval | في كل مسار استرجاع دون استثناء |
| A10 | AI Is Not Automatically Authority | مساعد ما لم تسمح سياسة صريحة |
| A11 | Commands ≠ Queries ≠ Events | تغيير، قراءة، تسجيل |
| A12 | Domain Boundaries Before Service Boundaries | Domain → Context → Application → Service → Module |
| A13 | Technology Must Follow Workload | لا تقنية قبل فهم الحمل والقيود |

## 4.2 مسلّمات V6 الجديدة

**A14 — Readiness Is Per Slice.**
الجاهزية للتنفيذ تُمنح لشريحة محددة، بعد جاهزية النواة المشتركة. لا ينتظر المشروع جاهزية كل المجالات.

**A15 — Machine-Consumed Means Machine-Readable.**
أي مواصفة سيستهلكها برنامج (توليد كود، اختبار، فحص اتساق) تُكتب بصيغة قابلة للقراءة آلياً. السرد النصي للتفسير فقط.

**A16 — Quality Is a Scenario, Not an Adjective.**
كل متطلب جودة يُكتب كسيناريو له مصدر ومحفز وبيئة واستجابة ومقياس. الصفة وحدها ("آمن"، "سريع") ليست متطلباً.

**A17 — Depth Proportional to Importance.**
ليس كل حقل يحتاج Claims وEvidence وثنائية زمنية. عمق النموذج يتحدد بمستوى الأهمية (ADR-P03). تطبيق الحد الأقصى على كل شيء نمط مضاد بقدر إهماله.

**A18 — Human Decisions Are Captured, Not Assumed.**
كل قرار يتطلب سلطة عمل أو أمن أو قانون له مالك بشري مسمى ونقطة اعتماد (القسم 21.4). الوكيل يقترح ويوثق الخيارات، ولا يقرر.

**A19 — Language Is Architecture.**
اللغة العربية والنقحرة والتقويم تؤثر على مطابقة الكيانات والبحث والتخزين والعرض. تُعالج في النموذج المعلوماتي، لا في طبقة الواجهة فقط.

**A20 — No Orphan Artifacts.**
كل مخرج له مستهلك معروف (مخرج آخر، أو تنفيذ، أو اختبار، أو قرار). المخرج الذي لا يستهلكه أحد لا يُنتج.

**A21 — Security Includes Inference.**
منع الوصول لا يكفي. يجب منع **الاستدلال** على وجود بيانات محجوبة عبر العدد أو الـ Facets أو زمن الاستجابة أو رسائل الخطأ أو الـ Tiles المخزنة مؤقتاً.

---

# 5. المنهجية المركّبة: التقنية المعتمدة لكل نشاط

V5 يحدد **ماذا** يُدرس. هذا القسم يحدد **كيف**، باستخدام تقنيات هندسية معروفة ومجربة، حتى تنتج الوكلاء والفرق مخرجات متسقة.

| النشاط | التقنية المعتمدة | المخرج |
|---|---|---|
| تعريف النظام والنطاق | System Context + Scope Statement (In / Out / Deferred) | System Definition |
| أصحاب المصلحة | Stakeholder Map (Power / Interest) + Decision Rights (RACI) | Stakeholder Model |
| القدرات | Business Capability Mapping (3 مستويات كحد أقصى) | Capability Map |
| سلاسل القيمة | Value Stream Mapping (محتفظ به من المشروع) | Value Streams |
| اكتشاف السلوك | **Event Storming** على ثلاث مراحل: Big Picture ثم Process Level ثم Design Level | Events، Commands، Policies، Aggregates، Read Models |
| صياغة المتطلبات | **EARS** (Easy Approach to Requirements Syntax) | Requirements Baseline |
| جودة المتطلبات | خصائص ISO/IEC/IEEE 29148 (Necessary، Unambiguous، Verifiable، Consistent…) | Requirements Quality Report |
| متطلبات الجودة | **Quality Attribute Scenarios** (أسلوب SEI) | Quality Scenarios |
| مراجعة المعمارية | **ATAM-lite**: Utility Tree، ثم Sensitivity Points، ثم Trade-offs، ثم Risks | Architecture Review Report |
| الحدود | DDD Context Mapping (Upstream/Downstream، ACL، Published Language…) | Context Map |
| التصميم الداخلي | Aggregate Design Canvas + State Transition Tables | Aggregate وState Machine Specs |
| توثيق المعمارية | **C4 Model** (Context، Container، Component) + هيكل arc42 | Solution Architecture Views |
| القرارات | **MADR** (Markdown ADR) | ADR Catalog |
| التهديدات الأمنية | **STRIDE** لكل حد ثقة + Attack Trees للمسارات الحرجة | Threat Model |
| تهديدات الخصوصية | **LINDDUN** | Privacy Threat Model |
| تهديدات الذكاء الاصطناعي | OWASP Top 10 for LLM Applications + Excessive Agency Analysis | AI Threat Model |
| متطلبات التحقق الأمني | OWASP ASVS (المستوى يحدد بقرار) | Security Verification Strategy |
| الاعتمادية | **FMEA** (Failure Mode and Effects Analysis) | Failure Mode Analysis |
| التدهور التدريجي | Degradation Matrix (القدرة × فشل الاعتمادية) | Resilience Architecture |
| الأداء والسعة | Workload Characterization + Queueing / Back-of-Envelope Models | Workload Catalog، Capacity Model |
| التكلفة | Unit Economics (تكلفة لكل عملية / مستأجر / طلب AI) | Cost Model |
| الحوكمة المعمارية | **Architecture Fitness Functions** | Fitness Model |
| القبول | **Gherkin** (Given / When / Then) | Acceptance Specs |
| الثوابت | Property-Based Test Specifications | Invariant Test Specs |
| التتبع | Graph of IDs (القسم 7) | Traceability Matrices (مولدة، لا مكتوبة يدوياً) |

**قاعدة:** إذا رأى وكيل أن تقنية أخرى أنسب لسياق معين، يسجل ذلك كمقترح مع السبب، ولا يستبدل التقنية المعتمدة بصمت.

---

# 6. الحالات المعرفية والأدلة

## 6.1 الحالات (من V5، محتفظ بها)

```text
VERIFIED      — تم التحقق منه بدليل مستقل
DOCUMENTED    — مذكور في مصدر موثق، غير معتمد رسمياً
OBSERVED      — لوحظ في نظام أو بيانات فعلية
INFERRED      — مستنتج منطقياً من معلومات أخرى
ASSUMED       — افتراض صريح مسجل في Assumption Register
UNKNOWN       — غير معروف، مسجل في Unknown Register
CONFLICTING   — مصادر متعارضة، مسجل كتعارض
PROPOSED      — اقتراح لم يُعتمد
REJECTED      — مرفوض مع السبب
APPROVED      — (إضافة V6) معتمد من مالك القرار البشري، مع الاسم والتاريخ
```

**إضافة V6:** حالة `APPROVED` منفصلة عن `VERIFIED`. الاعتماد قرار سلطة، والتحقق دليل حقيقة. قرار معماري قد يكون APPROVED دون أن يكون VERIFIED حتى يُختبر.

## 6.2 صيغة الوسم

كل عبارة جوهرية في أي مخرج تحمل وسمها ومرجعها:

```text
[DOC:PRJ§55] Task يبدأ بحالة DRAFT.
[INF] الانتقال من UNDER_REVIEW إلى IN_PROGRESS يمثل إعادة العمل.
[ASM:ASM-004] الواجهات الثلاث مطلوبة في الإصدار الأول.
[UNK:UNK-006] مستويات التصنيف الأمني غير معروفة.
[PRO:ADR-P01] نموذج ثنائي الزمن.
```

الرموز المختصرة: `VER`، `DOC`، `OBS`، `INF`، `ASM`، `UNK`، `CON`، `PRO`، `REJ`، `APR`.

المراجع: `PRJ§n` لمستند المشروع، `V5§n` لملف V5، `V6§n` لهذا الملف، أو معرّف أي مخرج.

## 6.3 أولوية المصادر (من V5، مع إضافة)

```text
Approved Architecture Decision
> Approved Requirement
> Approved Business / Domain Contract
> Approved API / Event Contract
> Verified System Behavior
> Current Implementation
> Existing Documentation         ← مستند المشروع الحالي هنا بالكامل
> Explicit Assumption
> Agent Inference                ← (إضافة V6) أدنى مرتبة، ولا يصبح حقيقة بالتكرار
```

---

# 7. نظام المعرّفات والتتبع

التتبع في V5 يعتمد على مصفوفات تُكتب يدوياً، وهي تنحرف بسرعة. في V6 **كل مخرج يحمل معرّفاً ثابتاً، ويعلن علاقاته في رأسه**، والمصفوفات تُولّد من هذه العلاقات.

## 7.1 البادئات

| البادئة | النوع | مثال |
|---|---|---|
| `OUT` | Business Outcome | OUT-01 |
| `CAP` | Capability | CAP-02.03 |
| `VS` | Value Stream | VS01 |
| `BP` | Business Process | BP05 |
| `BRL` | Business Rule | BRL-006 |
| `BRQ` | Business Requirement | BRQ-004 |
| `REQ` | System Requirement (وظيفي) | REQ-INF-012 |
| `QAS` | Quality Attribute Scenario | QAS-PERF-003 |
| `UC` | Use Case | UC-041 |
| `DOM` | Domain | DOM-13 |
| `BC` | Bounded Context | BC04 |
| `BO` | Business Object | BO-TASK |
| `AGG` | Aggregate | AGG-TASK |
| `INV` | Invariant | INV-TASK-03 |
| `SM` | State Machine | SM-TASK |
| `CMD` | Command | CMD-TASK-COMPLETE |
| `QRY` | Query | QRY-TASK-BY-PLAN |
| `EVT` | Event | EVT-TASK-COMPLETED |
| `POL` | Policy Rule | POL-AUTHZ-TASK-APPROVE |
| `API` | API Operation | API-OPS-TASK-COMPLETE |
| `WL` | Workload | WL-03 |
| `THR` | Threat | THR-SRCH-004 |
| `FM` | Failure Mode | FM-OUTBOX-002 |
| `SLO` | Service Level Objective | SLO-TASK-CMD-LAT |
| `TST` | Test / Acceptance Spec | TST-TASK-017 |
| `FIT` | Fitness Function | FIT-006 |
| `ADR` | Architecture Decision | ADR-012 (معتمد) / ADR-P01 (مقترح) |
| `RSK` | Risk | RSK-008 |
| `ASM` | Assumption | ASM-003 |
| `UNK` | Unknown | UNK-007 |
| `DEP` | Dependency | DEP-EXT-004 |
| `OQ` | Open Question | OQ-021 |
| `DEBT` | Technical Debt | DEBT-002 |
| `CR` | Baseline Correction | CR-14 |
| `SLC` | Slice | SLC-03 |
| `HAP` | Human Approval Point | HAP-05 |

**تحذير:** البادئة `BR` في مستند المشروع مستخدمة لنوعين (قواعد ومتطلبات). في V6 تُستبدل بـ `BRL` للقواعد و`BRQ` للمتطلبات (CR-07).

## 7.2 رأس المخرج (Front-matter)

كل ملف مواصفة يبدأ برأس موحد:

```yaml
---
id: AGG-TASK
type: aggregate
title: Task Aggregate
wave: W4
slice: SLC-03
tier: T1
bounded_context: BC04
owner_role: Operations Workstream
status: PROPOSED            # DRAFT | PROPOSED | IN_REVIEW | APPROVED | SUPERSEDED
epistemic_summary:
  documented: 12
  inferred: 5
  assumed: 1
  unknown: 2
approved_by: null           # اسم ودور، عند الاعتماد فقط
approved_at: null
traces:
  realizes: [UC-040, UC-041, UC-045]
  satisfies: [BRQ-004, BRL-006, BRL-007]
  constrained_by: [ADR-P02, ADR-P03]
  quality: [QAS-PERF-003, QAS-SEC-011]
  verified_by: [TST-TASK-001, TST-TASK-017]
open_unknowns: [UNK-017]
---
```

## 7.3 علاقات التتبع المعتمدة

```text
OUT   ←contributes─ BRQ
BRQ   ←refines──── REQ / QAS
REQ   ←realized── UC
UC    ←realized── CMD / QRY
CMD   ─handled by→ AGG
AGG   ─enforces──→ INV
AGG   ─emits─────→ EVT
CMD   ─authorized→ POL
CMD / QRY ─exposed→ API
QAS   ─driven by─→ WL
QAS   ─measured──→ SLO
THR   ─mitigated─→ control (REQ / POL / ADR)
FM    ─recovered→ strategy (ADR / REQ)
*     ─verified──→ TST / FIT
*     ─decided──→ ADR
```

المصفوفات الثلاث في V5 (RTM، Architecture، Quality) والمصفوفة الرابعة (Data Lineage) تُولّد من هذه العلاقات. لا تُكتب يدوياً.

---

# 8. مستودع المواصفات (Specification Package)

الهيكل التالي هو شكل المخرج النهائي. كل مجلد يقابل مجموعة من مخرجات V5.

```text
spec/
├── README.md                          # فهرس + حالة كل موجة وشريحة
├── 00-governance/
│   ├── registers/
│   │   ├── risks.yaml                 # V5#96
│   │   ├── assumptions.yaml           # V5#97
│   │   ├── unknowns.yaml              # V5#98
│   │   ├── dependencies.yaml          # V5#100
│   │   ├── open-questions.yaml        # V5#101
│   │   ├── technical-debt.yaml        # V5#91
│   │   ├── corrections.yaml           # (V6) تصحيحات خط الأساس
│   │   └── human-approvals.yaml       # (V6) نقاط الاعتماد البشري
│   ├── decisions/ADR-*.md             # V5#99, #106 — صيغة MADR
│   └── glossary.yaml                  # (V6) المصطلحات عربي/إنجليزي
├── 01-business/                       # V5#01–06, #10
│   ├── system-definition.md
│   ├── stakeholders.yaml
│   ├── outcomes.yaml
│   ├── capabilities.yaml
│   ├── value-streams.yaml
│   ├── processes/BP-*.md
│   └── business-rules.yaml
├── 02-requirements/                   # V5#07–09
│   ├── requirements.yaml              # صيغة EARS
│   ├── quality-scenarios.yaml         # QAS
│   ├── use-cases/UC-*.md
│   └── requirements-quality-report.md
├── 03-domain/                         # V5#11–16
│   ├── domains.yaml
│   ├── context-map.md
│   ├── ownership.yaml                 # مالك واحد لكل BO
│   └── contexts/BCxx/
│       ├── business-objects/BO-*.yaml
│       ├── aggregates/AGG-*.md
│       ├── state-machines/SM-*.yaml
│       ├── commands.yaml
│       ├── queries.yaml
│       ├── events.yaml
│       ├── invariants.yaml
│       └── policies.yaml
├── 04-information/                    # V5#17–32
│   ├── meta-model.md
│   ├── object-envelope.schema.json
│   ├── temporal-model.md
│   ├── spatial-model.md
│   ├── provenance-lineage.md
│   ├── confidence-model.md
│   ├── claim-evidence-model.md
│   ├── conflict-model.md
│   ├── entity-resolution.md
│   ├── importance-tiers.yaml          # (V6) ADR-P03
│   ├── language-model.md              # (V6) العربية والنقحرة
│   └── reference-data.yaml            # (V6) القوائم المرجعية
├── 05-contracts/                      # V5#64–65
│   ├── openapi/<context>.yaml         # OpenAPI 3.1
│   ├── asyncapi/<context>.yaml        # AsyncAPI 3
│   ├── schemas/                       # JSON Schema للكائنات والأحداث
│   └── errors.yaml                    # نموذج الأخطاء الموحد + رموزه
├── 06-data/                           # V5#33–38, #105
│   ├── logical-model/<context>.md
│   ├── storage-architecture.md
│   ├── projections.md                 # بحث، رسم، متجهات، تحليلات
│   ├── data-quality-rules.yaml
│   └── retention-schedule.yaml
├── 07-quality/                        # V5#39–43, #57–58
│   ├── workloads.yaml
│   ├── performance-model.md
│   ├── capacity-model.md
│   ├── scalability-model.md
│   ├── cost-model.md
│   └── slos.yaml
├── 08-security/                       # V5#44–49, #82
│   ├── trust-boundaries.md
│   ├── threat-model/THR-*.yaml
│   ├── privacy-threats.yaml           # LINDDUN
│   ├── classification-scheme.yaml
│   ├── authorization-model.md
│   ├── data-protection.md
│   └── security-verification.md
├── 09-reliability/                    # V5#50–56
│   ├── fmea.yaml
│   ├── degradation-matrix.yaml
│   ├── recovery-dr.md
│   ├── business-continuity.md
│   └── observability.md
├── 10-ai/                             # V5#59–63
│   ├── ai-architecture.md
│   ├── autonomy-matrix.yaml           # AIL لكل عملية
│   ├── ai-evaluation.md
│   ├── ai-threats.yaml
│   └── agent-governance.md
├── 11-integration/                    # V5#66–68
│   ├── external-systems.yaml
│   ├── interoperability-standards.md
│   └── offline-sync.md
├── 12-solution/                       # V5#35 + Solution Architecture
│   ├── c4-context.md
│   ├── c4-containers.md
│   ├── deployment-units.md
│   └── technology-decisions/TD-*.md
├── 13-verification/                   # V5#92–95
│   ├── verification-strategy.md
│   ├── acceptance/<context>/*.feature
│   ├── invariant-properties.yaml
│   ├── fitness-functions.yaml
│   └── spec-lint-rules.yaml           # (V6) القسم 16
├── 14-slices/SLC-*/readiness.md       # (V6) جاهزية كل شريحة
├── 15-traceability/                   # V5#102–105 — مولّدة
└── 16-reports/                        # V5#107–113
    ├── consistency-report.md
    ├── anti-pattern-report.md
    ├── architecture-review.md
    ├── gate-reports/G*.md
    ├── engineering-baseline.md
    └── evolution-roadmap.md
```

---

# 9. تنظيم الدراسة: الأدوار والمسارات

## 9.1 المبدأ

V5 يعرّف 48 وكيلاً. هذا صحيح كتخصصات، لكن تشغيل 48 وكيلاً مستقلاً ينتج تنسيقاً مكلفاً وتناقضات. في V6 تُجمَّع التخصصات في **مسارات عمل (Workstreams)**، وكل مسار يستخدم تخصصات V5 كأدوار داخله.

## 9.2 المسارات

```text
MASTER ORCHESTRATOR
│
├── Business & Requirements Stream        A01–A05
│
├── Context Streams (مسار لكل Bounded Context)
│   ├── BC01 Foundation                   A06 + A29 (جزئي)
│   ├── BC02 Information                  A07–A13
│   ├── BC03 Intelligence & Analysis      A14–A16
│   ├── BC04 Operations                   A15, A17, A18
│   ├── BC05 Resources & Readiness        A19–A21
│   ├── BC06 Knowledge & Products         A22–A24
│   ├── BC07 Platform Intelligence        A25, A26, A28
│   └── BC08 Governance & Runtime         A31, A34
│
├── Cross-Cutting Quality Streams
│   ├── Data & Integration                A25–A27, A45, A46
│   ├── Security & Privacy                A29, A30
│   ├── Performance, Capacity & Cost      A37–A40, A42
│   ├── Reliability & Operations          A33, A34, A41, A48
│   ├── AI Governance                     A28 + AI Security
│   └── Experience                        A43, A44
│
└── Architecture Board (مستقل)
    ├── Solution Architecture             A35
    ├── Architecture Review               A36
    ├── Fitness & Drift                   A47
    └── Verification                      A32
```

## 9.3 قواعد التفاعل

- **مسار السياق يملك** مخرجات سياقه (BO، AGG، SM، CMD، EVT، العقود).
- **مسار الجودة يراجع ويضيف** قيوده على مخرجات كل سياق (سيناريوهات جودة، تهديدات، أنماط فشل)، ولا يعدّل نموذج السياق مباشرة. يرفع تعارضاً.
- **مجلس المعمارية مستقل** ولا يؤلف المخرجات التي يراجعها.
- **الموافقة النهائية على القرارات الحرجة بشرية** (القسم 21.4).

## 9.4 عقد الوكيل (من V5، محتفظ به)

كل دور يملك عقداً بالحقول: `id`، `mission`، `scope`، `inputs`، `outputs`، `artifacts_owned`، `allowed_actions`، `forbidden_actions`، `dependencies`، `validation_rules`، `escalation_rules`، `stop_conditions`، `evidence_requirements`، `review_requirements`.

## 9.5 مستويات صلاحية الوكلاء (DAL)

لتجنب الالتباس مع استقلالية الذكاء الاصطناعي داخل المنتج (AIL)، تُسمى مستويات V5 للوكلاء **DAL**:

```text
DAL0 Advisory
DAL1 Analytical
DAL2 Specification
DAL3 Coordination
DAL4 Controlled Decision Proposal     ← الحد الأقصى في مرحلة الدراسة
DAL5 Autonomous Execution            ← ممنوع
```

---

# 10. دورة الدراسة: الموجات

## 10.1 الشكل العام

```text
W0 Setup
 ↓
W1 Discovery & Framing ─────────────── G0, G1
 ↓
W2 Requirements & Quality Scenarios ── G2
 ↓
W3 Information Kernel ──────────────── G3 (النواة)
 ↓
┌──────── تتكرر لكل شريحة ────────┐
│ W4 Slice Domain Design           │
│ W5 Slice Cross-Cutting Quality   │
│ W6 Slice Contracts & Acceptance  │
│ W7 Slice Review & Readiness ─── G6-SLC
└──────────────────────────────────┘
 ↓
W8 Solution & Technology Decisions ── G4, G5
   (تبدأ بعد W5 للشرائح الأساسية، وتتحدث مع كل شريحة)
 ↓
W9 Baseline Consolidation ─────────── G6 (للإصدار)
```

**لماذا هذا الترتيب؟**

- W1 وW2 لا يمكن إنجازهما بالتحليل وحده. يحتاجان إجابات بشرية (بنك الأسئلة، القسم 17).
- W3 هي المسار الحرج. كل السياقات تعتمد على النموذج الزمني ونموذج الادعاءات والملكية وحزمة الكائن. أي خطأ هنا ينتشر في كل شيء.
- W8 (اختيار التقنيات) تأتي **بعد** وجود أعباء عمل وسيناريوهات جودة لشرائح كافية، تطبيقاً للمسلّمة A13.

## 10.2 تفصيل الموجات

### W0 — Setup

- **الهدف:** تجهيز إطار العمل قبل أي تحليل.
- **الأنشطة:** إنشاء هيكل المواصفات (القسم 8)، والقوالب (القسم 12)، والسجلات فارغة، وقاموس المصطلحات الأولي. تحميل التصحيحات (القسم 14) والقرارات المقترحة (القسم 15) والمجهولات (القسم 17) إلى السجلات.
- **الخروج:** الهيكل قائم، والسجلات مهيأة بما في هذا الملف.

### W1 — Discovery & Framing

- **الهدف:** معرفة ما الذي نبنيه، ولمن، ولماذا، وما حدوده.
- **المدخلات:** مستند المشروع، ثم إجابات بنك الأسئلة (القسم 17).
- **التقنيات:** System Context، Scope Statement، Stakeholder Map، RACI، Capability Mapping، Event Storming (Big Picture).
- **المخرجات:** System Definition، Stakeholder Model، Outcomes (بمؤشرات قابلة للقياس)، Capability Map، Value Streams محدثة، نطاق الإصدار الأول (Release Scope)، قائمة الشرائح المعتمدة.
- **الخروج:** G0 وG1. المجهولات UNK-001 حتى UNK-008 مغلقة أو مقبولة صراحة. نطاق الإصدار الأول معتمد (HAP-02).

### W2 — Requirements & Quality Scenarios

- **الهدف:** Baseline متطلبات قابلة للتحقق.
- **التقنيات:** EARS، فحص ISO 29148، Quality Attribute Scenarios، Utility Tree.
- **المخرجات:** Requirements Baseline لنطاق الإصدار الأول، Requirements Quality Report، Business Rules Catalog مصحح، Use Case Catalog مكتمل للنطاق، Quality Scenarios بأولوية (H/M/L للأهمية × H/M/L للصعوبة)، Workload Catalog (هيكل + ما عُرف من أرقام).
- **الخروج:** G2. كل متطلب في النطاق يحقق ISO 29148، وكل QAS عالي الأولوية له مقياس أو TBD بمالك وموعد.

### W3 — Information Kernel

- **الهدف:** تثبيت النموذج المعلوماتي المشترك الذي تبنى عليه كل السياقات.
- **يشمل إلزامياً:**
  - ADR-P01 (النموذج الزمني)، ADR-P02 (أسلوب الحفظ)، ADR-P03 (مستويات الأهمية)، ADR-P13 (المعرفات).
  - Meta-Model، وحزمة الكائن (Object Envelope) مصححة (CR-03، CR-04، CR-27).
  - نماذج Claim وEvidence وSource وObservation وRelationship.
  - نموذج الثقة متعدد الأبعاد، ونموذج التعارض، ونموذج مطابقة الكيانات بما فيه Split/Unmerge.
  - نموذج الملكية الكامل لكل Business Object (CR-01، CR-02).
  - النموذج اللغوي (ADR-P15) والبيانات المرجعية (ADR-P14).
  - نموذج التصنيف الأمني والصلاحيات الأساسي (يعتمد على UNK-006).
- **الخروج:** G3 للنواة. لا تبدأ أي شريحة في W4 قبل اعتماد ADR-P01 وP02 وP03 (HAP-04).

### W4 — Slice Domain Design (لكل شريحة)

- **التقنيات:** Event Storming (Process ثم Design Level)، Aggregate Design Canvas، جداول الانتقال.
- **المخرجات:** Business Objects بقالب V5§50، Aggregates، State Machines كاملة، Commands، Queries، Events، Invariants، Policies.

### W5 — Slice Cross-Cutting Quality (لكل شريحة)

- **المخرجات:** Threat Model (STRIDE) لمسارات الشريحة، FMEA، Degradation Matrix، Workloads المحددة، سيناريوهات الجودة، متطلبات المراقبة، وأثر التكلفة.

### W6 — Slice Contracts & Acceptance (لكل شريحة)

- **المخرجات:** OpenAPI، AsyncAPI، JSON Schemas، النموذج المنطقي للبيانات، سياسات الصلاحية بصيغة جداول قرار، سيناريوهات Gherkin، مواصفات Property-Based للثوابت.

### W7 — Slice Review & Readiness (لكل شريحة)

- **الأنشطة:** تشغيل قواعد فحص المواصفة (القسم 16)، مراجعة مستقلة، ATAM-lite مصغر للشريحة، تحديث السجلات.
- **الخروج:** **G6-SLC** وفق القسم 20.2.

### W8 — Solution & Technology Decisions

- **الأنشطة:** C4 Context وContainers، حدود النشر (Deployment Units) وفق معايير V5§97، قرارات التقنية بصيغة V5§119 مبنية على أعباء عمل الشرائح المدروسة، نموذج التكلفة الإجمالي.
- **الخروج:** G4 وG5. ADR-P05 معتمد (HAP-08).

### W9 — Baseline Consolidation

- **الأنشطة:** تقرير الاتساق الكامل، تقرير الأنماط المضادة، مراجعة ATAM-lite كاملة للإصدار، توليد مصفوفات التتبع، Engineering Baseline، Evolution Roadmap.
- **الخروج:** G6 للإصدار الأول.

---

# 11. تقسيم النطاق: الإصدار والشرائح

## 11.1 الشريحة المفاهيمية الشاملة (SLC-00)

الشريحة في V5§117 (من Organization إلى Archive) تبقى كما هي، لكن كأداة تحقق مفاهيمية فقط. تُستخدم في نهاية W3 وفي W9 لـ"تمرير" سيناريو واحد عبر النموذج كله على الورق، والتأكد من أن كل انتقال بين سياقين له عقد (أمر أو حدث أو استعلام) ومالك.

**مثال السيناريو:** ملاحظة ميدانية تُسجَّل، ثم تُطابق مع كيان، ثم تدخل في تحليل، ثم تغير تقييماً، ثم تُحدّث موقفاً، ثم يُتخذ قرار، ثم تُعدل خطة، ثم تُنشأ مهمة، ثم يُخصص مورد، ثم تُنفذ، ثم تُقاس النتيجة، ثم يُستخلص درس، ثم تُؤرشف السجلات.

كل خطوة يجب أن تجيب: من المالك؟ ما الأمر؟ ما الحدث؟ ما الصلاحية؟ ما الزمن المسجل؟ ما مصدر الدليل؟

## 11.2 شرائح التنفيذ (PROPOSED)

الترتيب مبني على التبعيات: كل شريحة تعتمد على ما قبلها.

| الشريحة | المحتوى | يعتمد على | يثبت |
|---|---|---|---|
| SLC-01 | Tenancy، Identity، Organization، Authorization، Audit | W3 | نموذج الصلاحيات والعزل والتدقيق يعمل من طرف لطرف |
| SLC-02 | Source → Observation → Entity / Claim → Evidence، مع الزمن والمكان | SLC-01 | النواة المعلوماتية: الثنائية الزمنية، الـ Provenance، الثقة |
| SLC-03 | Task بدورة حياته الكاملة + Outbox + History | SLC-01 | نمط الـ Aggregate والأحداث والتزامن |
| SLC-04 | Conflict Management + Entity Resolution (Merge/Split) | SLC-02 | عدم الكتابة الصامتة، الدمج دون حذف |
| SLC-05 | Search Projection مؤمّنة + Graph Projection | SLC-02 | Authorization Before Retrieval ومنع الاستدلال |
| SLC-06 | Situation + Alerts | SLC-02، SLC-05 | الموقف كسياق، ومسار التنبيه |
| SLC-07 | Analysis Case → Run → Finding → Assessment | SLC-02 | قابلية إعادة الإنتاج والـ Lineage |
| SLC-08 | Decision → Plan → Version → Baseline → Tasks | SLC-03، SLC-07 | سلسلة القرار إلى التنفيذ |
| SLC-09 | Assets، Resources، Allocation، Eligibility | SLC-03، SLC-01 | التحقق من الأهلية والسعة |
| SLC-10 | AI Assisted Retrieval مؤرَّض (Grounded) | SLC-05 | AI يرث الصلاحيات، ولا اختلاق |
| SLC-11 | Offline Field Capture + Sync | SLC-02، SLC-04 | المزامنة والتعارض الميداني |
| SLC-12 | Products، Knowledge، Archive، Historical Reconstruction | SLC-07، SLC-08 | الذاكرة المؤسسية |
| SLC-13+ | Risk & Emergency، Training، Exercises، Logistics، Communications | حسب النطاق | — |

**نطاق الإصدار الأول:** قرار بشري (HAP-02). الاقتراح المبدئي هو SLC-01 إلى SLC-08، لأنها تغطي VS01 وVS02 وVS03، أي جوهر المنصة. لكن هذا يعتمد على UNK-001: إن كانت مهمة المؤسسة الأساسية الطوارئ مثلاً، فقد تتقدم SLC-13 على SLC-07.

## 11.3 قاعدة الشريحة الرفيعة

الشريحة **تنفيذياً** يجب أن تكون قابلة للبناء والاختبار خلال دورة تطوير واحدة محدودة. إذا تجاوزت ذلك، تُقسم. الشريحة المفاهيمية (SLC-00) مستثناة لأنها لا تُنفذ.

---

# 12. كتالوج المخرجات بالمستويات

## 12.1 المستويات

| المستوى | متى يجب أن يكتمل | المعنى |
|---|---|---|
| **T0 — Kernel** | قبل أي كود على الإطلاق | قرارات وأسس لو تغيرت بعد البناء لزم إعادة بناء واسعة |
| **T1 — Slice** | قبل كود الشريحة المعنية | مواصفة الشريحة القابلة للبرمجة |
| **T2 — Pre-Production** | قبل الإنتاج، ويبدأ مبكراً | ما يلزم للتشغيل الآمن، ولا يمنع البناء |
| **T3 — Continuous** | يُحدَّث باستمرار | سجلات وتقارير حية |

## 12.2 التوزيع (بترقيم V5§106)

| # | المخرج | المستوى | الموجة | الصيغة |
|---|---|---|---|---|
| 01 | System Definition | T0 | W1 | md |
| 02 | Business Architecture | T0 | W1 | md |
| 03 | Stakeholder Model | T0 | W1 | yaml |
| 04 | Capability Map | T0 | W1 | yaml |
| 05 | Value Streams | T0 | W1 | yaml |
| 06 | Business Processes | T1 | W1/W4 | md |
| 07 | Requirements Baseline | T0 للنطاق، T1 للتفاصيل | W2 | yaml (EARS) |
| 08 | Requirements Quality Report | T0 | W2 | md |
| 09 | Use Case Catalog | T1 | W2/W4 | md |
| 10 | Business Rules Catalog | T0 | W2 | yaml |
| 11 | Domain Model | T0 | W3 | md |
| 12 | Bounded Context Map | T0 | W3 | md + Mermaid |
| 13 | Business Object Catalog | T0 للنواة، T1 لبقية الكائنات | W3/W4 | yaml |
| 14 | Aggregate Catalog | T1 | W4 | md |
| 15 | State Machine Catalog | T1 | W4 | yaml |
| 16 | Domain Ownership Model | T0 | W3 | yaml |
| 17–24 | Information، Entity، Event، Relationship، Claim، Evidence، Source، Observation Models | T0 | W3 | md + JSON Schema |
| 25 | Temporal Architecture | T0 | W3 | md |
| 26 | Spatial Architecture | T0 | W3 | md |
| 27 | Temporal-Spatial Query Model | T1 | W4 (SLC-02) | md |
| 28–32 | Provenance، Lineage، Confidence، Conflict، Entity Resolution | T0 | W3 | md |
| 33 | Data Architecture | T0 (المبادئ) | W3 | md |
| 34 | Storage Architecture | T1 | W8 | md |
| 35–36 | Search، Graph Architecture | T1 | W4–W6 (SLC-05) | md |
| 37 | Analytics Architecture | T2 | W8 | md |
| 38 | Data Quality Architecture | T1 | W5 | yaml |
| 39 | Workload Catalog | T0 (الهيكل)، T1 (الأرقام) | W2/W5 | yaml |
| 40–42 | Performance، Capacity، Scalability Models | T1 | W5/W8 | md |
| 43 | Performance Test Strategy | T2 | W8 | md |
| 44 | Security Architecture | T0 | W3 | md |
| 45 | Threat Model | T0 للحدود العامة، T1 لكل شريحة | W3/W5 | yaml |
| 46 | Trust Boundary Model | T0 | W3 | md + Mermaid |
| 47 | Authorization Model | T0 | W3 | md + جداول قرار |
| 48 | Data Protection Model | T0 | W3 | md |
| 49 | Security Verification Strategy | T1 | W6 | md |
| 50–52 | Reliability، Resilience، FMEA | T1 | W5 | yaml |
| 53 | Disaster Recovery | T2 | W8 | md |
| 54 | Business Continuity | T2 | W8 | md |
| 55 | Observability Architecture | T1 | W5 | md |
| 56 | Operational Readiness | T2 | W9 | md |
| 57 | Cost Model | T0 (المحركات)، T2 (التفصيل) | W2/W8 | md |
| 58 | Cost/Performance Trade-offs | T1 | W8 | md |
| 59–60 | AI Architecture، AI Governance | T0 إن كان AI في الإصدار الأول | W3 | md |
| 61–62 | AI Security، AI Evaluation | T1 | W5 (SLC-10) | yaml |
| 63 | Agent Governance | T0 إن وُجد وكلاء في المنتج | W3 | md |
| 64–65 | API، Event Architecture | T0 (المعايير)، T1 (العقود) | W3/W6 | md + OpenAPI / AsyncAPI |
| 66 | Integration Architecture | T1 | W6 | yaml |
| 67 | Interoperability Architecture | T1 | W6 | md |
| 68 | Offline & Synchronization | T0 إن كان العمل الميداني في الإصدار الأول | W3 | md |
| 69–76 | Workflow، Planning، Task، Asset، Resource، Logistics، Risk، Readiness | T1 | W4 (حسب الشريحة) | md + yaml |
| 77–81 | Knowledge، Product، Reporting، Archive، Institutional Memory | T1 | W4 (SLC-12) | md |
| 82 | Privacy & Compliance | T0 | W1/W3 | md |
| 83–84 | Governance، Policy Architecture | T0 | W3 | md |
| 85 | Configuration Architecture | T1 | W8 | md |
| 86 | Audit Architecture | T0 | W3 | md |
| 87 | Migration Strategy | T2 | W8 | md |
| 88 | Evolution Strategy | T3 | W9 | md |
| 89 | Architecture Fitness Model | T0 | W3 | yaml |
| 90 | Architecture Drift Model | T3 | W9 | md |
| 91 | Technical Debt Strategy | T3 | W0 | yaml |
| 92–95 | Verification، Validation، Quality Model، Fitness Criteria | T0 (الاستراتيجية) | W2/W3 | md |
| 96–101 | السجلات | T3 | W0 ثم مستمر | yaml |
| 102–105 | مصفوفات التتبع | T3 (مولّدة) | كل موجة | مولّدة |
| 106 | ADR Catalog | T3 | كل موجة | md (MADR) |
| 107–109 | تقارير الاتساق والأنماط المضادة والمراجعة | T3 | W7/W9 | md |
| 110–111 | Implementation Readiness، Gate Reports | T3 | كل بوابة | md |
| 112 | Engineering Baseline | T3 | W9 | md |
| 113 | Evolution Roadmap | T3 | W9 | md |
| **V6-1** | Human Approval Register | T3 | W0 | yaml |
| **V6-2** | Baseline Corrections Register | T3 | W0 | yaml |
| **V6-3** | Glossary (عربي/إنجليزي) | T0 | W0/W3 | yaml |
| **V6-4** | Importance Tier Model | T0 | W3 | yaml |
| **V6-5** | Language & Transliteration Model | T0 | W3 | md |
| **V6-6** | Reference Data Catalog | T0 | W3 | yaml |
| **V6-7** | AI Autonomy Matrix | T0 إن كان AI في النطاق | W3 | yaml |
| **V6-8** | Slice Readiness Records | T1 | W7 | md |
| **V6-9** | Spec Lint Rules | T0 | W0 | yaml |

---

# 13. القوالب القابلة للبرمجة

القوالب التالية هي الحد الأدنى. أي حقل غير معروف يُكتب `TBD` مع مرجع `UNK-xxx`، ولا يُترك فارغاً ولا يُخترع.

## 13.1 متطلب (EARS)

صيغ EARS الخمس:

```text
Ubiquitous:     The <system> shall <response>.
Event-driven:   When <trigger>, the <system> shall <response>.
State-driven:   While <state>, the <system> shall <response>.
Unwanted:       If <condition>, then the <system> shall <response>.
Optional:       Where <feature is included>, the <system> shall <response>.
```

```yaml
- id: REQ-OPS-021
  type: functional
  pattern: event-driven
  statement: >
    When an assignee submits a task result, the system shall move the task
    to SUBMITTED and record the submission time and the result reference.
  rationale: BRL-006 يشترط مراجعة النتيجة قبل الإكمال
  source: [DOC:PRJ§55]
  stakeholders: [Operator, Manager]
  priority: must
  acceptance_criteria: [TST-TASK-009]
  verification_method: test
  traces: { satisfies: [BRQ-004], realized_by: [UC-043] }
  status: PROPOSED
```

## 13.2 سيناريو جودة (QAS)

```yaml
- id: QAS-SEC-004
  quality: security / confidentiality
  source: مستخدم مصادق عليه بلا صلاحية على تصنيف "X"
  stimulus: يبحث بكلمة تطابق وثيقة مصنفة "X"
  environment: تشغيل عادي
  artifact: Search Projection
  response: لا تظهر الوثيقة، ولا يتغير عدد النتائج أو الـ Facets بسببها
  response_measure: 0 تسرب في مجموعة اختبار الاستدلال المعتمدة
  workload: WL-02
  priority: { importance: H, difficulty: H }
  verified_by: [TST-SRCH-INF-001]
  status: PROPOSED
```

## 13.3 عبء عمل (Workload)

```yaml
- id: WL-06
  name: Event Streaming / Sensor Ingestion
  users: TBD            # UNK-005
  request_rate: TBD
  event_rate: { normal: TBD, peak: TBD, burst: TBD }   # UNK-005
  data_volume: TBD
  data_growth: TBD
  latency_requirement: TBD   # UNK-015
  consistency_requirement: eventual (INF)
  availability_requirement: TBD   # UNK-008
  security_requirement: classification-aware
  retention: TBD   # UNK-002
  decisions_blocked: [ADR-P05]
  closing_owner: Platform Stream + Sponsor
```

## 13.4 كائن عمل (Business Object — قالب V5§50 موسع)

```yaml
id: BO-OBSERVATION
name: Observation
domain: DOM-06
bounded_context: BC02
owner: BC02                      # مالك واحد فقط
purpose: تسجيل ما رصده مصدر في زمن ومكان محددين
importance_tier: T1              # ADR-P03
identity: { internal: ULID, global: "urn:<ns>:observation:<id>" }   # ADR-P13
attributes:
  - { name: observed_at, type: timestamp, temporal_role: observation_time, required: true }
  - { name: event_time, type: interval, temporal_role: event_time, required: false }
  - { name: geometry, type: geometry, crs_required: true, accuracy_required: true }
  - { name: source_ref, type: ref(BO-SOURCE), required: true }
relationships: [ { type: supports, target: BO-CLAIM, cardinality: "0..*" } ]
events: [EVT-OBS-RECORDED, EVT-OBS-VALIDATED, EVT-OBS-REJECTED]
state_machine: SM-OBSERVATION
temporal: bitemporal             # ADR-P01
spatial: required
evidence: can_be_evidence
provenance: required
confidence: [source_reliability, information_confidence, data_quality, verification_status, freshness, completeness, uncertainty]
security: { classification: required, compartments: TBD }   # UNK-006
versioning: immutable_after_validation (PRO)
audit: all_commands
api: API-INF-OBS-*
storage: TBD                     # ADR-P05
```

## 13.5 جدول انتقال الحالات — مثال مكتمل: Task

هذا مثال عملي يطبق القالب على Task، وهو الكائن الوحيد المصمم بعمق في مستند المشروع. يصحح CR-06.

**الحالة المعرفية:** الحالات من [DOC:PRJ§55]. الانتقالات والشروط وبعض الأحداث **[INF] / [PRO]**، لأن المستند لا يحددها. الأحداث المعلّمة (جديد) غير موجودة في المستند.

```yaml
id: SM-TASK
aggregate: AGG-TASK
states:
  non_terminal: [DRAFT, READY, ASSIGNED, ACCEPTED, IN_PROGRESS, BLOCKED,
                 SUBMITTED, UNDER_REVIEW, APPROVED, COMPLETED, SUSPENDED]
  terminal: [CLOSED, CANCELLED, REJECTED, EXPIRED, SUPERSEDED]
# ملاحظة: RESUMED وREWORK في المستند انتقالات وليست حالات (CR-06)

transitions:
  - { from: DRAFT,        cmd: CMD-TASK-MARK-READY,   to: READY,
      guard: "title, plan_ref, completion_criteria defined",      event: EVT-TASK-READIED }       # جديد
  - { from: READY,        cmd: CMD-TASK-ASSIGN,       to: ASSIGNED,
      guard: "assignee eligible (BRL-007) AND actor authorized", event: EVT-TASK-ASSIGNED }
  - { from: ASSIGNED,     cmd: CMD-TASK-ACCEPT,       to: ACCEPTED,
      guard: "actor = assignee",                                  event: EVT-TASK-ACCEPTED }
  - { from: ASSIGNED,     cmd: CMD-TASK-DECLINE,      to: READY,
      guard: "actor = assignee AND reason provided",              event: EVT-TASK-DECLINED }      # جديد
  - { from: ACCEPTED,     cmd: CMD-TASK-START,        to: IN_PROGRESS,
      guard: "actor = assignee AND dependencies satisfied",      event: EVT-TASK-STARTED }
  - { from: IN_PROGRESS,  cmd: CMD-TASK-BLOCK,        to: BLOCKED,
      guard: "blocking reason provided",                          event: EVT-TASK-BLOCKED }
  - { from: BLOCKED,      cmd: CMD-TASK-RESUME,       to: IN_PROGRESS,
      guard: "blocking reason resolved",                          event: EVT-TASK-RESUMED }
  - { from: IN_PROGRESS,  cmd: CMD-TASK-SUBMIT,       to: SUBMITTED,
      guard: "result attached",                                   event: EVT-TASK-SUBMITTED }
  - { from: SUBMITTED,    cmd: CMD-TASK-START-REVIEW, to: UNDER_REVIEW,
      guard: "actor has review authority",                        event: EVT-TASK-REVIEW-STARTED } # جديد
  - { from: UNDER_REVIEW, cmd: CMD-TASK-RETURN,       to: IN_PROGRESS,
      guard: "rework reason provided",                            event: EVT-TASK-RETURNED-FOR-REWORK }
  - { from: UNDER_REVIEW, cmd: CMD-TASK-APPROVE,      to: APPROVED,
      guard: "actor has approval authority AND actor != assignee (OQ-030)", event: EVT-TASK-APPROVED }
  - { from: UNDER_REVIEW, cmd: CMD-TASK-REJECT,       to: REJECTED,
      guard: "rejection reason provided",                         event: EVT-TASK-REJECTED }      # جديد
  - { from: APPROVED,     cmd: CMD-TASK-COMPLETE,     to: COMPLETED,
      guard: "all completion_criteria met (BRL-006)",             event: EVT-TASK-COMPLETED }
  - { from: COMPLETED,    cmd: CMD-TASK-CLOSE,        to: CLOSED,
      guard: "no open follow-ups (OQ-031)",                       event: EVT-TASK-CLOSED }
  - { from: "any non_terminal except SUSPENDED", cmd: CMD-TASK-SUSPEND, to: SUSPENDED,
      guard: "actor has suspend authority; prior_state recorded", event: EVT-TASK-SUSPENDED }     # جديد
  - { from: SUSPENDED,    cmd: CMD-TASK-UNSUSPEND,    to: "prior_state",
      guard: "actor has suspend authority",                       event: EVT-TASK-UNSUSPENDED }   # جديد
  - { from: "any non_terminal", cmd: CMD-TASK-CANCEL, to: CANCELLED,
      guard: "actor has cancel authority AND reason provided",    event: EVT-TASK-CANCELLED }     # جديد
  - { from: "any non_terminal", trigger: "system: due_at passed (policy)", to: EXPIRED,
      guard: "expiry policy enabled for task type (OQ-032)",       event: EVT-TASK-EXPIRED }       # جديد
  - { from: "any non_terminal", trigger: "EVT-PLAN-VERSION-BASELINED removes task", to: SUPERSEDED,
      guard: "new plan version does not include task",            event: EVT-TASK-SUPERSEDED }    # جديد

non_transition_events:
  - { cmd: CMD-TASK-ESCALATE, allowed_in: "any non_terminal", event: EVT-TASK-ESCALATED,
      note: "التصعيد لا يغير الحالة" }

invalid_transition_error: TASK_INVALID_STATE_TRANSITION   # في errors.yaml

invariants:
  - INV-TASK-01: "لا انتقال من COMPLETED أو أي حالة نهائية إلى IN_PROGRESS"      # [DOC:PRJ§94]
  - INV-TASK-02: "لا يصل Task إلى COMPLETED دون استيفاء كل completion_criteria"  # [DOC:BRL-006]
  - INV-TASK-03: "كل انتقال ينتج حدثاً واحداً بالضبط وسجل تدقيق"                  # [DOC:PRJ§94]
  - INV-TASK-04: "الحالات النهائية لا تقبل أي أمر يغير الحالة"                     # [PRO]
  - INV-TASK-05: "assignee في ASSIGNED وما بعدها مؤهل وقت الإسناد"               # [DOC:BRL-007]

concurrency: optimistic, aggregate version, conflict → HTTP 409 + TASK_VERSION_CONFLICT
idempotency: every command carries idempotency_key; duplicate returns original result

open_questions:
  - OQ-030: هل يُمنع أن يعتمد المنفذ مهمته بنفسه (فصل المهام)؟
  - OQ-031: ما الفرق التشغيلي بين APPROVED وCOMPLETED وCLOSED؟ هل يمكن دمج بعضها؟
  - OQ-032: هل انتهاء المهلة يُنهي المهمة آلياً أم يصعّدها فقط؟
  - OQ-033: هل REJECTED نهائية، أم تسمح بإعادة الفتح كمهمة جديدة مرتبطة؟
```

هذا الجدول يجعل الاختبارات مشتقة آلياً: لكل انتقال اختبار نجاح، ولكل حالة × أمر غير مدرج اختبار رفض برمز `TASK_INVALID_STATE_TRANSITION`.

## 13.6 أمر (Command)

```yaml
- id: CMD-TASK-COMPLETE
  aggregate: AGG-TASK
  intent: إكمال مهمة معتمدة بعد التحقق من معايير الإكمال
  actor_roles: [Manager, Planner]              # [INF] — يتطلب اعتماد
  authorization: POL-AUTHZ-TASK-COMPLETE
  payload_schema: schemas/commands/task-complete.v1.json
  preconditions: [ "state = APPROVED", INV-TASK-02 ]
  idempotency: required
  concurrency: expected_version required
  emits: [EVT-TASK-COMPLETED]
  errors: [TASK_INVALID_STATE_TRANSITION, TASK_CRITERIA_NOT_MET, TASK_VERSION_CONFLICT, AUTHZ_DENIED]
  audit: required
  api: API-OPS-TASK-COMPLETE        # POST /api/v1/operations/tasks/{id}/actions/complete
```

## 13.7 حدث (Event)

```yaml
- id: EVT-TASK-COMPLETED
  name: TaskCompleted
  version: 1
  category: domain
  producer: BC04
  aggregate: AGG-TASK
  schema: schemas/events/task-completed.v1.json
  envelope: EventEnvelope.v1
  partition_key: aggregate.id           # يضمن الترتيب لكل مهمة
  delivery: at-least-once via outbox; consumers idempotent via inbox
  consumers: [BC05 (release allocations), BC06 (lessons candidate), Search Projection]
  integration_event: EVT-INT-TASK-COMPLETED   # نسخة عامة منفصلة للتكامل الخارجي
  contains_classified_data: TBD          # UNK-006
  retention: TBD                         # UNK-002
```

## 13.8 سياسة صلاحية (جدول قرار)

```yaml
- id: POL-AUTHZ-TASK-COMPLETE
  subject: { role_in: [Manager, Planner], org_scope: task.org_unit_or_ancestor }
  action: complete
  resource: Task
  context_conditions:
    - classification(subject) >= classification(task)
    - purpose in [operations]
  decision: ALLOW
  otherwise: DENY
  obligations: [audit]
  status: PROPOSED
```

## 13.9 نمط فشل (FMEA)

```yaml
- id: FM-OUTBOX-001
  component: Outbox Publisher
  failure: الحالة حُفظت والحدث لم يُنشر
  cause: توقف الناشر أو عدم توفر ناقل الأحداث
  effect: الإسقاطات والمستهلكون متأخرون
  detection: عمر أقدم رسالة غير منشورة في Outbox > حد (TBD)
  severity: M
  likelihood: M
  prevention: ناشر متعدد النسخ بقفل
  mitigation: إعادة النشر من Outbox
  recovery: تلقائي عند العودة، مع ضمان عدم التكرار عبر Inbox
  data_loss: none
  user_impact: البحث والمواقف لا تعكس آخر تغيير مؤقتاً
  verified_by: [TST-OUTBOX-001]
```

## 13.10 تهديد (STRIDE)

```yaml
- id: THR-SRCH-004
  boundary: Application ↔ Search Projection
  stride: Information Disclosure
  asset: وجود وثائق مصنفة
  vector: الاستدلال من عدد النتائج أو الـ Facets
  likelihood: M
  impact: H
  controls: [ADR-P06, QAS-SEC-004]
  residual_risk: TBD
  status: PROPOSED
```

## 13.11 سيناريو قبول (Gherkin)

```gherkin
Feature: Task completion

  Scenario: Completing an approved task with all criteria met
    Given a task in state APPROVED with all completion criteria satisfied
    And the actor is a Manager of the task's organization unit
    When the actor completes the task with the current version
    Then the task state is COMPLETED
    And exactly one TaskCompleted event is recorded in the outbox
    And an audit record exists with the actor, time and correlation id

  Scenario: Completing a task that is still in progress
    Given a task in state IN_PROGRESS
    When a Manager completes the task
    Then the command is rejected with TASK_INVALID_STATE_TRANSITION
    And no event is recorded
```

## 13.12 قرار معماري (MADR)

```markdown
# ADR-P01: Temporal Model
- Status: PROPOSED
- Deciders: HAP-04
- Context / Problem: …
- Decision Drivers: …
- Considered Options: …
- Decision Outcome: …
- Consequences (positive / negative): …
- Impact: security / performance / cost / migration / operations
- Rejected Alternatives and why: …
- Blocked by: UNK-007
- Verified by: FIT-…, TST-…
```

---

# 14. تصحيحات خط الأساس (من الدراستين السابقتين)

هذه نتائج مراجعة مستند المشروع. كلها **PROPOSED**، وتُحمّل إلى `corrections.yaml` في W0. كل تصحيح يُغلق في الموجة المذكورة.

| ID | المشكلة في مستند المشروع | التصحيح | الموجة |
|---|---|---|---|
| CR-01 | Geometry له مالكان (PRJ§9) رغم قاعدة المالك الواحد | المالك BC02 Information وحده | W3 |
| CR-02 | لا مالك لـ Risk، Incident، Competency، Exercise، Product، Communication، Alert، Source، Evidence، Claim، Conflict، Relationship، Event | إكمال `ownership.yaml` لكل Business Object | W3 |
| CR-03 | Envelope يحمل `score` واحداً رغم مبدأ الثقة متعددة الأبعاد (PRJ§3.8 مقابل §11) | بنية ثقة بسبعة أبعاد (مع Uncertainty من V5§55)، دون رقم مجمع إلزامي | W3 |
| CR-04 | Envelope ينقصه Event Time وEffective Time، وRecord Time لحظة لا فترة | نموذج زمني وفق ADR-P01 | W3 |
| CR-05 | Situation موصوفة كـ View ومعاملة كـ Aggregate | حسم بـ ADR-P07 | W3 |
| CR-06 | حالات Task تخلط الحالات بالانتقالات، وأحداث ناقصة، ولا جدول انتقال | جدول القسم 13.5 كنقطة بداية | W4 (SLC-03) |
| CR-07 | البادئة BR لنوعين | BRL للقواعد، BRQ للمتطلبات | W0 |
| CR-08 | PRJ§47 يخلط الطبقات التقنية بسلسلة القيمة | فصلهما: C4 للتقني، Value Stream للعمل | W8 |
| CR-09 | لا Use Cases لـ VS04، VS05، Logistics، Communications، Exercises، Products، Collection، Policy Admin | إكمال الكتالوج للنطاق المعتمد | W2 |
| CR-10 | كلمة "مهم" غير معرفة (BR01، BR09، BR15، Provenance) | ADR-P03 مستويات الأهمية | W3 |
| CR-11 | Retrieval Service بلا مخزن متجهات في بنية التخزين | إضافة Vector Projection خاضعة للصلاحيات (ADR-P06) | W3/SLC-10 |
| CR-12 | الجانب الجغرافي بلا خدمة خرائط، ولا Tiles، ولا معايير OGC، ولا مسارات متحركة | ADR-P12 + Spatial Architecture موسعة | W3/SLC-02 |
| CR-13 | العمل دون اتصال مُختبَر وغير مصمم | ADR-P09 + Offline Sync Architecture | W3/SLC-11 |
| CR-14 | آلية عزل المستأجرين غير محددة | ADR-P04 | W3 |
| CR-15 | لا عملية Split/Unmerge رغم حالة SPLIT_REQUIRED | إضافة العملية والأحداث وإعادة توجيه المعرفات | W3/SLC-04 |
| CR-16 | `task_history` و`task_events` و`outbox` دون تحديد المرجع | ADR-P02 | W3 |
| CR-17 | الأمن بلا مستويات تصنيف، ولا Compartments، ولا Threat Model، ولا إدارة مفاتيح | W3 Security Kernel + UNK-006 | W3 |
| CR-18 | لا معالجة للغة العربية في البحث ومطابقة الكيانات | ADR-P15 + Language Model | W3 |
| CR-19 | لا إدارة للبيانات المرجعية والرئيسية | ADR-P14 + Reference Data Catalog | W3 |
| CR-20 | مستويات استقلالية AI غير مربوطة بعمليات، وL5 بلا موقف | AI Autonomy Matrix (AIL) + موقف صريح من AIL5 | W3 |
| CR-21 | خط الأساس التقني (Kafka، OpenSearch، Neo4j، Redis، K8s) قبل أعباء العمل | تُعاد تصنيفها كـ "مرشحين"، والقرار في ADR-P05 | W8 |
| CR-22 | قسم الحالة (PRJ§123) يضع ✓ دون أدلة | استبداله بتقارير البوابات بصيغة PASS/PARTIAL/FAIL/BLOCKED/UNKNOWN | W0 |
| CR-23 | شريحة التنفيذ الأولى (PRJ§87) واسعة جداً | شرائح رفيعة (القسم 11.2) | W1 |
| CR-24 | نموذج الصلاحيات بلا Jurisdiction (موجود في V5§30) | إضافته لسياق قرار السياسة | W3 |
| CR-25 | إعادة البناء التاريخي بلا حالة Unknown وبلا تعريف As-Of | إضافة Unknown، وتعريف As-Of-Valid وAs-Known-At | W3 |
| CR-26 | مراحل P00–P02 غير موثقة (مشكلة، نطاق، راعٍ، قيود، مؤشرات) | W1 بالكامل | W1 |
| CR-27 | حقل `updated` في Envelope يوحي بالكتابة فوق القيم | التحديث في T1/T2 ينتج إصداراً، و`updated` مجرد مؤشر | W3 |
| CR-28 | ملف V5 مبتور في القسم 124 | استكمال في V6§22 | W0 |
| CR-29 | AnalysisCase (12 مكوناً) وPlan (14 مكوناً) مرشحان لـ God Aggregate | اختبار الحدود مقابل الثوابت، وفصل ما لا يحتاج اتساقاً فورياً | W4 |
| CR-30 | المخرجات O1–O6 غير مربوطة بالمتطلبات | ربط OUT ← BRQ في التتبع | W2 |

---

# 15. القرارات المعمارية المقترحة (ADR Backlog)

كل قرار هنا **PROPOSED**. "الخيار المرجح مبدئياً" رأي هندسي مبني على مستند المشروع ومبادئه، وليس قراراً. يعتمده مالك بشري في نقطة الاعتماد المذكورة.

## ADR-P01 — النموذج الزمني

- **المشكلة:** خمسة أزمنة معرفة في المبادئ، ونموذج البيانات لا يمثلها، والإعادة التاريخية غامضة.
- **الخيارات:**
  1. ثنائي الزمن كامل: فترة Valid Time وفترة Record (Transaction) Time لكل كائن T1، مع Event وObservation وEffective كسمات حسب نوع الكائن.
  2. زمن أحادي (Valid) + جدول إصدارات مؤرخ.
  3. Event Sourcing مع إعادة البناء من الأحداث.
- **الخيار المرجح مبدئياً:** (1) لكائنات T1 فقط، و(2) لكائنات T2. السبب: سؤالا "ماذا كان صحيحاً في تاريخ X" و"ماذا كنا نعرف في تاريخ X" كلاهما مطلوب في سياق تحليلي، والخيار (1) وحده يجيب عن الثاني دون إعادة تشغيل الأحداث.
- **محجوب بـ:** UNK-007، UNK-015. **الاعتماد:** HAP-04.

## ADR-P02 — أسلوب الحفظ

- **الخيارات:** (1) State + History + Outbox. (2) Event Sourcing. (3) مختلط حسب الـ Aggregate.
- **الخيار المرجح مبدئياً:** (1) كافتراضي، و(2) فقط حيث يكون تسلسل الأحداث هو المنتج نفسه (مثل سجلات الحوادث إن لزم). مع حسم أن `history` هو مرجع الإعادة التاريخية، والأحداث للتكامل.
- **الاعتماد:** HAP-04.

## ADR-P03 — مستويات الأهمية

```text
T1 Evidential   : Claims + Evidence + Provenance + Conflict + ثنائية زمنية + ثقة كاملة
                  (معلومات الكيانات من مصادر، الملاحظات، التقييمات، النتائج التحليلية)
T2 Governed     : Versioning + Approval + Audit + Valid Time
                  (الخطط، القرارات، المهام، السياسات، المنتجات)
T3 Operational  : Audit فقط
                  (الإعدادات التشغيلية، التفضيلات الإدارية)
T4 Ephemeral    : لا تدقيق تفصيلي
                  (حالة الواجهة، الجلسات المؤقتة)
```

- **القاعدة:** المستوى يُحدد **لكل سمة** في الكائن، لا للكائن ككل فقط. اسم الكيان قد يكون T1 بينما ملاحظة داخلية عليه T3.
- **محجوب بـ:** UNK-007. **الاعتماد:** HAP-04.

## ADR-P04 — عزل المستأجرين

- **الخيارات:** (1) Row-Level Security في قاعدة مشتركة. (2) Schema لكل مستأجر. (3) قاعدة لكل مستأجر. (4) هجين حسب التصنيف.
- **يجب أن يشمل:** الإسقاطات (بحث، رسم، متجهات)، والتخزين الكائني، والنسخ الاحتياطية، والسجلات، والتحليلات.
- **محجوب بـ:** UNK-002، UNK-004، UNK-006. **الاعتماد:** HAP-05.

## ADR-P05 — البصمة التقنية الأولية

- **الخيارات:** (1) PostgreSQL/PostGIS كنواة وحيدة مبدئياً (بحث نصي، pgvector، استعلامات عودية للعلاقات) + Object Storage، مع التوسع عند إثبات الحاجة. (2) الحزمة الكاملة المقترحة في PRJ§77 من البداية.
- **الخيار المرجح مبدئياً:** (1)، لأن البحث والرسم معرّفان في المستند كإسقاطات قابلة لإعادة البناء، فالتحول لاحقاً منخفض المخاطر، والعبء التشغيلي المبكر أقل بكثير. **لكن** القرار ينقلب إن أظهر WL-06 معدلات أحداث عالية أو أظهر WL-08 تنقلات عميقة على عقد كثيفة.
- **محجوب بـ:** WL-02، WL-06، WL-08، UNK-003، UNK-012. **الاعتماد:** HAP-08.

## ADR-P06 — الأمن داخل الإسقاطات

- **النطاق:** فهارس البحث، الرسم، المتجهات، الـ Tiles، الـ Cache، التصدير.
- **الخيارات:** (1) تصفية وقت الاستعلام بسمات أمنية مفهرسة. (2) فهارس مجزأة حسب التصنيف أو المستأجر. (3) مزيج.
- **متطلبات إلزامية أياً كان الخيار:** منع الاستدلال من العدد والـ Facets، وعدم تخزين Tiles مؤقتاً عبر مستويات صلاحية مختلفة، وإعادة فحص الصلاحية للنتائج قبل إرسالها إلى AI.
- **الاعتماد:** HAP-05.

## ADR-P07 — طبيعة Situation

- **الخيارات:** (1) Aggregate يملك التعريف (النطاق الجغرافي والزمني، المعايير، العضوية، حالة التنبيه) بينما محتواه إسقاط. (2) إسقاط خالص بلا حالة.
- **الخيار المرجح مبدئياً:** (1)، لأن المستند يعرّف أوامر إنشاء ومراجعة وتنبيهات، وهي حالة تحتاج مالكاً.

## ADR-P08 — المحو مقابل الثبات

- **المشكلة:** عدم الحذف، والأحداث الثابتة، والأرشفة، تتعارض مع الإتلاف القانوني وطلبات المحو.
- **الخيارات:** Crypto-shredding (تشفير بيانات شخصية بمفتاح لكل موضوع وإتلاف المفتاح)، أو Tombstones مع إزالة المحتوى، أو استثناءات قانونية موثقة.
- **محجوب بـ:** UNK-002. **الاعتماد:** HAP-03.

## ADR-P09 — المزامنة الميدانية

- **الخيارات:** (1) إرسال الأوامر المسجلة محلياً وإعادة تطبيقها مركزياً، مع تحويل التعارضات إلى Conflict Engine. (2) CRDT لأنواع بيانات محددة (ملاحظات نصية مثلاً). (3) نسخ للقراءة فقط دون اتصال.
- **الخيار المرجح مبدئياً:** (1) مع (2) لأنواع محدودة. Last-Write-Wins ممنوع للبيانات T1/T2 [DOC:PRJ§110].
- **يجب أن يعالج:** اختلاف الساعات (الزمن المسجل على الجهاز ليس Record Time)، وفقدان الجهاز وتشفيره، وانتهاء صلاحية البيانات المحلية.
- **محجوب بـ:** UNK-009.

## ADR-P10 — فصل التسميات

AIL0–AIL5 لاستقلالية الذكاء الاصطناعي في المنتج، وDAL0–DAL5 لصلاحيات وكلاء الدراسة. **الحالة:** يمكن اعتماده مباشرة.

## ADR-P11 — محرك السياسات وتمثيلها

- **الخيارات:** لغة سياسات تصريحية بمحرك متخصص، أو جداول قرار مخصصة مفسرة داخل التطبيق.
- **في الدراسة:** تُكتب السياسات كجداول قرار محايدة (القسم 13.8)، ويؤجل اختيار المحرك إلى W8.

## ADR-P12 — تقديم الخرائط وأمنها

- **النطاق:** Vector Tiles وRaster Tiles، وCloud-Optimized GeoTIFF للصور، و3D Tiles إن لزم، والتوافق مع OGC API (Features / Tiles / Maps) عند الحاجة للتكامل.
- **القيد الأمني:** Tiles مخصصة لكل مستوى صلاحية، أو توليد عند الطلب، مع منع التخزين المؤقت المشترك (ADR-P06).
- **محجوب بـ:** WL-03، UNK-010.

## ADR-P13 — المعرفات

- **الاقتراح:** ULID داخلياً (مرتبة زمنياً)، وURN عام بصيغة `urn:<namespace>:<object_type>:<id>` بدلاً من الصيغة غير القياسية في PRJ§12، مع سجل `ExternalIdentifier` كما في المستند، وسجل إعادة توجيه للمعرفات بعد الدمج.

## ADR-P14 — البيانات المرجعية

- **النطاق:** قوائم الرموز (أنواع الكيانات، أنواع العلاقات، تصنيفات، وحدات القياس، أنواع الأصول…)، ومالكها، وإصداراتها، وأثر تغييرها على البيانات التاريخية.

## ADR-P15 — اللغة ومطابقة الكيانات

- **يجب أن يحدد:** توحيد الكتابة العربية (الهمزات، الألف المقصورة، التاء المربوطة، التشكيل، التطويل)، وتمثيل الأسماء بصيغها المتعددة (أصلية، منقحرة، ألقاب، سلاسل النسب)، ومحللات البحث العربية، وتخزين الاسم الأصلي دون تعديل مع صيغ مطبّعة للمطابقة، والتقويم الهجري إن لزم.
- **محجوب بـ:** UNK-011.

---

# 16. قواعد فحص المواصفة (Spec Lint Rules)

هذه القواعد تحوّل فحص الاتساق (V5§110) إلى فحص آلي على مستودع المواصفات. تُكتب في `spec-lint-rules.yaml` وتُطبق في W7 وW9. **مخالفة أي قاعدة بمستوى ERROR تمنع G6-SLC.**

| ID | القاعدة | المستوى |
|---|---|---|
| SL-01 | كل BO له مالك واحد بالضبط في `ownership.yaml` | ERROR |
| SL-02 | كل CMD مرتبط بـ AGG واحد وPOL واحد على الأقل | ERROR |
| SL-03 | كل CMD يغير الحالة ينتج EVT واحداً على الأقل | ERROR |
| SL-04 | كل انتقال في SM له CMD أو trigger، وحدث، وشرط | ERROR |
| SL-05 | لكل SM: كل حالة × كل أمر إما انتقال مدرج أو رفض صريح | ERROR |
| SL-06 | كل حالة غير نهائية لها طريق إلى حالة نهائية | ERROR |
| SL-07 | كل EVT له مخطط بإصدار ومستهلك واحد على الأقل أو مبرر | ERROR |
| SL-08 | كل API يرتبط بـ CMD أو QRY | ERROR |
| SL-09 | كل QRY يحدد سياسة الصلاحية ونطاق الاسترجاع المسموح قبل التنفيذ | ERROR |
| SL-10 | كل BO بمستوى T1 يحدد الأزمنة ومصدر الدليل والثقة | ERROR |
| SL-11 | لا حقل باسم `created_at` أو `updated_at` يُستخدم كزمن حدث أو صلاحية | ERROR |
| SL-12 | كل سمة مكانية تحدد CRS والدقة | ERROR |
| SL-13 | لا استعلام أو عقد يقرأ من BO خارج سياقه إلا عبر API أو حدث أو إسقاط معلن | ERROR |
| SL-14 | كل Projection تحدد مصدرها وطريقة إعادة بنائها والتأخر المقبول والصلاحية | ERROR |
| SL-15 | كل REQ في النطاق له acceptance_criteria وverification_method | ERROR |
| SL-16 | كل QAS بأولوية H له مقياس أو TBD بمرجع UNK ومالك | ERROR |
| SL-17 | كل THR بأثر H له ضابط أو قبول مخاطرة صريح | ERROR |
| SL-18 | كل FM بشدة H له استراتيجية تعافٍ واختبار | ERROR |
| SL-19 | لا مخرج بحالة APPROVED دون `approved_by` و`approved_at` | ERROR |
| SL-20 | كل معرّف مذكور في `traces` موجود فعلاً | ERROR |
| SL-21 | كل عملية AI تحدد مستوى AIL ومرجعها في Autonomy Matrix | ERROR |
| SL-22 | كل UNK بحالة open ويحجب قراراً في الشريحة يمنع G6-SLC | ERROR |
| SL-23 | لا مخرج بلا مستهلك (A20) | WARNING |
| SL-24 | Aggregate بأكثر من 7 كيانات داخلية يحتاج تبريراً | WARNING |
| SL-25 | لا ذكر لتقنية محددة في مخرجات W1–W7 إلا مع مرجع ADR | WARNING |
| SL-26 | كل مصطلح عمل مستخدم موجود في `glossary.yaml` بالعربية والإنجليزية | WARNING |
| SL-27 | كل حدث تكامل منفصل عن الحدث الداخلي (Domain vs Integration) | WARNING |
| SL-28 | كل سياسة تحدد ما يحدث عند فشل محرك السياسات (fail-closed افتراضياً) | ERROR |

---

# 17. المجهولات وبنك الأسئلة

## 17.1 سجل المجهولات الأولي

| ID | السؤال | القرارات المحجوبة | الأولوية | الموجة |
|---|---|---|---|---|
| UNK-001 | ما المؤسسة والقطاع والمهمة الأساسية؟ | النطاق، ترتيب الشرائح، التصنيف | حرجة | W1 |
| UNK-002 | ما الإطار التنظيمي والقانوني ومتطلبات إقامة البيانات؟ | ADR-P04، P08، الاحتفاظ، الاستضافة | حرجة | W1 |
| UNK-003 | بيئة التشغيل: سحابة، محلي، معزول تماماً، أم مزيج؟ | ADR-P05، استضافة نماذج AI، التكلفة | حرجة | W1 |
| UNK-004 | عدد المؤسسات والوحدات والمستخدمين والمناطق؟ | ADR-P04، السعة، الحاجة للـ Multi-Tenancy | حرجة | W1 |
| UNK-005 | أحجام البيانات ومعدلات الحساسات والصور؟ | WL-06، WL-11، التخزين | عالية | W2 |
| UNK-006 | مستويات التصنيف الأمني والـ Compartments ومبدأ Need-to-Know؟ | نموذج الصلاحيات كاملاً | حرجة | W1 |
| UNK-007 | ما المعلومات التي تحتاج أثراً كاملاً للأدلة والمصدر؟ | ADR-P01، P03 | حرجة | W1 |
| UNK-008 | متطلبات التوفر وقيم RPO وRTO لكل قدرة حرجة؟ | الاعتمادية، التعافي، التكلفة | عالية | W2 |
| UNK-009 | متطلبات العمل الميداني دون اتصال؟ | ADR-P09، SLC-11 | عالية | W1 |
| UNK-010 | قائمة الأنظمة الخارجية الفعلية وعقودها ومعاييرها؟ | التكامل، ADR-P12 | عالية | W2 |
| UNK-011 | اللغات، وقواعد الأسماء، والتقويم المطلوب؟ | ADR-P15 | عالية | W1 |
| UNK-012 | الميزانية وحجم الفريق والجدول الزمني؟ | نطاق الإصدار، ADR-P05 | حرجة | W1 |
| UNK-013 | من يملك تحديد مستوى استقلالية AI لكل عملية؟ | AI Autonomy Matrix | عالية | W1 |
| UNK-014 | ما البيانات القديمة المطلوب ترحيلها ومن أين؟ | Migration Strategy | متوسطة | W2 |
| UNK-015 | ما درجة الآنية المطلوبة للمواقف والتنبيهات؟ | WL-01، WL-06، ADR-P07 | عالية | W2 |
| UNK-016 | هل توجد متطلبات إمكانية وصول ملزمة (معيار ومستوى)؟ | Accessibility | متوسطة | W2 |
| UNK-017 | ما قواعد فصل المهام (من يعتمد ومن ينفذ)؟ | SM-TASK، السياسات | متوسطة | W4 |

## 17.2 بنك الأسئلة لأصحاب القرار

الأسئلة مصممة لتُطرح في جلسات W1 وW2. كل إجابة تُسجل بمصدرها (الاسم، الدور، التاريخ) وتغلق المجهول المرتبط.

**الاستراتيجية والنطاق**

1. ما المشكلة التي تحلها المنصة اليوم؟ وما الذي يحدث الآن بدونها؟ (UNK-001)
2. ما النتائج الثلاث الأهم التي يجب أن تتحقق خلال السنة الأولى، وكيف تُقاس؟
3. ما الذي خارج النطاق صراحة؟
4. من راعي المشروع، ومن يملك قرار النطاق والأولويات؟
5. هل هناك موعد أو حدث خارجي يفرض جدولاً؟ (UNK-012)

**المؤسسة والمستخدمون**

6. كم مؤسسة ستستخدم المنصة؟ هل هي مؤسسة واحدة بوحدات، أم مؤسسات مستقلة تحتاج عزلاً كاملاً؟ (UNK-004)
7. كم مستخدماً إجمالاً، وكم منهم في وقت واحد في الذروة؟
8. ما الأدوار الفعلية؟ ومن يعتمد القرارات والخطط والمهام؟ (UNK-017)
9. أين يعمل المستخدمون جغرافياً؟ وهل يعمل بعضهم في الميدان دون اتصال؟ كم ساعة أو يوماً؟ (UNK-009)

**البيانات والمعلومات**

10. ما مصادر المعلومات الحالية، وما حجمها وأنواعها (وثائق، صور، فيديو، بيانات حساسات)؟ (UNK-005)
11. ما المعلومات التي يجب أن يُعرف مصدرها ودليلها دائماً، وما التي يكفي فيها سجل التعديل؟ (UNK-007)
12. هل تحتاجون معرفة "ماذا كنا نعرف في تاريخ معين" أم فقط "ماذا كان صحيحاً في تاريخ معين"؟ (UNK-007)
13. هل توجد بيانات حالية يجب ترحيلها؟ من أي أنظمة؟ (UNK-014)
14. بأي لغات تُكتب البيانات والأسماء؟ وهل تحتاجون التقويم الهجري؟ (UNK-011)

**الأمن والقانون**

15. ما مستويات التصنيف المستخدمة؟ هل توجد أقسام معلومات لا يطلع عليها إلا من يحتاجها؟ (UNK-006)
16. ما القوانين واللوائح التي تنطبق؟ هل يجب أن تبقى البيانات داخل الدولة أو داخل مباني المؤسسة؟ (UNK-002)
17. هل توجد متطلبات محو أو إتلاف للبيانات بعد مدة؟ (UNK-002)
18. من يعتمد الاستثناءات الأمنية؟

**التشغيل والبيئة**

19. أين ستعمل المنصة: سحابة عامة، سحابة وطنية، مركز بيانات المؤسسة، أم بيئة معزولة عن الإنترنت؟ (UNK-003)
20. ما أقصى مدة توقف مقبولة لكل قدرة حرجة؟ وما أقصى بيانات يمكن فقدانها؟ (UNK-008)
21. هل يوجد فريق تشغيل؟ ما حجمه وخبرته؟ (UNK-012)
22. ما سرعة تحديث الموقف والتنبيهات المطلوبة: ثوانٍ، دقائق، أم ساعات؟ (UNK-015)

**التكامل**

23. ما الأنظمة الموجودة التي يجب التكامل معها؟ وهل لها واجهات برمجية؟ (UNK-010)
24. هل يجب الالتزام بمعايير تبادل جغرافية أو قطاعية محددة؟

**الذكاء الاصطناعي**

25. ما المهام التي تريدون أن يساعد فيها AI؟ وما المهام الممنوعة عليه؟ (UNK-013)
26. هل يُسمح لـ AI باتخاذ أي إجراء دون موافقة بشرية؟ في أي عمليات؟
27. هل يمكن استخدام نماذج خارجية، أم يجب أن تعمل النماذج محلياً؟ (UNK-003)

**الموارد**

28. ما الميزانية التقريبية للبناء والتشغيل السنوي؟ (UNK-012)
29. ما حجم الفريق الهندسي المتاح؟

---

# 18. المخاطر والافتراضات الأولية

## 18.1 سجل المخاطر

| ID | الخطر | الاحتمال | الأثر | التخفيف | المالك |
|---|---|---|---|---|---|
| RSK-001 | نطاق 26 مجالاً للإصدار الأول يؤدي لفشل التسليم | H | H | شرائح رفيعة، ونطاق معتمد (HAP-02) | الراعي |
| RSK-002 | غموض النموذج الزمني يسبب أخطاء بيانات يصعب إصلاحها | M | H | ADR-P01 قبل أي تصميم منطقي | BC02 |
| RSK-003 | تسرب صلاحيات عبر الإسقاطات أو الـ Cache أو الـ Tiles | M | H | ADR-P06، QAS-SEC، اختبارات الاستدلال | Security |
| RSK-004 | إفراط في نموذج الأدلة يضر الأداء والاستخدام | M | M | ADR-P03 | BC02 |
| RSK-005 | عبء تشغيلي يفوق قدرة الفريق | M | H | ADR-P05 مبني على أعباء العمل | Platform |
| RSK-006 | ضعف مطابقة الأسماء العربية | H | M | ADR-P15، بيانات اختبار عربية | BC02 |
| RSK-007 | تعارض المحو القانوني مع الثبات | M | H | ADR-P08 | Privacy |
| RSK-008 | تعارضات المزامنة الميدانية تفسد البيانات | M | H | ADR-P09 | BC02 |
| RSK-009 | قدرات AI محدودة في بيئة معزولة | M | M | اختبار نماذج محلية مبكراً (SLC-10) | AI |
| RSK-010 | الدراسة تتحول لوثائق بلا تنفيذ | M | H | قواعد A20، ومعيار القسم 2، وجاهزية بالشريحة | Orchestrator |
| RSK-011 | تأخر إجابات أصحاب القرار يوقف الدراسة | H | H | بنك الأسئلة مبكراً، وقبول افتراضات صريحة مؤقتة بموافقة | الراعي |

## 18.2 الافتراضات الضمنية في مستند المشروع

| ID | الافتراض | يجب التحقق عبر |
|---|---|---|
| ASM-001 | PostgreSQL/PostGIS يكفي كمصدر حقيقة لكل الأعباء التشغيلية | WL-01، WL-03، ADR-P05 |
| ASM-002 | Multi-Tenancy مطلوب | UNK-004 |
| ASM-003 | الواجهات الثلاث (ويب، سطح مكتب، جوال) مطلوبة في الإصدار الأول | HAP-02 |
| ASM-004 | المستخدمون عرب أساساً [INF من لغة المستند] | UNK-011 |
| ASM-005 | يوجد فريق قادر على تشغيل حزمة متعددة القواعد | UNK-012 |
| ASM-006 | ناقل أحداث مخصص مطلوب | WL-06 |
| ASM-007 | قاعدة رسم مخصصة مطلوبة | WL-08 |

---

# 19. نموذج الجودة والأنماط المضادة

## 19.1 أبعاد التقييم (من V5، محتفظ بها)

Correctness، Security، Performance، Scalability، Availability، Reliability، Resilience، Data Quality، Traceability، Auditability، Maintainability، Operability، Observability، Interoperability، Usability، Accessibility، Cost Efficiency، Evolvability، AI Quality، AI Safety.

التقييم لكل بُعد: **PASS / PARTIAL / FAIL / BLOCKED / UNKNOWN** مع السبب والدليل. لا درجة مجمعة.

## 19.2 الأنماط المضادة الواجب فحصها (V5§109 + إضافات V6)

من V5: CRUD-First، Microservice Explosion، Shared Database، Distributed Monolith، God Service، God Aggregate، Hidden Coupling، Event Soup، Notification/Event Confusion، Search as SoT، Graph as SoT، AI as Authority، Authorization After Retrieval، Silent Overwrite، Missing Provenance، Missing Temporal Semantics، Missing Ownership، Over-centralized Core، Premature Technology Selection، Premature Kubernetes، Premature Microservices، Unbounded Agents، Unbounded Permissions، Missing Failure Strategy، Missing Recovery، Missing Observability، Unmeasured Performance، Unmodeled Capacity، Hidden Technical Debt.

إضافات V6:

- **Maximum Rigor Everywhere:** تطبيق نموذج T1 على كل البيانات.
- **Inference Leakage:** منع الوصول مع السماح بالاستدلال على الوجود.
- **Timestamp Collapse:** استخدام `created_at` لكل أنواع الزمن.
- **Checkmark Readiness:** إعلان الاكتمال دون أدلة.
- **Documentation Without Consumer:** مخرجات لا يستهلكها أحد.
- **Universal Envelope Coupling:** كل السياقات تعتمد على نموذج مركزي واحد، فيتحول أي تغيير فيه إلى تغيير في الجميع.
- **Language-Blind Matching:** مطابقة كيانات تتجاهل خصائص اللغة.
- **Shared Tile Cache Across Clearances:** تخزين مؤقت مشترك للخرائط بين مستويات صلاحية مختلفة.

## 19.3 التقييم الحالي لمستند المشروع

| النمط | الحالة |
|---|---|
| Premature Technology Selection | DETECTED (CR-21) |
| Premature Kubernetes | DETECTED، خفيف |
| Unmeasured Performance / Unmodeled Capacity | DETECTED |
| Hidden Technical Debt | DETECTED (لا سجل) |
| Checkmark Readiness | DETECTED (CR-22) |
| Timestamp Collapse | PARTIAL (CR-04) |
| God Aggregate | AT RISK (CR-29) |
| Over-centralized Core / Universal Envelope Coupling | AT RISK |
| Event Soup | AT RISK (CR-16) |
| Shared Database | AT RISK، مخفف باختبارات المعمارية |
| Inference Leakage | AT RISK (CR-17) |
| Language-Blind Matching | DETECTED (CR-18) |
| Premature Microservices، Search/Graph as SoT، AI as Authority، Notification/Event Confusion | AVOIDED |

---

# 20. معايير الجاهزية

## 20.1 البوابات

```text
G0 Strategic Approval       ← W1
G1 Business Architecture    ← W1
G2 Requirements Baseline    ← W2
G3 System Architecture      ← W3 (النواة)
G4 Solution Architecture    ← W8
G5 Detailed Design          ← W8 + شرائح النطاق
G6-SLC Slice Readiness      ← W7 لكل شريحة    (جديد في V6)
G6 Implementation Readiness ← W9 للإصدار
G7–G11                      ← خارج نطاق مرحلة الدراسة
```

## 20.2 جاهزية الشريحة (G6-SLC)

الشريحة جاهزة للبرمجة فقط إذا:

- G3 للنواة PASS، وADR-P01 وP02 وP03 بحالة APPROVED.
- كل Aggregate في الشريحة يستوفي البنود الأحد عشر في القسم 2.2.
- قواعد الفحص في القسم 16 بلا أي ERROR.
- Threat Model وFMEA للشريحة مكتملان، وكل تهديد أو نمط فشل بأثر H معالج أو مقبول صراحة.
- سيناريوهات القبول تغطي: المسار الطبيعي، كل انتقال ممنوع، كل قرار صلاحية (ALLOW / DENY / REDACT…)، سيناريو استدلال أمني واحد على الأقل حيث يوجد استرجاع.
- لا UNK مفتوح يحجب قراراً في الشريحة.
- مراجعة مستقلة من مجلس المعمارية.
- اعتماد بشري للشريحة (HAP-09).

## 20.3 جاهزية الإصدار (G6)

- كل شرائح النطاق G6-SLC.
- G4 وG5 PASS، وADR-P05 معتمد.
- مصفوفات التتبع مولدة، وكل BRQ في النطاق يصل إلى TST.
- تقرير الاتساق بلا تعارضات مفتوحة.
- تقرير الأنماط المضادة: لا DETECTED بلا خطة معالجة.
- استراتيجيات النشر والتعافي والمراقبة والترحيل موجودة بمستوى T2 الأولي.
- اعتماد بشري (HAP-10).

**إذا نقص أي شرط:** الحكم PARTIAL أو BLOCKED أو UNKNOWN مع السبب. لا يُعلن READY.

---

# 21. بروتوكول تنفيذ المنسق الرئيسي

## 21.1 وحدة العمل

**جلسة واحدة = موجة واحدة، أو موجة واحدة لشريحة واحدة.** محاولة إنتاج الحزمة كلها في جلسة واحدة تنتج مخرجات سطحية ومتناقضة، وهو ما يمنعه هذا البروتوكول.

## 21.2 مدخلات كل جلسة

1. هذا الملف (V6).
2. مستند المشروع.
3. مستودع المواصفات بحالته الحالية (أو الملخص `spec/README.md` مع الملفات المعنية بالموجة).
4. إجابات أصحاب القرار الجديدة إن وُجدت.
5. تحديد صريح: الموجة المطلوبة والشريحة إن وجدت.

## 21.3 مخرجات كل جلسة

1. **الملفات** المنتجة أو المعدلة، كل منها برأس القسم 7.2.
2. **تحديثات السجلات:** مجهولات جديدة أو مغلقة، مخاطر، افتراضات، أسئلة مفتوحة، ADRs مقترحة.
3. **تقرير الجلسة** بالصيغة:

```text
SESSION REPORT
Wave / Slice:
Artifacts produced:       [IDs]
Artifacts updated:        [IDs]
Epistemic summary:        documented / inferred / assumed / unknown counts
New unknowns:             [UNK-…]
Decisions needing human:  [HAP-…, ADR-P…]
Lint results:             errors / warnings
Gate status:              PASS / PARTIAL / FAIL / BLOCKED / UNKNOWN + reason
Next recommended session:
```

## 21.4 نقاط الاعتماد البشري (إلزامية)

| ID | القرار | الموجة |
|---|---|---|
| HAP-01 | اعتماد System Definition وبيان المشكلة (G0) | W1 |
| HAP-02 | نطاق الإصدار الأول وترتيب الشرائح | W1 |
| HAP-03 | الإطار القانوني والتنظيمي، وADR-P08 | W1/W3 |
| HAP-04 | ADR-P01، P02، P03 (النواة المعلوماتية) | W3 |
| HAP-05 | نموذج التصنيف والصلاحيات، وADR-P04، P06 | W3 |
| HAP-06 | AI Autonomy Matrix والموقف من AIL5 | W3 |
| HAP-07 | قيم RPO وRTO والتوفر لكل قدرة حرجة | W2/W5 |
| HAP-08 | ADR-P05 والتقنيات | W8 |
| HAP-09 | جاهزية كل شريحة (G6-SLC) | W7 |
| HAP-10 | جاهزية الإصدار (G6) | W9 |

يُسجل كل اعتماد في `human-approvals.yaml`: القرار، المعتمِد، الدور، التاريخ، الأدلة، الشروط.

## 21.5 شروط التوقف (من V5§112، محتفظ بها)

يتوقف الوكيل ويُخرج BLOCKED أو UNKNOWN إذا: نقصت المعلومات الأساسية، أو وُجد تعارض غير محلول، أو لم يوجد مصدر، أو كان القرار خارج صلاحياته أو يتطلب سلطة عمل أو استثناءً أمنياً أو قراراً سياسياً أو تنظيمياً أو افتراضاً عالي الأثر، أو كانت الأدلة غير كافية.

**إضافة V6:** التوقف لا يعني إنهاء الجلسة. يستمر الوكيل في المخرجات غير المحجوبة، ويسجل المحجوب بوضوح.

## 21.6 حلقة الدراسة داخل الجلسة (من V5§114)

```text
UNDERSTAND → INSPECT → MODEL → IDENTIFY UNKNOWNs → ANALYZE
→ GENERATE OPTIONS → EVALUATE TRADE-OFFS → PROPOSE → CROSS-REVIEW
→ VALIDATE (Spec Lint) → RECORD DECISION → TRACE → BASELINE
```

## 21.7 المراجعة المتقاطعة

```text
Author Role → Independent Review → Consistency (Spec Lint)
→ Security Review → Quality Review → Orchestrator → Human Approval (للحرج)
```

إذا اختلفت الأدوار: لا تصويت. يُسجل التعارض بأدلته وقيوده وبدائله، ويُرفع كقرار بشري (V5§87).

---

# 22. القواعد المطلقة

## 22.1 قواعد V5 (1–60، محتفظ بها)

1. لا تخترع Requirements.
2. لا تخترع Business Facts.
3. لا تحول Assumption إلى Fact.
4. لا تخفِ Unknown.
5. لا تحل Conflict بصمت.
6. Entity ≠ Event.
7. Evidence ≠ Truth.
8. Projection ≠ Source of Truth.
9. AI ≠ Authority by default.
10. Authorization Before Retrieval.
11. Search لا يتجاوز Security.
12. Graph لا يتجاوز Security.
13. AI لا يتجاوز Security.
14. Agent لا يتجاوز صلاحياته.
15. Domain ≠ Microservice.
16. Database Table ≠ Domain Model.
17. لكل Business Object مالك واضح.
18. لا Silent Overwrite.
19. Preserve History.
20. Temporal Semantics إلزامية حيث تنطبق.
21. Spatial Semantics إلزامية حيث تنطبق.
22. Provenance للمعلومات المهمة.
23. Confidence قابلة للتفسير.
24. Workload قبل Technology.
25. Performance قابلة للقياس.
26. Capacity مدروسة.
27. Scalability مدروسة.
28. Security تبدأ من Threat Model.
29. Reliability تشمل Failure Modes.
30. Resilience تشمل Degraded Modes.
31. Recovery قابلة للتحقق.
32. Observability ليست مجرد Logs.
33. Cost يدخل في القرارات المعمارية.
34. AI يجب أن يكون Traceable.
35. Agent Memory ليست Source of Truth.
36. لا Majority Vote للقرارات المعمارية.
37. كل قرار مهم ADR.
38. كل Requirement مهم Traceable.
39. كل Architecture مهمة قابلة للتحقق.
40. لا Production Code في هذه المرحلة.
41. لا Implementation Execution في هذه المرحلة.
42. لا Production Readiness قبل استكمال الدراسة.
43. لا Implementation-Ready مع Unknowns حرجة غير معالجة.
44. لا Technology قبل فهم Workload.
45. لا Complexity بدون Justification.
46. لا Microservice بدون Boundary واضح.
47. لا Event بدون سبب.
48. لا Graph بدون Relationship Workload.
49. لا AI بدون Use Case وGovernance.
50. لا Automation بدون Authority Model.
51. Architecture قابلة للتطور، لا وثيقة ثابتة.
52. كل استنتاج مهم قابل للتتبع.
53. كل Constraint مهم موثق.
54. كل Risk مهم له Mitigation أو قبول صريح.
55. كل Critical Unknown يظهر في Gate.
56. كل Architecture Decision يوضح Alternatives وTrade-offs.
57. كل Quality Attribute له Verification Strategy.
58. كل Critical Dependency معروفة.
59. كل Critical Failure Mode له Recovery Strategy.
60. لا يعتبر النظام ناجحاً لأنه يعمل في الحالة الطبيعية فقط.

## 22.2 قواعد V6 الجديدة (61–76)

61. الجاهزية تُمنح لشريحة، لا لكل النظام دفعة واحدة.
62. ما يستهلكه برنامج يُكتب بصيغة يقرأها برنامج.
63. كل متطلب جودة سيناريو قابل للقياس، لا صفة.
64. عمق النمذجة يتبع مستوى الأهمية (T1–T4) لكل سمة.
65. كل مخرج له معرّف ثابت ورأس تتبع، ولا تُكتب مصفوفات التتبع يدوياً.
66. كل State Machine جدول كامل: لا خلية حالة × أمر بلا حكم.
67. الانتقالات ليست حالات، والتصعيد ليس انتقالاً.
68. `created_at` لا يمثل أي زمن عمل.
69. منع الوصول لا يكفي؛ امنع الاستدلال على الوجود.
70. اللغة العربية جزء من النموذج المعلوماتي، لا من الواجهة فقط.
71. APPROVED يتطلب اسماً ودوراً وتاريخاً؛ علامة ✓ ليست اعتماداً.
72. استنتاج الوكيل أدنى مرتبة في أولوية المصادر، ولا يصبح حقيقة بالتكرار.
73. لا مخرج بلا مستهلك.
74. جلسة واحدة = موجة واحدة؛ لا إنتاج للحزمة كلها دفعة واحدة.
75. الخيار "المرجح مبدئياً" في أي ADR رأي، ولا يُبنى عليه قبل الاعتماد.
76. فشل محرك السياسات يعني الرفض (fail-closed) ما لم يقرر غير ذلك صراحة.

---

# 23. خريطة الانتقال من الوضع الحالي

الوضع الحالي للمشروع، مقاساً بهذا الملف:

| البوابة | الحالة الحالية | ما يغلقها |
|---|---|---|
| G0 | UNKNOWN | W1 + HAP-01 |
| G1 | PARTIAL | W1: Capability Map، Stakeholders، Decision Rights |
| G2 | FAIL | W2: Baseline بصيغة EARS، QAS، Use Cases مكتملة |
| G3 | PARTIAL | W3: CR-01 إلى CR-05، CR-10 إلى CR-19، ADR-P01 إلى P04 |
| G4 / G5 | PARTIAL | W8 بعد أعباء العمل |
| G6 | BLOCKED | كل ما سبق + الشرائح |

**أول ثلاث جلسات مقترحة:**

1. **جلسة W0:** إنشاء هيكل المواصفات، وتحميل التصحيحات والقرارات المقترحة والمجهولات والمخاطر من هذا الملف إلى السجلات، وقاموس المصطلحات الأولي.
2. **جلسة W1-أ (مع أصحاب القرار):** طرح بنك الأسئلة (القسم 17.2) وتسجيل الإجابات. لا يمكن لوكيل تنفيذ هذه الجلسة وحده.
3. **جلسة W1-ب:** بناء System Definition وStakeholder Model وCapability Map ونطاق الإصدار المقترح من الإجابات، ورفعها لـ HAP-01 وHAP-02.

**إذا تأخرت الإجابات:** يمكن البدء بـ W3 جزئياً (الأجزاء غير المحجوبة: الملكية، نموذج Claim/Evidence، جدول Task، تصحيحات التسمية)، مع ترك ADR-P01 وP03 وP04 بحالة PROPOSED حتى تصل الإجابات. هذا يسرع الدراسة دون بناء قرارات على تخمين.

---

# 24. البيان الختامي

هذه المنصة ليست تطبيقاً برمجياً فقط، بل **بنية تحتية مؤسسية للمعلومات والمعرفة والتخطيط والعمليات ودعم القرار**. والدراسة ليست دراسة معمارية برمجية فقط، بل **دراسة هندسة أنظمة شاملة** تجمع هندسة الأعمال والمتطلبات والمجالات والمعلومات والمعمارية والبيانات والأمن والأداء والاعتمادية والذكاء الاصطناعي والتشغيل والحوكمة والتحقق والتطور.

ويجب ألا يبدأ البناء البرمجي لأي جزء إلا بعد أن تصبح مواصفته:

> **Coherent, Evidence-Based, Traceable, Secure, Performant, Reliable, Observable, Verifiable — and Programmable:**
> قابلة للتنفيذ دون أن يتخذ المنفذ قراراً معمارياً أو قرار عمل بنفسه، وقابلة للتحقق آلياً من مطابقة التنفيذ لها، ومعتمدة من أصحاب القرار بأسمائهم.

ولا يُطلب من المعمارية أن تكون كاملة، بل أن تكون **صحيحة بما يكفي للبناء عليها، وصريحة فيما لا تعرفه بعد.**
