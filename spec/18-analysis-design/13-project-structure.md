---
id: AD-13-PROJECT-STRUCTURE
type: design-document
title: "13 — هيكلية المشروع (المستودع، الحزم، الوحدات، التسمية)"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design, المرحلة 1"
decided_by: [ADR-P18, ADR-P17]
depends_on: [TD-15, TD-17, TD-01]
---

# 13 — هيكلية المشروع

تحدد هذه الوثيقة **شكل المستودع البرمجي قبل كتابة أي سطر كود**: أين يعيش كل شيء، وكيف يُسمّى، ومن يعتمد على من. هي تفصيل قرار [ADR-P18](../00-governance/decisions/ADR-P18.md)، والحلقات داخل كل حزمة من [11-hexagonal-reference.md](11-hexagonal-reference.md).

> لغة الخدمات TypeScript (TD-15) ولغة طرق التحليل Python؛ الأسماء أدناه مستقلة عن اللغة، وامتداد الملفات يتبع اللغة عند التنفيذ.

## 1. الشجرة العليا

```text
platform-repo/
├── contracts/                     # مولَّد من spec/05-contracts — لا يُحرَّر يدويًا
│   ├── openapi/                   # 28 ملفًا → stubs للخوادم + عملاء
│   ├── asyncapi/                  # 19 ملفًا → أنواع الأحداث
│   └── errors/                    # 19 كتالوجًا → تعدادات رموز الأخطاء
├── shared-kernel/                 # أنواع قيم فقط، بلا I/O
│   ├── identifiers/               # ULID + URN (ADR-P13)
│   ├── time/                      # فترات ثنائية الزمن، الدقة (ADR-P01)
│   ├── language/                  # LocalizedName، الأشكال الأصلية/المطبَّعة (ADR-P15)
│   ├── security/                  # التسميات الأمنية، SecurityContext (نوع فقط)
│   └── errors/                    # غلاف الخطأ الموحّد
├── contexts/                      # نموذج واحد لكل Bounded Context (ADR-P17)
│   ├── bc01-foundation/
│   ├── bc02-information/
│   ├── bc03-intelligence/
│   ├── bc04-operations/
│   ├── bc05-readiness/
│   ├── bc06-knowledge/
│   ├── bc07-platform/
│   └── bc08-governance/
├── platform/                      # آليات Adapters مشتركة — لا منافذ سياقات ولا أنواع أعمال
│   ├── unit-of-work/              # معاملة: نطاق المستأجر + state + history + outbox + audit + inbox + سجل Idempotency
│   ├── outbox/  inbox/  idempotency/
│   ├── pep-client/                # OPA مدمج + ذاكرة القرار بـsecurity_version
│   ├── scheduler/                 # سلال زمنية + lease (TD-13)
│   ├── encryption/                # مفتاح الموضوع عبر OpenBao (ADR-P08)
│   └── telemetry/                 # OpenTelemetry (TD-14)
├── services/                      # وحدة قابلة للنشر لكل وحدة نشر (16)
│   ├── du-01-gateway/   du-02-foundation/   du-03-governance/
│   ├── du-04-information/   du-05-ingestion/   du-06-intelligence/
│   ├── du-07-evaluators/   du-08-operations/   du-09-discovery/
│   ├── du-10-field-sync/   du-11-adapters/   du-12-tiles/
│   ├── du-13-analysis-jobs/   du-14-readiness/   du-15-knowledge/
│   └── du-16-ai-serving/
├── clients/                       # واجهات المستخدم (12-solution/ui-architecture.md)
│   ├── web/                       # React + MapLibre
│   └── field-mobile/              # React Native + SQLCipher
├── analysis-methods/              # Python: طرق التحليل والمعالجة المكانية (صور DU-13)
├── deploy/
│   ├── cell/                      # بيانات الخلية لكل ملف (shared / dedicated / sovereign)
│   ├── migrations/<schema>/       # ترحيل للأمام فقط، expand/contract (TD-17)
│   └── bundle/                    # تعريف حزمة Zarf الموقَّعة
└── tooling/                       # مولِّد العقود من spec، فحوص المعمارية (FIT-20)
```

## 2. داخل حزمة سياق — `contexts/bcNN-<name>/`

المثال BC04 (العمليات). كل Aggregate مجلد، وكل أمر أو استعلام أو معالج عملية مجلد صغير واحد (ADR-P17: «hexagonal outside, slices inside»).

