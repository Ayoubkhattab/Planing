---
id: AD-15-EVENT-DESIGN
type: event-design
title: "تصميم الأحداث — القنوات والغلاف والتسليم والكتالوج"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
sources: [05-contracts/asyncapi-slc*.md, 03-domain/contexts/BC*/events-*.md, 00-governance/decisions/ADR-P02.md, 12-solution/technology-decisions.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# تصميم الأحداث (Event Design)

العقد المعتمد هو ملفات AsyncAPI 3.0 في `05-contracts/` (19 ملفًا). هذا الملف يشرح اصطلاحاتها المشتركة ويضع كل الرسائل (**585** = 584 حدث مجال + الحدث المشتق `EVT-SEC-VERSION-INCREMENTED`) في كتالوج واحد حسب القناة.

## 1. الوسيط والقنوات

| البند | القرار | المصدر |
|---|---|---|
| الوسيط | Apache Kafka (KRaft) لكل خلية، يديره Strimzi | TD-04 (`12-solution/technology-decisions.md`) |
| النشر | Transactional outbox: الحدث يُكتب في جدول `outbox` في نفس معاملة تغيير الحالة (ADR-P02، FIT-04)، ثم ينقله CDC (Debezium) إلى Kafka (TD-04) | ADR-P02، TD-04 |
| القنوات | قناة لكل مجال: `{cell}.<domain>.events` — 11 قناة، والمجال هو مقطع السياق في مسارات الواجهات | AsyncAPI `channels` |
| قناة الأولوية | `{cell}.security.versions` مخصصة لـ`EVT-SEC-VERSION-INCREMENTED` بأولوية عالية، لأن إبطال الصلاحيات لا ينتظر | TD-04؛ `asyncapi-slc01.md` |
| ملكية القناة | لكل قناة سياق منتِج واحد؛ BC07 ينشر في `ai` و`field` و`integration` و`discovery`، وBC01 في `foundation` و`security.versions` | كتالوجات الأحداث وملفات AsyncAPI |

## 2. الغلاف (EventEnvelope)

كل رسالة = الغلاف + `payload` خاص بالحدث.

| الحقل | إلزامي | المعنى |
|---|---|---|
| `event_id` | نعم | معرّف فريد للحدث؛ مفتاح عدم التكرار عند المستهلك |
| `event_type` | نعم | معرّف الحدث (`EVT-TASK-ASSIGNED`) |
| `event_version` | نعم | إصدار مخطط الحمولة |
| `producer` | نعم | الخدمة المنتجة |
| `aggregate` { `type`، `id`، `version` } | نعم | الـAggregate وإصداره بعد التغيير؛ يسمح للمستهلك بكشف الترتيب والفجوات |
| `occurred_at` | نعم | زمن وقوع التغيير (زمن العمل) |
| `recorded_at` | نعم | زمن تسجيل الخادم (FIT-09) |
| `tenant_id` | نعم | المستأجر (FIT-02) |
| `correlation_id` | نعم | من `X-Correlation-Id` في الطلب الأصلي |
| `causation_id` | لا | الحدث الذي تسبب في هذا الحدث (سلاسل العمليات) |
| `security` | لا | علامات الـAggregate الأمنية؛ المستهلك يحترمها في الإسقاطات (ADR-P06) |
| `payload` | نعم | حمولة عامة مشتركة بين أحداث المجال الـ584: `aggregate_urn`، `from_state`، `to_state` (إلزامية)، و`actor`، `reason`، `changes` (اختيارية؛ `changes` كائن غير مُنمَّط). حمولة `EVT-SEC-VERSION-INCREMENTED`: `subject_urn`، `security_version`، `cause_event_id` (كلها إلزامية) |

## 3. الترتيب والتقسيم

- مفتاح التقسيم `tenant_id + aggregate.id` لكل الأحداث (584)، و`tenant_id + subject_urn` لحدث إصدار الأمن. النتيجة: **أحداث الـAggregate الواحد مرتبة**، ولا ضمان ترتيب بين Aggregates مختلفة.
- المستهلك الذي يحتاج ترتيبًا عابرًا للـAggregates يعتمد على `aggregate.version` و`causation_id`، لا على ترتيب الوصول.

## 4. ضمان التسليم وعدم التكرار

| الجانب | الاصطلاح | المصدر |
|---|---|---|
| التسليم | **مرة واحدة على الأقل** (at-least-once) عبر outbox | ADR-P02؛ ترويسة كل ملف AsyncAPI |
| عدم التكرار | كل مستهلك يسجل `(tenant_id, consumer, event_id)` في جدول `inbox` في نفس معاملة أثره؛ الحدث المكرر يُتجاهل | `06-data/logical-model/slc-01.md`؛ ترويسة ملفات AsyncAPI |
| موقع المستهلك في الكود | محوّل Kafka وارد ← معالج عملية (process handler) في حلقة التطبيق ← خط الأوامر إن كان الأثر أمرًا | ADR-P17؛ `11-hexagonal-reference.md` §4 |
| التدقيق | سجل التدقيق يُكتب في `audit_outbox` (إدراج فقط) مع الحالة، منفصلًا عن أحداث المجال | `slc-01.md`؛ `08-security/audit-architecture.md` |

## 5. إعادة المحاولة والرسائل المسمومة

| البند | الحالة |
|---|---|
| إعادة المحاولة عند فشل المستهلك | المصدر الوحيد لفشل التسليم «outbox; retry / deliver on recovery» (`09-reliability/fmea-slc03.md`)، دون عدد محاولات أو تأخير **[Missing — الأرقام]** |
| الرسائل المسمومة وقائمة الرسائل الميتة (DLQ) | **[Missing]** — لا تذكرها المواصفات. اقتراح للمرحلة 4 (`23-crosscutting.md`): محاولات محدودة بتأخير متزايد، ثم نقل الرسالة إلى `{cell}.<domain>.events.dlq` مع سبب الفشل، وتنبيه، وأداة إعادة تشغيل. الترتيب لكل Aggregate يفرض إيقاف معالجة ذلك الـAggregate فقط حتى تُعالج الرسالة **[Inferred]** |
| الاحتفاظ في Kafka | **[Missing]** — يُحدد في `22-deployment-design.md`؛ الإسقاطات تُعاد بناؤها من مالكي البيانات لا من Kafka (FIT-11) |

## 6. تطور المخططات

- الإصدار الرئيسي السابق لعقد API أو حدث يبقى مدعومًا 6 أشهر على الأقل (QAS-EVO-001)، والتغيير الكاسر بلا إصدار رئيسي جديد ممنوع (FIT-14).
- إضافة حقل اختياري إلى الحمولة تغيير غير كاسر ويُبقي `event_version` **[Inferred]**.
- التغيير الكاسر يرفع `event_version`، والمنتج ينشر الإصدارين طوال فترة الدعم **[Derived]** من القاعدتين أعلاه.

## 7. الأحداث المؤثرة أمنيًا

55 رسالة معلَّمة «يؤثر أمنياً»: 54 حدث مجال تغيّر صلاحية أو تصنيفًا أو عضوية، و`EVT-SEC-VERSION-INCREMENTED` نفسه. مستهلكو الأحداث الـ54 في الكتالوج خدمةُ إصدارات الأمن (التي تنشر `EVT-SEC-VERSION-INCREMENTED` على قناة الأولوية) وذواكرُ قرارات PEP. قرارات ALLOW تُخزَّن مؤقتًا ≤ 60 ثانية بمفتاح يتضمن `security_version`، ورفع الإصدار يبطلها **فورًا** (`08-security/authorization-model.md` §5؛ TD-04).

## 8. الكتالوج

مرتب حسب القناة. «ينتجه» و«المستهلكون» من كتالوجات الأحداث `03-domain/contexts/BC*/events-*.md` (تطابق `x-consumers` في AsyncAPI إلا في صياغة `EVT-SIM-EVALUATION-RECORDED`)؛ الإشارة `(R2)` أو `(R3)` تعني مستهلكًا يأتي في إصدار لاحق.

<!-- BEGIN GENERATED: build_analysis_design.py -->

### ملخص القنوات

| القناة | العنوان | عدد الأحداث |
|---|---|---|
| ai.events | `{cell}.ai.events` | 37 |
| discovery.events | `{cell}.discovery.events` | 7 |
| field.events | `{cell}.field.events` | 17 |
| foundation.events | `{cell}.foundation.events` | 73 |
| governance.events | `{cell}.governance.events` | 43 |
| information.events | `{cell}.information.events` | 106 |
| integration.events | `{cell}.integration.events` | 21 |
| intelligence.events | `{cell}.intelligence.events` | 59 |
| knowledge.events | `{cell}.knowledge.events` | 42 |
| operations.events | `{cell}.operations.events` | 101 |
| readiness.events | `{cell}.readiness.events` | 78 |
| security.versions | `{cell}.security.versions` | 1 |

#### ai.events — `{cell}.ai.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-AIR-CANCELLED | AGG-AI-REQUEST | CMD-AIR-CANCEL | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-COMPLETED | AGG-AI-REQUEST | SYS:output grounded | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-CONTEXT-SEALED | AGG-AI-REQUEST | SYS:context package sealed | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-FAILED | AGG-AI-REQUEST | SYS:error or timeout | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-INSUFFICIENT-EVIDENCE | AGG-AI-REQUEST | SYS:no sufficient evidence retrieved, SYS:output not grounded | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-RECEIVED | AGG-AI-REQUEST | CMD-AIR-SUBMIT | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-REFUSED | AGG-AI-REQUEST | SYS:policy denied | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIR-RETRIEVING | AGG-AI-REQUEST | SYS:retrieval started | — | AI result creator (reviewable operations); Usage accounting; Audit (encrypted prompt/output log) |
| EVT-AIRS-ACCEPTED | AGG-AI-RESULT | CMD-AIRS-ACCEPT | — | Owner contexts (effects on acceptance); Evaluation feedback store |
| EVT-AIRS-PARTIALLY-ACCEPTED | AGG-AI-RESULT | CMD-AIRS-ACCEPT-PARTIALLY | — | Owner contexts (effects on acceptance); Evaluation feedback store |
| EVT-AIRS-PROPOSED | AGG-AI-RESULT | SYS:request COMPLETED for a reviewable operation | — | Owner contexts (effects on acceptance); Evaluation feedback store |
| EVT-AIRS-REJECTED | AGG-AI-RESULT | CMD-AIRS-REJECT | — | Owner contexts (effects on acceptance); Evaluation feedback store |
| EVT-AIRS-REVIEW-STARTED | AGG-AI-RESULT | CMD-AIRS-START-REVIEW | — | Owner contexts (effects on acceptance); Evaluation feedback store |
| EVT-EVS-ACTIVATED | AGG-EVAL-SUITE | CMD-EVS-ACTIVATE | — | Evaluation runner |
| EVT-EVS-DRAFTED | AGG-EVAL-SUITE | CMD-EVS-DRAFT | — | Evaluation runner |
| EVT-EVS-EDITED | AGG-EVAL-SUITE | CMD-EVS-EDIT | — | Evaluation runner |
| EVT-EVS-SUPERSEDED | AGG-EVAL-SUITE | SYS:successor activated | — | Evaluation runner |
| EVT-MDL-APPROVED | AGG-MODEL-VERSION | CMD-MDL-APPROVE | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-DEPRECATED | AGG-MODEL-VERSION | CMD-MDL-DEPRECATE | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-DRIFT-DETECTED | AGG-MODEL-VERSION | SYS:monitoring drift detected | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-EVALUATION-FAILED | AGG-MODEL-VERSION | CMD-MDL-FAIL-EVALUATION | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-EVALUATION-STARTED | AGG-MODEL-VERSION | CMD-MDL-START-EVALUATION | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-PROMOTED | AGG-MODEL-VERSION | CMD-MDL-PROMOTE | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-REGISTERED | AGG-MODEL-VERSION | CMD-MDL-REGISTER | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-REINSTATED | AGG-MODEL-VERSION | CMD-MDL-REINSTATE | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-RETIRED | AGG-MODEL-VERSION | CMD-MDL-RETIRE | — | Inference servers (load/unload); Routing validation |
| EVT-MDL-STAGED | AGG-MODEL-VERSION | CMD-MDL-STAGE | — | Inference servers (load/unload); Routing validation |
| EVT-RTG-ACTIVATED | AGG-AI-ROUTING | CMD-RTG-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Model router; PEP cache |
| EVT-RTG-DISCARDED | AGG-AI-ROUTING | CMD-RTG-DISCARD | — | Model router; PEP cache |
| EVT-RTG-DRAFTED | AGG-AI-ROUTING | CMD-RTG-DRAFT | — | Model router; PEP cache |
| EVT-RTG-EDITED | AGG-AI-ROUTING | CMD-RTG-EDIT | — | Model router; PEP cache |
| EVT-RTG-SUPERSEDED | AGG-AI-ROUTING | SYS:successor activated | — | Model router; PEP cache |
| EVT-TOL-ACTIVATED | AGG-AI-TOOL | CMD-TOL-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway |
| EVT-TOL-DISABLED | AGG-AI-TOOL | CMD-TOL-DISABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Tool gateway |
| EVT-TOL-ENABLED | AGG-AI-TOOL | CMD-TOL-ENABLE | — | Tool gateway |
| EVT-TOL-REGISTERED | AGG-AI-TOOL | CMD-TOL-REGISTER | — | Tool gateway |
| EVT-TOL-RETIRED | AGG-AI-TOOL | CMD-TOL-RETIRE | — | Tool gateway |

#### discovery.events — `{cell}.discovery.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-PRJ-BUILD-STARTED | AGG-PROJECTION-VERSION | CMD-PRJ-CREATE-VERSION | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-DEGRADED | AGG-PROJECTION-VERSION | SYS:lag above threshold | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-FAILED | AGG-PROJECTION-VERSION | SYS:build failed, CMD-PRJ-CANCEL-BUILD | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-PROMOTED | AGG-PROJECTION-VERSION | CMD-PRJ-PROMOTE | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-READY | AGG-PROJECTION-VERSION | SYS:full rebuild reached live checkpoint | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-RECOVERED | AGG-PROJECTION-VERSION | SYS:lag back within target | — | Query router (alias switch); Operations alerting |
| EVT-PRJ-RETIRED | AGG-PROJECTION-VERSION | CMD-PRJ-RETIRE | — | Query router (alias switch); Operations alerting |

#### field.events — `{cell}.field.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-PKG-BUILDING | AGG-PRELOAD-PACKAGE | SYS:build started | — | Package builder; Sync delta (purge list) |
| EVT-PKG-DOWNLOADED | AGG-PRELOAD-PACKAGE | CMD-PKG-CONFIRM-DOWNLOAD | — | Package builder; Sync delta (purge list) |
| EVT-PKG-EXPIRED | AGG-PRELOAD-PACKAGE | SYS:expires_at reached | — | Package builder; Sync delta (purge list) |
| EVT-PKG-READY | AGG-PRELOAD-PACKAGE | SYS:build finished | — | Package builder; Sync delta (purge list) |
| EVT-PKG-REQUESTED | AGG-PRELOAD-PACKAGE | CMD-PKG-REQUEST | — | Package builder; Sync delta (purge list) |
| EVT-PKG-REVOKED | AGG-PRELOAD-PACKAGE | SYS:user security_version changed or device not ACTIVE, CMD-PKG-REVOKE | — | Package builder; Sync delta (purge list) |
| EVT-SCF-ASSIGNED | AGG-SYNC-CONFLICT | CMD-SCF-ASSIGN | — | Reviewer notification; Sync delta (conflict notice to field user) |
| EVT-SCF-DISCARDED | AGG-SYNC-CONFLICT | CMD-SCF-DISCARD | — | Reviewer notification; Sync delta (conflict notice to field user) |
| EVT-SCF-OPENED | AGG-SYNC-CONFLICT | SYS:stale state-changing command | — | Reviewer notification; Sync delta (conflict notice to field user) |
| EVT-SCF-REAPPLIED | AGG-SYNC-CONFLICT | CMD-SCF-REAPPLY | — | Reviewer notification; Sync delta (conflict notice to field user) |
| EVT-SCF-RESOLVED-MANUALLY | AGG-SYNC-CONFLICT | CMD-SCF-RESOLVE-MANUALLY | — | Reviewer notification; Sync delta (conflict notice to field user) |
| EVT-SYN-BATCH-RECEIVED | AGG-SYNC-SESSION | CMD-SYN-UPLOAD-BATCH | — | Owner contexts (commands applied via their APIs); Field telemetry |
| EVT-SYN-COMPLETED | AGG-SYNC-SESSION | SYS:all uploaded commands processed without conflict | — | Owner contexts (commands applied via their APIs); Field telemetry |
| EVT-SYN-COMPLETED-WITH-CONFLICTS | AGG-SYNC-SESSION | SYS:all processed with ≥ 1 sync conflict | — | Owner contexts (commands applied via their APIs); Field telemetry |
| EVT-SYN-FAILED | AGG-SYNC-SESSION | SYS:idle timeout (5 min) or transport loss | — | Owner contexts (commands applied via their APIs); Field telemetry |
| EVT-SYN-OPENED | AGG-SYNC-SESSION | CMD-SYN-OPEN | — | Owner contexts (commands applied via their APIs); Field telemetry |
| EVT-SYN-REJECTED | AGG-SYNC-SESSION | SYS:device LOST or SUSPENDED at handshake | — | Owner contexts (commands applied via their APIs); Field telemetry |

#### foundation.events — `{cell}.foundation.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-AUT-DELEGATED | AGG-AUTHORITY-GRANT | CMD-AUT-DELEGATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-EXPIRED | AGG-AUTHORITY-GRANT | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-GRANT-REJECTED | AGG-AUTHORITY-GRANT | CMD-AUT-REJECT-GRANT | — | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-GRANT-REQUESTED | AGG-AUTHORITY-GRANT | CMD-AUT-GRANT | — | Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-GRANTED | AGG-AUTHORITY-GRANT | CMD-AUT-APPROVE-GRANT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-RESUMED | AGG-AUTHORITY-GRANT | CMD-AUT-RESUME | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-REVOKED | AGG-AUTHORITY-GRANT | CMD-AUT-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-AUT-SUSPENDED | AGG-AUTHORITY-GRANT | CMD-AUT-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Notification (delegates informed on revoke/expire) |
| EVT-CLR-EXPIRED | AGG-CLEARANCE | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-CLR-GRANTED | AGG-CLEARANCE | CMD-CLR-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-CLR-MODIFIED | AGG-CLEARANCE | CMD-CLR-MODIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-CLR-REINSTATED | AGG-CLEARANCE | CMD-CLR-REINSTATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-CLR-REQUESTED | AGG-CLEARANCE | CMD-CLR-GRANT | — | Search/Directory projection (BC01 read model) |
| EVT-CLR-REVOKED | AGG-CLEARANCE | CMD-CLR-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-CLR-SUSPENDED | AGG-CLEARANCE | CMD-CLR-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-DEV-ACTIVATED | AGG-DEVICE | CMD-DEV-CONFIRM | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-ENROLL-REQUESTED | AGG-DEVICE | CMD-DEV-ENROLL | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-KEY-ROTATED | AGG-DEVICE | CMD-DEV-ROTATE-KEY | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-REINSTATED | AGG-DEVICE | CMD-DEV-REINSTATE | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-REPORTED-LOST | AGG-DEVICE | CMD-DEV-REPORT-LOST | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-RETIRED | AGG-DEVICE | CMD-DEV-RETIRE | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-SUSPENDED | AGG-DEVICE | CMD-DEV-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-DEV-WIPED | AGG-DEVICE | SYS:wipe confirmed by device | — | Sync gateway (device registry cache); Preload packages (revoke on LOST/SUSPENDED); Security-version service |
| EVT-HRS-APPROVED | AGG-HR-SYNC-PROPOSAL | CMD-HRS-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Role assignments / users (BC01); Security Officer notification (leave) |
| EVT-HRS-EXPIRED | AGG-HR-SYNC-PROPOSAL | SYS:14 days without decision | — | Role assignments / users (BC01); Security Officer notification (leave) |
| EVT-HRS-PROPOSED | AGG-HR-SYNC-PROPOSAL | SYS:HRIS change received | — | Role assignments / users (BC01); Security Officer notification (leave) |
| EVT-HRS-REJECTED | AGG-HR-SYNC-PROPOSAL | CMD-HRS-REJECT | — | Role assignments / users (BC01); Security Officer notification (leave) |
| EVT-HRS-SUPERSEDED | AGG-HR-SYNC-PROPOSAL | SYS:newer HR change for the same person | — | Role assignments / users (BC01); Security Officer notification (leave) |
| EVT-ORG-CREATED | AGG-ORGANIZATION | CMD-ORG-CREATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-DEACTIVATED | AGG-ORGANIZATION | CMD-ORG-DEACTIVATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-REACTIVATED | AGG-ORGANIZATION | CMD-ORG-REACTIVATE | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-RENAMED | AGG-ORGANIZATION | CMD-ORG-RENAME | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-UNIT-ADDED | AGG-ORGANIZATION | CMD-ORG-ADD-UNIT | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-UNIT-DEACTIVATED | AGG-ORGANIZATION | CMD-ORG-DEACTIVATE-UNIT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-UNIT-MOVED | AGG-ORGANIZATION | CMD-ORG-MOVE-UNIT | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-ORG-UNIT-RENAMED | AGG-ORGANIZATION | CMD-ORG-RENAME-UNIT | — | Search/Directory projection (BC01 read model); All contexts' org-scope read models |
| EVT-PER-DEACTIVATED | AGG-PERSON | CMD-PER-DEACTIVATE | — | Search/Directory projection (BC01 read model) |
| EVT-PER-DETAILS-UPDATED | AGG-PERSON | CMD-PER-UPDATE-DETAILS | — | Search/Directory projection (BC01 read model) |
| EVT-PER-ERASED | AGG-PERSON | CMD-PER-ERASE | — | Search/Directory projection (BC01 read model) |
| EVT-PER-REACTIVATED | AGG-PERSON | CMD-PER-REACTIVATE | — | Search/Directory projection (BC01 read model) |
| EVT-PER-REGISTERED | AGG-PERSON | CMD-PER-REGISTER | — | Search/Directory projection (BC01 read model) |
| EVT-RAS-ASSIGNED | AGG-ROLE-ASSIGNMENT | CMD-RAS-ASSIGN | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-RAS-EXPIRED | AGG-ROLE-ASSIGNMENT | SYS:valid_to reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-RAS-REVOKED | AGG-ROLE-ASSIGNMENT | CMD-RAS-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-ROL-ACTIVATED | AGG-ROLE | CMD-ROL-ACTIVATE | — | Search/Directory projection (BC01 read model) |
| EVT-ROL-DEFINED | AGG-ROLE | CMD-ROL-DEFINE | — | Search/Directory projection (BC01 read model) |
| EVT-ROL-PERMISSIONS-CHANGED | AGG-ROLE | CMD-ROL-SET-PERMISSIONS | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-ROL-RETIRED | AGG-ROLE | CMD-ROL-RETIRE | — | Search/Directory projection (BC01 read model) |
| EVT-SVC-CLOSED | AGG-SERVICE-ACCOUNT | CMD-SVC-CLOSE | — | Search/Directory projection (BC01 read model) |
| EVT-SVC-CREATED | AGG-SERVICE-ACCOUNT | CMD-SVC-CREATE | — | Search/Directory projection (BC01 read model) |
| EVT-SVC-CREDENTIAL-ROTATED | AGG-SERVICE-ACCOUNT | CMD-SVC-ROTATE-CREDENTIAL | — | Search/Directory projection (BC01 read model) |
| EVT-SVC-DISABLED | AGG-SERVICE-ACCOUNT | CMD-SVC-DISABLE | — | Search/Directory projection (BC01 read model) |
| EVT-SVC-ENABLED | AGG-SERVICE-ACCOUNT | CMD-SVC-ENABLE | — | Search/Directory projection (BC01 read model) |
| EVT-TEN-ACTIVATED | AGG-TENANT | CMD-TEN-COMPLETE-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-DECOMMISSION-STARTED | AGG-TENANT | CMD-TEN-START-DECOMMISSION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-DECOMMISSIONED | AGG-TENANT | CMD-TEN-COMPLETE-DECOMMISSION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-MIGRATED | AGG-TENANT | CMD-TEN-COMPLETE-CELL-MIGRATION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-MIGRATION-STARTED | AGG-TENANT | CMD-TEN-START-CELL-MIGRATION | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-PROVISIONING-FAILED | AGG-TENANT | CMD-TEN-FAIL-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-PROVISIONING-STARTED | AGG-TENANT | CMD-TEN-PROVISION, CMD-TEN-RETRY-PROVISIONING | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-QUOTAS-UPDATED | AGG-TENANT | CMD-TEN-UPDATE-QUOTAS | — | Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-REACTIVATED | AGG-TENANT | CMD-TEN-REACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-TEN-SUSPENDED | AGG-TENANT | CMD-TEN-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); Provisioning saga / cell controller |
| EVT-USR-ACTIVATED | AGG-USER | CMD-USR-RECORD-FIRST-SIGN-IN | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-CLOSED | AGG-USER | CMD-USR-CLOSE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-DISABLED | AGG-USER | CMD-USR-DISABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-ENABLED | AGG-USER | CMD-USR-ENABLE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-IDENTITY-LINKED | AGG-USER | CMD-USR-LINK-IDENTITY | — | Search/Directory projection (BC01 read model) |
| EVT-USR-IDENTITY-UNLINKED | AGG-USER | CMD-USR-UNLINK-IDENTITY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-LOCKED | AGG-USER | CMD-USR-LOCK | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-USR-PERSON-LINKED | AGG-USER | CMD-USR-LINK-PERSON | — | Search/Directory projection (BC01 read model) |
| EVT-USR-PROVISIONED | AGG-USER | CMD-USR-PROVISION | — | Search/Directory projection (BC01 read model) |
| EVT-USR-UNLOCKED | AGG-USER | CMD-USR-UNLOCK | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |

