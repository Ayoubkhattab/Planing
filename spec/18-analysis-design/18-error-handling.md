---
id: AD-18-ERROR-HANDLING
type: error-handling
title: "معالجة الأخطاء — النموذج والأولوية وإعادة المحاولة والكتالوج"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 4)"
sources: [05-contracts/errors-*.md, 05-contracts/openapi-*.md, 00-governance/decisions/ADR-P17.md, 00-governance/decisions/ADR-P19.md, 03-domain/contexts/BC*/aggregates/AGG-*.md, 08-security/audit-architecture.md, 09-reliability/observability-slc*.md, 12-solution/technology-decisions.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# معالجة الأخطاء

كيف يرفض النظام طلبًا، وبأي رمز وحالة HTTP، وأي خطأ يغلب حين يتعدد السبب، ومتى يعيد العميل أو النظام المحاولة. الكتالوج المعتمد في `05-contracts/errors-*.md` (19 ملفًا، 313 رمزًا مميزًا بعد CR-75 وCR-78)؛ هذا الملف يصنّفه ويضيف ما يلزم للتنفيذ.

## 1. نموذج الخطأ

كل استجابة خطأ جسمها `ApiError` (`14-api-design.md` §3):

| الحقل | المعنى | القاعدة |
|---|---|---|
| `code` | رمز ثابت من الكتالوج (`TASK_INVALID_STATE_TRANSITION`) | العقد بين الخادم والعميل؛ لا يُعاد تسميته إلا بإصدار رئيسي (FIT-14) |
| `message` | نص للإنسان بلغة الطلب (العربية افتراضيًا، والإنجليزية) | يُبنى من مفتاح رسالة = الرمز وقالب مترجم **[Derived]** من ADR-P15 (اللغة) |
| `details` | بيانات منظمة: الحقول المخالفة، الحالة الحالية المسموح إفشاؤها، دور المعتمِد (`APPROVAL_REQUIRED`، CR-75) | لا بيانات شخصية ولا أي سمة لمورد غير مرئي |
| `correlation_id` | من `X-Correlation-Id` | يربط الخطأ بالأحداث والتدقيق |
| `trace_id` | معرّف التتبع (OpenTelemetry، TD-14) | للتشخيص |
| `retryable` | هل تجوز إعادة المحاولة | من عمود `retryable` في الكتالوج |
| `policy` | `decision`، `reason_code` | عند رفض التخويل فقط؛ `reason_code` من قائمة مغلقة تسمي القاعدة لا بيانات المورد (ADR-P19) |

لا تتسرب تفاصيل داخلية (استثناءات، استعلامات، مسارات) إلى الاستجابة؛ تذهب إلى سجل التقنية بمعرّفات فقط (`08-security/data-protection.md`).

## 2. الفئات وحالات HTTP

| الفئة | HTTP | أمثلة | من أين |
|---|---|---|---|
| طلب غير صالح | 400 | `VALIDATION_FAILED` | محوّل HTTP: مخطط العقد والحقول الإلزامية |
| مصادقة | 401 | `MFA_STEP_UP_REQUIRED` †؛ رمز غائب أو منتهٍ **[Missing]** (§8) | البوابة؛ الخطوة 6 في خط الأوامر |
| تخويل وعدم إفصاح | 403 / 404 / 422 | `AUTHZ_DENIED`، `PERMISSION_DENIED`، `NOT_FOUND`، `SEGREGATION_OF_DUTIES` (الخطوتان 2 و5)؛ `APPROVAL_REQUIRED` † (الخطوة 6) | منفذ التخويل |
| تزامن وعدم تكرار | 409 / 422 | `VERSION_CONFLICT`، `IDEMPOTENCY_KEY_REUSED` | الخطوتان 3 و7 |
| انتقال حالة غير مسموح | 409 | `*_INVALID_STATE_TRANSITION` (89 رمزًا، رمز لكل Aggregate) | حلقة المجال: مصفوفة الحالة × الأمر |
| قاعدة عمل أو شرط انتقال | 422 | `*_INVALID`، `*_REQUIRED`، `ASSIGNEE_NOT_ELIGIBLE`… | حلقة المجال: الشروط والثوابت |
| منصة | 429 / 503 | `RATE_LIMITED`، `POLICY_ENGINE_UNAVAILABLE`، `AUDIT_UNAVAILABLE` | البوابة والحصص؛ محرك السياسات؛ التدقيق |

أرقام الخطوات في هذا الملف هي خطوات خط الأوامر في ADR-P17 (1–10). † رمز من ADR-P19 أضافه CR-75 إلى كل كتالوج في جولة تصحيح المصادر (مطبَّق)، فهو ضمن الـ313 رمزًا في §9.

## 3. أين يُنشأ الخطأ وكيف يُحوَّل (ADR-P17)

| الحلقة | ما تنتجه | التحويل |
|---|---|---|
| المجال | أخطاء مجال مُنمَّطة: انتقال مرفوض، شرط غير متحقق (برمزه من جدول الانتقالات)، ثابت مخالَف | لا تعرف HTTP؛ تحمل الرمز فقط |
| التطبيق | رفض التخويل، غير موجود، تعارض الإصدار، تكرار المفتاح، التزام غير مستوفى، تعذّر التدقيق | من خط الأوامر |
| المحوّلات | خطأ مخطط الطلب؛ تحويل كل خطأ إلى `ApiError` وحالة HTTP من الكتالوج | جدول تحويل مولَّد من `x-error-codes` والكتالوج |

العملية الواحدة لا تعيد إلا الرموز المعلنة في `x-error-codes` لها، ورموز المنصة العامة. فحص V4 في `verify_study.py` يغطي جزءًا من ذلك فقط: قوائم أخطاء الأوامر مقابل الكتالوج، ورموز الشروط مقابل قوائم الأوامر؛ أما تطابق `x-error-codes` في العقود مع قوائم الأوامر فيُضاف فحصًا في التنفيذ **[Derived]**.

## 4. أي خطأ يغلب

حين يتعدد السبب، الخطأ الأول بترتيب الفحص هو المُعاد، وترتيب الفحص هو ترتيب خط الأوامر (ADR-P17):

| الخطوة | الفحص | الرمز |
|---|---|---|
| قبل الخط | المصادقة والحصص عند البوابة | 401 (§8)، `RATE_LIMITED` |
| قبل الخط | مخطط الطلب في المحوّل | `VALIDATION_FAILED` — لا يمس البيانات، فلا إفصاح |
| 1 | نطاق المستأجر من SecurityContext | — (لا مدخل للمستأجر في الطلب) |
| 2 | التخويل الأولي قبل أي تحميل | `NOT_FOUND`، `POLICY_ENGINE_UNAVAILABLE`؛ في أمر الإنشاء يُقيَّم على النطاق الأب |
| 3 | عدم التكرار | إعادة الاستجابة المحفوظة، أو `IDEMPOTENCY_KEY_REUSED` — انظر التحفظ أدناه |
| 4 | تحميل الـAggregate | `NOT_FOUND` إن لم يوجد |
| 5 | التخويل الكامل بالمورد المحمَّل | `NOT_FOUND` (غير مرئي)، `AUTHZ_DENIED` (مرئي، أو أمر إنشاء مرفوض — ADR-P19)، `SEGREGATION_OF_DUTIES` |
| 6 | الالتزامات قبل التنفيذ | `MFA_STEP_UP_REQUIRED` †، `APPROVAL_REQUIRED` †، `LEGAL_HOLD_ACTIVE` |
| 7 | الإصدار المتوقع | `VERSION_CONFLICT` |
| 8 | المجال | `*_INVALID_STATE_TRANSITION` ثم رموز الشروط بترتيب عمود الشرط |
| 9 | الحفظ والتدقيق | `AUDIT_UNAVAILABLE` |

ترتيب الشروط داخل الخطوة 8 حين يفشل أكثر من شرط: الحالة أولًا، ثم الشروط بترتيب ورودها في جدول الانتقالات **[Derived]**.

**تحفظ على الخطوة 3 (عولج بـCR-80):** ما بعد الخطوة 5 لا يكشف شيئًا قبل قرار التخويل، لكن الخطوة 3 تسبقه. جدول `idempotency_keys` مفتاحه `(tenant_id, key)` (`06-data/logical-model/slc-01.md`)، فمستخدم ثانٍ في المستأجر نفسه يعيد استعمال مفتاح غيره يتلقى `ResourceRef` المحفوظ (urn، الإصدار، الحالة) أو `IDEMPOTENCY_KEY_REUSED`، وهذا يخالف ADR-P17 2.5 («nothing about the resource … is returned before this decision»). المقترح: مفتاح عدم التكرار بنطاق المستدعي `(tenant_id, principal_id, key)`، فلا يُطابق إلا طلبات المستدعي نفسه، مع بقاء الترتيب كما هو — CR-80. المفاتيح عشوائية (ULID) فالتصادم غير المقصود نادر، لكن التخمين أو التسريب ممكن.

## 5. إعادة المحاولة

### 5.1 من العميل

| الرمز | إعادة؟ | كيف |
|---|---|---|
| `VERSION_CONFLICT` | نعم | يعيد تحميل المورد، ويعيد بناء الأمر على الإصدار الجديد إن بقي منطقيًا، بمفتاح `Idempotency-Key` جديد |
| `MFA_STEP_UP_REQUIRED` | نعم | بعد المصادقة المعززة، **بنفس** `Idempotency-Key` (لم يُنفَّذ شيء) |
| `RATE_LIMITED`، `POLICY_ENGINE_UNAVAILABLE` | نعم | تأخير متزايد مع عشوائية، بنفس `Idempotency-Key`؛ ترويسة `Retry-After` **[Missing]** (§8) |
| انقطاع الشبكة أو مهلة دون استجابة | نعم | بنفس `Idempotency-Key`: إن كان الأمر نُفِّذ تُعاد استجابته المحفوظة (24 ساعة) |
| كل ما سواه | لا | خطأ منطقي يحتاج تغيير الطلب أو الحالة أو الصلاحية |

`Idempotency-Key` إلزامي على كل أمر (477)، فإعادة المحاولة آمنة دائمًا: التكرار بنفس الحمولة لا يُنفِّذ مرتين.

### 5.2 داخل النظام

| المسار | السلوك | المصدر |
|---|---|---|
| ناقل الـoutbox | مرة واحدة على الأقل حتى النجاح؛ المستهلك يزيل التكرار بالـinbox | ADR-P02، `15-event-design.md` §4 |
| مستهلك الأحداث | 5 إعادات بتأخير متزايد ثم DLQ (إلا موضوع نسخ الأمن: لا إيقاف، بل إبطال وإعادة بناء)، وإيقاف مفتاح الـAggregate وحده؛ رفض المجال للأمر الناتج نتيجة عادية تُدقَّق ويُنبَّه عليها (C-SYS) لا رسالة ميتة | ADR-P20؛ `23-crosscutting.md` §6 |
| ناقل التدقيق | تراكم محلي؛ رفض الأوامر المغيرة للحالة بعد 24 ساعة أو 80 % من السعة | `audit-architecture.md` |
| الانتقالات التلقائية (`SYS:`) والعمّال | نفس خط الأوامر؛ الفشل يُسجَّل ويُنبَّه عليه، ولا يُسقَط بصمت | `05-user-stories/00-guide.md` ضابط C-SYS |
| المزامنة الميدانية | الأمر المرفوض دون اتصال لا يصبح خطأ HTTP للمستخدم بل تعارض مزامنة (AGG-SYNC-CONFLICT) يحسمه محلل أو المستخدم | ADR-P09 |
| استدعاء سياق آخر (OHS) | يفشل مغلقًا: الأمر الذي يحتاج نتيجة الاستدعاء يُرفض — رمز لذلك **[Missing]** (§8) | THR-S03-04 |

## 6. المراقبة

- كل رفض يُسجَّل في سجل التدقيق بنتيجته (`outcome: rejected` و`error_code`) — `audit-architecture.md` (AuditRecord).
- مقاييس لكل شريحة في `09-reliability/observability-slc*.md` (مثل `authz.decisions_total{decision}` بتنبيه عند قفزة الرفض)؛ التتبع يمر بـ`gateway.resolve_context → pep.decide → command.handle → db.commit`.
- مقياس عام لعدد الأخطاء حسب الرمز والعملية والمستأجر **[Derived]** لاكتشاف الرموز غير المتوقعة (مثل رمز «لا يُطلَق» يظهر فعلًا).

## 7. في قصص المستخدم

كل قصة أمر تسرد رموزها في Scenario Outline «is rejected» بحالة HTTP وشرط كل رمز (`05-user-stories/`)؛ فهذا الملف هو الفهرس، والقصة هي المرجع لكل عملية.

## 8. فجوات وتصحيحات

| البند | الحالة |
|---|---|
| `401` لرمز غائب أو منتهٍ، و`413` (حجم الطلب)، و`415` (نوع المحتوى) عند البوابة | مطبَّق — `UNAUTHENTICATED` (401)، `PAYLOAD_TOO_LARGE` (413)، `UNSUPPORTED_MEDIA_TYPE` (415) في كل كتالوج، والاستجابات معلنة في العقود (CR-78) |
| فشل استدعاء سياق آخر مغلقًا | مطبَّق — `DEPENDENCY_UNAVAILABLE` (503، قابل لإعادة المحاولة) للحالة العامة، و`ELIGIBILITY_UNAVAILABLE` على `CMD-TASK-ASSIGN` و`CMD-TASK-REASSIGN` (CR-78) |
| ترويسة `Retry-After` مع 429 و503 القابل لإعادة المحاولة | مطبَّق في العقود (CR-78)؛ لا تُرسل مع `AUDIT_UNAVAILABLE` ما دام غير قابل لإعادة المحاولة |
| رموز ADR-P19 (`MFA_STEP_UP_REQUIRED`، `APPROVAL_REQUIRED`) و`401`/`403` في العقود | مطبَّق — CR-75 (العلامة † في هذا الملف) |
| مفتاح عدم التكرار بنطاق المستأجر لا المستدعي (§4) | مطبَّق — `(tenant_id, principal_id, key)` (CR-80) |
| رموز أسباب الرفض غير المتزامن (§9.1: `POLICY_DENIED`، `GEOGRAPHY_MISMATCH`…) | فئة مستقلة: تُحمل في حقل سبب حالة `REJECTED` لا في `ApiError.code`. `POLICY_DENIED` للفحص 6 في `allocation-readiness-spec.md` §1 يذكر `REQUIRE_APPROVAL` مثالًا، بينما مصفوفة AGG-ALLOCATION ترسل الطلب إلى `PENDING_APPROVAL` (استثناء ADR-P19): التوفيق المقترح أن `REQUIRE_APPROVAL` ← `PENDING_APPROVAL` و`POLICY_DENIED` لالتزام آخر غير مستوفى **[Needs Review]** — S-29 |
| أوامر لا يُطلق فيها رمز انتقال الحالة أبدًا (§9.1) | تبقى دفاعيًا: المصفوفة قد تتغير، والرمز لا يضر **[Derived]**؛ تصحيح المصدر S-03 |
| رموز تذكرها المواصفات ولا يذكرها الكتالوج (§9.1) | **[Needs Review]** — S-27: بقي ثلاثة يذكرها `requirements.md` (`CLASSIFICATION_REQUIRED`، `GEOMETRY_INVALID`، `SOURCE_REQUIRED`)؛ `ELIGIBILITY_UNAVAILABLE` أُضيف (CR-78) |
| `AUDIT_UNAVAILABLE` غير قابل لإعادة المحاولة رغم أنه ظرف مؤقت | **[Needs Review]** — قيمة المصدر محفوظة |

## 9. الكتالوج

<!-- BEGIN GENERATED: build_analysis_design.py -->

### 9.1 الملخص

| الفئة | الرموز | HTTP | قابل لإعادة المحاولة |
|---|---|---|---|
| 1. طلب غير صالح | 3 | 400, 413, 415 | 0 |
| 2. مصادقة وتخويل وعدم إفصاح | 7 | 401, 403, 403→404, 404, 422 | 1 |
| 3. تزامن وعدم تكرار | 2 | 409, 422 | 1 |
| 4. انتقال حالة غير مسموح | 89 | 409 | 0 |
| 5. قاعدة عمل أو شرط انتقال | 207 | 422 | 0 |
| 6. منصة واعتماديات | 5 | 429, 503, 503 (request denied) | 4 |
| **المجموع** | **313** | | 6 |

**أوامر لا يُطلِق فيها رمز `*_INVALID_STATE_TRANSITION` أبدًا (6)** — الأمر مسموح من كل حالات المصفوفة (S-03): `CLAIM_INVALID_STATE_TRANSITION` في `CMD-CLM-RECLASSIFY`، `ENTITY_INVALID_STATE_TRANSITION` في `CMD-ENT-RECLASSIFY`، `EVIDENCE_INVALID_STATE_TRANSITION` في `CMD-EVD-RECLASSIFY`، `OBSERVATION_INVALID_STATE_TRANSITION` في `CMD-OBS-RECLASSIFY`، `REALWORLD_EVENT_INVALID_STATE_TRANSITION` في `CMD-RWE-RECLASSIFY`، `RELATIONSHIP_INVALID_STATE_TRANSITION` في `CMD-REL-RECLASSIFY`.

**رموز تذكرها المواصفات وليست في كتالوج الأخطاء (3)** **[Needs Review]** (S-27):

| الرمز | أين يُذكر |
|---|---|
| `CLASSIFICATION_REQUIRED` | `02-requirements/requirements.md` |
| `GEOMETRY_INVALID` | `02-requirements/requirements.md` |
| `SOURCE_REQUIRED` | `02-requirements/requirements.md` |

**رموز أسباب لحالة رفض غير متزامنة (7)** — تُحمل في حقل السبب لحالة `REJECTED` أو مع رمز خطأ، وليست رموز HTTP؛ فئة مستقلة عن الكتالوج (§8):

| السبب | أين يُذكر |
|---|---|
| `CERTIFICATION_EXPIRED` | `13-verification/acceptance/SLC-09/invariants-slc09.md` |
| `GEOGRAPHY_MISMATCH` | `03-domain/contexts/BC05/allocation-readiness-spec.md`, `13-verification/acceptance/SLC-09/invariants-slc09.md` |
| `POLICY_DENIED` | `03-domain/contexts/BC05/allocation-readiness-spec.md` |
| `POOL_NOT_ACTIVE` | `03-domain/contexts/BC05/allocation-readiness-spec.md` |
| `REQUIRES_CERTIFICATION` | `13-verification/acceptance/SLC-03/invariants-slc03.md` |
| `RESOURCE_TYPE_MISMATCH` | `03-domain/contexts/BC05/allocation-readiness-spec.md` |
| `WINDOW_OUTSIDE_TARGET` | `03-domain/contexts/BC05/allocation-readiness-spec.md` |

### 9.2 طلب غير صالح

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `PAYLOAD_TOO_LARGE` | 413 | لا | — (منصة) | — | — |
| `UNSUPPORTED_MEDIA_TYPE` | 415 | لا | — (منصة) | — | — |
| `VALIDATION_FAILED` | 400 | لا | 477 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | — |

### 9.3 مصادقة وتخويل وعدم إفصاح

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `APPROVAL_REQUIRED` | 403 | لا | — (منصة) | — | — |
| `AUTHZ_DENIED` | 403→404 | لا | 477 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | — |
| `MFA_STEP_UP_REQUIRED` | 401 | نعم | — (منصة) | — | — |
| `NOT_FOUND` | 404 | لا | — (منصة) | — | — |
| `PERMISSION_DENIED` | 403→404 | لا | 1 | BC01 | actor has authority.grant permission; decision type exists; scope unit ACTIVE (AUTHORITY-GRANT) |
| `SEGREGATION_OF_DUTIES` | 422 | لا | 45 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | approver is Executive in scope; approver ≠ requester (AUTHORITY-GRANT) |
| `UNAUTHENTICATED` | 401 | لا | — (منصة) | — | — |

### 9.4 تزامن وعدم تكرار

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 477 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | — |
| `VERSION_CONFLICT` | 409 | نعم | 477 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | — |

### 9.5 انتقال حالة غير مسموح

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `ADAPTER_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC07 | — |
| `AI_REQUEST_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC07 | — |
| `AI_RESULT_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC07 | — |
| `AI_ROUTING_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC07 | — |
| `AI_TOOL_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC07 | — |
| `ALERT_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC03 | — |
| `ALERT_RULE_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC03 | — |
| `ALLOCATION_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC05 | — |
| `ANALYSIS_CASE_INVALID_STATE_TRANSITION` | 409 | لا | 13 | BC03 | — |
| `ANALYSIS_METHOD_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC03 | — |
| `ANALYSIS_RUN_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC03 | — |
| `ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC06 | — |
| `ASSESSMENT_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC03 | — |
| `ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC05 | — |
| `ASSET_INVALID_STATE_TRANSITION` | 409 | لا | 11 | BC05 | — |
| `ASSET_RESERVATION_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC05 | — |
| `ATTACHMENT_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC02 | — |
| `AUTHORITY_GRANT_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC01 | — |
| `CAP_MESSAGE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC03 | — |
| `CLAIM_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC02 | — |
| `CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC08 | — |
| `CLEARANCE_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC01 | — |
| `COLLECTION_PLAN_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC02 | — |
| `COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION` | 409 | لا | 7 | BC02 | — |
| `CONFLICT_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC02 | — |
| `COORDINATION_CASE_INVALID_STATE_TRANSITION` | 409 | لا | 8 | BC04 | — |
| `CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC02 | — |
| `CORRELATION_RULE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC02 | — |
| `DECISION_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC04 | — |
| `DECISION_REQUEST_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC04 | — |
| `DEVICE_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC01 | — |
| `DISPOSITION_RUN_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC08 | — |
| `DISTRIBUTION_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC06 | — |
| `ENTITY_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC02 | — |
| `ERASURE_REQUEST_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC08 | — |
| `ER_CASE_INVALID_STATE_TRANSITION` | 409 | لا | 9 | BC02 | — |
| `EVAL_SUITE_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC07 | — |
| `EVIDENCE_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC02 | — |
| `EVIDENCE_LINK_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC02 | — |
| `EXERCISE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC05 | — |
| `EXTERNAL_ID_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC02 | — |
| `FINDING_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC03 | — |
| `HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC01 | — |
| `IMPORT_BATCH_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC02 | — |
| `INCIDENT_INVALID_STATE_TRANSITION` | 409 | لا | 9 | BC04 | — |
| `INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC07 | — |
| `KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION` | 409 | لا | 8 | BC06 | — |
| `LEGAL_HOLD_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC08 | — |
| `LOGISTICS_REQUEST_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC05 | — |
| `MAINTENANCE_ORDER_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC05 | — |
| `MATCH_RULESET_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC02 | — |
| `MODEL_VERSION_INVALID_STATE_TRANSITION` | 409 | لا | 8 | BC07 | — |
| `NOTIFICATION_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC04 | — |
| `OBSERVATION_INVALID_STATE_TRANSITION` | 409 | لا | 5 | BC02 | — |
| `ORGANIZATION_INVALID_STATE_TRANSITION` | 409 | لا | 7 | BC01 | — |
| `OUTCOME_TRACKER_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC04 | — |
| `PERSON_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC01 | — |
| `PLAN_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC04 | — |
| `PLAN_VERSION_INVALID_STATE_TRANSITION` | 409 | لا | 7 | BC04 | — |
| `POLICY_SET_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC08 | — |
| `PRELOAD_PACKAGE_INVALID_STATE_TRANSITION` | 409 | لا | 2 | BC07 | — |
| `PRODUCT_INVALID_STATE_TRANSITION` | 409 | لا | 7 | BC06 | — |
| `PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC06 | — |
| `PROJECTION_VERSION_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC07 | — |
| `QUALIFICATION_RECORD_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC05 | — |
| `REALWORLD_EVENT_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC02 | — |
| `RECONSTRUCTION_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC06 | — |
| `RELATIONSHIP_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC02 | — |
| `RESOURCE_POOL_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC05 | — |
| `RETENTION_SCHEDULE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC08 | — |
| `RISK_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC04 | — |
| `ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC01 | — |
| `ROLE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC01 | — |
| `ROLE_REQUIREMENT_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC05 | — |
| `SCENARIO_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC05 | — |
| `SECURITY_EXCEPTION_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC08 | — |
| `SENSOR_STREAM_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC07 | — |
| `SERVICE_ACCOUNT_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC01 | — |
| `SHIPMENT_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC05 | — |
| `SIMULATION_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC05 | — |
| `SITUATION_INVALID_STATE_TRANSITION` | 409 | لا | 6 | BC03 | — |
| `SOURCE_INVALID_STATE_TRANSITION` | 409 | لا | 7 | BC02 | — |
| `SUBSCRIPTION_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC04 | — |
| `SYNC_CONFLICT_INVALID_STATE_TRANSITION` | 409 | لا | 4 | BC07 | — |
| `SYNC_SESSION_INVALID_STATE_TRANSITION` | 409 | لا | 1 | BC07 | — |
| `TASK_INVALID_STATE_TRANSITION` | 409 | لا | 23 | BC04 | — |
| `TASK_TYPE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | BC04 | — |
| `TENANT_INVALID_STATE_TRANSITION` | 409 | لا | 10 | BC01 | — |
| `USER_INVALID_STATE_TRANSITION` | 409 | لا | 9 | BC01 | — |

### 9.6 قاعدة عمل أو شرط انتقال

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `ACTIVITY_ALREADY_TASKED` | 422 | لا | 1 | BC02 | activity not yet tasked (COLLECTION-PLAN) |
| `ACTIVITY_INVALID` | 422 | لا | 1 | BC02 | method in RD-COLLECTION-METHODS; source(s) ACTIVE; area ⊆ requirement areas; window ⊆ requirement windows; as… (COLLECTION-PLAN) |
| `ADAPTER_INVALID` | 422 | لا | 1 | BC07 | source ACTIVE; service account ACTIVE; mapping spec present (ADAPTER) |
| `AI_OPERATION_NOT_ALLOWED` | 422 | لا | 1 | BC07 | operation ∈ AI autonomy matrix and allowed at the tenant's routing; user authenticated; purpose; input size ≤… (AI-REQUEST) |
| `ALERT_RULE_INVALID` | 422 | لا | 2 | BC03 | condition kind in RD-ALERT-RULE-TYPES; parameters valid; severity; dedupe window; situation ACTIVE or tenant-… (ALERT-RULE) |
| `ALLOCATION_INVALID` | 422 | لا | 1 | BC05 | pool ACTIVE; quantity > 0 in pool unit; window; priority 1–5; target task/activity/logistics-request (CR-62,… (ALLOCATION) |
| `ALLOCATION_NOT_COMMITTED` | 422 | لا | 1 | BC05 | dispatcher; linked allocation still COMMITTED; creates a Shipment (AGG-SHIPMENT) referencing this request and… (LOGISTICS-REQUEST) |
| `ASSESSMENT_INCOMPLETE` | 422 | لا | 1 | BC03 | findings ≥ 1 (ACCEPTED), evidence, assumptions, uncertainty, confidence, methodology, limitations all present… (ASSESSMENT) |
| `ASSESSMENT_INVALID` | 422 | لا | 2 | BC02, BC03 | updates information_confidence / verification_status only (T2 versioned assessment); value and times untouched (CLAIM) |
| `ASSET_INVALID` | 422 | لا | 1 | BC05 | type in RD-ASSET-TYPES; owner org; custody holder ACTIVE; linked information entity (entity_type asset-ref) c… (ASSET) |
| `ASSET_NOT_AVAILABLE` | 422 | لا | 1 | BC05 | asset available (or covered by the caller's CONFIRMED reservation); asset certifications satisfy the task typ… (ASSET-ASSIGNMENT) |
| `ASSET_NOT_SERVICEABLE` | 422 | لا | 1 | BC05 | maintenance order COMPLETED; condition serviceable; required certifications valid (ASSET) |
| `ASSET_RESERVED` | 422 | لا | 1 | BC05 | asset available for the window (INV-AST-01); purpose; requester authorized in asset owner scope (ASSET-RESERVATION) |
| `ASSIGNEE_NOT_ELIGIBLE` | 422 | لا | 2 | BC04 | assignee ACTIVE user; assignee clearance ≥ task label; EligibilityCheck(assignee, task type, now) ∈ {ELIGIBLE… (TASK) |
| `ATTACHMENT_REJECTED` | 422 | لا | 1 | BC02 | size ≤ tenant limit; mime allowed; returns direct upload target (≤ 5 min); same sha256 already STORED in tena… (ATTACHMENT) |
| `ATTESTATION_FAILED` | 422 | لا | 1 | BC01 | hardware attestation valid (or MDM compliance); Administrator or MDM policy (DEVICE) |
| `AUTHORITY_EXCEEDS_DELEGATOR` | 422 | لا | 1 | BC01 | parent grant effective and delegable; scope ⊆ parent; limits ≤ parent; period ⊆ parent; depth ≤ 2; delegate ≠… (AUTHORITY-GRANT) |
| `AUTHORITY_REQUIRED` | 422 | لا | 5 | BC04, BC05, BC06 | AuthorityCheck(decider, decision type, scope, now) = authorized — grant chain stored as authority snapshot (B… (DECISION) |
| `BATCH_KEY_REUSED` | 422 | لا | 1 | BC02 | adapter ACTIVE (or authorized manual import); batch_key unique per adapter: same key + same content hash retu… (IMPORT-BATCH) |
| `CANARY_BELOW_THRESHOLD` | 422 | لا | 1 | BC07 | canary metrics within thresholds for ≥ 7 days; approver ≠ stager (MODEL-VERSION) |
| `CAPACITY_BELOW_COMMITMENTS` | 422 | لا | 1 | BC05 | new capacity with valid_from; reason; a reduction below committed quantity requires pre-emption decisions fir… (RESOURCE-POOL) |
| `CAPACITY_UNAVAILABLE` | 422 | لا | 1 | BC05 | approver with allocation authority ≠ requester; capacity still available (ALLOCATION) |
| `CASE_HAS_PUBLISHED_ASSESSMENT` | 422 | لا | 1 | BC03 | reason; no PUBLISHED assessment references the case (ANALYSIS-CASE) |
| `CASE_INVALID` | 422 | لا | 5 | BC03 | title; owner; label (ANALYSIS-CASE) |
| `CASE_NOT_DEFINED` | 422 | لا | 1 | BC03 | question and scope present (REQ-ANL-001) (ANALYSIS-CASE) |
| `CELL_UNAVAILABLE` | 422 | لا | 1 | BC01 | target cell exists and has capacity (TENANT) |
| `CERTIFICATION_INVALID` | 422 | لا | 1 | BC05 | certification code, issuer, valid_from/to; evidence (ASSET) |
| `CHANGE_TIME_INVALID` | 422 | لا | 1 | BC02 | t_change ∈ (valid_from, valid_to): closes record, re-records old value with valid_to = t_change, asserts new… (CLAIM) |
| `CHECKPOINT_INVALID` | 422 | لا | 1 | BC05 | checkpoint strictly after the previous checkpoint in time (append-only, gapless — mirrors INV-AST-02); locati… (SHIPMENT) |
| `CITATION_ABOVE_LABEL` | 422 | لا | 1 | BC04 | assessment or evidence visible; pinned URN + version; cited label ≤ request label (DECISION-REQUEST) |
| `CLAIM_INVALID` | 422 | لا | 1 | BC02 | subject exists; predicate in RD-PREDICATES; value matches predicate type/unit/cardinality; ≥ 1 source, all AC… (CLAIM) |
| `CLASSIFICATION_CHANGE_NOT_AUTHORIZED` | 422 | لا | 12 | BC02, BC03, BC04, BC05 | authority per tenant policy (REQ-GOV-004); new version; bumps object security_version (CLAIM) |
| `CLEARANCE_EXISTS` | 422 | لا | 1 | BC01 | Security Officer; level and compartments exist in ACTIVE scheme; subject has no other non-terminal clearance (CLEARANCE) |
| `CLEARANCE_INVALID` | 422 | لا | 1 | BC01 | same rules as grant; creates new version (CLEARANCE) |
| `CONDITION_INVALID` | 422 | لا | 1 | BC05 | condition grade in RD-CONDITION-GRADES; inspector; unserviceable grades require CMD-AST-MARK-UNSERVICEABLE (ASSET) |
| `CONDITION_REPORT_REQUIRED` | 422 | لا | 1 | BC05 | condition report; asset condition updated accordingly (ASSET-ASSIGNMENT) |
| `CONFLICT_INVALID` | 422 | لا | 1 | BC02 | analyst names ≥ 2 visible CURRENT claims on the same cluster and predicate with overlapping valid time (CONFLICT) |
| `CONNECTION_INVALID` | 422 | لا | 1 | BC07 | system kind ∈ {erp, hris, dms, cmms, sensor_gateway, cap_endpoint}; endpoint on an internal network; protocol… (INTEGRATION-CONNECTION) |
| `CONNECTION_IN_USE` | 422 | لا | 1 | BC07 | no ACTIVE adapter or stream bound; egress rule removed (INTEGRATION-CONNECTION) |
| `CONNECTION_NOT_ACTIVE` | 422 | لا | 1 | BC07 | connection ACTIVE; mapping to CMD-OBS-RECORD batches tested (SENSOR-STREAM) |
| `CONSUMPTION_INVALID` | 422 | لا | 1 | BC05 | quantity in pool unit; time; consumption beyond commitment flagged (REQ-RES-010) (ALLOCATION) |
| `COORDINATION_INVALID` | 422 | لا | 1 | BC04 | title; purpose; lead organization; linked decisions/plans/situations visible to the opener; label (COORDINATION-CASE) |
| `CORRELATION_INVALID` | 422 | لا | 1 | BC02 | analyst; ≥ 2 visible inputs; kind; rationale (CORRELATION-PROPOSAL) |
| `CREDENTIAL_LIFETIME_EXCEEDED` | 422 | لا | 1 | BC01 | new credential expiry ≤ 90 days (SERVICE-ACCOUNT) |
| `CUSTODY_INVALID` | 422 | لا | 2 | BC02, BC05 | actor is current holder or custodian role; new holder named (EVIDENCE) |
| `DECISION_PENDING` | 422 | لا | 1 | BC04 | actor belongs to the responsible participant; status ∈ {in_progress, done, waived with reason}; items requiri… (COORDINATION-CASE) |
| `DECISION_REQUEST_INCOMPLETE` | 422 | لا | 1 | BC04 | ≥ 2 options (one may be 'no action'); ≥ 1 citation (REQ-DEC-001, OUT-04) (DECISION-REQUEST) |
| `DECISION_REQUEST_INVALID` | 422 | لا | 2 | BC04 | question; required decision type (RD-DECISION-TYPES); scope unit; deadline; label (DECISION-REQUEST) |
| `DELIVERY_INVALID` | 422 | لا | 1 | BC05 | receiving party confirms; delivered_quantity ≤ planned quantity; a shortfall is recorded, never hidden (INV-S… (SHIPMENT) |
| `DEPARTURE_INVALID` | 422 | لا | 1 | BC05 | carrier confirmed; departure checkpoint recorded (SHIPMENT) |
| `DEPENDENCIES_NOT_MET` | 422 | لا | 1 | BC04 | actor = assignee; all predecessor tasks COMPLETED or CLOSED (TASK) |
| `DEVICE_LIMIT_REACHED` | 422 | لا | 1 | BC01 | user ACTIVE; device public key; platform; MDM reference; ≤ 3 active devices per user (DEVICE) |
| `DEVICE_NOT_ACTIVE` | 422 | لا | 1 | BC07 | device ACTIVE; user authenticated (fresh token); device signature on handshake; clock offset measured (server… (SYNC-SESSION) |
| `DEVICE_NOT_WIPED` | 422 | لا | 1 | BC01 | device synced and wiped (confirmation) or Security Officer override (DEVICE) |
| `DRAFT_EXISTS` | 422 | لا | 5 | BC03, BC04, BC07, BC08 | case exists; either new assessment or revision of a PUBLISHED version (copies content); at most one DRAFT/IN_… (ASSESSMENT) |
| `DRY_RUN_REQUIRED` | 422 | لا | 1 | BC03 | dry-run on last 24 h of events completed and reviewed (expected alert volume shown) (ALERT-RULE) |
| `ENTITY_INVALID` | 422 | لا | 1 | BC02 | type in RD-ENTITY-TYPES; each initial claim valid as CMD-CLM-ASSERT; Entity + initial Claims created in one u… (ENTITY) |
| `ENTITY_TYPE_INCOMPATIBLE` | 422 | لا | 1 | BC02 | compatible type per RD-ENTITY-TYPES; new version; reason (ENTITY) |
| `ERASURE_INVALID` | 422 | لا | 1 | BC08 | legal basis reference; subject identification (platform person URN and/or information entity URNs of type per… (ERASURE-REQUEST) |
| `ER_PAIR_INVALID` | 422 | لا | 1 | BC02 | same conditions; proposer is Analyst or AI suggestion (AIL1, agent recorded) (ER-CASE) |
| `EVALUATION_BELOW_THRESHOLD` | 422 | لا | 1 | BC07 | report meets thresholds: citation accuracy ≥ 95 %, hallucination ≤ 2 %, insufficient-evidence recall ≥ 95 %,… (MODEL-VERSION) |
| `EVALUATION_MISSING` | 422 | لا | 1 | BC05 | every participant on the linked exercise has ≥ 1 recorded evaluation (INV-SIM-02) (SIMULATION) |
| `EVALUATION_TOO_OLD` | 422 | لا | 1 | BC07 | rollback; evaluation ≤ 90 days old (MODEL-VERSION) |
| `EVENT_INVALID` | 422 | لا | 1 | BC02 | type in RD-EVENT-TYPES; initial claims include event_time (fuzzy) and location (REALWORLD-EVENT) |
| `EVENT_TYPE_INCOMPATIBLE` | 422 | لا | 1 | BC02 | compatible type; reason (REALWORLD-EVENT) |
| `EVIDENCE_ABOVE_CASE_LABEL` | 422 | لا | 1 | BC03 | items visible to actor; each pinned with known_at = now; item label ≤ case label (ANALYSIS-CASE) |
| `EVIDENCE_INVALID` | 422 | لا | 2 | BC02 | attachment STORED or observation_ref; type in RD-EVIDENCE-TYPES; source ACTIVE (EVIDENCE) |
| `EXCEPTION_NOT_ALLOWED` | 422 | لا | 1 | BC08 | targets a tenant policy rule (not platform baseline); duration ≤ 30 days; justification (SECURITY-EXCEPTION) |
| `EXERCISE_INVALID` | 422 | لا | 3 | BC05 | scenario ACTIVE at this instant, frozen thereafter (INV-EXR-01); objectives; participants; purpose; role_ref… (EXERCISE) |
| `EXTERNAL_ID_TAKEN` | 422 | لا | 1 | BC02 | (system, external_id) has no ACTIVE mapping; target exists (EXTERNAL-ID) |
| `FINDING_INVALID` | 422 | لا | 2 | BC03 | statement; ≥ 1 source among SUCCEEDED runs of the case or selected evidence; uncertainty; label ≥ sources (FINDING) |
| `FIXITY_MISMATCH` | 422 | لا | 1 | BC06 | restored from replica; fixity re-verified (ARCHIVE-PACKAGE) |
| `FORMAT_INVALID` | 422 | لا | 1 | BC06 | new preservation representation added; originals kept; preservation event recorded (ARCHIVE-PACKAGE) |
| `FULFILMENT_INSUFFICIENT` | 422 | لا | 1 | BC02 | requester; fulfilment as seen by the requester is ANSWERED, or PARTIAL with explicit acceptance note (COLLECTION-REQUIREMENT) |
| `GRANT_EXPIRED` | 422 | لا | 1 | BC01 | period not ended (AUTHORITY-GRANT) |
| `HASH_MISMATCH` | 422 | لا | 1 | BC02 | stored bytes hash = declared sha256; size matches (ATTACHMENT) |
| `HOLD_INVALID` | 422 | لا | 2 | BC08 | Legal/Compliance authority; scope = any of: record classes, object URNs, data subjects, org units, time range… (LEGAL-HOLD) |
| `IDENTITY_ALREADY_LINKED` | 422 | لا | 1 | BC01 | (issuer, subject) unique in tenant; issuer is a configured IdP (USER) |
| `INCIDENT_INVALID` | 422 | لا | 2 | BC04 | category_ref (RD-HAZARD-CATEGORIES)؛ description؛ scope_refs ≥ 1؛ risk_ref اختياري (خطر تحقَّق)؛ severity ابت… (INCIDENT) |
| `INJECT_INVALID` | 422 | لا | 1 | BC05 | inject_ref belongs to the linked scenario; delivered_at strictly after the previous delivery (INV-SIM-01) (SIMULATION) |
| `KNOWLEDGE_INCOMPLETE` | 422 | لا | 1 | BC06 | ≥ 1 statement; lessons: ≥ 1 evidence link (KNOWLEDGE-OBJECT) |
| `KNOWLEDGE_INVALID` | 422 | لا | 2 | BC06 | type ∈ {procedure, lesson, best_practice, policy_knowledge}; lessons reference a terminal source (task, plan,… (KNOWLEDGE-OBJECT) |
| `LAST_ACTIVE_PROJECTION` | 422 | لا | 1 | BC07 | operator; not the only ACTIVE version of its kind (PROJECTION-VERSION) |
| `LAST_IDENTITY` | 422 | لا | 2 | BC01 | if ACTIVE, at least one identity remains (USER) |
| `LEGAL_HOLD_ACTIVE` | 422 | لا | 3 | BC01, BC02 | erasure order recorded; no legal hold; destroys subject key (ADR-P08) (PERSON) |
| `LINK_DUPLICATE` | 422 | لا | 1 | BC02 | evidence not WITHDRAWN; claim exists; stance ∈ {SUPPORTS, REFUTES, CONTEXT}; no ACTIVE duplicate (evidence, c… (EVIDENCE-LINK) |
| `LINK_REQUIRED` | 422 | لا | 1 | BC05 | linked to a task or plan activity (ASSET-RESERVATION) |
| `LOCATOR_INVALID` | 422 | لا | 1 | BC02 | locator within attachment bounds (EVIDENCE) |
| `LOGISTICS_REQUEST_INVALID` | 422 | لا | 1 | BC05 | item pool ACTIVE (AGG-RESOURCE-POOL, resource_type in RD-LOGISTICS-ITEM-TYPES); quantity > 0 in pool unit; de… (LOGISTICS-REQUEST) |
| `MAINTENANCE_ORDER_REQUIRED` | 422 | لا | 1 | BC05 | maintenance order IN_PROGRESS for this asset (ASSET) |
| `MAINTENANCE_OVERLAP` | 422 | لا | 2 | BC05 | asset not DISPOSED; kind ∈ {scheduled, corrective}; window; no overlap with another non-terminal order of the… (MAINTENANCE-ORDER) |
| `MAJOR_CHANGE_REQUIRES_VERSION` | 422 | لا | 1 | BC04 | only minor fields (descriptions, notes, attachments) per BRL-005; recorded as annotation, baseline content un… (PLAN-VERSION) |
| `MANIFEST_MISMATCH` | 422 | لا | 1 | BC07 | device acknowledges manifest hash (PRELOAD-PACKAGE) |
| `MAPPING_TESTS_FAILED` | 422 | لا | 1 | BC07 | mapping tests pass; new immutable mapping version (ADAPTER) |
| `MATCH_CONTRADICTS_NOT_A_MATCH` | 422 | لا | 1 | BC02 | types compatible; neither entity RETIRED; merged cluster contains no NOT_A_MATCH pair; merged cluster size ≤… (ER-CASE) |
| `MEASUREMENT_INVALID` | 422 | لا | 1 | BC04 | value with unit convertible to metric unit (UCUM); measured_at; source = manual \| task result \| observation r… (OUTCOME-TRACKER) |
| `METHOD_BACKS_PUBLISHED_WORK` | 422 | لا | 1 | BC03 | no run of this version backs a PUBLISHED or SUPERSEDED assessment (reproducibility preserved) (ANALYSIS-METHOD) |
| `METHOD_INVALID` | 422 | لا | 1 | BC03 | code + version unique; parameter JSON schema; execution image digest from internal registry; deterministic fl… (ANALYSIS-METHOD) |
| `MIGRATION_NOT_RECONCILED` | 422 | لا | 1 | BC01 | system; export/import reconciled (TENANT) |
| `MODEL_INVALID` | 422 | لا | 1 | BC07 | family, version, weights digest in internal registry, licence reviewed, languages (must include ar and en for… (MODEL-VERSION) |
| `MODEL_IN_ACTIVE_ROUTE` | 422 | لا | 1 | BC07 | reason; routes using it must be switched first (MODEL-VERSION) |
| `NOT_ASSIGNED_REVIEWER` | 422 | لا | 1 | BC02 | actor = assigned reviewer (or Analyst lead) (CONFLICT) |
| `NOT_ASSIGNEE` | 422 | لا | 1 | BC04 | actor = assignee (TASK) |
| `NOT_A_RECIPIENT` | 422 | لا | 2 | BC03 | actor is a recipient (ALERT) |
| `NOT_RECIPIENT` | 422 | لا | 1 | BC04 | actor = recipient; content fetched through normal authorized query (NOTIFICATION) |
| `NOT_SUSPENDED` | 422 | لا | 1 | BC04 | suspend authority; suspended = true (TASK) |
| `OBSERVATION_INVALID` | 422 | لا | 1 | BC02 | source ACTIVE; location with CRS + accuracy + valid geometry; UCUM units; observed_at ≤ server time + 5 min;… (OBSERVATION) |
| `OPEN_FOLLOW_UPS` | 422 | لا | 1 | BC04 | no open follow-up tasks (TASK) |
| `OPEN_RESPONSIBILITIES` | 422 | لا | 1 | BC04 | all responsibilities done or waived; closing note (COORDINATION-CASE) |
| `ORG_IN_USE` | 422 | لا | 1 | BC01 | all non-root units inactive; no active assignments (ORGANIZATION) |
| `ORG_NAME_TAKEN` | 422 | لا | 2 | BC01 | tenant ACTIVE; name unique in tenant; creates root unit (ORGANIZATION) |
| `ORG_UNIT_CYCLE` | 422 | لا | 1 | BC01 | new parent ACTIVE, same org, not a descendant (no cycle); root cannot move (ORGANIZATION) |
| `ORG_UNIT_INVALID_PARENT` | 422 | لا | 1 | BC01 | parent unit ACTIVE; sibling name unique (ORGANIZATION) |
| `ORG_UNIT_IN_USE` | 422 | لا | 1 | BC01 | no active children; no active role assignments, grants or clearances scoped only to it (BC01 query) (ORGANIZATION) |
| `ORG_UNIT_NAME_TAKEN` | 422 | لا | 1 | BC01 | sibling name unique (ORGANIZATION) |
| `OUTCOME_REQUIRED` | 422 | لا | 1 | BC05 | outcome ∈ {serviceable, failed}; work performed; parts consumed (optional allocation refs) (MAINTENANCE-ORDER) |
| `OWNER_REJECTED` | 422 | لا | 5 | BC01, BC02, BC07 | Administrator in scope of the affected units; applies CMD-RAS-ASSIGN / CMD-RAS-REVOKE and, for leave, CMD-USR… (HR-SYNC-PROPOSAL) |
| `OWNER_REQUIRED` | 422 | لا | 2 | BC01 | owner user ACTIVE; purpose stated (SERVICE-ACCOUNT) |
| `PARTICIPANTS_REQUIRED` | 422 | لا | 1 | BC04 | ≥ 2 participants (COORDINATION-CASE) |
| `PARTICIPANT_HAS_RESPONSIBILITIES` | 422 | لا | 1 | BC04 | not the lead; no open responsibilities (COORDINATION-CASE) |
| `PARTICIPANT_INVALID` | 422 | لا | 1 | BC04 | org unit in the same tenant; participant role; access scope (sections); participant's members cleared for cas… (COORDINATION-CASE) |
| `PERSON_ALREADY_LINKED` | 422 | لا | 1 | BC01 | person ACTIVE, not linked to another user (USER) |
| `PERSON_DUPLICATE` | 422 | لا | 1 | BC01 | names per language-model; no duplicate HR id (PERSON) |
| `PLAN_EMPTY` | 422 | لا | 1 | BC02 | ≥ 1 activity; creates one field task per activity through SLC-03 with plan_ref = this collection plan (CR-59) (COLLECTION-PLAN) |
| `PLAN_INVALID` | 422 | لا | 1 | BC04 | title; owner; org scope; implements ≥ 1 decision (RECORDED) or objective (REQ-OPS-002), or for plan_kind=CONT… (PLAN) |
| `PLAN_LINK_INVALID` | 422 | لا | 1 | BC04 | سلطة؛ ينشئ/يربط Plan (SLC-08، plan_kind=CONTINGENCY، triggered_by=هذه الحادثة — CR-60)؛ أمر صريح دائماً، ليس… (INCIDENT) |
| `PLAN_NOT_COMPLETABLE` | 422 | لا | 1 | BC04 | all plan tasks terminal; every outcome has ≥ 1 measurement (PLAN) |
| `PLAN_VERSION_INCOMPLETE` | 422 | لا | 1 | BC04 | complete per REQ-OPS-001; change classification computed vs current baseline (major/minor, BRL-005) (PLAN-VERSION) |
| `PLAN_VERSION_INVALID` | 422 | لا | 1 | BC04 | objectives, outcomes (metric, unit, target, due), phases, activities (stable ids, task_generating flag, task… (PLAN-VERSION) |
| `POLICY_INVALID` | 422 | لا | 1 | BC08 | tables validate against schema (POLICY-SET) |
| `POLICY_TESTS_FAILED` | 422 | لا | 1 | BC08 | embedded policy tests all pass; tenant rules only restrict platform baseline (POLICY-SET) |
| `POOL_HAS_COMMITMENTS` | 422 | لا | 1 | BC05 | no COMMITTED or PENDING allocations (RESOURCE-POOL) |
| `POOL_INVALID` | 422 | لا | 1 | BC05 | type in RD-RESOURCE-TYPES; unit (UCUM); org scope; initial capacity; label (RESOURCE-POOL) |
| `PRELOAD_NOT_ALLOWED` | 422 | لا | 1 | BC07 | device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested level ≤ tenant offline max leve… (PRELOAD-PACKAGE) |
| `PRODUCT_INCOMPLETE` | 422 | لا | 1 | BC06 | all required sections present; AI-drafted sections reviewed (REQ-AI-005) (PRODUCT) |
| `PRODUCT_INVALID` | 422 | لا | 1 | BC06 | template ACTIVE (version pinned); parameters valid; audience (org units/roles); target label ≥ labels of scop… (PRODUCT) |
| `PRODUCT_NOT_APPROVED` | 422 | لا | 1 | BC06 | product APPROVED; recipients (users, org units); formats ⊆ {pdf, docx, in_app}; distributor authorized (DISTRIBUTION) |
| `PROJECTION_BUILD_IN_PROGRESS` | 422 | لا | 1 | BC07 | kind ∈ {search, graph, vector (R2, SLC-10)}; document schema version, embedding model version (vector), analy… (PROJECTION-VERSION) |
| `PROJECTION_NOT_VERIFIED` | 422 | لا | 1 | BC07 | operator; verification passed; previous ACTIVE of same kind → RETIRED in the same step (alias switch) (PROJECTION-VERSION) |
| `QUALIFICATION_EXPIRED` | 422 | لا | 1 | BC05 | validity not ended (QUALIFICATION-RECORD) |
| `QUALIFICATION_INVALID` | 422 | لا | 2 | BC05 | person ACTIVE; code in RD-COMPETENCIES; level valid; valid_from < valid_to; issuer; evidence ref optional (QUALIFICATION-RECORD) |
| `QUALITY_RULES_INVALID` | 422 | لا | 1 | BC07 | range, rate-of-change, stale-after, duplicate window; violations become data_quality issues, not rejections (SENSOR-STREAM) |
| `QUOTA_EXCEEDED` | 422 | لا | 1 | BC03 | definition complete; active situations per tenant ≤ quota (SITUATION) |
| `QUOTA_EXCEEDS_CAPACITY` | 422 | لا | 1 | BC01 | quotas ≤ cell capacity (TENANT) |
| `RATING_INVALID` | 422 | لا | 1 | BC02 | rating ∈ A–F; valid_from given; creates bitemporal reliability claim (SOURCE) |
| `RATIONALE_REQUIRED` | 422 | لا | 1 | BC04 | rationale ∈ {retired,accepted_permanently,materialized}؛ إن كان materialized فـ incident_ref إلزامي (INV-RIS-… (RISK) |
| `REASON_REQUIRED` | 422 | لا | 131 | BC01, BC02, BC03, BC04, BC05, BC06, BC07, BC08 | reason (AUTHORITY-GRANT) |
| `RECONSTRUCTION_INVALID` | 422 | لا | 1 | BC06 | scope (objects, situation, plan, decision basis); valid_at T; known_at K ≤ now; purpose (audit, legal, lesson… (RECONSTRUCTION) |
| `RELATIONSHIP_INVALID` | 422 | لا | 1 | BC02 | type in RD-RELATIONSHIP-TYPES; endpoint types allowed; creates identity + existence claim (valid interval, so… (RELATIONSHIP) |
| `RELEASE_NOT_ALLOWED` | 422 | لا | 1 | BC03 | tenant CAP enabled; alert RAISED/ACKNOWLEDGED; alert label ≤ tenant external release level; content = CAP fie… (CAP-MESSAGE) |
| `REPRODUCTION_NOT_ALLOWED` | 422 | لا | 1 | BC03 | source run SUCCEEDED; reproducer cleared for source run label; method version ACTIVE or DEPRECATED; copies in… (ANALYSIS-RUN) |
| `REQUIREMENT_INCOMPLETE` | 422 | لا | 1 | BC02 | area, window, priority and ≥ 1 EEI present (REQ-COL-001) (COLLECTION-REQUIREMENT) |
| `REQUIREMENT_INVALID` | 422 | لا | 3 | BC02 | question; requester; label (COLLECTION-REQUIREMENT) |
| `REQUIREMENT_NOT_APPROVED` | 422 | لا | 1 | BC02 | ≥ 1 APPROVED collection requirement; planner in scope; label ≥ requirements (COLLECTION-PLAN) |
| `RESPONSE_REQUIRED` | 422 | لا | 1 | BC04 | commander؛ ≥ 1 response_task_ref (مهام SLC-03 مرتبطة عبر incident_ref — CR-61) (INCIDENT) |
| `RESPONSE_TASKS_OPEN` | 422 | لا | 1 | BC04 | كل مهام الاستجابة في حالة نهائية (INV-INC-02)؛ ملاحظة حل (INCIDENT) |
| `RESPONSIBILITY_INVALID` | 422 | لا | 2 | BC04 | participant exists; item, due; flag requires_authority (decision type) when the action needs that organizatio… (COORDINATION-CASE) |
| `RESULT_ITEM_INVALID` | 422 | لا | 1 | BC04 | actor = assignee; item = note \| evidence URN \| observation URN \| measurement (TASK) |
| `RESULT_REQUIRED` | 422 | لا | 1 | BC04 | actor = assignee; result has ≥ 1 item (TASK) |
| `REVIEWER_NOT_AUTHORIZED` | 422 | لا | 1 | BC07 | assignee authorized on the target (SYNC-CONFLICT) |
| `REVIEWER_NOT_CLEARED` | 422 | لا | 4 | BC02, BC07 | reviewer cleared for every member claim label (CONFLICT) |
| `RISK_INVALID` | 422 | لا | 1 | BC04 | category_ref (RD-HAZARD-CATEGORIES، مرجع لكل مستأجر — نمط R2-Q1)؛ description؛ scope_refs ≥ 1 (أصل/منطقة/منظم… (RISK) |
| `ROLE_CODE_TAKEN` | 422 | لا | 1 | BC01 | code unique in tenant (ROLE) |
| `ROLE_EMPTY` | 422 | لا | 1 | BC01 | ≥ 1 permission (ROLE) |
| `ROLE_IN_USE` | 422 | لا | 1 | BC01 | not a system role; no active assignments (ROLE) |
| `ROLE_REQUIREMENT_INVALID` | 422 | لا | 2 | BC05 | role exists (BC01); requirements reference RD-COMPETENCIES (ROLE-REQUIREMENT) |
| `ROUTING_INVALID` | 422 | لا | 1 | BC07 | for each operation: model version in PRODUCTION (or STAGED with canary share), prompt template version, allow… (AI-ROUTING) |
| `RULESET_BELOW_TARGET` | 422 | لا | 1 | BC02 | evaluation meets QAS-ER-001 (candidate recall ≥ 95 %) and QAS-ER-002; approver ≠ author; previous ACTIVE → SU… (MATCH-RULESET) |
| `RULESET_INVALID` | 422 | لا | 1 | BC02 | blocking keys, features, weights, thresholds valid; evaluation run on labelled test set attached (MATCH-RULESET) |
| `RULE_BELOW_TARGET` | 422 | لا | 1 | BC02 | evaluation on a labelled set: precision ≥ 70 % of proposals (recalibrate after pilot); approver ≠ author (CORRELATION-RULE) |
| `RULE_INVALID` | 422 | لا | 2 | BC02 | kind ∈ {same_event, co_location, track_association, same_entity_hint} (CORRELATION-RULE) |
| `RUNS_IN_PROGRESS` | 422 | لا | 1 | BC03 | reason; no QUEUED or RUNNING runs (ANALYSIS-CASE) |
| `RUN_INVALID` | 422 | لا | 1 | BC03 | case OPEN; method ACTIVE; parameters valid against schema; inputs pinned (dataset refs with known_at = submis… (ANALYSIS-RUN) |
| `SCENARIO_INVALID` | 422 | لا | 2 | BC05 | title; exercise_type_ref in RD-EXERCISE-TYPES; situation; target_competencies ⊆ RD-COMPETENCIES; injects orde… (SCENARIO) |
| `SCHEDULE_INCOMPLETE` | 422 | لا | 1 | BC08 | every record class in RD-RECORD-CLASSES has exactly one rule (REQ-GOV-006); approver = Legal/Compliance autho… (RETENTION-SCHEDULE) |
| `SCHEDULE_INVALID` | 422 | لا | 1 | BC08 | each rule: record class (RD-RECORD-CLASSES), period (ISO 8601 duration), trigger ∈ {recorded, closed, superse… (RETENTION-SCHEDULE) |
| `SCHEME_INVALID` | 422 | لا | 2 | BC08 | codes immutable once used; ranks strictly ordered; removal not allowed, only deprecation (CLASSIFICATION-SCHEME) |
| `SECTION_NOT_EDITABLE` | 422 | لا | 1 | BC06 | only narrative sections; data sections change only by regeneration (PRODUCT) |
| `SECURITY_REVIEW_REQUIRED` | 422 | لا | 1 | BC07 | security review passed (injection, exfiltration, scope); approver = Security Officer (AI-TOOL) |
| `SEQUENCE_GAP` | 422 | لا | 1 | BC07 | ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed by device key; batch hash chain… (SYNC-SESSION) |
| `SEVERITY_MUST_INCREASE` | 422 | لا | 1 | BC04 | سبب؛ new_severity أعلى من الحالية فقط (INV-INC-01)؛ إشعار المستوى الأعلى (INCIDENT) |
| `SHIPMENT_INVALID` | 422 | لا | 1 | BC05 | logistics_request APPROVED; origin pool with sufficient COMMITTED allocation quantity for the linked request;… (SHIPMENT) |
| `SIGNATURE_INVALID` | 422 | لا | 1 | BC01 | signed by current key; new public key (DEVICE) |
| `SIMULATION_INVALID` | 422 | لا | 1 | BC05 | system-issued in the same unit of work as CMD-EXR-START; exercise_ref SCHEDULED transitioning to IN_PROGRESS;… (SIMULATION) |
| `SITUATION_INVALID` | 422 | لا | 2 | BC03 | name; extent (polygon or buffer around an entity); time window; criteria valid per SPEC-SITUATION §2; owner;… (SITUATION) |
| `SOD_ROLE_CONFLICT` | 422 | لا | 1 | BC01 | role ACTIVE; user not CLOSED; scope unit ACTIVE; assigner administers the scope; no SoD-incompatible active r… (ROLE-ASSIGNMENT) |
| `SOURCE_INVALID` | 422 | لا | 1 | BC02 | type in RD-SOURCE-TYPES; initial reliability A–F; person-type sources get protection_level ≥ 1 and label ≥ te… (SOURCE) |
| `STREAM_INVALID` | 422 | لا | 1 | BC07 | connection (sensor_gateway) exists; BC02 Source of type sensor ACTIVE; quantity + UCUM unit; expected rate; l… (SENSOR-STREAM) |
| `SUBSCRIPTION_EXISTS` | 422 | لا | 1 | BC04 | target (situation \| alert rule) visible to subscriber; channels ⊆ {in_app, push}; one ACTIVE per (user, targe… (SUBSCRIPTION) |
| `SUBSCRIPTION_INVALID` | 422 | لا | 1 | BC04 | channels valid; quiet hours valid (critical severity bypasses quiet hours) (SUBSCRIPTION) |
| `SUITE_INVALID` | 422 | لا | 1 | BC07 | sets: groundedness (≥ 500 items), citation, insufficient-evidence, prompt-injection, exfiltration, cross-tena… (EVAL-SUITE) |
| `SUITE_NOT_ACTIVE` | 422 | لا | 1 | BC07 | evaluation suite ACTIVE (AGG-EVAL-SUITE) (MODEL-VERSION) |
| `SYSTEM_ROLE_LOCKED` | 422 | لا | 1 | BC01 | permissions exist in catalog; system roles are locked; ACTIVE → new version (ROLE) |
| `TARGET_INVALID` | 422 | لا | 1 | BC06 | target plan/task/product visible; reuse counted (OUT-06) (KNOWLEDGE-OBJECT) |
| `TARGET_NOT_VISIBLE` | 422 | لا | 1 | BC04 | target still visible (SUBSCRIPTION) |
| `TASK_CRITERIA_NOT_MET` | 422 | لا | 1 | BC04 | attestation-type criteria confirmed by an authorized actor; all criteria satisfied (BRL-006) (TASK) |
| `TASK_INVALID` | 422 | لا | 2 | BC04 | task type ACTIVE (version pinned); plan_ref (operations, collection or contingency plan — CR-59, CR-61) or in… (TASK) |
| `TASK_NOT_READY` | 422 | لا | 1 | BC04 | title, ≥ 1 completion criterion, owner; dependencies reference existing tasks without cycle (TASK) |
| `TASK_SUSPENDED` | 422 | لا | 21 | BC04 | — |
| `TASK_TYPE_CODE_TAKEN` | 422 | لا | 1 | BC04 | code unique in tenant (TASK-TYPE) |
| `TASK_TYPE_INVALID` | 422 | لا | 2 | BC04 | required qualifications exist in RD-COMPETENCIES; criteria templates valid; ACTIVE → new version (existing ta… (TASK-TYPE) |
| `TEMPLATE_INVALID` | 422 | لا | 2 | BC06 | code unique; product kind ∈ {report, briefing, map_product, analytical_product} (PRODUCT-TEMPLATE) |
| `TENANT_NAMESPACE_TAKEN` | 422 | لا | 1 | BC01 | namespace unique; cell_mode valid for tenant profile (INV-TEN-03) (TENANT) |
| `TENANT_NOT_ACTIVE` | 422 | لا | 1 | BC01 | tenant ACTIVE; via SCIM or admin (USER) |
| `TENANT_PROVISIONING_INCOMPLETE` | 422 | لا | 1 | BC01 | system; all provisioning steps confirmed (isolation, keys, scheme, roles, quotas, audit stream) (TENANT) |
| `TOOL_INVALID` | 422 | لا | 1 | BC07 | name; input JSON schema; underlying platform query or command; effect ∈ {read, propose}; required permission;… (AI-TOOL) |
| `TREATMENT_INVALID` | 422 | لا | 1 | BC04 | treatment_strategy ∈ {avoid,reduce,transfer,accept}؛ ≥ 1 إجراء معالجة إلا عند accept (INV-RIS-03)؛ موافق مخوَ… (RISK) |

### 9.7 منصة واعتماديات

| الرمز | HTTP | إعادة | الأوامر | السياقات | مثال الشرط (Aggregate) |
|---|---|---|---|---|---|
| `AUDIT_UNAVAILABLE` | 503 | لا | — (منصة) | — | — |
| `DEPENDENCY_UNAVAILABLE` | 503 | نعم | — (منصة) | — | — |
| `ELIGIBILITY_UNAVAILABLE` | 503 | نعم | 2 | BC04 | — |
| `POLICY_ENGINE_UNAVAILABLE` | 503 (request denied) | نعم | — (منصة) | — | — |
| `RATE_LIMITED` | 429 | نعم | — (منصة) | — | — |

<!-- END GENERATED: build_analysis_design.py -->