```text
contexts/bc04-operations/
├── domain/
│   ├── task/                          # AGG-TASK
│   │   ├── task                       # جذر الـAggregate: الحالة + version
│   │   ├── task-transitions           # جدول الانتقالات = مصفوفة SL-05 حرفيًا
│   │   ├── task-invariants            # INV-TASK-*
│   │   ├── task-events                # EVT-TASK-*
│   │   └── task-errors                # TASK_INVALID_STATE_TRANSITION ...
│   ├── plan/  plan-version/  decision/  decision-request/
│   ├── risk/  incident/  coordination-case/  ...
│   └── value-objects/                 # قيم خاصة بالسياق
├── application/
│   ├── commands/
│   │   ├── task-assign/               # CMD-TASK-ASSIGN → معالج + مدخلات الشرط
│   │   ├── task-approve/              # CMD-TASK-APPROVE
│   │   └── ...                        # 82 أمرًا في BC04
│   ├── queries/
│   │   ├── task-get/  task-list/      # QRY-TASK-*
│   │   └── ...                        # 21 استعلامًا
│   └── processes/
│       ├── on-qual-recorded/          # حدث مستهلَك: EVT-QUAL-RECORDED (إعادة فحص تعيين المهام)
│       └── task/
│           └── sys-due-passed-escalation-policy/   # مُحفِّز SYS: تحت مجلد الـAggregate صاحبه
└── ports/
    ├── task-repository                # + لكل Aggregate
    ├── eligibility-client             # OHS BC05 (fail-closed)
    ├── authority-client               # OHS BC01 AuthorityCheck
    └── task-read-model                # قوائم المهام بـallowed_scope
```

## 3. داخل وحدة نشر — `services/du-NN-<name>/`

الوحدة **رفيعة**: تركّب حزم السياقات التي تشغّلها مع المحوّلات والإعدادات، ولا تحتوي منطق أعمال.

```text
services/du-08-operations/
├── composition-root                   # ربط المنافذ بالمحوّلات، بدء التشغيل
├── adapters/
│   ├── inbound/
│   │   ├── http/                      # stubs مولَّدة من contracts/openapi/*-slc03,06,08,15,17 + تحويل إلى أنواع التطبيق
│   │   ├── kafka/                     # مستهلكو الأحداث من BC02/BC03/BC05
│   │   └── scheduler/                 # عمّال SYS: للمهام والخطط
│   └── outbound/
│       ├── postgres/                  # schema operations فقط
│       ├── opa/                       # PEP
│       └── clients/                   # BC01 AuthorityCheck، BC05 EligibilityCheck
├── config/                            # حدود المعدل، المهل، أحجام المجمّعات (لا أسرار)
└── health/                            # فحوص الجاهزية والحياة
```

## 4. خريطة الوحدات ← السياقات ← المحوّلات

| الوحدة | السياق (الحزمة) | Inbound الرئيسية | Outbound الرئيسية | الإصدار |
|---|---|---|---|---|
| du-01-gateway | — | HTTP (كل الطلبات) | BC01 SecurityContext | R1 |
| du-02-foundation | bc01 | HTTP، SCIM، scheduler | PostgreSQL `foundation`، OPA، Valkey | R1 |
| du-03-governance | bc08 | HTTP، Kafka (استيعاب التدقيق)، scheduler (الإتلاف) | PostgreSQL `governance`، OpenBao/HSM، S3 Object Lock | R1 |
| du-04-information | bc02 | HTTP، Kafka | PostgreSQL `information`، OPA، BC01 | R1 |
| du-05-ingestion | bc02 | HTTP عالي المعدل، استيراد، ماسح | PostgreSQL `information`، S3 | R1 |
| du-06-intelligence | bc03 | HTTP، Kafka | PostgreSQL `intelligence`، OPA، BC02 as-of | R1 |
| du-07-evaluators | bc03 | Kafka (تدفقي، ≤ 5 ث) | PostgreSQL `intelligence`، إشعارات | R1 |
| du-08-operations | bc04 (+ جزء bc05 في R1: التأهيل والأهلية، SLC-03) | HTTP، Kafka، scheduler | PostgreSQL `operations` (+ `readiness` في R1)، BC05 Eligibility، BC01 Authority | R1 |
| du-09-discovery | bc07 | HTTP (بحث/رسم)، Kafka (بناة الإسقاطات) | OpenSearch، مخزن الإسقاطات في PostgreSQL (slc-05) | R1 |
| du-10-field-sync | bc07 | بوابة المزامنة | PostgreSQL `field`، أوامر السياقات المالكة، S3 (الحزم) | R1 |
| du-11-adapters | bc07 | موصلات الأنظمة الخارجية (ACL) | PostgreSQL `integration`، أوامر BC02 عبر العقد | R1 (+R2) |
| du-12-tiles | — | OGC Tiles/Features | دوال/views طبقات منشورة من السياقات المالكة في PostGIS، قراءة فقط بنطاق الصلاحية (11 §8) | R1 |
| du-13-analysis-jobs | — (صور `analysis-methods/`) | Kueue jobs | BC03 عبر العقد | R1 |
| du-14-readiness | bc05 (كاملًا، ينتقل من DU-08) | HTTP، Kafka، scheduler | PostgreSQL `readiness` | R2 |
| du-15-knowledge | bc06 | HTTP، Kafka، scheduler | PostgreSQL `knowledge`، S3 | R2 |
| du-16-ai-serving | bc07 | HTTP | PostgreSQL `ai`، vLLM، OpenSearch k-NN؛ لا أوامر كتابة في R2 — أدوات الاقتراح تنشئ AI Results فقط | R2 |