#### governance.events — `{cell}.governance.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-CLS-ACTIVATED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-DISCARDED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-DISCARD | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-DRAFTED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-DRAFT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-EDITED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-EDIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-CLS-SUPERSEDED | AGG-CLASSIFICATION-SCHEME | SYS:successor activated | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-DSP-APPROVED | AGG-DISPOSITION-RUN | CMD-DSP-APPROVE | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-CANCELLED | AGG-DISPOSITION-RUN | CMD-DSP-CANCEL | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-COMPLETED | AGG-DISPOSITION-RUN | SYS:all buckets processed | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-COMPLETED-WITH-EXCEPTIONS | AGG-DISPOSITION-RUN | SYS:some buckets failed | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-EXECUTING | AGG-DISPOSITION-RUN | SYS:execution started | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-PLANNED | AGG-DISPOSITION-RUN | SYS:scheduled evaluation (daily) | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-DSP-SUBMITTED | AGG-DISPOSITION-RUN | CMD-DSP-SUBMIT | — | Key manager (bucket key destruction); Owner contexts (purge plaintext caches, projections); Audit |
| EVT-ERS-APPROVED | AGG-ERASURE-REQUEST | CMD-ERS-APPROVE | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-BLOCKED | AGG-ERASURE-REQUEST | SYS:hold matches subject | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-COMPLETED | AGG-ERASURE-REQUEST | SYS:all contexts confirmed | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-EXECUTING | AGG-ERASURE-REQUEST | SYS:execution started | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-RECEIVED | AGG-ERASURE-REQUEST | CMD-ERS-REGISTER | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-REJECTED | AGG-ERASURE-REQUEST | CMD-ERS-REJECT | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-SCOPED | AGG-ERASURE-REQUEST | SYS:subject scope resolved | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-ERS-UNBLOCKED | AGG-ERASURE-REQUEST | SYS:hold released | — | Key manager (subject key destruction); BC01 / BC02 / BC05 (scope + confirmation); Projections (purge) |
| EVT-EXC-ACTIVATED | AGG-SECURITY-EXCEPTION | CMD-EXC-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-EXC-EXPIRED | AGG-SECURITY-EXCEPTION | SYS:end reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-EXC-FIRST-APPROVED | AGG-SECURITY-EXCEPTION | CMD-EXC-APPROVE | — | Search/Directory projection (BC01 read model) |
| EVT-EXC-REJECTED | AGG-SECURITY-EXCEPTION | CMD-EXC-REJECT | — | Search/Directory projection (BC01 read model) |
| EVT-EXC-REQUESTED | AGG-SECURITY-EXCEPTION | CMD-EXC-REQUEST | — | Search/Directory projection (BC01 read model) |
| EVT-EXC-REVOKED | AGG-SECURITY-EXCEPTION | CMD-EXC-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) |
| EVT-LHD-EXTENDED | AGG-LEGAL-HOLD | CMD-LHD-EXTEND | — | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| EVT-LHD-PLACED | AGG-LEGAL-HOLD | CMD-LHD-PLACE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| EVT-LHD-RELEASE-CANCELLED | AGG-LEGAL-HOLD | CMD-LHD-CANCEL-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| EVT-LHD-RELEASE-REQUESTED | AGG-LEGAL-HOLD | CMD-LHD-REQUEST-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| EVT-LHD-RELEASED | AGG-LEGAL-HOLD | CMD-LHD-APPROVE-RELEASE | — | HoldCheck cache (all owners); Disposition planner; Erasure executor |
| EVT-POL-ACTIVATED | AGG-POLICY-SET | SYS:effective_from reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-APPROVED | AGG-POLICY-SET | CMD-POL-APPROVE | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-DRAFTED | AGG-POLICY-SET | CMD-POL-DRAFT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-EDITED | AGG-POLICY-SET | CMD-POL-EDIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-REJECTED | AGG-POLICY-SET | CMD-POL-REJECT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-SUBMITTED | AGG-POLICY-SET | CMD-POL-SUBMIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-POL-SUPERSEDED | AGG-POLICY-SET | SYS:successor activated | — | Search/Directory projection (BC01 read model); PDP bundle distributor |
| EVT-RTS-ACTIVATED | AGG-RETENTION-SCHEDULE | CMD-RTS-ACTIVATE | — | Disposition planner; Key-bucket policy (class period sizing) |
| EVT-RTS-DISCARDED | AGG-RETENTION-SCHEDULE | CMD-RTS-DISCARD | — | Disposition planner; Key-bucket policy (class period sizing) |
| EVT-RTS-DRAFTED | AGG-RETENTION-SCHEDULE | CMD-RTS-DRAFT | — | Disposition planner; Key-bucket policy (class period sizing) |
| EVT-RTS-EDITED | AGG-RETENTION-SCHEDULE | CMD-RTS-EDIT | — | Disposition planner; Key-bucket policy (class period sizing) |
| EVT-RTS-SUPERSEDED | AGG-RETENTION-SCHEDULE | SYS:successor activated | — | Disposition planner; Key-bucket policy (class period sizing) |

#### information.events — `{cell}.information.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-ATT-ERASED | AGG-ATTACHMENT | CMD-ATT-ERASE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Content scanner; Evidence registrar |
| EVT-ATT-EXPIRED | AGG-ATTACHMENT | SYS:upload window 24 h elapsed | — | Content scanner; Evidence registrar |
| EVT-ATT-QUARANTINED | AGG-ATTACHMENT | SYS:scan failed | — | Content scanner; Evidence registrar |
| EVT-ATT-STORED | AGG-ATTACHMENT | SYS:scan passed | — | Content scanner; Evidence registrar |
| EVT-ATT-UPLOAD-INITIATED | AGG-ATTACHMENT | CMD-ATT-INITIATE-UPLOAD | — | Content scanner; Evidence registrar |
| EVT-ATT-UPLOADED | AGG-ATTACHMENT | CMD-ATT-COMPLETE-UPLOAD | — | Content scanner; Evidence registrar |
| EVT-CLM-ASSERTED | AGG-CLAIM | CMD-CLM-ASSERT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CLM-ASSESSED | AGG-CLAIM | CMD-CLM-ASSESS | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CLM-CHANGED | AGG-CLAIM | CMD-CLM-RECORD-CHANGE | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CLM-CORRECTED | AGG-CLAIM | CMD-CLM-CORRECT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CLM-RECLASSIFIED | AGG-CLAIM | CMD-CLM-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CLM-RETRACTED | AGG-CLAIM | CMD-CLM-RETRACT | — | Current-view maintainer (async materialized resolved views); Conflict detector (SLC-04); Situation membership (SLC-06); Search/Graph projections (SLC-05) |
| EVT-CNF-ACCEPTED | AGG-CONFLICT | CMD-CNF-ACCEPT | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-ASSIGNED | AGG-CONFLICT | CMD-CNF-ASSIGN | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-CLAIM-ADDED | AGG-CONFLICT | SYS:incompatible claim joined | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-DETECTED | AGG-CONFLICT | SYS:conflict rule matched | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-RAISED | AGG-CONFLICT | CMD-CNF-RAISE | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-REOPENED | AGG-CONFLICT | CMD-CNF-REOPEN | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-RESOLVED | AGG-CONFLICT | CMD-CNF-RESOLVE | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-REVIEW-STARTED | AGG-CONFLICT | CMD-CNF-START-REVIEW | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CNF-SUPERSEDED | AGG-CONFLICT | SYS:member set no longer conflicting | — | Resolved-view materializer (SLC-05); Analyst notifications; Situation membership (SLC-06: DISPUTED markers) |
| EVT-CPL-ACTIVATED | AGG-COLLECTION-PLAN | CMD-CPL-ACTIVATE | — | Task creation (SLC-03); Notification (units) |
| EVT-CPL-ACTIVITY-ADDED | AGG-COLLECTION-PLAN | CMD-CPL-ADD-ACTIVITY | — | Task creation (SLC-03); Notification (units) |
| EVT-CPL-ACTIVITY-REMOVED | AGG-COLLECTION-PLAN | CMD-CPL-REMOVE-ACTIVITY | — | Task creation (SLC-03); Notification (units) |
| EVT-CPL-CANCELLED | AGG-COLLECTION-PLAN | CMD-CPL-CANCEL | — | Task creation (SLC-03); Notification (units) |
| EVT-CPL-COMPLETED | AGG-COLLECTION-PLAN | SYS:all activity tasks terminal, CMD-CPL-COMPLETE | — | Task creation (SLC-03); Notification (units) |
| EVT-CPL-CREATED | AGG-COLLECTION-PLAN | CMD-CPL-CREATE | — | Task creation (SLC-03); Notification (units) |
| EVT-CRP-ACCEPTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-ACCEPT | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| EVT-CRP-EXPIRED | AGG-CORRELATION-PROPOSAL | SYS:not reviewed within 30 days | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| EVT-CRP-PROPOSED | AGG-CORRELATION-PROPOSAL | SYS:correlation rule score ≥ threshold, CMD-CRP-PROPOSE | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| EVT-CRP-REJECTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-REJECT | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| EVT-CRP-REVIEW-STARTED | AGG-CORRELATION-PROPOSAL | CMD-CRP-START-REVIEW | — | Owner commands on acceptance (BC02 events/relationships, SLC-04 ER); Rule evaluation feedback |
| EVT-CRQ-AMENDED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-AMEND | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-APPROVED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-APPROVE | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-CANCELLED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-CANCEL | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-DRAFTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-DRAFT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-EDITED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-EDIT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-EXPIRED | AGG-COLLECTION-REQUIREMENT | SYS:due passed | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-FULFILMENT-UPDATED | AGG-COLLECTION-REQUIREMENT | SYS:validated observation matched | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-REJECTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-REJECT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-SATISFIED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-MARK-SATISFIED | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRQ-SUBMITTED | AGG-COLLECTION-REQUIREMENT | CMD-CRQ-SUBMIT | — | Matching engine (reload EEIs); Collection board; Search projection (SLC-05); Notification (requester) |
| EVT-CRR-ACTIVATED | AGG-CORRELATION-RULE | CMD-CRR-ACTIVATE | — | Correlation engine |
| EVT-CRR-DEFINED | AGG-CORRELATION-RULE | CMD-CRR-DEFINE | — | Correlation engine |
| EVT-CRR-EDITED | AGG-CORRELATION-RULE | CMD-CRR-EDIT | — | Correlation engine |
| EVT-CRR-RETIRED | AGG-CORRELATION-RULE | CMD-CRR-RETIRE | — | Correlation engine |
| EVT-ENT-RECLASSIFIED | AGG-ENTITY | CMD-ENT-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| EVT-ENT-REGISTERED | AGG-ENTITY | CMD-ENT-REGISTER | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| EVT-ENT-REINSTATED | AGG-ENTITY | CMD-ENT-REINSTATE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| EVT-ENT-RETIRED | AGG-ENTITY | CMD-ENT-RETIRE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| EVT-ENT-TYPE-CHANGED | AGG-ENTITY | CMD-ENT-CHANGE-TYPE | — | ER candidate generator (SLC-04); Search/Graph projections (SLC-05) |
| EVT-ER-MATCH-CONFIRMED | AGG-ER-CASE | CMD-ER-CONFIRM-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-MATCHED | AGG-ER-CASE | CMD-ER-DECIDE-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-NOT-MATCHED | AGG-ER-CASE | CMD-ER-DECIDE-NOT-MATCH, CMD-ER-DECIDE-NOT-MATCH | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-PARKED | AGG-ER-CASE | CMD-ER-PARK | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-PROPOSED | AGG-ER-CASE | SYS:candidate generator score ≥ propose threshold, CMD-ER-PROPOSE | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-RESUMED | AGG-ER-CASE | CMD-ER-RESUME | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-REVIEW-STARTED | AGG-ER-CASE | CMD-ER-START-REVIEW | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-SPLIT | AGG-ER-CASE | CMD-ER-SPLIT | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-SPLIT-REQUESTED | AGG-ER-CASE | CMD-ER-REQUEST-SPLIT | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-ER-WITHDRAWN | AGG-ER-CASE | CMD-ER-WITHDRAW | — | Cluster maintainer (same transaction) → EVT cluster changed; Conflict detector (re-run on cluster change); Search/Graph projections (canonical ids); Situation membership (SLC-06) |
| EVT-EVD-CUSTODY-TRANSFERRED | AGG-EVIDENCE | CMD-EVD-TRANSFER-CUSTODY | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVD-LOCATOR-UPDATED | AGG-EVIDENCE | CMD-EVD-UPDATE-LOCATOR | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVD-RECLASSIFIED | AGG-EVIDENCE | CMD-EVD-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVD-REGISTERED | AGG-EVIDENCE | CMD-EVD-REGISTER | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVD-SEALED | AGG-EVIDENCE | CMD-EVD-SEAL | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVD-WITHDRAWN | AGG-EVIDENCE | CMD-EVD-WITHDRAW | — | Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system identity for linked claims, recomputing verification from remaining SUPPORTS links); Search projection (SLC-05) |
| EVT-EVL-LINKED | AGG-EVIDENCE-LINK | CMD-EVL-LINK | — | Search/Graph projections (SLC-05) |
| EVT-EVL-UNLINKED | AGG-EVIDENCE-LINK | CMD-EVL-UNLINK | — | Search/Graph projections (SLC-05) |
| EVT-EXT-ENDED | AGG-EXTERNAL-ID | CMD-EXT-END | — | Import worker cache |
| EVT-EXT-MAPPED | AGG-EXTERNAL-ID | CMD-EXT-MAP | — | Import worker cache |
| EVT-IMP-CANCELLED | AGG-IMPORT-BATCH | CMD-IMP-CANCEL | — | Import worker; Adapter owner notification |
| EVT-IMP-COMPLETED | AGG-IMPORT-BATCH | SYS:all records applied | — | Import worker; Adapter owner notification |
| EVT-IMP-COMPLETED-WITH-QUARANTINE | AGG-IMPORT-BATCH | SYS:finished with invalid records | — | Import worker; Adapter owner notification |
| EVT-IMP-FAILED | AGG-IMPORT-BATCH | SYS:unrecoverable error | — | Import worker; Adapter owner notification |
| EVT-IMP-PROCESSING-STARTED | AGG-IMPORT-BATCH | SYS:processing started | — | Import worker; Adapter owner notification |
| EVT-IMP-QUARANTINE-ACCEPTED | AGG-IMPORT-BATCH | CMD-IMP-ACCEPT-QUARANTINE | — | Import worker; Adapter owner notification |
| EVT-IMP-RECEIVED | AGG-IMPORT-BATCH | CMD-IMP-SUBMIT | — | Import worker; Adapter owner notification |
| EVT-IMP-REPROCESSING | AGG-IMPORT-BATCH | CMD-IMP-REPROCESS-QUARANTINE | — | Import worker; Adapter owner notification |
| EVT-MRS-ACTIVATED | AGG-MATCH-RULESET | CMD-MRS-ACTIVATE | — | Candidate generator (reloads ruleset) |
| EVT-MRS-DRAFTED | AGG-MATCH-RULESET | CMD-MRS-DRAFT | — | Candidate generator (reloads ruleset) |
| EVT-MRS-EDITED | AGG-MATCH-RULESET | CMD-MRS-EDIT | — | Candidate generator (reloads ruleset) |
| EVT-MRS-SUPERSEDED | AGG-MATCH-RULESET | SYS:successor activated | — | Candidate generator (reloads ruleset) |
| EVT-OBS-AMENDED | AGG-OBSERVATION | CMD-OBS-AMEND | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-OBS-EVIDENCE-ATTACHED | AGG-OBSERVATION | CMD-OBS-ATTACH-EVIDENCE | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-OBS-RECLASSIFIED | AGG-OBSERVATION | CMD-OBS-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-OBS-RECORDED | AGG-OBSERVATION | CMD-OBS-RECORD | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-OBS-REJECTED | AGG-OBSERVATION | CMD-OBS-REJECT | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-OBS-VALIDATED | AGG-OBSERVATION | CMD-OBS-VALIDATE | — | Derived-claim processor (position summarization); Situation membership (SLC-06); Search projection (SLC-05) |
| EVT-REL-RECLASSIFIED | AGG-RELATIONSHIP | CMD-REL-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| EVT-REL-REGISTERED | AGG-RELATIONSHIP | CMD-REL-REGISTER | — | Search/Graph projections (SLC-05) |
| EVT-REL-REINSTATED | AGG-RELATIONSHIP | CMD-REL-REINSTATE | — | Search/Graph projections (SLC-05) |
| EVT-REL-RETIRED | AGG-RELATIONSHIP | CMD-REL-RETIRE | — | Search/Graph projections (SLC-05) |
| EVT-RWE-RECLASSIFIED | AGG-REALWORLD-EVENT | CMD-RWE-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| EVT-RWE-REGISTERED | AGG-REALWORLD-EVENT | CMD-RWE-REGISTER | — | Search/Graph projections (SLC-05) |
| EVT-RWE-REINSTATED | AGG-REALWORLD-EVENT | CMD-RWE-REINSTATE | — | Search/Graph projections (SLC-05) |
| EVT-RWE-RETIRED | AGG-REALWORLD-EVENT | CMD-RWE-RETIRE | — | Search/Graph projections (SLC-05) |
| EVT-RWE-TYPE-CHANGED | AGG-REALWORLD-EVENT | CMD-RWE-CHANGE-TYPE | — | Search/Graph projections (SLC-05) |
| EVT-SRC-PROFILE-UPDATED | AGG-SOURCE | CMD-SRC-UPDATE-PROFILE | — | Search/Graph projections (SLC-05) |
| EVT-SRC-PROTECTION-CHANGED | AGG-SOURCE | CMD-SRC-SET-PROTECTION | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| EVT-SRC-RECLASSIFIED | AGG-SOURCE | CMD-SRC-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Graph projections (SLC-05) |
| EVT-SRC-REGISTERED | AGG-SOURCE | CMD-SRC-REGISTER | — | Search/Graph projections (SLC-05) |
| EVT-SRC-REINSTATED | AGG-SOURCE | CMD-SRC-REINSTATE | — | Search/Graph projections (SLC-05) |
| EVT-SRC-RELIABILITY-RATED | AGG-SOURCE | CMD-SRC-RATE-RELIABILITY | — | Search/Graph projections (SLC-05) |
| EVT-SRC-RETIRED | AGG-SOURCE | CMD-SRC-RETIRE | — | Search/Graph projections (SLC-05) |
| EVT-SRC-SUSPENDED | AGG-SOURCE | CMD-SRC-SUSPEND | — | Search/Graph projections (SLC-05) |