أسماء الـschemas مأخوذة من `06-data/logical-model/`. مخزن الإسقاطات في slc-05 لا يحمل اسم schema صريحًا **[Missing]**، ويُثبَّت في `16-database-schema.md` (المرحلة 2).

## 5. قواعد التسمية

| العنصر في المواصفات | الاسم في المستودع | مثال |
|---|---|---|
| `AGG-<NAME>` | مجلد Domain بالاسم بحروف صغيرة وشرطات | `AGG-DECISION-REQUEST` → `domain/decision-request/` |
| `CMD-<PFX>-<VERB>` | المعرّف بلا `CMD-`، بحروف صغيرة | `CMD-TASK-ADD-RESULT-ITEM` → `commands/task-add-result-item/` |
| `QRY-<PFX>-<NAME>` | مجلد استعلام بنفس القاعدة | `QRY-AUT-CHECK` → `queries/aut-check/` |
| حدث مستهلَك `EVT-<...>` | `processes/on-` + المعرّف بلا `EVT-` | `EVT-QUAL-RECORDED` → `processes/on-qual-recorded/` |
| مُحفِّز `SYS:<trigger>` | `processes/<aggregate>/sys-` + نص المحفِّز بحروف صغيرة وشرطات (المحفِّز نفسه يتكرر في أكثر من Aggregate) | `SYS:valid_to reached` في AGG-CLEARANCE → `processes/clearance/sys-valid-to-reached/` |
| رمز خطأ | تعداد مولَّد في `contracts/errors/` | `TASK_INVALID_STATE_TRANSITION` |
| سياسة `POL-<...>` | لا كود؛ اسم الإجراء في DecisionRequest = رمز الأمر | `action = CMD-TASK-APPROVE` |
| وحدة نشر `DU-NN` | `services/du-NN-<name>/` | `DU-08` → `services/du-08-operations/` |

**القاعدة:** كل معرّف في `spec/` يتحول إلى مكان واحد في المستودع بقاعدة تحويل واحدة. الاتجاه العكسي ليس تحويلًا نصيًا دائمًا (يضيع الترميز والشرطات السفلية في أسماء المحفِّزات)، لذلك يُحفظ في مصفوفة التتبع `25-traceability-matrix.md` (المرحلة 5).

## 6. العقود المولَّدة

- `contracts/` تُولَّد من `spec/05-contracts` بأداة داخل `tooling/`، بنفس مبدأ أدوات المواصفة: **مولَّد لا يُحرَّر يدويًا** (راجع CR-71 لما يحدث حين يُخالَف هذا المبدأ).
- تغيير عقد متوافق = تعديل المواصفة، ثم إعادة التوليد، ثم تحديث المنتجين والمستهلكين في **نفس** الـcommit (ADR-P18 الدافع 3).
- تغيير عقد كاسر = إصدار رئيسي جديد يعيش بجانب السابق **6 أشهر على الأقل** (QAS-EVO-001، FIT-14): `contracts/openapi/<file>/v<N>/`، والخادم يقدّم الإصدارين؛ هذا ما يسمح للأجهزة الميدانية غير المتصلة بالعمل بإصدار أقدم.
- فحص V2/V3 في `verify_study.py` يضمن أن كل أمر واستعلام وحدث في الكتالوجات له عقد مطابق قبل التوليد.

## 7. قاعدة البيانات والترحيل

- كل schema يملكها سياق واحد يعدّلها وحده (FIT-01، TD-01)؛ وقد يملك السياق أكثر من schema (BC07: `integration`، `field`، `ai`، ومخزن الإسقاطات).
- الترحيل في `deploy/migrations/<schema>/` للأمام فقط بنمط expand/contract (TD-17)؛ لا ترحيل يحذف عمودًا قبل أن يتوقف كل إصدار سابق عن استخدامه.
- جداول `_history` و`outbox` و`audit_outbox` و`inbox` تنشئها قوالب `platform/unit-of-work` لكل schema بنفس الشكل (`06-data/logical-model/`).

## 8. الملكية والمراجعة

- مالك معلَن لكل مجلد في `contexts/*` و`services/*` (ملف ملكية على مستوى المستودع).
- أي تعديل في `shared-kernel/` أو `platform/` يحتاج مراجعة مالك المعمارية، لأنه يمس كل السياقات.
- أي تعديل في `contracts/` يأتي من تعديل في `spec/05-contracts` مرتبط بـCR أو ADR.

## 9. ممنوعات بنيوية (تُفحص آليًا — FIT-20)

1. `contexts/bcA/*` يستورد `contexts/bcB/*`.
2. `services/du-X/*` يستورد `services/du-Y/*`.
3. `contexts/*/domain/*` يستورد أي شيء خارج `shared-kernel/`.
4. `platform/*` يحتوي نوع أعمال من أي سياق.
5. ملف في `contracts/` لا يطابق مخرجات المولِّد.
6. ترحيل في `deploy/migrations/<schema>/` يلمس schema أخرى.