#### integration.events — `{cell}.integration.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-ADP-ACTIVATED | AGG-ADAPTER | CMD-ADP-ACTIVATE | — | Import worker |
| EVT-ADP-MAPPING-UPDATED | AGG-ADAPTER | CMD-ADP-UPDATE-MAPPING | — | Import worker |
| EVT-ADP-REGISTERED | AGG-ADAPTER | CMD-ADP-REGISTER | — | Import worker |
| EVT-ADP-RESUMED | AGG-ADAPTER | CMD-ADP-RESUME | — | Import worker |
| EVT-ADP-RETIRED | AGG-ADAPTER | CMD-ADP-RETIRE | — | Import worker |
| EVT-ADP-SUSPENDED | AGG-ADAPTER | CMD-ADP-SUSPEND | — | Import worker |
| EVT-CON-ACTIVATED | AGG-INTEGRATION-CONNECTION | CMD-CON-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-DEGRADED | AGG-INTEGRATION-CONNECTION | SYS:health checks failing 5 min | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-RECOVERED | AGG-INTEGRATION-CONNECTION | SYS:health restored | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-REGISTERED | AGG-INTEGRATION-CONNECTION | CMD-CON-REGISTER | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-RESUMED | AGG-INTEGRATION-CONNECTION | CMD-CON-RESUME | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-RETIRED | AGG-INTEGRATION-CONNECTION | CMD-CON-RETIRE | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-SUSPENDED | AGG-INTEGRATION-CONNECTION | CMD-CON-SUSPEND | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-TEST-FAILED | AGG-INTEGRATION-CONNECTION | CMD-CON-FAIL-TEST | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-CON-TEST-STARTED | AGG-INTEGRATION-CONNECTION | CMD-CON-TEST | — | Egress gateway (allow-list); Adapters (bind/unbind); Operations alerting |
| EVT-SNS-ACTIVATED | AGG-SENSOR-STREAM | CMD-SNS-ACTIVATE | — | Ingestion workers (SLC-02 batches); Operations alerting |
| EVT-SNS-PAUSED | AGG-SENSOR-STREAM | CMD-SNS-PAUSE | — | Ingestion workers (SLC-02 batches); Operations alerting |
| EVT-SNS-QUALITY-RULES-SET | AGG-SENSOR-STREAM | CMD-SNS-SET-QUALITY-RULES | — | Ingestion workers (SLC-02 batches); Operations alerting |
| EVT-SNS-REGISTERED | AGG-SENSOR-STREAM | CMD-SNS-REGISTER | — | Ingestion workers (SLC-02 batches); Operations alerting |
| EVT-SNS-RETIRED | AGG-SENSOR-STREAM | CMD-SNS-RETIRE | — | Ingestion workers (SLC-02 batches); Operations alerting |
| EVT-SNS-STALE | AGG-SENSOR-STREAM | SYS:no data beyond stale-after | — | Ingestion workers (SLC-02 batches); Operations alerting |

#### intelligence.events — `{cell}.intelligence.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-ACS-ASSUMPTION-ADDED | AGG-ANALYSIS-CASE | CMD-ACS-ADD-ASSUMPTION | — | Search projection (SLC-05) |
| EVT-ACS-ASSUMPTION-RETIRED | AGG-ANALYSIS-CASE | CMD-ACS-RETIRE-ASSUMPTION | — | Search projection (SLC-05) |
| EVT-ACS-CANCELLED | AGG-ANALYSIS-CASE | CMD-ACS-CANCEL | — | Search projection (SLC-05) |
| EVT-ACS-CLOSED | AGG-ANALYSIS-CASE | CMD-ACS-CLOSE | — | Search projection (SLC-05) |
| EVT-ACS-CREATED | AGG-ANALYSIS-CASE | CMD-ACS-CREATE | — | Search projection (SLC-05) |
| EVT-ACS-DEFINED | AGG-ANALYSIS-CASE | CMD-ACS-DEFINE | — | Search projection (SLC-05) |
| EVT-ACS-EVIDENCE-DESELECTED | AGG-ANALYSIS-CASE | CMD-ACS-DESELECT-EVIDENCE | — | Search projection (SLC-05) |
| EVT-ACS-EVIDENCE-SELECTED | AGG-ANALYSIS-CASE | CMD-ACS-SELECT-EVIDENCE | — | Search projection (SLC-05) |
| EVT-ACS-HYPOTHESIS-ADDED | AGG-ANALYSIS-CASE | CMD-ACS-ADD-HYPOTHESIS | — | Search projection (SLC-05) |
| EVT-ACS-HYPOTHESIS-UPDATED | AGG-ANALYSIS-CASE | CMD-ACS-UPDATE-HYPOTHESIS | — | Search projection (SLC-05) |
| EVT-ACS-OPENED | AGG-ANALYSIS-CASE | CMD-ACS-OPEN | — | Search projection (SLC-05) |
| EVT-ACS-RECLASSIFIED | AGG-ANALYSIS-CASE | CMD-ACS-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search projection (SLC-05) |
| EVT-ACS-REOPENED | AGG-ANALYSIS-CASE | CMD-ACS-REOPEN | — | Search projection (SLC-05) |
| EVT-ACS-SCENARIO-DEFINED | AGG-ANALYSIS-CASE | CMD-ACS-DEFINE-SCENARIO | — | Search projection (SLC-05) |
| EVT-ALR-ACKNOWLEDGED | AGG-ALERT | CMD-ALR-ACKNOWLEDGE | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-ALR-DISMISSED | AGG-ALERT | CMD-ALR-DISMISS | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-ALR-ESCALATED | AGG-ALERT | SYS:unacknowledged beyond escalation delay | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-ALR-RAISED | AGG-ALERT | SYS:rule condition met | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-ALR-REPEATED | AGG-ALERT | SYS:condition met again within dedupe window | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-ALR-RESOLVED | AGG-ALERT | CMD-ALR-RESOLVE, SYS:condition cleared and rule auto_resolve | — | Notification fan-out (recipients = cleared subscribers); COP (alerts layer); Escalation scheduler |
| EVT-AMT-ACTIVATED | AGG-ANALYSIS-METHOD | CMD-AMT-ACTIVATE | — | Job scheduler (image allow-list) |
| EVT-AMT-DEPRECATED | AGG-ANALYSIS-METHOD | CMD-AMT-DEPRECATE | — | Job scheduler (image allow-list) |
| EVT-AMT-REGISTERED | AGG-ANALYSIS-METHOD | CMD-AMT-REGISTER | — | Job scheduler (image allow-list) |
| EVT-AMT-RETIRED | AGG-ANALYSIS-METHOD | CMD-AMT-RETIRE | — | Job scheduler (image allow-list) |
| EVT-ARL-ACTIVATED | AGG-ALERT-RULE | CMD-ARL-ACTIVATE | — | Alert evaluator (reload rules) |
| EVT-ARL-DEFINED | AGG-ALERT-RULE | CMD-ARL-DEFINE | — | Alert evaluator (reload rules) |
| EVT-ARL-DISABLED | AGG-ALERT-RULE | CMD-ARL-DISABLE | — | Alert evaluator (reload rules) |
| EVT-ARL-EDITED | AGG-ALERT-RULE | CMD-ARL-EDIT | — | Alert evaluator (reload rules) |
| EVT-ARL-ENABLED | AGG-ALERT-RULE | CMD-ARL-ENABLE | — | Alert evaluator (reload rules) |
| EVT-ARL-RETIRED | AGG-ALERT-RULE | CMD-ARL-RETIRE | — | Alert evaluator (reload rules) |
| EVT-ASM-DISCARDED | AGG-ASSESSMENT | CMD-ASM-DISCARD | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-DRAFTED | AGG-ASSESSMENT | CMD-ASM-DRAFT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-EDITED | AGG-ASSESSMENT | CMD-ASM-EDIT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-PUBLISHED | AGG-ASSESSMENT | CMD-ASM-PUBLISH | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-RETURNED | AGG-ASSESSMENT | CMD-ASM-RETURN | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-SUBMITTED | AGG-ASSESSMENT | CMD-ASM-SUBMIT | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-SUPERSEDED | AGG-ASSESSMENT | SYS:newer version published | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-ASM-WITHDRAWN | AGG-ASSESSMENT | CMD-ASM-WITHDRAW | — | Decision requests (SLC-08: pinned references); Situation membership (assessment layer); Search projection (SLC-05); Products (SLC-12, R2) |
| EVT-CAP-CANCELLED | AGG-CAP-MESSAGE | CMD-CAP-CANCEL | — | CAP gateway; Audit |
| EVT-CAP-FAILED | AGG-CAP-MESSAGE | SYS:delivery failed after retries | — | CAP gateway; Audit |
| EVT-CAP-PREPARED | AGG-CAP-MESSAGE | CMD-CAP-PREPARE | — | CAP gateway; Audit |
| EVT-CAP-RETRY | AGG-CAP-MESSAGE | CMD-CAP-RETRY | — | CAP gateway; Audit |
| EVT-CAP-SENT | AGG-CAP-MESSAGE | CMD-CAP-RELEASE | — | CAP gateway; Audit |
| EVT-FND-ACCEPTED | AGG-FINDING | CMD-FND-ACCEPT | — | Assessment review flags |
| EVT-FND-EDITED | AGG-FINDING | CMD-FND-EDIT | — | Assessment review flags |
| EVT-FND-RECORDED | AGG-FINDING | CMD-FND-RECORD | — | Assessment review flags |
| EVT-FND-WITHDRAWN | AGG-FINDING | CMD-FND-WITHDRAW | — | Assessment review flags |
| EVT-RUN-CANCELLED | AGG-ANALYSIS-RUN | CMD-RUN-CANCEL | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-FAILED | AGG-ANALYSIS-RUN | SYS:error or timeout | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-QUEUED | AGG-ANALYSIS-RUN | CMD-RUN-SUBMIT, CMD-RUN-REPRODUCE | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-STARTED | AGG-ANALYSIS-RUN | SYS:worker lease acquired | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-RUN-SUCCEEDED | AGG-ANALYSIS-RUN | SYS:completed | — | Job scheduler / compute workers; Lineage writer (BC02 LineageRecord); Case owner notification |
| EVT-SIT-ACTIVATED | AGG-SITUATION | CMD-SIT-ACTIVATE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-CLOSED | AGG-SITUATION | CMD-SIT-CLOSE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-CREATED | AGG-SITUATION | CMD-SIT-CREATE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-DEFINITION-CHANGED | AGG-SITUATION | CMD-SIT-EDIT-DEFINITION | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-PAUSED | AGG-SITUATION | CMD-SIT-PAUSE | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-RECLASSIFIED | AGG-SITUATION | CMD-SIT-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |
| EVT-SIT-RESUMED | AGG-SITUATION | CMD-SIT-RESUME | — | Membership evaluator (reload definition); Alert evaluator; Tile cache invalidation; Search projection (SLC-05) |

#### knowledge.events — `{cell}.knowledge.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-ARC-ARCHIVED | AGG-ARCHIVE-PACKAGE | SYS:package validated | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-DISPOSED | AGG-ARCHIVE-PACKAGE | SYS:disposition DESTROY executed for the package bucket | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-FORMAT-MIGRATED | AGG-ARCHIVE-PACKAGE | CMD-ARC-MIGRATE-FORMAT | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-INGEST-FAILED | AGG-ARCHIVE-PACKAGE | SYS:validation failed | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-INGEST-STARTED | AGG-ARCHIVE-PACKAGE | SYS:disposition action ARCHIVE for a bucket or record set, CMD-ARC-RETRY-INGEST | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-INTEGRITY-FAILED | AGG-ARCHIVE-PACKAGE | SYS:integrity check failed | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-REPAIRED | AGG-ARCHIVE-PACKAGE | CMD-ARC-REPAIR | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-ARC-TRANSFERRED | AGG-ARCHIVE-PACKAGE | CMD-ARC-TRANSFER | — | Archive catalogue; Disposition (SLC-12a); Audit |
| EVT-DST-CANCELLED | AGG-DISTRIBUTION | CMD-DST-CANCEL | — | Notification (recipients); Audit |
| EVT-DST-COMPLETED | AGG-DISTRIBUTION | SYS:all recipients authorized and delivered | — | Notification (recipients); Audit |
| EVT-DST-COMPLETED-WITH-EXCLUSIONS | AGG-DISTRIBUTION | SYS:some recipients not authorized | — | Notification (recipients); Audit |
| EVT-DST-STARTED | AGG-DISTRIBUTION | CMD-DST-DISTRIBUTE | — | Notification (recipients); Audit |
| EVT-KNO-DISCARDED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-DISCARD | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-DRAFTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-DRAFT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-EDITED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-EDIT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-PUBLISHED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-PUBLISH | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-REJECTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-REJECT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-RETIRED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RETIRE | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-RETURNED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RETURN | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-REUSED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-RECORD-REUSE | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-SUBMITTED | AGG-KNOWLEDGE-OBJECT | CMD-KNO-SUBMIT | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-KNO-SUPERSEDED | AGG-KNOWLEDGE-OBJECT | SYS:newer version published | — | Knowledge suggestion index; Search projection (SLC-05); Business telemetry (OUT-06) |
| EVT-PRD-APPROVED | AGG-PRODUCT | CMD-PRD-APPROVE | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-CREATED | AGG-PRODUCT | CMD-PRD-CREATE | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-DISCARDED | AGG-PRODUCT | CMD-PRD-DISCARD | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-GENERATED | AGG-PRODUCT | SYS:generation succeeded | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-GENERATION-FAILED | AGG-PRODUCT | SYS:generation failed | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-GENERATION-STARTED | AGG-PRODUCT | CMD-PRD-GENERATE | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-NARRATIVE-EDITED | AGG-PRODUCT | CMD-PRD-EDIT-NARRATIVE | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-RETURNED | AGG-PRODUCT | CMD-PRD-RETURN | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-SUBMITTED | AGG-PRODUCT | CMD-PRD-SUBMIT | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-SUPERSEDED | AGG-PRODUCT | SYS:newer version approved | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PRD-WITHDRAWN | AGG-PRODUCT | CMD-PRD-WITHDRAW | — | Distribution; Search projection (SLC-05); Notification (reviewers) |
| EVT-PTM-ACTIVATED | AGG-PRODUCT-TEMPLATE | CMD-PTM-ACTIVATE | — | Product generator |
| EVT-PTM-DEFINED | AGG-PRODUCT-TEMPLATE | CMD-PTM-DEFINE | — | Product generator |
| EVT-PTM-EDITED | AGG-PRODUCT-TEMPLATE | CMD-PTM-EDIT | — | Product generator |
| EVT-PTM-RETIRED | AGG-PRODUCT-TEMPLATE | CMD-PTM-RETIRE | — | Product generator |
| EVT-REC-CANCELLED | AGG-RECONSTRUCTION | CMD-REC-CANCEL | — | Requester notification; Audit |
| EVT-REC-COMPLETED | AGG-RECONSTRUCTION | SYS:completed | — | Requester notification; Audit |
| EVT-REC-FAILED | AGG-RECONSTRUCTION | SYS:failed | — | Requester notification; Audit |
| EVT-REC-REQUESTED | AGG-RECONSTRUCTION | CMD-REC-REQUEST | — | Requester notification; Audit |
| EVT-REC-STARTED | AGG-RECONSTRUCTION | SYS:worker started | — | Requester notification; Audit |

#### operations.events — `{cell}.operations.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-CRD-ACTIVATED | AGG-COORDINATION-CASE | CMD-CRD-ACTIVATE | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-CANCELLED | AGG-COORDINATION-CASE | CMD-CRD-CANCEL | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-CLOSED | AGG-COORDINATION-CASE | CMD-CRD-CLOSE | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-DECISION-RECORDED | AGG-COORDINATION-CASE | SYS:linked decision recorded | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-DECISION-REQUESTED | AGG-COORDINATION-CASE | CMD-CRD-REQUEST-DECISION | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-OPENED | AGG-COORDINATION-CASE | CMD-CRD-OPEN | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-PARTICIPANT-ADDED | AGG-COORDINATION-CASE | CMD-CRD-ADD-PARTICIPANT | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-PARTICIPANT-REMOVED | AGG-COORDINATION-CASE | CMD-CRD-REMOVE-PARTICIPANT | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-RESPONSIBILITY-ASSIGNED | AGG-COORDINATION-CASE | CMD-CRD-ASSIGN-RESPONSIBILITY | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-CRD-RESPONSIBILITY-UPDATED | AGG-COORDINATION-CASE | CMD-CRD-UPDATE-RESPONSIBILITY | — | Decision requests (SLC-08); Notification (participants); Search projection (SLC-05) |
| EVT-DEC-ANNULLED | AGG-DECISION | CMD-DEC-ANNUL | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports |
| EVT-DEC-RECORDED | AGG-DECISION | CMD-DEC-RECORD | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports |
| EVT-DEC-SUPERSEDED | AGG-DECISION | SYS:superseding decision recorded | — | Decision request (DECIDED); Plans implementing it (review flag on supersede/annul); Search projection (SLC-05); Audit reports |
| EVT-DRQ-CITED | AGG-DECISION-REQUEST | CMD-DRQ-CITE | — | Search projection (SLC-05) |
| EVT-DRQ-CREATED | AGG-DECISION-REQUEST | CMD-DRQ-CREATE | — | Search projection (SLC-05) |
| EVT-DRQ-DECIDED | AGG-DECISION-REQUEST | SYS:decision recorded for this request | — | Search projection (SLC-05) |
| EVT-DRQ-ESCALATED | AGG-DECISION-REQUEST | SYS:deadline passed | — | Search projection (SLC-05) |
| EVT-DRQ-OPENED | AGG-DECISION-REQUEST | CMD-DRQ-OPEN | — | Search projection (SLC-05) |
| EVT-DRQ-OPTION-ADDED | AGG-DECISION-REQUEST | CMD-DRQ-ADD-OPTION | — | Search projection (SLC-05) |
| EVT-DRQ-WITHDRAWN | AGG-DECISION-REQUEST | CMD-DRQ-WITHDRAW | — | Search projection (SLC-05) |
| EVT-INC-ASSESSED | AGG-INCIDENT | CMD-INC-ASSESS | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-CANCELLED | AGG-INCIDENT | CMD-INC-CANCEL | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-CLOSED | AGG-INCIDENT | CMD-INC-CLOSE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-CONTAINED | AGG-INCIDENT | CMD-INC-CONTAIN | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-CONTINGENCY-ACTIVATED | AGG-INCIDENT | CMD-INC-ACTIVATE-CONTINGENCY | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-DE-ESCALATED | AGG-INCIDENT | CMD-INC-DE-ESCALATE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-ESCALATED | AGG-INCIDENT | CMD-INC-ESCALATE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-REPORTED | AGG-INCIDENT | CMD-INC-REPORT | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-RESOLVED | AGG-INCIDENT | CMD-INC-RESOLVE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-RESPONSE-DISPATCHED | AGG-INCIDENT | CMD-INC-DISPATCH-RESPONSE | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-INC-SLA-BREACHED | AGG-INCIDENT | SYS:response SLA elapsed without dispatch | — | Search projection (SLC-05); Notification (SLC-06); اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5) |
| EVT-NTF-EXPIRED | AGG-NOTIFICATION | SYS:TTL (30 d) elapsed | — | Push gateway; In-app inbox |
| EVT-NTF-FAILED | AGG-NOTIFICATION | SYS:delivery failed after retries | — | Push gateway; In-app inbox |
| EVT-NTF-QUEUED | AGG-NOTIFICATION | SYS:notifiable event for recipient | — | Push gateway; In-app inbox |
| EVT-NTF-READ | AGG-NOTIFICATION | CMD-NTF-MARK-READ | — | Push gateway; In-app inbox |
| EVT-NTF-SENT | AGG-NOTIFICATION | SYS:delivered to channel | — | Push gateway; In-app inbox |
| EVT-NTF-WITHHELD | AGG-NOTIFICATION | SYS:recipient no longer authorized at delivery | — | Push gateway; In-app inbox |
| EVT-OUT-MEASURED | AGG-OUTCOME-TRACKER | CMD-OUT-RECORD | — | Plan progress view; Business telemetry (OUT-05) |
| EVT-OUT-MEASUREMENT-CORRECTED | AGG-OUTCOME-TRACKER | CMD-OUT-CORRECT | — | Plan progress view; Business telemetry (OUT-05) |
| EVT-OUT-TARGET-CHANGED | AGG-OUTCOME-TRACKER | SYS:target changed by new baseline | — | Plan progress view; Business telemetry (OUT-05) |
| EVT-OUT-TRACKER-CLOSED | AGG-OUTCOME-TRACKER | SYS:plan closed or cancelled | — | Plan progress view; Business telemetry (OUT-05) |
| EVT-OUT-TRACKER-CREATED | AGG-OUTCOME-TRACKER | SYS:outcome baselined | — | Plan progress view; Business telemetry (OUT-05) |
| EVT-PLN-ACTIVATED | AGG-PLAN | SYS:first version baselined | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-CANCELLED | AGG-PLAN | CMD-PLN-CANCEL | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-CLOSED | AGG-PLAN | CMD-PLN-CLOSE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-COMPLETED | AGG-PLAN | CMD-PLN-COMPLETE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-CREATED | AGG-PLAN | CMD-PLN-CREATE | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-RECLASSIFIED | AGG-PLAN | CMD-PLN-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-RESUMED | AGG-PLAN | CMD-PLN-RESUME | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-REVIEW-FLAGGED | AGG-PLAN | SYS:implemented decision annulled or superseded | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLN-SUSPENDED | AGG-PLAN | CMD-PLN-SUSPEND | — | Task synchronizer (suspend/cancel cascades); Outcome trackers (close); Notification (owners, assignees) |
| EVT-PLV-BASELINED | AGG-PLAN-VERSION | CMD-PLV-APPROVE | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-DISCARDED | AGG-PLAN-VERSION | CMD-PLV-DISCARD | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-DRAFTED | AGG-PLAN-VERSION | CMD-PLV-DRAFT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-EDITED | AGG-PLAN-VERSION | CMD-PLV-EDIT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-MINOR-AMENDED | AGG-PLAN-VERSION | CMD-PLV-AMEND-MINOR | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-REJECTED | AGG-PLAN-VERSION | CMD-PLV-REJECT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-RETURNED | AGG-PLAN-VERSION | CMD-PLV-RETURN | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-SUBMITTED | AGG-PLAN-VERSION | CMD-PLV-SUBMIT | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-PLV-SUPERSEDED | AGG-PLAN-VERSION | SYS:newer version baselined | — | Task synchronizer (SPEC-PLAN §3); Outcome trackers; Plan identity (activation); Search projection (SLC-05) |
| EVT-RIS-ASSESSED | AGG-RISK | CMD-RIS-ASSESS | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-RIS-CLOSED | AGG-RISK | CMD-RIS-CLOSE | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-RIS-IDENTIFIED | AGG-RISK | CMD-RIS-IDENTIFY | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-RIS-MATERIALIZATION-LINKED | AGG-RISK | SYS:incident references this risk as risk_ref | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-RIS-REASSESSED | AGG-RISK | CMD-RIS-REASSESS | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-RIS-TREATMENT-PLANNED | AGG-RISK | CMD-RIS-PLAN-TREATMENT | — | Search projection (SLC-05); Coordination cases (SLC-15، عند ارتباط النطاق) |
| EVT-SUB-CHANNELS-UPDATED | AGG-SUBSCRIPTION | CMD-SUB-UPDATE-CHANNELS | — | Notification fan-out index |
| EVT-SUB-ENDED | AGG-SUBSCRIPTION | CMD-SUB-UNSUBSCRIBE, SYS:subscriber lost visibility of target | — | Notification fan-out index |
| EVT-SUB-PAUSED | AGG-SUBSCRIPTION | CMD-SUB-PAUSE | — | Notification fan-out index |
| EVT-SUB-RESUMED | AGG-SUBSCRIPTION | CMD-SUB-RESUME | — | Notification fan-out index |
| EVT-SUB-SUBSCRIBED | AGG-SUBSCRIPTION | CMD-SUB-SUBSCRIBE | — | Notification fan-out index |
| EVT-TASK-ACCEPTED | AGG-TASK | CMD-TASK-ACCEPT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-APPROVED | AGG-TASK | CMD-TASK-APPROVE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-ASSIGNED | AGG-TASK | CMD-TASK-ASSIGN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-BLOCKED | AGG-TASK | CMD-TASK-BLOCK | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-CANCELLED | AGG-TASK | CMD-TASK-CANCEL | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-CLOSED | AGG-TASK | CMD-TASK-CLOSE, SYS:follow-up window (7 d) elapsed without open follow-ups | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-COMPLETED | AGG-TASK | SYS:all completion criteria satisfied, CMD-TASK-COMPLETE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-CREATED | AGG-TASK | CMD-TASK-CREATE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-DECLINED | AGG-TASK | CMD-TASK-DECLINE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-DUE-CHANGED | AGG-TASK | CMD-TASK-SET-DUE | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-EDITED | AGG-TASK | CMD-TASK-EDIT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-ESCALATED | AGG-TASK | CMD-TASK-ESCALATE, SYS:due passed (escalation policy) | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-EXPIRED | AGG-TASK | SYS:due passed and task type expires_on_due | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-READIED | AGG-TASK | CMD-TASK-MARK-READY | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-REASSIGNED | AGG-TASK | CMD-TASK-REASSIGN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-RECLASSIFIED | AGG-TASK | CMD-TASK-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-REJECTED | AGG-TASK | CMD-TASK-REJECT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-RESULT-ITEM-ADDED | AGG-TASK | CMD-TASK-ADD-RESULT-ITEM | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-RESUMED | AGG-TASK | CMD-TASK-RESUME | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-RETURNED-FOR-REWORK | AGG-TASK | CMD-TASK-RETURN | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-REVIEW-STARTED | AGG-TASK | CMD-TASK-START-REVIEW | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-STARTED | AGG-TASK | CMD-TASK-START | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-SUBMITTED | AGG-TASK | CMD-TASK-SUBMIT | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-SUPERSEDED | AGG-TASK | SYS:plan version baselined without this task | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-SUSPENDED | AGG-TASK | CMD-TASK-SUSPEND | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TASK-UNSUSPENDED | AGG-TASK | CMD-TASK-UNSUSPEND | — | Notification service (SLC-06); Plan progress (SLC-08); Outcome measurement (SLC-08); Search projection (SLC-05); Resources release (SLC-09, R2) |
| EVT-TTY-ACTIVATED | AGG-TASK-TYPE | CMD-TTY-ACTIVATE | — | Task command handler cache |
| EVT-TTY-DEFINED | AGG-TASK-TYPE | CMD-TTY-DEFINE | — | Task command handler cache |
| EVT-TTY-EDITED | AGG-TASK-TYPE | CMD-TTY-EDIT | — | Task command handler cache |
| EVT-TTY-RETIRED | AGG-TASK-TYPE | CMD-TTY-RETIRE | — | Task command handler cache |

#### readiness.events — `{cell}.readiness.events`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-ALC-APPROVAL-REQUIRED | AGG-ALLOCATION | SYS:checks passed, policy requires approval | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-COMMITTED | AGG-ALLOCATION | SYS:all checks passed, CMD-ALC-APPROVE | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-CONSUMED | AGG-ALLOCATION | CMD-ALC-RECORD-CONSUMPTION | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-PREEMPTED | AGG-ALLOCATION | CMD-ALC-PREEMPT | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-REJECTED | AGG-ALLOCATION | SYS:a check failed, CMD-ALC-REJECT, SYS:provisional hold (1 h) elapsed | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-RELEASED | AGG-ALLOCATION | CMD-ALC-RELEASE, SYS:linked task terminal | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ALC-REQUESTED | AGG-ALLOCATION | CMD-ALC-REQUEST | — | Capacity ledger; Task (SLC-03) notifications; Plan progress (SLC-08) |
| EVT-ASG-ASSIGNED | AGG-ASSET-ASSIGNMENT | CMD-ASG-ASSIGN | — | Availability view; Task (SLC-03) |
| EVT-ASG-CANCELLED | AGG-ASSET-ASSIGNMENT | CMD-ASG-CANCEL | — | Availability view; Task (SLC-03) |
| EVT-ASG-RETURNED | AGG-ASSET-ASSIGNMENT | CMD-ASG-RETURN, SYS:linked task terminal | — | Availability view; Task (SLC-03) |
| EVT-AST-CERTIFICATION-SET | AGG-ASSET | CMD-AST-SET-CERTIFICATION | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-CONDITION-UPDATED | AGG-ASSET | CMD-AST-UPDATE-CONDITION | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-CUSTODY-TRANSFERRED | AGG-ASSET | CMD-AST-TRANSFER-CUSTODY | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-DISPOSED | AGG-ASSET | CMD-AST-DISPOSE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-MAINTENANCE-STARTED | AGG-ASSET | CMD-AST-START-MAINTENANCE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-RECLASSIFIED | AGG-ASSET | CMD-AST-RECLASSIFY | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-RECOVERED | AGG-ASSET | CMD-AST-RECOVER | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-REGISTERED | AGG-ASSET | CMD-AST-REGISTER | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-REPORTED-LOST | AGG-ASSET | CMD-AST-REPORT-LOST | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-RETURNED-TO-SERVICE | AGG-ASSET | CMD-AST-RETURN-TO-SERVICE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-AST-UNSERVICEABLE | AGG-ASSET | CMD-AST-MARK-UNSERVICEABLE, CMD-AST-FAIL-MAINTENANCE | — | Availability view; Situation assets layer (SLC-06); Search projection (SLC-05); Reservations/assignments (flags) |
| EVT-EXR-ABORTED | AGG-EXERCISE | SYS:linked simulation aborted | — | Search projection (SLC-05) |
| EVT-EXR-CANCELLED | AGG-EXERCISE | CMD-EXR-CANCEL | — | Search projection (SLC-05) |
| EVT-EXR-COMPLETED | AGG-EXERCISE | SYS:linked simulation completed | — | Search projection (SLC-05) |
| EVT-EXR-PLANNED | AGG-EXERCISE | CMD-EXR-PLAN | — | Search projection (SLC-05) |
| EVT-EXR-SCHEDULED | AGG-EXERCISE | CMD-EXR-SCHEDULE | — | Search projection (SLC-05) |
| EVT-EXR-STARTED | AGG-EXERCISE | CMD-EXR-START | — | Simulation (creation trigger); Search projection (SLC-05) |
| EVT-LGR-APPROVED | AGG-LOGISTICS-REQUEST | SYS:linked allocation committed, SYS:linked allocation committed | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-CANCELLED | AGG-LOGISTICS-REQUEST | CMD-LGR-CANCEL | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-DISPATCHED | AGG-LOGISTICS-REQUEST | CMD-LGR-DISPATCH | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-FULFILLED | AGG-LOGISTICS-REQUEST | SYS:linked shipment delivered in full | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-PARTIALLY-FULFILLED | AGG-LOGISTICS-REQUEST | SYS:linked shipment resolved short | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-PENDING-APPROVAL | AGG-LOGISTICS-REQUEST | SYS:linked allocation requires approval | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-REJECTED | AGG-LOGISTICS-REQUEST | SYS:linked allocation rejected, SYS:linked allocation rejected | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-LGR-REQUESTED | AGG-LOGISTICS-REQUEST | CMD-LGR-REQUEST | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) |
| EVT-MNT-CANCELLED | AGG-MAINTENANCE-ORDER | CMD-MNT-CANCEL | — | Asset (start/return via policy); Availability view |
| EVT-MNT-COMPLETED | AGG-MAINTENANCE-ORDER | CMD-MNT-COMPLETE | — | Asset (start/return via policy); Availability view |
| EVT-MNT-PLANNED | AGG-MAINTENANCE-ORDER | CMD-MNT-PLAN | — | Asset (start/return via policy); Availability view |
| EVT-MNT-RESCHEDULED | AGG-MAINTENANCE-ORDER | CMD-MNT-RESCHEDULE | — | Asset (start/return via policy); Availability view |
| EVT-MNT-STARTED | AGG-MAINTENANCE-ORDER | CMD-MNT-START | — | Asset (start/return via policy); Availability view |
| EVT-QUAL-EXPIRED | AGG-QUALIFICATION-RECORD | SYS:valid_to reached | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-QUAL-RECORDED | AGG-QUALIFICATION-RECORD | CMD-QUAL-RECORD | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-QUAL-REINSTATED | AGG-QUALIFICATION-RECORD | CMD-QUAL-REINSTATE | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-QUAL-RENEWED | AGG-QUALIFICATION-RECORD | CMD-QUAL-RENEW | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-QUAL-REVOKED | AGG-QUALIFICATION-RECORD | CMD-QUAL-REVOKE | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-QUAL-SUSPENDED | AGG-QUALIFICATION-RECORD | CMD-QUAL-SUSPEND | — | Eligibility cache invalidation; Task assignment re-check report |
| EVT-RPL-CAPACITY-ADJUSTED | AGG-RESOURCE-POOL | CMD-RPL-ADJUST-CAPACITY | — | Capacity ledger |
| EVT-RPL-CLOSED | AGG-RESOURCE-POOL | CMD-RPL-CLOSE | — | Capacity ledger |
| EVT-RPL-CREATED | AGG-RESOURCE-POOL | CMD-RPL-CREATE | — | Capacity ledger |
| EVT-RPL-RESUMED | AGG-RESOURCE-POOL | CMD-RPL-RESUME | — | Capacity ledger |
| EVT-RPL-SUSPENDED | AGG-RESOURCE-POOL | CMD-RPL-SUSPEND | — | Capacity ledger |
| EVT-RRQ-ACTIVATED | AGG-ROLE-REQUIREMENT | CMD-RRQ-ACTIVATE | — | Readiness evaluator; Eligibility cache |
| EVT-RRQ-DEFINED | AGG-ROLE-REQUIREMENT | CMD-RRQ-DEFINE | — | Readiness evaluator; Eligibility cache |
| EVT-RRQ-EDITED | AGG-ROLE-REQUIREMENT | CMD-RRQ-EDIT | — | Readiness evaluator; Eligibility cache |
| EVT-RRQ-RETIRED | AGG-ROLE-REQUIREMENT | CMD-RRQ-RETIRE | — | Readiness evaluator; Eligibility cache |
| EVT-RSV-CANCELLED | AGG-ASSET-RESERVATION | CMD-RSV-CANCEL | — | Availability view |
| EVT-RSV-CONFIRMED | AGG-ASSET-RESERVATION | CMD-RSV-CONFIRM | — | Availability view |
| EVT-RSV-EXPIRED | AGG-ASSET-RESERVATION | SYS:hold expiry (24 h) reached | — | Availability view |
| EVT-RSV-HELD | AGG-ASSET-RESERVATION | CMD-RSV-HOLD | — | Availability view |
| EVT-RSV-RELEASED | AGG-ASSET-RESERVATION | CMD-RSV-RELEASE, SYS:linked task or plan terminal | — | Availability view |
| EVT-SCN-ACTIVATED | AGG-SCENARIO | CMD-SCN-ACTIVATE | — | Exercise (frozen scenario reference on plan); Search projection (SLC-05) |
| EVT-SCN-DEFINED | AGG-SCENARIO | CMD-SCN-DEFINE | — | Search projection (SLC-05) |
| EVT-SCN-EDITED | AGG-SCENARIO | CMD-SCN-EDIT | — | Search projection (SLC-05) |
| EVT-SCN-RETIRED | AGG-SCENARIO | CMD-SCN-RETIRE | — | Search projection (SLC-05) |
| EVT-SHP-CANCELLED | AGG-SHIPMENT | CMD-SHP-CANCEL | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-CHECKPOINT-RECORDED | AGG-SHIPMENT | CMD-SHP-RECORD-CHECKPOINT | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-DAMAGED | AGG-SHIPMENT | CMD-SHP-REPORT-DAMAGE | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-DELIVERED | AGG-SHIPMENT | CMD-SHP-DELIVER | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-DEPARTED | AGG-SHIPMENT | CMD-SHP-DEPART | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-LOST | AGG-SHIPMENT | CMD-SHP-REPORT-LOST | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SHP-PLANNED | AGG-SHIPMENT | CMD-SHP-PLAN | — | Logistics Request (fulfillment status); Search projection (SLC-05) |
| EVT-SIM-ABORTED | AGG-SIMULATION | CMD-SIM-ABORT | — | Exercise (ABORTED trigger); Search projection (SLC-05) |
| EVT-SIM-COMPLETED | AGG-SIMULATION | CMD-SIM-COMPLETE | — | Exercise (COMPLETED trigger); Knowledge Object (optional AAR terminal source, SLC-12 — CR-63); Search projection (SLC-05) |
| EVT-SIM-EVALUATION-RECORDED | AGG-SIMULATION | CMD-SIM-RECORD-EVALUATION | — | Qualification Record (optional evidence source, SLC-03 — unmodified, evidence:urn already generic); Search projection (SLC-05) |
| EVT-SIM-INJECT-DELIVERED | AGG-SIMULATION | CMD-SIM-DELIVER-INJECT | — | Search projection (SLC-05) |
| EVT-SIM-PAUSED | AGG-SIMULATION | CMD-SIM-PAUSE | — | Search projection (SLC-05) |
| EVT-SIM-RESUMED | AGG-SIMULATION | CMD-SIM-RESUME | — | Search projection (SLC-05) |
| EVT-SIM-STARTED | AGG-SIMULATION | CMD-SIM-START | — | Exercise (IN_PROGRESS trigger); Search projection (SLC-05) |

#### security.versions — `{cell}.security.versions`

| الحدث | Aggregate | ينتجه | يؤثر أمنيًا | المستهلكون |
|---|---|---|---|---|
| EVT-SEC-VERSION-INCREMENTED | (derived) SecurityVersion | security-version service on any security-affecting event | نعم | All PEPs; Projection security-version tables; SecurityContext cache |

<!-- END GENERATED: build_analysis_design.py -->
