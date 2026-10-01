---
id: AD-14-API-DESIGN
type: api-design
title: "تصميم الواجهات البرمجية — الاصطلاحات والكتالوج الكامل"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 2)"
sources: [05-contracts/openapi-*.md, 05-contracts/errors-*.md, 03-domain/contexts/BC*/commands-*.md, 03-domain/contexts/BC*/queries-*.md, 08-security/policies-slc*.md]
generator: 17-system-study/_build/build_analysis_design.py
---

# تصميم الواجهات البرمجية (API Design)

العقد المعتمد هو ملفات OpenAPI 3.1 في `05-contracts/` (28 ملفًا، مولَّدة من المواصفات). هذا الملف يشرح الاصطلاحات المشتركة بينها ويضع **كل** عملياتها (611) في كتالوج واحد مرتب حسب السياق والمورد. في الكود، العقود تُنسخ إلى `contracts/` كما هي، والأنواع المولَّدة منها لا تتجاوز حلقة المحوّلات (ADR-P18، FIT-20).

## 1. الشكل العام

| البند | الاصطلاح | المصدر |
|---|---|---|
| العنوان الأساسي | `https://{cell}.platform.local/api/v1/<context>/<resource>` | `servers` في كل عقد |
| سياقات المسار | `foundation`، `information`، `intelligence`، `operations`، `readiness`، `knowledge`، `governance`، `integration`، `ai`، `field`، `discovery` | المسارات في العقود |
| نمط الواجهة | **مبني على المهام (task-based)** وفق CQRS: الأوامر `POST`، والاستعلامات `GET` (أو `POST` حين يكون جسم الطلب معقدًا) | 491 `POST` و120 `GET`؛ لا `PUT` ولا `PATCH` ولا `DELETE` |
| الإنشاء | `POST /…/<resources>` ← `201` | 83 عملية: 82 بفاعل بشري أو خدمة، و`CMD-SIM-START` يصدره النظام. استثناءان ينشئان من مورد قائم عبر `actions`: `CMD-AUT-DELEGATE` و`CMD-RUN-REPRODUCE` (`201`) |
| أمر على مورد | `POST /…/<resources>/{id}/actions/<verb>` ← `202` | الفعل هو فعل الأمر بحروف صغيرة |
| الاستعلام | `GET /…/<resources>` (قائمة) أو `GET /…/<resources>/{id}` (عنصر) ← `200` | 134 استعلامًا (133 في الكتالوجات + `QRY-LABEL-CHECK`): 120 `GET` و14 `POST` (§6) |
| معرّف العملية | `operationId` = معرّف الأمر أو الاستعلام في المواصفات (`CMD-TASK-ASSIGN`) | يربط الكود بالقصة والسياسة والاختبار |
| الامتدادات | أوامر: `x-aggregate`، `x-policy`، `x-events`، `x-error-codes`، `x-offline-capable`، `x-internal`؛ استعلامات: `x-authorized`، `x-requirement` | سياسة الاستعلام ليست في العقد؛ معرّفها من `08-security/policies-slc*.md` |

**لماذا لا `DELETE`:** لا يُحذف سجل فعليًا؛ الإنهاء أمر ينقل إلى حالة نهائية، والمحو إتلاف مفتاح (`05-user-stories/00-guide.md`، ضابط C-DEL).

## 2. الترويسات

| الترويسة | إلزامية في | الغرض | عند المخالفة |
|---|---|---|---|
| `Authorization: Bearer <token>` | كل العمليات | هوية المستخدم أو حساب الخدمة (OIDC — `08-security/trust-boundaries.md`) | رفض من البوابة (الرمز غير موثق في العقود — §10) |
| `Idempotency-Key` (≤ 128 حرفًا) | كل الأوامر (477) | عدم التكرار؛ يُحفظ 24 ساعة في `idempotency_keys` مع `request_hash` و`response`: التكرار بنفس الحمولة يعيد الاستجابة المحفوظة | نفس المفتاح بحمولة مختلفة ← `IDEMPOTENCY_KEY_REUSED` (422) |
| `If-Match` | كل الأوامر عدا الإنشاء (394) | الإصدار المتوقع (تزامن متفائل) | `VERSION_CONFLICT` (409)، بعد التخويل الكامل فقط |
| `X-Purpose` | كل العمليات عدا `QRY-LABEL-CHECK` (610) | غرض الوصول (`operations`، `analysis`، `audit`، `administration`… — `authorization-model.md` §2)؛ مدخل لقرار السياسة والتدقيق | `VALIDATION_FAILED` |
| `X-Correlation-Id` | كل العمليات (611) | ربط الطلب بالأحداث والسجلات (`correlation_id` في غلاف الحدث) | `VALIDATION_FAILED` |

## 3. الاستجابات

| الحالة | الجسم | متى |
|---|---|---|
| `201` | `ResourceRef` { `urn`، `id`، `version`، `state` } | إنشاء |
| `202` | `ResourceRef` | أمر على مورد قائم (مقبول ومحفوظ؛ الآثار اللاحقة عبر الأحداث)؛ وكذلك الاستعلام `QRY-AUD-VERIFY` لأنه يبدأ عملية تحقق |
| `200` | العنصر، أو `Page` { `items`، `next_cursor` } | استعلام |
| `4xx` / `5xx` | `ApiError` { `code`، `message`، `details`، `correlation_id`، `trace_id`، `retryable`، `policy` { `decision`، `reason_code` } } | خطأ |

## 4. الأخطاء المشتركة

الرموز الأربعة العامة (`VALIDATION_FAILED`، `AUTHZ_DENIED`، `VERSION_CONFLICT`، `IDEMPOTENCY_KEY_REUSED`) ورموز المنصة (`RATE_LIMITED`، `POLICY_ENGINE_UNAVAILABLE`، `AUDIT_UNAVAILABLE`) ممكنة في كل أمر ولا تُكرَّر في الكتالوج. أما رموز الانتقال والشروط فعمود «أخطاء خاصة» يذكرها لكل عملية. الكتالوج الكامل للأخطاء (306 رموز) في `05-contracts/errors-*.md` ويُفصَّل في `18-error-handling.md` (المرحلة 4).

| الرمز | HTTP | إعادة المحاولة | المعنى |
|---|---|---|---|
| `VALIDATION_FAILED` | 400 | لا | حقل إلزامي مفقود أو غير صالح |
| `AUTHZ_DENIED` | 403→404 | لا | السياسة ترفض. المورد غير المرئي يُعاد `404` بنفس شكل غير الموجود (ADR-P06 البند 5)؛ ويُعاد `403` لمورد يراه المستخدم دون أن يحق له الإجراء (ADR-P19)؛ إعلان `403` في العقود بـCR-75 |
| `MFA_STEP_UP_REQUIRED` | 401 | نعم، بعد المصادقة المعززة | التزام `mfa` غير مستوفى؛ تحدٍّ بقوة المصادقة المطلوبة، وإعادة بنفس `Idempotency-Key` (ADR-P19؛ يُضاف بـCR-75) |
| `APPROVAL_REQUIRED` | 403 | لا | قرار `REQUIRE_APPROVAL`؛ `details.approver` يسمي دور المعتمِد (ADR-P19؛ يُضاف بـCR-75) |
| `NOT_FOUND` | 404 | لا | المورد غير موجود أو غير مرئي |
| `VERSION_CONFLICT` | 409 | نعم (بعد إعادة تحميل المورد وإعادة بناء الأمر) | `If-Match` لا يطابق |
| `*_INVALID_STATE_TRANSITION` | 409 | لا | الأمر غير مسموح من الحالة الحالية |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | نفس المفتاح بحمولة مختلفة |
| أخطاء الشروط (`*_INVALID`، `REASON_REQUIRED`، `SEGREGATION_OF_DUTIES`…) | 422 | لا | شرط انتقال أو قاعدة لم تتحقق |
| `RATE_LIMITED` | 429 | نعم | تجاوز حصة المستأجر |
| `POLICY_ENGINE_UNAVAILABLE` | 503 | نعم | محرك السياسات غير متاح ← الطلب مرفوض (FIT-16) |
| `AUDIT_UNAVAILABLE` | 503 | لا | مخزن التدقيق معطل وتراكمت السجلات محليًا أكثر من 24 ساعة أو 80 % من السعة ← تُرفض **الأوامر المغيرة للحالة** فقط؛ قبل ذلك تستمر الأوامر (`08-security/audit-architecture.md`) |

## 5. القوائم والزمن

| البند | الاصطلاح | المصدر |
|---|---|---|
| الترقيم | بمؤشر فقط: `cursor` و`limit` (1–200، الافتراضي 50)؛ لا إزاحة | FIT-13؛ 74 استعلامًا |
| النطاق | `allowed_scope` من قرار السياسة يُطبَّق قبل العدّ والترتيب والترقيم | ADR-P06، CR-47 |
| الزمن المزدوج | `valid_at` (متى كان صحيحًا) و`known_at` (متى عُرف) | 16 استعلامًا؛ ADR-P01 |
| البحث | `QRY-SRCH-QUERY` بجسم طلب (`text`، `types`، `geo`، `time`، `valid_at`، `filters`، `facets`، `sort`، `cursor`، `limit`)؛ `q` (إلزامي) في `QRY-SRCH-SUGGEST`؛ `depth` في `QRY-GRAPH-NEIGHBORHOOD` | استعلامات BC07 للاكتشاف |

## 6. استعلامات بـ`POST`

14 استعلامًا تستخدم `POST` لأن مدخلاتها بنية لا تناسب معاملات الرابط (بحث، مسارات رسم بياني، فحوص مجمّعة، تنزيل). هي **استعلامات** لا تغيّر الحالة، فلا تحمل `Idempotency-Key` ولا `If-Match`: `QRY-SRCH-QUERY`، `QRY-GRAPH-PATHS`، `QRY-LABEL-CHECK`، `QRY-AUT-CHECK`، `QRY-PDP-DECIDE`، `QRY-AUD-VERIFY`، `QRY-LHD-CHECK`، `QRY-ATT-DOWNLOAD`، `QRY-RUN-ARTIFACT`، `QRY-KNO-SUGGEST`، `QRY-ARC-RETRIEVE`، `QRY-ELIG-CHECK`، `QRY-AST-AVAILABILITY`، `QRY-READINESS`.

## 7. الواجهات الداخلية ودون اتصال

| الفئة | العمليات | الاصطلاح |
|---|---|---|
| داخلية (6) | `CMD-TEN-COMPLETE-PROVISIONING`، `CMD-TEN-FAIL-PROVISIONING`، `CMD-TEN-COMPLETE-CELL-MIGRATION`، `CMD-TEN-COMPLETE-DECOMMISSION`، `CMD-USR-RECORD-FIRST-SIGN-IN` (في `openapi-foundation-internal-slc01.md`)، و`CMD-SIM-START` (`x-internal: true` داخل عقد readiness العام) | يستدعيها النظام بهوية عبء عمل؛ البوابة لا تعرض أي عملية تحمل `x-internal` أو تقع في عقد داخلي |
| دون اتصال | `x-offline-capable: true` على 6 أوامر (`CMD-TASK-ACCEPT`، `START`، `BLOCK`، `RESUME`، `ADD-RESULT-ITEM`، `SUBMIT`)؛ و`CommandEnvelope` في `openapi-field-slc11.md` يقبل 12 أمرًا (تلك الستة + `CMD-OBS-RECORD`، `CMD-OBS-AMEND`، `CMD-OBS-ATTACH-EVIDENCE`، `CMD-EVD-REGISTER`، `CMD-ATT-INITIATE-UPLOAD`، `CMD-ATT-COMPLETE-UPLOAD`) | الجهاز ينفذها محليًا ويرسلها في جلسة مزامنة داخل `CommandEnvelope` { `client_command_id` (ULID)، `seq`، `prev_hash`، `base_version`، `device_time`، `target_command`، `target_urn`، `payload`، `signature` }؛ عدم مطابقة `base_version` يفتح تعارض مزامنة بدل `VERSION_CONFLICT` (ADR-P09، `11-hexagonal-reference.md` §8). الفرق بين 6 و12 **[Needs Review]** |
| العقود العابرة | `QRY-LABEL-CHECK` على `/api/v1/{context}/label-checks` | يقدمه كل سياق يملك موارد معلَّمة، لإعادة فحص العلامات مجمّعة (CR-47) |

## 8. الإصدارات

- الإصدار في المسار (`/api/v1`). التغيير الكاسر يتطلب إصدارًا رئيسيًا جديدًا (FIT-14)، والإصدار الرئيسي السابق يبقى مدعومًا 6 أشهر على الأقل (QAS-EVO-001، ADR-P18).
- العقد يُولَّد من المواصفات؛ لا يُعدَّل يدويًا، و`contracts/` في المستودع يجب أن يطابق ناتج المولِّد (FIT-20).

## 9. من العقد إلى الكود

| عنصر العقد | الموقع في الكود (ADR-P17، `13-project-structure.md`) |
|---|---|
| مسار + طريقة | محوّل HTTP وارد في وحدة النشر؛ يحوّل الأنواع المولَّدة إلى أمر أو استعلام التطبيق |
| `operationId` = `CMD-*` | معالج أمر واحد في حلقة التطبيق، يمر بخط الأوامر ذي الخطوات العشر |
| `operationId` = `QRY-*` | معالج استعلام واحد يقرأ نموذج قراءة أو إسقاطًا، لا الـAggregate |
| `x-policy` | معرّف السياسة الذي يرسله منفذ التخويل إلى محرك السياسات |
| `x-events` | الأحداث التي يكتبها المعالج في الـoutbox داخل نفس المعاملة |
| `x-error-codes` | أخطاء المجال التي يحوّلها المحوّل إلى `ApiError` بحالة HTTP من §4 |
| `ApiError.policy.decision` | قيمة قرار السياسة: `ALLOW`، `DENY`، `CONDITIONAL`، `REDACT`، `AGGREGATE`، `REQUIRE_APPROVAL` (`authorization-model.md`) |
| أنواع حقول الحمولة | في قصة كل أمر (`05-user-stories/`) وكتالوج الأوامر، لا في هذا الكتالوج؛ المعرّفات `Urn` بالنمط `^urn:[a-z0-9-]+:[a-z0-9-]+:<ULID>$` (ADR-P13) |

## 10. فجوات وملاحظات

| البند | الحالة |
|---|---|
| استعلامات التاريخ لإعادة البناء: لا يوجد استعلام تاريخ عام للـAggregate إلا `QRY-TASK-HISTORY` (توجد استعلامات إصدارات وخطوط زمنية خاصة مثل `QRY-ASM-VERSIONS`) | **[Missing]** (مسجل في `11-hexagonal-reference.md` §8) |
| `403` مذكور في ترويسة `errors-*.md` لكن لا عملية تعلنه في العقود | محسوم: `403` للمورد المرئي (ADR-P19)؛ إعلانه في العقود بـCR-75 (جولة تصحيح المصادر) |
| التزام قبل التنفيذ غير مستوفى (MFA، موافقة — ADR-P17 الخطوة 6) بلا رمز خطأ في أي `errors-*.md` | محسوم: `MFA_STEP_UP_REQUIRED` و`APPROVAL_REQUIRED` (ADR-P19)؛ إضافتهما بـCR-75 |
| `CMD-SIM-START` داخلي (`x-internal`) لكنه في عقد عام | محسوم: يُنقل إلى عقد داخلي (CR-76، قرار مالك المشروع 2026-10-01) |
| رموز رفض البوابة (المصادقة، حجم الطلب، نوع المحتوى) غير موثقة في العقود | **[Missing]** — تُضاف في `18-error-handling.md` |

## 11. الكتالوج

الكتالوج مرتب حسب السياق ثم المورد (أول ثلاثة مقاطع بعد `/api/v1`). عمود «النوع» من تصنيف العمليات في `05-user-stories/00-guide.md` §4، و«المدخلات» حقول جسم الطلب للأوامر (`!` = إلزامي) ومعاملات الرابط للاستعلامات. قصة كل عملية في `05-user-stories/us-bcNN.md` بمعرّف `US-BCnn-<المعرّف بلا البادئة>`.

<!-- BEGIN GENERATED: build_analysis_design.py -->

### ملخص الكتالوج

إجمالي العمليات: **611**.

| BC | أوامر | استعلامات | داخلية | المجموع |
|---|---|---|---|---|
| BC01 | 67 | 10 | 5 | 77 |
| BC02 | 92 | 27 | 0 | 119 |
| BC03 | 52 | 17 | 0 | 69 |
| BC04 | 82 | 21 | 0 | 103 |
| BC05 | 69 | 20 | 1 | 89 |
| BC06 | 29 | 8 | 0 | 37 |
| BC07 | 58 | 19 | 0 | 77 |
| BC08 | 28 | 11 | 0 | 39 |
| — | 0 | 1 | 0 | 1 |

#### BC01 — Foundation — الأساس

##### `/api/v1/foundation/authority-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/authority-checks` | QRY-AUT-CHECK | جلب | POL-AUT-CHECK | actor!, decision_type!, scope!, at!, amount | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/foundation/authority-grants`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/foundation/authority-grants` | QRY-AUT-LIST | جلب | POL-AUT-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/foundation/authority-grants` | CMD-AUT-GRANT | إنشاء | POL-AUT-GRANT | holder!, decision_types!, org_scope!, include_descendants!, limits, valid_from!, valid_to, delegable! | 201, 400, 404, 409, 422, 429, 503 | PERMISSION_DENIED |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/approve-grant` | CMD-AUT-APPROVE-GRANT | سير عمل | POL-AUT-APPROVE-GRANT | — | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/delegate` | CMD-AUT-DELEGATE | إنشاء | POL-AUT-DELEGATE | delegate!, decision_types!, org_scope!, include_descendants!, limits, valid_from!, valid_to!, delegable! | 201, 400, 404, 409, 422, 429, 503 | AUTHORITY_EXCEEDS_DELEGATOR |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/reject-grant` | CMD-AUT-REJECT-GRANT | حذف / إنهاء | POL-AUT-REJECT-GRANT | reason! | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/resume` | CMD-AUT-RESUME | سير عمل | POL-AUT-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, GRANT_EXPIRED |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/revoke` | CMD-AUT-REVOKE | حذف / إنهاء | POL-AUT-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/foundation/authority-grants/{id}/actions/suspend` | CMD-AUT-SUSPEND | سير عمل | POL-AUT-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_GRANT_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/foundation/clearances`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/clearances` | CMD-CLR-GRANT | إنشاء | POL-CLR-GRANT | user!, level!, compartments!, caveat_attributes, valid_to | 201, 400, 404, 409, 422, 429, 503 | CLEARANCE_EXISTS |
| POST | `/api/v1/foundation/clearances/{id}/actions/approve` | CMD-CLR-APPROVE | سير عمل | POL-CLR-APPROVE | — | 202, 400, 404, 409, 422, 429, 503 | CLEARANCE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/foundation/clearances/{id}/actions/modify` | CMD-CLR-MODIFY | تعديل | POL-CLR-MODIFY | level!, compartments!, caveat_attributes | 202, 400, 404, 409, 422, 429, 503 | CLEARANCE_INVALID, CLEARANCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/clearances/{id}/actions/reinstate` | CMD-CLR-REINSTATE | سير عمل | POL-CLR-REINSTATE | — | 202, 400, 404, 409, 422, 429, 503 | CLEARANCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/clearances/{id}/actions/revoke` | CMD-CLR-REVOKE | حذف / إنهاء | POL-CLR-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | CLEARANCE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/foundation/clearances/{id}/actions/suspend` | CMD-CLR-SUSPEND | سير عمل | POL-CLR-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | CLEARANCE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/foundation/devices`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/foundation/devices` | QRY-DEV-LIST | جلب | POL-DEV-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/foundation/devices` | CMD-DEV-ENROLL | إنشاء | POL-DEV-ENROLL | user!, public_key!, platform!, mdm_ref | 201, 400, 404, 409, 422, 429, 503 | DEVICE_LIMIT_REACHED |
| POST | `/api/v1/foundation/devices/{id}/actions/confirm` | CMD-DEV-CONFIRM | سير عمل | POL-DEV-CONFIRM | attestation! | 202, 400, 404, 409, 422, 429, 503 | ATTESTATION_FAILED, DEVICE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/devices/{id}/actions/reinstate` | CMD-DEV-REINSTATE | سير عمل | POL-DEV-REINSTATE | reason! | 202, 400, 404, 409, 422, 429, 503 | DEVICE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/foundation/devices/{id}/actions/report-lost` | CMD-DEV-REPORT-LOST | سير عمل | POL-DEV-REPORT-LOST | lost_at!, note | 202, 400, 404, 409, 422, 429, 503 | DEVICE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/devices/{id}/actions/retire` | CMD-DEV-RETIRE | حذف / إنهاء | POL-DEV-RETIRE | reason!, override | 202, 400, 404, 409, 422, 429, 503 | DEVICE_INVALID_STATE_TRANSITION, DEVICE_NOT_WIPED |
| POST | `/api/v1/foundation/devices/{id}/actions/rotate-key` | CMD-DEV-ROTATE-KEY | تعديل | POL-DEV-ROTATE-KEY | new_public_key!, signature! | 202, 400, 404, 409, 422, 429, 503 | DEVICE_INVALID_STATE_TRANSITION, SIGNATURE_INVALID |
| POST | `/api/v1/foundation/devices/{id}/actions/suspend` | CMD-DEV-SUSPEND | سير عمل | POL-DEV-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | DEVICE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/foundation/hr-sync-proposals`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/foundation/hr-sync-proposals` | QRY-HRS-QUEUE | جلب | POL-HRS-QUEUE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/foundation/hr-sync-proposals/{id}/actions/approve` | CMD-HRS-APPROVE | حذف / إنهاء | POL-HRS-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION, OWNER_REJECTED |
| POST | `/api/v1/foundation/hr-sync-proposals/{id}/actions/reject` | CMD-HRS-REJECT | حذف / إنهاء | POL-HRS-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/foundation/me`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/foundation/me/security-context` | QRY-SEC-CONTEXT | جلب | POL-SEC-CONTEXT | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/foundation/organizations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/organizations` | CMD-ORG-CREATE | إنشاء | POL-ORG-CREATE | name!, root_unit_name! | 201, 400, 404, 409, 422, 429, 503 | ORG_NAME_TAKEN |
| POST | `/api/v1/foundation/organizations/{id}/actions/add-unit` | CMD-ORG-ADD-UNIT | تعديل | POL-ORG-ADD-UNIT | parent_unit!, name! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_INVALID_PARENT |
| POST | `/api/v1/foundation/organizations/{id}/actions/deactivate` | CMD-ORG-DEACTIVATE | سير عمل | POL-ORG-DEACTIVATE | reason! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_IN_USE |
| POST | `/api/v1/foundation/organizations/{id}/actions/deactivate-unit` | CMD-ORG-DEACTIVATE-UNIT | تعديل | POL-ORG-DEACTIVATE-UNIT | unit!, reason! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_IN_USE |
| POST | `/api/v1/foundation/organizations/{id}/actions/move-unit` | CMD-ORG-MOVE-UNIT | تعديل | POL-ORG-MOVE-UNIT | unit!, new_parent! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_CYCLE |
| POST | `/api/v1/foundation/organizations/{id}/actions/reactivate` | CMD-ORG-REACTIVATE | سير عمل | POL-ORG-REACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/organizations/{id}/actions/rename` | CMD-ORG-RENAME | تعديل | POL-ORG-RENAME | name! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_NAME_TAKEN |
| POST | `/api/v1/foundation/organizations/{id}/actions/rename-unit` | CMD-ORG-RENAME-UNIT | تعديل | POL-ORG-RENAME-UNIT | unit!, name! | 202, 400, 404, 409, 422, 429, 503 | ORGANIZATION_INVALID_STATE_TRANSITION, ORG_UNIT_NAME_TAKEN |
| GET | `/api/v1/foundation/organizations/{org_id}/units` | QRY-ORG-TREE | جلب | POL-ORG-TREE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/foundation/persons`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/persons` | CMD-PER-REGISTER | إنشاء | POL-PER-REGISTER | names!, hr_id, contact | 201, 400, 404, 409, 422, 429, 503 | PERSON_DUPLICATE |
| POST | `/api/v1/foundation/persons/{id}/actions/deactivate` | CMD-PER-DEACTIVATE | سير عمل | POL-PER-DEACTIVATE | reason! | 202, 400, 404, 409, 422, 429, 503 | PERSON_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/persons/{id}/actions/erase` | CMD-PER-ERASE | حذف / إنهاء | POL-PER-ERASE | erasure_order_ref! | 202, 400, 404, 409, 422, 429, 503 | LEGAL_HOLD_ACTIVE, PERSON_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/persons/{id}/actions/reactivate` | CMD-PER-REACTIVATE | سير عمل | POL-PER-REACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | PERSON_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/persons/{id}/actions/update-details` | CMD-PER-UPDATE-DETAILS | تعديل | POL-PER-UPDATE-DETAILS | names, contact | 202, 400, 404, 409, 422, 429, 503 | PERSON_INVALID_STATE_TRANSITION |

##### `/api/v1/foundation/role-assignments`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/role-assignments` | CMD-RAS-ASSIGN | إنشاء | POL-RAS-ASSIGN | user!, role!, org_scope!, include_descendants!, valid_from!, valid_to | 201, 400, 404, 409, 422, 429, 503 | SOD_ROLE_CONFLICT |
| POST | `/api/v1/foundation/role-assignments/{id}/actions/revoke` | CMD-RAS-REVOKE | حذف / إنهاء | POL-RAS-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, ROLE_ASSIGNMENT_INVALID_STATE_TRANSITION |

##### `/api/v1/foundation/roles`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/roles` | CMD-ROL-DEFINE | إنشاء | POL-ROL-DEFINE | code!, name! | 201, 400, 404, 409, 422, 429, 503 | ROLE_CODE_TAKEN |
| POST | `/api/v1/foundation/roles/{id}/actions/activate` | CMD-ROL-ACTIVATE | سير عمل | POL-ROL-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | ROLE_EMPTY, ROLE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/roles/{id}/actions/retire` | CMD-ROL-RETIRE | حذف / إنهاء | POL-ROL-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | ROLE_INVALID_STATE_TRANSITION, ROLE_IN_USE |
| POST | `/api/v1/foundation/roles/{id}/actions/set-permissions` | CMD-ROL-SET-PERMISSIONS | تعديل | POL-ROL-SET-PERMISSIONS | permissions! | 202, 400, 404, 409, 422, 429, 503 | ROLE_INVALID_STATE_TRANSITION, SYSTEM_ROLE_LOCKED |

##### `/api/v1/foundation/service-accounts`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/service-accounts` | CMD-SVC-CREATE | إنشاء | POL-SVC-CREATE | name!, owner!, purpose! | 201, 400, 404, 409, 422, 429, 503 | OWNER_REQUIRED |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/close` | CMD-SVC-CLOSE | حذف / إنهاء | POL-SVC-CLOSE | — | 202, 400, 404, 409, 422, 429, 503 | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/disable` | CMD-SVC-DISABLE | سير عمل | POL-SVC-DISABLE | reason | 202, 400, 404, 409, 422, 429, 503 | SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/enable` | CMD-SVC-ENABLE | سير عمل | POL-SVC-ENABLE | — | 202, 400, 404, 409, 422, 429, 503 | OWNER_REQUIRED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/service-accounts/{id}/actions/rotate-credential` | CMD-SVC-ROTATE-CREDENTIAL | تعديل | POL-SVC-ROTATE-CREDENTIAL | public_key!, expires_at! | 202, 400, 404, 409, 422, 429, 503 | CREDENTIAL_LIFETIME_EXCEEDED, SERVICE_ACCOUNT_INVALID_STATE_TRANSITION |

##### `/api/v1/foundation/tenants`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/foundation/tenants` | CMD-TEN-PROVISION | إنشاء | POL-TEN-PROVISION | namespace!, display_name!, cell_mode!, sovereign!, top_level_enabled!, jurisdiction!, quotas! | 201, 400, 404, 409, 422, 429, 503 | TENANT_NAMESPACE_TAKEN |
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-cell-migration` | CMD-TEN-COMPLETE-CELL-MIGRATION | نظام (داخلي) | POL-TEN-COMPLETE-CELL-MIGRATION | reconciliation_report! | 202, 400, 404, 409, 422, 429, 503 | MIGRATION_NOT_RECONCILED, TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-decommission` | CMD-TEN-COMPLETE-DECOMMISSION | نظام (داخلي) | POL-TEN-COMPLETE-DECOMMISSION | — | 202, 400, 404, 409, 422, 429, 503 | TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/complete-provisioning` | CMD-TEN-COMPLETE-PROVISIONING | نظام (داخلي) | POL-TEN-COMPLETE-PROVISIONING | steps! | 202, 400, 404, 409, 422, 429, 503 | TENANT_INVALID_STATE_TRANSITION, TENANT_PROVISIONING_INCOMPLETE |
| POST | `/api/v1/foundation/tenants/{id}/actions/fail-provisioning` | CMD-TEN-FAIL-PROVISIONING | نظام (داخلي) | POL-TEN-FAIL-PROVISIONING | failed_step!, reason! | 202, 400, 404, 409, 422, 429, 503 | TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/reactivate` | CMD-TEN-REACTIVATE | سير عمل | POL-TEN-REACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/retry-provisioning` | CMD-TEN-RETRY-PROVISIONING | سير عمل | POL-TEN-RETRY-PROVISIONING | — | 202, 400, 404, 409, 422, 429, 503 | TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/start-cell-migration` | CMD-TEN-START-CELL-MIGRATION | سير عمل | POL-TEN-START-CELL-MIGRATION | target_cell! | 202, 400, 404, 409, 422, 429, 503 | CELL_UNAVAILABLE, TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/start-decommission` | CMD-TEN-START-DECOMMISSION | سير عمل | POL-TEN-START-DECOMMISSION | reason!, second_approver! | 202, 400, 404, 409, 422, 429, 503 | LEGAL_HOLD_ACTIVE, TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/suspend` | CMD-TEN-SUSPEND | سير عمل | POL-TEN-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TENANT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/tenants/{id}/actions/update-quotas` | CMD-TEN-UPDATE-QUOTAS | تعديل | POL-TEN-UPDATE-QUOTAS | quotas! | 202, 400, 404, 409, 422, 429, 503 | QUOTA_EXCEEDS_CAPACITY, TENANT_INVALID_STATE_TRANSITION |
| GET | `/api/v1/foundation/tenants/{tenant_id}` | QRY-TEN-GET | جلب | POL-TEN-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/foundation/users`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/foundation/users` | QRY-USR-LIST | جلب | POL-USR-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/foundation/users` | CMD-USR-PROVISION | إنشاء | POL-USR-PROVISION | username!, person, source! | 201, 400, 404, 409, 422, 429, 503 | TENANT_NOT_ACTIVE |
| POST | `/api/v1/foundation/users/{id}/actions/close` | CMD-USR-CLOSE | حذف / إنهاء | POL-USR-CLOSE | reason! | 202, 400, 404, 409, 422, 429, 503 | USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/disable` | CMD-USR-DISABLE | سير عمل | POL-USR-DISABLE | reason | 202, 400, 404, 409, 422, 429, 503 | USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/enable` | CMD-USR-ENABLE | سير عمل | POL-USR-ENABLE | — | 202, 400, 404, 409, 422, 429, 503 | LAST_IDENTITY, USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/link-identity` | CMD-USR-LINK-IDENTITY | تعديل | POL-USR-LINK-IDENTITY | issuer!, subject! | 202, 400, 404, 409, 422, 429, 503 | IDENTITY_ALREADY_LINKED, USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/link-person` | CMD-USR-LINK-PERSON | تعديل | POL-USR-LINK-PERSON | person! | 202, 400, 404, 409, 422, 429, 503 | PERSON_ALREADY_LINKED, USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/lock` | CMD-USR-LOCK | سير عمل | POL-USR-LOCK | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/record-first-sign-in` | CMD-USR-RECORD-FIRST-SIGN-IN | نظام (داخلي) | POL-USR-RECORD-FIRST-SIGN-IN | issuer!, subject! | 202, 400, 404, 409, 422, 429, 503 | USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/unlink-identity` | CMD-USR-UNLINK-IDENTITY | تعديل | POL-USR-UNLINK-IDENTITY | issuer!, subject! | 202, 400, 404, 409, 422, 429, 503 | LAST_IDENTITY, USER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/foundation/users/{id}/actions/unlock` | CMD-USR-UNLOCK | سير عمل | POL-USR-UNLOCK | reason! | 202, 400, 404, 409, 422, 429, 503 | USER_INVALID_STATE_TRANSITION |
| GET | `/api/v1/foundation/users/{user_id}` | QRY-USR-GET | جلب | POL-USR-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/foundation/users/{user_id}/clearance` | QRY-CLR-GET | جلب | POL-CLR-GET | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC02 — Information — نواة المعلومات

##### `/api/v1/information/attachments`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/attachments` | CMD-ATT-INITIATE-UPLOAD | إنشاء | POL-ATT-INITIATE-UPLOAD | client_id, sha256!, size_bytes!, mime_type!, file_name, label! | 201, 400, 404, 409, 422, 429, 503 | ATTACHMENT_REJECTED |
| POST | `/api/v1/information/attachments/{attachment_id}/download-grants` | QRY-ATT-DOWNLOAD | جلب | POL-ATT-DOWNLOAD | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/attachments/{id}/actions/complete-upload` | CMD-ATT-COMPLETE-UPLOAD | سير عمل | POL-ATT-COMPLETE-UPLOAD | — | 202, 400, 404, 409, 422, 429, 503 | ATTACHMENT_INVALID_STATE_TRANSITION, HASH_MISMATCH |
| POST | `/api/v1/information/attachments/{id}/actions/erase` | CMD-ATT-ERASE | حذف / إنهاء | POL-ATT-ERASE | erasure_order_ref! | 202, 400, 404, 409, 422, 429, 503 | ATTACHMENT_INVALID_STATE_TRANSITION, LEGAL_HOLD_ACTIVE |

##### `/api/v1/information/claims`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/claims` | CMD-CLM-ASSERT | إنشاء | POL-CLM-ASSERT | subject!, predicate!, value!, valid!, source_refs!, derived_from, confidence!, label! | 201, 400, 404, 409, 422, 429, 503 | CLAIM_INVALID |
| GET | `/api/v1/information/claims/{claim_id}` | QRY-CLM-GET | جلب | POL-CLM-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/claims/{id}/actions/assess` | CMD-CLM-ASSESS | تعديل | POL-CLM-ASSESS | information_confidence, verification_status, rationale! | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID, CLAIM_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/claims/{id}/actions/correct` | CMD-CLM-CORRECT | تعديل | POL-CLM-CORRECT | value!, valid, source_refs!, confidence!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLAIM_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/claims/{id}/actions/reclassify` | CMD-CLM-RECLASSIFY | تعديل | POL-CLM-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLAIM_INVALID_STATE_TRANSITION, CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| POST | `/api/v1/information/claims/{id}/actions/record-change` | CMD-CLM-RECORD-CHANGE | حذف / إنهاء | POL-CLM-RECORD-CHANGE | t_change!, new_value!, source_refs!, confidence! | 202, 400, 404, 409, 422, 429, 503 | CHANGE_TIME_INVALID, CLAIM_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/claims/{id}/actions/retract` | CMD-CLM-RETRACT | تعديل | POL-CLM-RETRACT | reason! | 202, 400, 404, 409, 422, 429, 503 | CLAIM_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/collection-plans`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/collection-plans` | CMD-CPL-CREATE | إنشاء | POL-CPL-CREATE | requirements!, title!, label! | 201, 400, 404, 409, 422, 429, 503 | REQUIREMENT_NOT_APPROVED |
| POST | `/api/v1/information/collection-plans/{id}/actions/activate` | CMD-CPL-ACTIVATE | سير عمل | POL-CPL-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_PLAN_INVALID_STATE_TRANSITION, PLAN_EMPTY |
| POST | `/api/v1/information/collection-plans/{id}/actions/add-activity` | CMD-CPL-ADD-ACTIVITY | تعديل | POL-CPL-ADD-ACTIVITY | method!, sources!, area!, window!, unit!, task_type!, eei_refs! | 202, 400, 404, 409, 422, 429, 503 | ACTIVITY_INVALID, COLLECTION_PLAN_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/collection-plans/{id}/actions/cancel` | CMD-CPL-CANCEL | حذف / إنهاء | POL-CPL-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/collection-plans/{id}/actions/complete` | CMD-CPL-COMPLETE | حذف / إنهاء | POL-CPL-COMPLETE | reason! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/collection-plans/{id}/actions/remove-activity` | CMD-CPL-REMOVE-ACTIVITY | تعديل | POL-CPL-REMOVE-ACTIVITY | activity_id! | 202, 400, 404, 409, 422, 429, 503 | ACTIVITY_ALREADY_TASKED, COLLECTION_PLAN_INVALID_STATE_TRANSITION |
| GET | `/api/v1/information/collection-plans/{plan_id}` | QRY-CPL-GET | جلب | POL-CPL-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/collection-requirements`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/collection-requirements` | QRY-CRQ-BOARD | جلب | POL-CRQ-BOARD | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/collection-requirements` | CMD-CRQ-DRAFT | إنشاء | POL-CRQ-DRAFT | question!, label! | 201, 400, 404, 409, 422, 429, 503 | REQUIREMENT_INVALID |
| POST | `/api/v1/information/collection-requirements/{id}/actions/amend` | CMD-CRQ-AMEND | تعديل | POL-CRQ-AMEND | due, area, eeis, reason! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, REQUIREMENT_INVALID |
| POST | `/api/v1/information/collection-requirements/{id}/actions/approve` | CMD-CRQ-APPROVE | سير عمل | POL-CRQ-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/information/collection-requirements/{id}/actions/cancel` | CMD-CRQ-CANCEL | حذف / إنهاء | POL-CRQ-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/collection-requirements/{id}/actions/edit` | CMD-CRQ-EDIT | تعديل | POL-CRQ-EDIT | area!, window!, priority!, due!, eeis! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, REQUIREMENT_INVALID |
| POST | `/api/v1/information/collection-requirements/{id}/actions/mark-satisfied` | CMD-CRQ-MARK-SATISFIED | حذف / إنهاء | POL-CRQ-MARK-SATISFIED | acceptance_note | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, FULFILMENT_INSUFFICIENT |
| POST | `/api/v1/information/collection-requirements/{id}/actions/reject` | CMD-CRQ-REJECT | حذف / إنهاء | POL-CRQ-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/collection-requirements/{id}/actions/submit` | CMD-CRQ-SUBMIT | سير عمل | POL-CRQ-SUBMIT | — | 202, 400, 404, 409, 422, 429, 503 | COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION, REQUIREMENT_INCOMPLETE |
| GET | `/api/v1/information/collection-requirements/{requirement_id}` | QRY-CRQ-GET | جلب | POL-CRQ-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/information/collection-requirements/{requirement_id}/fulfilment` | QRY-CRQ-EVIDENCE | جلب | POL-CRQ-EVIDENCE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/conflicts`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/conflicts` | QRY-CNF-LIST | جلب | POL-CNF-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/conflicts` | CMD-CNF-RAISE | إنشاء | POL-CNF-RAISE | claims!, predicate!, note | 201, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID |
| GET | `/api/v1/information/conflicts/{conflict_id}` | QRY-CNF-GET | جلب | POL-CNF-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/conflicts/{id}/actions/accept` | CMD-CNF-ACCEPT | سير عمل | POL-CNF-ACCEPT | rationale! | 202, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/conflicts/{id}/actions/assign` | CMD-CNF-ASSIGN | تعديل | POL-CNF-ASSIGN | reviewer! | 202, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID_STATE_TRANSITION, REVIEWER_NOT_CLEARED |
| POST | `/api/v1/information/conflicts/{id}/actions/reopen` | CMD-CNF-REOPEN | سير عمل | POL-CNF-REOPEN | reason!, evidence | 202, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/conflicts/{id}/actions/resolve` | CMD-CNF-RESOLVE | سير عمل | POL-CNF-RESOLVE | preferred_claim!, rationale!, evidence | 202, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/information/conflicts/{id}/actions/start-review` | CMD-CNF-START-REVIEW | سير عمل | POL-CNF-START-REVIEW | — | 202, 400, 404, 409, 422, 429, 503 | CONFLICT_INVALID_STATE_TRANSITION, NOT_ASSIGNED_REVIEWER |

##### `/api/v1/information/correlation-proposals`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/correlation-proposals` | QRY-CRP-QUEUE | جلب | POL-CRP-QUEUE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/correlation-proposals` | CMD-CRP-PROPOSE | إنشاء | POL-CRP-PROPOSE | kind!, inputs!, rationale! | 201, 400, 404, 409, 422, 429, 503 | CORRELATION_INVALID |
| POST | `/api/v1/information/correlation-proposals/{id}/actions/accept` | CMD-CRP-ACCEPT | حذف / إنهاء | POL-CRP-ACCEPT | note | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, OWNER_REJECTED |
| POST | `/api/v1/information/correlation-proposals/{id}/actions/reject` | CMD-CRP-REJECT | حذف / إنهاء | POL-CRP-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/correlation-proposals/{id}/actions/start-review` | CMD-CRP-START-REVIEW | سير عمل | POL-CRP-START-REVIEW | — | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_PROPOSAL_INVALID_STATE_TRANSITION, REVIEWER_NOT_CLEARED |
| GET | `/api/v1/information/correlation-proposals/{proposal_id}` | QRY-CRP-GET | جلب | POL-CRP-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/correlation-rules`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/correlation-rules` | CMD-CRR-DEFINE | إنشاء | POL-CRR-DEFINE | kind!, name! | 201, 400, 404, 409, 422, 429, 503 | RULE_INVALID |
| POST | `/api/v1/information/correlation-rules/{id}/actions/activate` | CMD-CRR-ACTIVATE | سير عمل | POL-CRR-ACTIVATE | evaluation_report! | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_RULE_INVALID_STATE_TRANSITION, RULE_BELOW_TARGET |
| POST | `/api/v1/information/correlation-rules/{id}/actions/edit` | CMD-CRR-EDIT | تعديل | POL-CRR-EDIT | parameters! | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_RULE_INVALID_STATE_TRANSITION, RULE_INVALID |
| POST | `/api/v1/information/correlation-rules/{id}/actions/retire` | CMD-CRR-RETIRE | حذف / إنهاء | POL-CRR-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | CORRELATION_RULE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/entities`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/entities` | QRY-ENT-LIST | جلب | POL-ENT-LIST | valid_at, known_at, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/entities` | CMD-ENT-REGISTER | إنشاء | POL-ENT-REGISTER | entity_type!, label!, initial_claims, external_ids | 201, 400, 404, 409, 422, 429, 503 | ENTITY_INVALID |
| GET | `/api/v1/information/entities/{entity_id}` | QRY-ENT-RESOLVED | جلب | POL-ENT-RESOLVED | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/information/entities/{entity_id}/claims` | QRY-ENT-CLAIMS | جلب | POL-ENT-CLAIMS | valid_at, known_at, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/information/entities/{entity_id}/identity-cluster` | QRY-CLUSTER-GET | جلب | POL-CLUSTER-GET | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/information/entities/{entity_id}/positions` | QRY-ENT-POSITIONS | جلب | POL-ENT-POSITIONS | valid_at, known_at, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/information/entities/{entity_id}/relationships` | QRY-REL-LIST | جلب | POL-REL-LIST | valid_at, known_at, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/entities/{id}/actions/change-type` | CMD-ENT-CHANGE-TYPE | تعديل | POL-ENT-CHANGE-TYPE | entity_type!, reason! | 202, 400, 404, 409, 422, 429, 503 | ENTITY_INVALID_STATE_TRANSITION, ENTITY_TYPE_INCOMPATIBLE |
| POST | `/api/v1/information/entities/{id}/actions/reclassify` | CMD-ENT-RECLASSIFY | تعديل | POL-ENT-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, ENTITY_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/entities/{id}/actions/reinstate` | CMD-ENT-REINSTATE | سير عمل | POL-ENT-REINSTATE | reason! | 202, 400, 404, 409, 422, 429, 503 | ENTITY_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/entities/{id}/actions/retire` | CMD-ENT-RETIRE | سير عمل | POL-ENT-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | ENTITY_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/er-cases`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/er-cases` | QRY-ER-QUEUE | جلب | POL-ER-QUEUE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/er-cases` | CMD-ER-PROPOSE | إنشاء | POL-ER-PROPOSE | left!, right!, rationale!, agent | 201, 400, 404, 409, 422, 429, 503 | ER_PAIR_INVALID |
| GET | `/api/v1/information/er-cases/{case_id}` | QRY-ER-GET | جلب | POL-ER-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/er-cases/{id}/actions/confirm-match` | CMD-ER-CONFIRM-MATCH | سير عمل | POL-ER-CONFIRM-MATCH | rationale! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/information/er-cases/{id}/actions/decide-match` | CMD-ER-DECIDE-MATCH | سير عمل | POL-ER-DECIDE-MATCH | rationale!, second_reviewer | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, MATCH_CONTRADICTS_NOT_A_MATCH |
| POST | `/api/v1/information/er-cases/{id}/actions/decide-not-match` | CMD-ER-DECIDE-NOT-MATCH | حذف / إنهاء | POL-ER-DECIDE-NOT-MATCH | rationale! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/er-cases/{id}/actions/park` | CMD-ER-PARK | سير عمل | POL-ER-PARK | rationale! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/er-cases/{id}/actions/request-split` | CMD-ER-REQUEST-SPLIT | سير عمل | POL-ER-REQUEST-SPLIT | reason!, evidence | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/er-cases/{id}/actions/resume` | CMD-ER-RESUME | سير عمل | POL-ER-RESUME | reason! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/er-cases/{id}/actions/split` | CMD-ER-SPLIT | حذف / إنهاء | POL-ER-SPLIT | rationale!, record_not_a_match! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/information/er-cases/{id}/actions/start-review` | CMD-ER-START-REVIEW | سير عمل | POL-ER-START-REVIEW | — | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REVIEWER_NOT_CLEARED |
| POST | `/api/v1/information/er-cases/{id}/actions/withdraw` | CMD-ER-WITHDRAW | حذف / إنهاء | POL-ER-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | ER_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/events`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/events` | CMD-RWE-REGISTER | إنشاء | POL-RWE-REGISTER | event_type!, label!, initial_claims! | 201, 400, 404, 409, 422, 429, 503 | EVENT_INVALID |
| GET | `/api/v1/information/events/{event_id}` | QRY-RWE-GET | جلب | POL-RWE-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/events/{id}/actions/change-type` | CMD-RWE-CHANGE-TYPE | تعديل | POL-RWE-CHANGE-TYPE | event_type!, reason! | 202, 400, 404, 409, 422, 429, 503 | EVENT_TYPE_INCOMPATIBLE, REALWORLD_EVENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/events/{id}/actions/reclassify` | CMD-RWE-RECLASSIFY | تعديل | POL-RWE-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, REALWORLD_EVENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/events/{id}/actions/reinstate` | CMD-RWE-REINSTATE | سير عمل | POL-RWE-REINSTATE | reason! | 202, 400, 404, 409, 422, 429, 503 | REALWORLD_EVENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/events/{id}/actions/retire` | CMD-RWE-RETIRE | سير عمل | POL-RWE-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REALWORLD_EVENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/evidence`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/evidence` | CMD-EVD-REGISTER | إنشاء | POL-EVD-REGISTER | client_id, evidence_type!, attachment, observation_ref, locator, source!, collected_at!, label! | 201, 400, 404, 409, 422, 429, 503 | EVIDENCE_INVALID |
| GET | `/api/v1/information/evidence/{evidence_id}` | QRY-EVD-GET | جلب | POL-EVD-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/evidence/{id}/actions/reclassify` | CMD-EVD-RECLASSIFY | تعديل | POL-EVD-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, EVIDENCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/evidence/{id}/actions/seal` | CMD-EVD-SEAL | سير عمل | POL-EVD-SEAL | — | 202, 400, 404, 409, 422, 429, 503 | EVIDENCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/evidence/{id}/actions/transfer-custody` | CMD-EVD-TRANSFER-CUSTODY | تعديل | POL-EVD-TRANSFER-CUSTODY | new_holder!, action! | 202, 400, 404, 409, 422, 429, 503 | CUSTODY_INVALID, EVIDENCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/evidence/{id}/actions/update-locator` | CMD-EVD-UPDATE-LOCATOR | تعديل | POL-EVD-UPDATE-LOCATOR | locator! | 202, 400, 404, 409, 422, 429, 503 | EVIDENCE_INVALID_STATE_TRANSITION, LOCATOR_INVALID |
| POST | `/api/v1/information/evidence/{id}/actions/withdraw` | CMD-EVD-WITHDRAW | حذف / إنهاء | POL-EVD-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | EVIDENCE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/evidence-links`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/evidence-links` | CMD-EVL-LINK | إنشاء | POL-EVL-LINK | evidence!, claim!, stance!, note | 201, 400, 404, 409, 422, 429, 503 | LINK_DUPLICATE |
| POST | `/api/v1/information/evidence-links/{id}/actions/unlink` | CMD-EVL-UNLINK | حذف / إنهاء | POL-EVL-UNLINK | reason! | 202, 400, 404, 409, 422, 429, 503 | EVIDENCE_LINK_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/information/external-ids`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/external-ids` | CMD-EXT-MAP | إنشاء | POL-EXT-MAP | system!, external_id!, object!, valid_from! | 201, 400, 404, 409, 422, 429, 503 | EXTERNAL_ID_TAKEN |
| POST | `/api/v1/information/external-ids/{id}/actions/end` | CMD-EXT-END | حذف / إنهاء | POL-EXT-END | valid_to!, reason! | 202, 400, 404, 409, 422, 429, 503 | EXTERNAL_ID_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/information/external-ids/{system}/{external_id}` | QRY-EXT-RESOLVE | جلب | POL-EXT-RESOLVE | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/import-batches`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/import-batches` | CMD-IMP-SUBMIT | إنشاء | POL-IMP-SUBMIT | adapter!, batch_key!, content_sha256!, format!, payload_attachment! | 201, 400, 404, 409, 422, 429, 503 | BATCH_KEY_REUSED |
| GET | `/api/v1/information/import-batches/{batch_id}` | QRY-IMP-GET | جلب | POL-IMP-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/import-batches/{id}/actions/accept-quarantine` | CMD-IMP-ACCEPT-QUARANTINE | حذف / إنهاء | POL-IMP-ACCEPT-QUARANTINE | reason! | 202, 400, 404, 409, 422, 429, 503 | IMPORT_BATCH_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/import-batches/{id}/actions/cancel` | CMD-IMP-CANCEL | حذف / إنهاء | POL-IMP-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | IMPORT_BATCH_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/import-batches/{id}/actions/reprocess-quarantine` | CMD-IMP-REPROCESS-QUARANTINE | سير عمل | POL-IMP-REPROCESS-QUARANTINE | mapping_version, corrections | 202, 400, 404, 409, 422, 429, 503 | IMPORT_BATCH_INVALID_STATE_TRANSITION |

##### `/api/v1/information/lineage`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/lineage/{object_urn}` | QRY-LIN-TRACE | جلب | POL-LIN-TRACE | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/match-rulesets`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/match-rulesets` | CMD-MRS-DRAFT | إنشاء | POL-MRS-DRAFT | entity_type!, based_on | 201, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/match-rulesets/{id}/actions/activate` | CMD-MRS-ACTIVATE | سير عمل | POL-MRS-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | MATCH_RULESET_INVALID_STATE_TRANSITION, RULESET_BELOW_TARGET |
| POST | `/api/v1/information/match-rulesets/{id}/actions/edit` | CMD-MRS-EDIT | تعديل | POL-MRS-EDIT | blocking_keys!, features!, thresholds!, evaluation_attachment! | 202, 400, 404, 409, 422, 429, 503 | MATCH_RULESET_INVALID_STATE_TRANSITION, RULESET_INVALID |
| GET | `/api/v1/information/match-rulesets/{ruleset_id}` | QRY-MRS-GET | جلب | POL-MRS-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/observations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/information/observations` | QRY-OBS-LIST | جلب | POL-OBS-LIST | valid_at, known_at, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/information/observations` | CMD-OBS-RECORD | إنشاء | POL-OBS-RECORD | client_id, source!, observer!, observed_at!, event_time, location!, method!, measurements, narrative, attachments, label!, field_session, device | 201, 400, 404, 409, 422, 429, 503 | OBSERVATION_INVALID |
| POST | `/api/v1/information/observations/{id}/actions/amend` | CMD-OBS-AMEND | تعديل | POL-OBS-AMEND | changes!, reason! | 202, 400, 404, 409, 422, 429, 503 | OBSERVATION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/observations/{id}/actions/attach-evidence` | CMD-OBS-ATTACH-EVIDENCE | تعديل | POL-OBS-ATTACH-EVIDENCE | evidence! | 202, 400, 404, 409, 422, 429, 503 | EVIDENCE_INVALID, OBSERVATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/observations/{id}/actions/reclassify` | CMD-OBS-RECLASSIFY | تعديل | POL-OBS-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, OBSERVATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/observations/{id}/actions/reject` | CMD-OBS-REJECT | حذف / إنهاء | POL-OBS-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | OBSERVATION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/information/observations/{id}/actions/validate` | CMD-OBS-VALIDATE | حذف / إنهاء | POL-OBS-VALIDATE | note | 202, 400, 404, 409, 422, 429, 503 | OBSERVATION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| GET | `/api/v1/information/observations/{observation_id}` | QRY-OBS-GET | جلب | POL-OBS-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/information/relationships`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/relationships` | CMD-REL-REGISTER | إنشاء | POL-REL-REGISTER | relationship_type!, source_ref!, target_ref!, valid!, source_refs!, label! | 201, 400, 404, 409, 422, 429, 503 | RELATIONSHIP_INVALID |
| POST | `/api/v1/information/relationships/{id}/actions/reclassify` | CMD-REL-RECLASSIFY | تعديل | POL-REL-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, RELATIONSHIP_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/relationships/{id}/actions/reinstate` | CMD-REL-REINSTATE | سير عمل | POL-REL-REINSTATE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, RELATIONSHIP_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/relationships/{id}/actions/retire` | CMD-REL-RETIRE | سير عمل | POL-REL-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, RELATIONSHIP_INVALID_STATE_TRANSITION |

##### `/api/v1/information/sources`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/information/sources` | CMD-SRC-REGISTER | إنشاء | POL-SRC-REGISTER | type!, name!, owner_org!, reliability!, valid_from!, protection_level, label! | 201, 400, 404, 409, 422, 429, 503 | SOURCE_INVALID |
| POST | `/api/v1/information/sources/{id}/actions/rate-reliability` | CMD-SRC-RATE-RELIABILITY | تعديل | POL-SRC-RATE-RELIABILITY | reliability!, valid_from!, rationale! | 202, 400, 404, 409, 422, 429, 503 | RATING_INVALID, SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/reclassify` | CMD-SRC-RECLASSIFY | تعديل | POL-SRC-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/reinstate` | CMD-SRC-REINSTATE | سير عمل | POL-SRC-REINSTATE | — | 202, 400, 404, 409, 422, 429, 503 | SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/retire` | CMD-SRC-RETIRE | حذف / إنهاء | POL-SRC-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/set-protection` | CMD-SRC-SET-PROTECTION | تعديل | POL-SRC-SET-PROTECTION | protection_level!, second_approver | 202, 400, 404, 409, 422, 429, 503 | SEGREGATION_OF_DUTIES, SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/suspend` | CMD-SRC-SUSPEND | سير عمل | POL-SRC-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SOURCE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/information/sources/{id}/actions/update-profile` | CMD-SRC-UPDATE-PROFILE | تعديل | POL-SRC-UPDATE-PROFILE | name, contact | 202, 400, 404, 409, 422, 429, 503 | SOURCE_INVALID_STATE_TRANSITION |
| GET | `/api/v1/information/sources/{source_id}` | QRY-SRC-GET | جلب | POL-SRC-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC03 — Intelligence — الوعي والتحليل

##### `/api/v1/intelligence/alert-rules`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/intelligence/alert-rules` | CMD-ARL-DEFINE | إنشاء | POL-ARL-DEFINE | situation, scope!, kind!, parameters!, severity!, dedupe_window!, escalation, auto_resolve!, label! | 201, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/activate` | CMD-ARL-ACTIVATE | سير عمل | POL-ARL-ACTIVATE | dry_run_ref! | 202, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID_STATE_TRANSITION, DRY_RUN_REQUIRED |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/disable` | CMD-ARL-DISABLE | سير عمل | POL-ARL-DISABLE | reason! | 202, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/edit` | CMD-ARL-EDIT | تعديل | POL-ARL-EDIT | parameters!, severity, dedupe_window, escalation | 202, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID, ALERT_RULE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/enable` | CMD-ARL-ENABLE | سير عمل | POL-ARL-ENABLE | — | 202, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/alert-rules/{id}/actions/retire` | CMD-ARL-RETIRE | حذف / إنهاء | POL-ARL-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | ALERT_RULE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/intelligence/alerts`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/alerts` | QRY-ALR-LIST | جلب | POL-ALR-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/alerts/{id}/actions/acknowledge` | CMD-ALR-ACKNOWLEDGE | سير عمل | POL-ALR-ACKNOWLEDGE | note | 202, 400, 404, 409, 422, 429, 503 | ALERT_INVALID_STATE_TRANSITION, NOT_A_RECIPIENT |
| POST | `/api/v1/intelligence/alerts/{id}/actions/dismiss` | CMD-ALR-DISMISS | حذف / إنهاء | POL-ALR-DISMISS | reason! | 202, 400, 404, 409, 422, 429, 503 | ALERT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/alerts/{id}/actions/resolve` | CMD-ALR-RESOLVE | حذف / إنهاء | POL-ALR-RESOLVE | note! | 202, 400, 404, 409, 422, 429, 503 | ALERT_INVALID_STATE_TRANSITION, NOT_A_RECIPIENT |

##### `/api/v1/intelligence/analysis-cases`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/analysis-cases` | QRY-ACS-LIST | جلب | POL-ACS-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/analysis-cases` | CMD-ACS-CREATE | إنشاء | POL-ACS-CREATE | title!, owner!, label! | 201, 400, 404, 409, 422, 429, 503 | CASE_INVALID |
| GET | `/api/v1/intelligence/analysis-cases/{case_id}` | QRY-ACS-GET | جلب | POL-ACS-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/analysis-cases/{case_id}/findings` | QRY-FND-LIST | جلب | POL-FND-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/analysis-cases/{case_id}/scenario-comparison` | QRY-SCN-COMPARE | جلب | POL-SCN-COMPARE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/add-assumption` | CMD-ACS-ADD-ASSUMPTION | تعديل | POL-ACS-ADD-ASSUMPTION | statement!, criticality! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_INVALID |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/add-hypothesis` | CMD-ACS-ADD-HYPOTHESIS | تعديل | POL-ACS-ADD-HYPOTHESIS | statement! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_INVALID |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/cancel` | CMD-ACS-CANCEL | حذف / إنهاء | POL-ACS-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_HAS_PUBLISHED_ASSESSMENT |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/close` | CMD-ACS-CLOSE | سير عمل | POL-ACS-CLOSE | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, RUNS_IN_PROGRESS |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/define` | CMD-ACS-DEFINE | تعديل | POL-ACS-DEFINE | question!, extent, window! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_INVALID |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/define-scenario` | CMD-ACS-DEFINE-SCENARIO | تعديل | POL-ACS-DEFINE-SCENARIO | name!, assumptions!, parameter_overrides | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_INVALID |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/deselect-evidence` | CMD-ACS-DESELECT-EVIDENCE | تعديل | POL-ACS-DESELECT-EVIDENCE | selection_id!, reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/open` | CMD-ACS-OPEN | سير عمل | POL-ACS-OPEN | — | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CASE_NOT_DEFINED |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/reclassify` | CMD-ACS-RECLASSIFY | تعديل | POL-ACS-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/reopen` | CMD-ACS-REOPEN | سير عمل | POL-ACS-REOPEN | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/retire-assumption` | CMD-ACS-RETIRE-ASSUMPTION | تعديل | POL-ACS-RETIRE-ASSUMPTION | assumption_id!, reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/select-evidence` | CMD-ACS-SELECT-EVIDENCE | تعديل | POL-ACS-SELECT-EVIDENCE | items!, note | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, EVIDENCE_ABOVE_CASE_LABEL |
| POST | `/api/v1/intelligence/analysis-cases/{id}/actions/update-hypothesis` | CMD-ACS-UPDATE-HYPOTHESIS | تعديل | POL-ACS-UPDATE-HYPOTHESIS | hypothesis_id!, status!, rationale!, findings | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/intelligence/analysis-methods`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/analysis-methods` | QRY-AMT-LIST | جلب | POL-AMT-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/analysis-methods` | CMD-AMT-REGISTER | إنشاء | POL-AMT-REGISTER | code!, version!, parameter_schema!, image_digest!, deterministic!, description! | 201, 400, 404, 409, 422, 429, 503 | METHOD_INVALID |
| POST | `/api/v1/intelligence/analysis-methods/{id}/actions/activate` | CMD-AMT-ACTIVATE | سير عمل | POL-AMT-ACTIVATE | validation_report! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/intelligence/analysis-methods/{id}/actions/deprecate` | CMD-AMT-DEPRECATE | سير عمل | POL-AMT-DEPRECATE | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/analysis-methods/{id}/actions/retire` | CMD-AMT-RETIRE | حذف / إنهاء | POL-AMT-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_METHOD_INVALID_STATE_TRANSITION, METHOD_BACKS_PUBLISHED_WORK |

##### `/api/v1/intelligence/analysis-runs`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/intelligence/analysis-runs` | CMD-RUN-SUBMIT | إنشاء | POL-RUN-SUBMIT | case!, method!, parameters!, inputs!, scenario, assumptions, seed, label! | 201, 400, 404, 409, 422, 429, 503 | RUN_INVALID |
| POST | `/api/v1/intelligence/analysis-runs/{id}/actions/cancel` | CMD-RUN-CANCEL | حذف / إنهاء | POL-RUN-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | ANALYSIS_RUN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/analysis-runs/{id}/actions/reproduce` | CMD-RUN-REPRODUCE | إنشاء | POL-RUN-REPRODUCE | source_run! | 201, 400, 404, 409, 422, 429, 503 | REPRODUCTION_NOT_ALLOWED |
| GET | `/api/v1/intelligence/analysis-runs/{run_id}` | QRY-RUN-GET | جلب | POL-RUN-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/analysis-runs/{run_id}/artifact-grants` | QRY-RUN-ARTIFACT | جلب | POL-RUN-ARTIFACT | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/intelligence/assessments`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/intelligence/assessments` | CMD-ASM-DRAFT | إنشاء | POL-ASM-DRAFT | case!, assessment, title!, label! | 201, 400, 404, 409, 422, 429, 503 | DRAFT_EXISTS |
| GET | `/api/v1/intelligence/assessments/{assessment_id}` | QRY-ASM-GET | جلب | POL-ASM-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/assessments/{assessment_id}/versions` | QRY-ASM-VERSIONS | جلب | POL-ASM-VERSIONS | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/assessments/{id}/actions/discard` | CMD-ASM-DISCARD | حذف / إنهاء | POL-ASM-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/assessments/{id}/actions/edit` | CMD-ASM-EDIT | تعديل | POL-ASM-EDIT | key_judgments!, citations!, assumptions!, uncertainty!, confidence!, methodology!, limitations! | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID, ASSESSMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/assessments/{id}/actions/publish` | CMD-ASM-PUBLISH | سير عمل | POL-ASM-PUBLISH | note | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/intelligence/assessments/{id}/actions/return` | CMD-ASM-RETURN | سير عمل | POL-ASM-RETURN | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/assessments/{id}/actions/submit` | CMD-ASM-SUBMIT | سير عمل | POL-ASM-SUBMIT | — | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INCOMPLETE, ASSESSMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/assessments/{id}/actions/withdraw` | CMD-ASM-WITHDRAW | حذف / إنهاء | POL-ASM-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSESSMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/intelligence/base-maps`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/base-maps/{layer}/{z}/{x}/{y}` | QRY-BASE-TILE | جلب | POL-BASE-TILE | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/intelligence/cap-messages`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/cap-messages` | QRY-CAP-LIST | جلب | POL-CAP-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/cap-messages` | CMD-CAP-PREPARE | إنشاء | POL-CAP-PREPARE | alert!, template!, connection! | 201, 400, 404, 409, 422, 429, 503 | RELEASE_NOT_ALLOWED |
| POST | `/api/v1/intelligence/cap-messages/{id}/actions/cancel` | CMD-CAP-CANCEL | حذف / إنهاء | POL-CAP-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | CAP_MESSAGE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/intelligence/cap-messages/{id}/actions/release` | CMD-CAP-RELEASE | حذف / إنهاء | POL-CAP-RELEASE | note | 202, 400, 404, 409, 422, 429, 503 | CAP_MESSAGE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/intelligence/cap-messages/{id}/actions/retry` | CMD-CAP-RETRY | سير عمل | POL-CAP-RETRY | — | 202, 400, 404, 409, 422, 429, 503 | CAP_MESSAGE_INVALID_STATE_TRANSITION |

##### `/api/v1/intelligence/findings`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/intelligence/findings` | CMD-FND-RECORD | إنشاء | POL-FND-RECORD | case!, statement!, sources!, uncertainty!, label! | 201, 400, 404, 409, 422, 429, 503 | FINDING_INVALID |
| POST | `/api/v1/intelligence/findings/{id}/actions/accept` | CMD-FND-ACCEPT | سير عمل | POL-FND-ACCEPT | note | 202, 400, 404, 409, 422, 429, 503 | FINDING_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/intelligence/findings/{id}/actions/edit` | CMD-FND-EDIT | تعديل | POL-FND-EDIT | statement, sources, uncertainty | 202, 400, 404, 409, 422, 429, 503 | FINDING_INVALID, FINDING_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/findings/{id}/actions/withdraw` | CMD-FND-WITHDRAW | حذف / إنهاء | POL-FND-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | FINDING_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/intelligence/situations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/intelligence/situations` | QRY-SIT-LIST | جلب | POL-SIT-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/intelligence/situations` | CMD-SIT-CREATE | إنشاء | POL-SIT-CREATE | name!, extent!, window!, criteria!, owner!, label! | 201, 400, 404, 409, 422, 429, 503 | SITUATION_INVALID |
| POST | `/api/v1/intelligence/situations/{id}/actions/activate` | CMD-SIT-ACTIVATE | سير عمل | POL-SIT-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | QUOTA_EXCEEDED, SITUATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/close` | CMD-SIT-CLOSE | حذف / إنهاء | POL-SIT-CLOSE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SITUATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/edit-definition` | CMD-SIT-EDIT-DEFINITION | تعديل | POL-SIT-EDIT-DEFINITION | extent, window, criteria, reason! | 202, 400, 404, 409, 422, 429, 503 | SITUATION_INVALID, SITUATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/pause` | CMD-SIT-PAUSE | سير عمل | POL-SIT-PAUSE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SITUATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/reclassify` | CMD-SIT-RECLASSIFY | تعديل | POL-SIT-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, SITUATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/intelligence/situations/{id}/actions/resume` | CMD-SIT-RESUME | سير عمل | POL-SIT-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | SITUATION_INVALID_STATE_TRANSITION |
| GET | `/api/v1/intelligence/situations/{situation_id}` | QRY-SIT-GET | جلب | POL-SIT-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/situations/{situation_id}/changes` | QRY-SIT-CHANGES | جلب | POL-SIT-CHANGES | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/situations/{situation_id}/picture` | QRY-SIT-COP | جلب | POL-SIT-COP | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/intelligence/situations/{situation_id}/tiles/{layer}/{z}/{x}/{y}` | QRY-SIT-TILE | جلب | POL-SIT-TILE | — | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC04 — Operations — التخطيط والتنفيذ

##### `/api/v1/operations/coordination-cases`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/coordination-cases` | QRY-CRD-LIST | جلب | POL-CRD-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/coordination-cases` | CMD-CRD-OPEN | إنشاء | POL-CRD-OPEN | title!, purpose!, lead_org!, links, label! | 201, 400, 404, 409, 422, 429, 503 | COORDINATION_INVALID |
| GET | `/api/v1/operations/coordination-cases/{case_id}` | QRY-CRD-GET | جلب | POL-CRD-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/activate` | CMD-CRD-ACTIVATE | سير عمل | POL-CRD-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, PARTICIPANTS_REQUIRED |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/add-participant` | CMD-CRD-ADD-PARTICIPANT | تعديل | POL-CRD-ADD-PARTICIPANT | org_unit!, role!, access_scope! | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, PARTICIPANT_INVALID |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/assign-responsibility` | CMD-CRD-ASSIGN-RESPONSIBILITY | تعديل | POL-CRD-ASSIGN-RESPONSIBILITY | participant!, item!, due!, requires_authority | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, RESPONSIBILITY_INVALID |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/cancel` | CMD-CRD-CANCEL | حذف / إنهاء | POL-CRD-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/close` | CMD-CRD-CLOSE | حذف / إنهاء | POL-CRD-CLOSE | note! | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, OPEN_RESPONSIBILITIES |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/remove-participant` | CMD-CRD-REMOVE-PARTICIPANT | تعديل | POL-CRD-REMOVE-PARTICIPANT | org_unit!, reason! | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, PARTICIPANT_HAS_RESPONSIBILITIES |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/request-decision` | CMD-CRD-REQUEST-DECISION | تعديل | POL-CRD-REQUEST-DECISION | responsibility_id!, question!, options! | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, RESPONSIBILITY_INVALID |
| POST | `/api/v1/operations/coordination-cases/{id}/actions/update-responsibility` | CMD-CRD-UPDATE-RESPONSIBILITY | تعديل | POL-CRD-UPDATE-RESPONSIBILITY | responsibility_id!, status!, note | 202, 400, 404, 409, 422, 429, 503 | COORDINATION_CASE_INVALID_STATE_TRANSITION, DECISION_PENDING |

##### `/api/v1/operations/decision-requests`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/decision-requests` | QRY-DRQ-LIST | جلب | POL-DRQ-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/decision-requests` | CMD-DRQ-CREATE | إنشاء | POL-DRQ-CREATE | question!, decision_type!, scope!, deadline!, context_refs, label! | 201, 400, 404, 409, 422, 429, 503 | DECISION_REQUEST_INVALID |
| POST | `/api/v1/operations/decision-requests/{id}/actions/add-option` | CMD-DRQ-ADD-OPTION | تعديل | POL-DRQ-ADD-OPTION | text!, expected_impact | 202, 400, 404, 409, 422, 429, 503 | DECISION_REQUEST_INVALID, DECISION_REQUEST_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/decision-requests/{id}/actions/cite` | CMD-DRQ-CITE | تعديل | POL-DRQ-CITE | citations! | 202, 400, 404, 409, 422, 429, 503 | CITATION_ABOVE_LABEL, DECISION_REQUEST_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/decision-requests/{id}/actions/open` | CMD-DRQ-OPEN | سير عمل | POL-DRQ-OPEN | — | 202, 400, 404, 409, 422, 429, 503 | DECISION_REQUEST_INCOMPLETE, DECISION_REQUEST_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/decision-requests/{id}/actions/withdraw` | CMD-DRQ-WITHDRAW | حذف / إنهاء | POL-DRQ-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | DECISION_REQUEST_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/operations/decision-requests/{request_id}` | QRY-DRQ-GET | جلب | POL-DRQ-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/operations/decisions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/decisions` | CMD-DEC-RECORD | إنشاء | POL-DEC-RECORD | request, selected_option!, rationale!, effective_from!, citations, supersedes, ad_hoc_reason, label! | 201, 400, 404, 409, 422, 429, 503 | AUTHORITY_REQUIRED |
| GET | `/api/v1/operations/decisions/{decision_id}` | QRY-DEC-GET | جلب | POL-DEC-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/decisions/{decision_id}/basis` | QRY-DEC-BASIS | جلب | POL-DEC-BASIS | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/decisions/{id}/actions/annul` | CMD-DEC-ANNUL | حذف / إنهاء | POL-DEC-ANNUL | reason! | 202, 400, 404, 409, 422, 429, 503 | AUTHORITY_REQUIRED, DECISION_INVALID_STATE_TRANSITION |

##### `/api/v1/operations/incidents`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/incidents` | QRY-INC-LIST | جلب | POL-INC-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/incidents` | CMD-INC-REPORT | إنشاء | POL-INC-REPORT | category_ref!, description!, scope_refs!, risk_ref, label! | 201, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID |
| POST | `/api/v1/operations/incidents/{id}/actions/activate-contingency` | CMD-INC-ACTIVATE-CONTINGENCY | تعديل | POL-INC-ACTIVATE-CONTINGENCY | plan_template_ref! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, PLAN_LINK_INVALID |
| POST | `/api/v1/operations/incidents/{id}/actions/assess` | CMD-INC-ASSESS | سير عمل | POL-INC-ASSESS | severity!, affected_scope_refs! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID, INCIDENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/incidents/{id}/actions/cancel` | CMD-INC-CANCEL | حذف / إنهاء | POL-INC-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/incidents/{id}/actions/close` | CMD-INC-CLOSE | حذف / إنهاء | POL-INC-CLOSE | closing_note!, after_action_ref | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/incidents/{id}/actions/contain` | CMD-INC-CONTAIN | سير عمل | POL-INC-CONTAIN | containment_note! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/incidents/{id}/actions/de-escalate` | CMD-INC-DE-ESCALATE | تعديل | POL-INC-DE-ESCALATE | reason!, new_severity! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/incidents/{id}/actions/dispatch-response` | CMD-INC-DISPATCH-RESPONSE | سير عمل | POL-INC-DISPATCH-RESPONSE | commander!, response_task_refs! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, RESPONSE_REQUIRED |
| POST | `/api/v1/operations/incidents/{id}/actions/escalate` | CMD-INC-ESCALATE | تعديل | POL-INC-ESCALATE | reason!, new_severity! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, SEVERITY_MUST_INCREASE |
| POST | `/api/v1/operations/incidents/{id}/actions/resolve` | CMD-INC-RESOLVE | سير عمل | POL-INC-RESOLVE | resolution_note! | 202, 400, 404, 409, 422, 429, 503 | INCIDENT_INVALID_STATE_TRANSITION, RESPONSE_TASKS_OPEN |
| GET | `/api/v1/operations/incidents/{incident_id}` | QRY-INC-GET | جلب | POL-INC-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/incidents/{incident_id}/recovery-status` | QRY-INC-RECOVERY-STATUS | جلب | POL-INC-RECOVERY-STATUS | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/operations/notifications`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/notifications` | QRY-NTF-INBOX | جلب | POL-NTF-INBOX | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/notifications/{id}/actions/mark-read` | CMD-NTF-MARK-READ | حذف / إنهاء | POL-NTF-MARK-READ | — | 202, 400, 404, 409, 422, 429, 503 | NOTIFICATION_INVALID_STATE_TRANSITION, NOT_RECIPIENT |

##### `/api/v1/operations/outcome-trackers`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/outcome-trackers/{id}/actions/correct` | CMD-OUT-CORRECT | تعديل | POL-OUT-CORRECT | measurement_id!, value!, unit!, reason! | 202, 400, 404, 409, 422, 429, 503 | OUTCOME_TRACKER_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/outcome-trackers/{id}/actions/record` | CMD-OUT-RECORD | تعديل | POL-OUT-RECORD | value!, unit!, measured_at!, source!, source_ref, note | 202, 400, 404, 409, 422, 429, 503 | MEASUREMENT_INVALID, OUTCOME_TRACKER_INVALID_STATE_TRANSITION |

##### `/api/v1/operations/plan-versions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/plan-versions` | CMD-PLV-DRAFT | إنشاء | POL-PLV-DRAFT | plan!, based_on | 201, 400, 404, 409, 422, 429, 503 | DRAFT_EXISTS |
| POST | `/api/v1/operations/plan-versions/{id}/actions/amend-minor` | CMD-PLV-AMEND-MINOR | تعديل | POL-PLV-AMEND-MINOR | annotations! | 202, 400, 404, 409, 422, 429, 503 | MAJOR_CHANGE_REQUIRES_VERSION, PLAN_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/plan-versions/{id}/actions/approve` | CMD-PLV-APPROVE | سير عمل | POL-PLV-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/operations/plan-versions/{id}/actions/discard` | CMD-PLV-DISCARD | حذف / إنهاء | POL-PLV-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/plan-versions/{id}/actions/edit` | CMD-PLV-EDIT | تعديل | POL-PLV-EDIT | objectives!, outcomes!, constraints, assumptions, phases!, activities!, milestones, dependencies, resource_notes | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INVALID, PLAN_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/plan-versions/{id}/actions/reject` | CMD-PLV-REJECT | حذف / إنهاء | POL-PLV-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/plan-versions/{id}/actions/return` | CMD-PLV-RETURN | سير عمل | POL-PLV-RETURN | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/plan-versions/{id}/actions/submit` | CMD-PLV-SUBMIT | سير عمل | POL-PLV-SUBMIT | — | 202, 400, 404, 409, 422, 429, 503 | PLAN_VERSION_INCOMPLETE, PLAN_VERSION_INVALID_STATE_TRANSITION |

##### `/api/v1/operations/plans`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/plans` | CMD-PLN-CREATE | إنشاء | POL-PLN-CREATE | title!, owner!, org_scope!, implements, plan_kind!, triggered_by, window!, label! | 201, 400, 404, 409, 422, 429, 503 | PLAN_INVALID |
| POST | `/api/v1/operations/plans/{id}/actions/cancel` | CMD-PLN-CANCEL | حذف / إنهاء | POL-PLN-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/plans/{id}/actions/close` | CMD-PLN-CLOSE | حذف / إنهاء | POL-PLN-CLOSE | after_action_notes | 202, 400, 404, 409, 422, 429, 503 | PLAN_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/plans/{id}/actions/complete` | CMD-PLN-COMPLETE | سير عمل | POL-PLN-COMPLETE | note | 202, 400, 404, 409, 422, 429, 503 | PLAN_INVALID_STATE_TRANSITION, PLAN_NOT_COMPLETABLE |
| POST | `/api/v1/operations/plans/{id}/actions/reclassify` | CMD-PLN-RECLASSIFY | تعديل | POL-PLN-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, PLAN_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/plans/{id}/actions/resume` | CMD-PLN-RESUME | سير عمل | POL-PLN-RESUME | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/operations/plans/{id}/actions/suspend` | CMD-PLN-SUSPEND | سير عمل | POL-PLN-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | PLAN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/operations/plans/{plan_id}` | QRY-PLN-GET | جلب | POL-PLN-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/plans/{plan_id}/outcomes/{outcome_id}/measurements` | QRY-OUT-SERIES | جلب | POL-OUT-SERIES | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/plans/{plan_id}/progress` | QRY-PLN-PROGRESS | جلب | POL-PLN-PROGRESS | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/plans/{plan_id}/versions` | QRY-PLV-LIST | جلب | POL-PLV-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/plans/{plan_id}/versions/{version}/diff` | QRY-PLV-DIFF | جلب | POL-PLV-DIFF | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/operations/risks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/risks` | QRY-RIS-REGISTER | جلب | POL-RIS-REGISTER | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/risks` | CMD-RIS-IDENTIFY | إنشاء | POL-RIS-IDENTIFY | category_ref!, description!, scope_refs!, label! | 201, 400, 404, 409, 422, 429, 503 | RISK_INVALID |
| POST | `/api/v1/operations/risks/{id}/actions/assess` | CMD-RIS-ASSESS | سير عمل | POL-RIS-ASSESS | likelihood!, impact! | 202, 400, 404, 409, 422, 429, 503 | RISK_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/operations/risks/{id}/actions/close` | CMD-RIS-CLOSE | حذف / إنهاء | POL-RIS-CLOSE | rationale!, incident_ref | 202, 400, 404, 409, 422, 429, 503 | RATIONALE_REQUIRED, RISK_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/risks/{id}/actions/plan-treatment` | CMD-RIS-PLAN-TREATMENT | سير عمل | POL-RIS-PLAN-TREATMENT | treatment_strategy!, treatment_task_refs, approver! | 202, 400, 404, 409, 422, 429, 503 | RISK_INVALID_STATE_TRANSITION, TREATMENT_INVALID |
| POST | `/api/v1/operations/risks/{id}/actions/reassess` | CMD-RIS-REASSESS | سير عمل | POL-RIS-REASSESS | likelihood!, impact!, reason! | 202, 400, 404, 409, 422, 429, 503 | RISK_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| GET | `/api/v1/operations/risks/{risk_id}` | QRY-RIS-GET | جلب | POL-RIS-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/operations/subscriptions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/subscriptions` | CMD-SUB-SUBSCRIBE | إنشاء | POL-SUB-SUBSCRIBE | target!, channels!, quiet_hours | 201, 400, 404, 409, 422, 429, 503 | SUBSCRIPTION_EXISTS |
| POST | `/api/v1/operations/subscriptions/{id}/actions/pause` | CMD-SUB-PAUSE | سير عمل | POL-SUB-PAUSE | — | 202, 400, 404, 409, 422, 429, 503 | SUBSCRIPTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/subscriptions/{id}/actions/resume` | CMD-SUB-RESUME | سير عمل | POL-SUB-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | SUBSCRIPTION_INVALID_STATE_TRANSITION, TARGET_NOT_VISIBLE |
| POST | `/api/v1/operations/subscriptions/{id}/actions/unsubscribe` | CMD-SUB-UNSUBSCRIBE | حذف / إنهاء | POL-SUB-UNSUBSCRIBE | reason | 202, 400, 404, 409, 422, 429, 503 | SUBSCRIPTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/subscriptions/{id}/actions/update-channels` | CMD-SUB-UPDATE-CHANNELS | تعديل | POL-SUB-UPDATE-CHANNELS | channels!, quiet_hours | 202, 400, 404, 409, 422, 429, 503 | SUBSCRIPTION_INVALID, SUBSCRIPTION_INVALID_STATE_TRANSITION |

##### `/api/v1/operations/task-types`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/operations/task-types` | CMD-TTY-DEFINE | إنشاء | POL-TTY-DEFINE | code!, name! | 201, 400, 404, 409, 422, 429, 503 | TASK_TYPE_CODE_TAKEN |
| POST | `/api/v1/operations/task-types/{id}/actions/activate` | CMD-TTY-ACTIVATE | سير عمل | POL-TTY-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | TASK_TYPE_INVALID, TASK_TYPE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/task-types/{id}/actions/edit` | CMD-TTY-EDIT | تعديل | POL-TTY-EDIT | qualification_requirements!, criteria_templates!, escalation!, expires_on_due!, review_steps | 202, 400, 404, 409, 422, 429, 503 | TASK_TYPE_INVALID, TASK_TYPE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/operations/task-types/{id}/actions/retire` | CMD-TTY-RETIRE | حذف / إنهاء | POL-TTY-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_TYPE_INVALID_STATE_TRANSITION |
| GET | `/api/v1/operations/task-types/{task_type_id}` | QRY-TTY-GET | جلب | POL-TTY-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/operations/tasks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/operations/tasks` | QRY-TASK-LIST | جلب | POL-TASK-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/operations/tasks` | CMD-TASK-CREATE | إنشاء | POL-TASK-CREATE | task_type!, title!, description, plan_ref, incident_ref, ad_hoc_reason, owner!, org_scope!, due_at, dependencies, follow_up_of, label! | 201, 400, 404, 409, 422, 429, 503 | TASK_INVALID, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/accept` | CMD-TASK-ACCEPT | سير عمل · دون اتصال | POL-TASK-ACCEPT | — | 202, 400, 404, 409, 422, 429, 503 | NOT_ASSIGNEE, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/add-result-item` | CMD-TASK-ADD-RESULT-ITEM | تعديل · دون اتصال | POL-TASK-ADD-RESULT-ITEM | kind!, ref, note, measurement | 202, 400, 404, 409, 422, 429, 503 | RESULT_ITEM_INVALID, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/approve` | CMD-TASK-APPROVE | سير عمل | POL-TASK-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | SEGREGATION_OF_DUTIES, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/assign` | CMD-TASK-ASSIGN | سير عمل | POL-TASK-ASSIGN | assignee!, note | 202, 400, 404, 409, 422, 429, 503 | ASSIGNEE_NOT_ELIGIBLE, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/block` | CMD-TASK-BLOCK | سير عمل · دون اتصال | POL-TASK-BLOCK | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/cancel` | CMD-TASK-CANCEL | حذف / إنهاء | POL-TASK-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/close` | CMD-TASK-CLOSE | حذف / إنهاء | POL-TASK-CLOSE | note | 202, 400, 404, 409, 422, 429, 503 | OPEN_FOLLOW_UPS, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/complete` | CMD-TASK-COMPLETE | سير عمل | POL-TASK-COMPLETE | attestations! | 202, 400, 404, 409, 422, 429, 503 | TASK_CRITERIA_NOT_MET, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/decline` | CMD-TASK-DECLINE | سير عمل | POL-TASK-DECLINE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/edit` | CMD-TASK-EDIT | تعديل | POL-TASK-EDIT | title, description, criteria, dependencies | 202, 400, 404, 409, 422, 429, 503 | TASK_INVALID, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/escalate` | CMD-TASK-ESCALATE | تعديل | POL-TASK-ESCALATE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/mark-ready` | CMD-TASK-MARK-READY | سير عمل | POL-TASK-MARK-READY | — | 202, 400, 404, 409, 422, 429, 503 | TASK_INVALID_STATE_TRANSITION, TASK_NOT_READY, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/reassign` | CMD-TASK-REASSIGN | سير عمل | POL-TASK-REASSIGN | assignee!, reason! | 202, 400, 404, 409, 422, 429, 503 | ASSIGNEE_NOT_ELIGIBLE, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/reclassify` | CMD-TASK-RECLASSIFY | تعديل | POL-TASK-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_CHANGE_NOT_AUTHORIZED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/reject` | CMD-TASK-REJECT | حذف / إنهاء | POL-TASK-REJECT | reason!, create_follow_up! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/resume` | CMD-TASK-RESUME | سير عمل · دون اتصال | POL-TASK-RESUME | note! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/return` | CMD-TASK-RETURN | سير عمل | POL-TASK-RETURN | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/set-due` | CMD-TASK-SET-DUE | تعديل | POL-TASK-SET-DUE | due_at!, reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/start` | CMD-TASK-START | سير عمل · دون اتصال | POL-TASK-START | — | 202, 400, 404, 409, 422, 429, 503 | DEPENDENCIES_NOT_MET, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/start-review` | CMD-TASK-START-REVIEW | سير عمل | POL-TASK-START-REVIEW | — | 202, 400, 404, 409, 422, 429, 503 | SEGREGATION_OF_DUTIES, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/submit` | CMD-TASK-SUBMIT | سير عمل · دون اتصال | POL-TASK-SUBMIT | summary! | 202, 400, 404, 409, 422, 429, 503 | RESULT_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/suspend` | CMD-TASK-SUSPEND | تعديل | POL-TASK-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| POST | `/api/v1/operations/tasks/{id}/actions/unsuspend` | CMD-TASK-UNSUSPEND | تعديل | POL-TASK-UNSUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | NOT_SUSPENDED, TASK_INVALID_STATE_TRANSITION, TASK_SUSPENDED |
| GET | `/api/v1/operations/tasks/{task_id}` | QRY-TASK-GET | جلب | POL-TASK-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/operations/tasks/{task_id}/history` | QRY-TASK-HISTORY | جلب | POL-TASK-HISTORY | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC05 — Readiness — الموارد والجاهزية

##### `/api/v1/readiness/allocations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/allocations` | QRY-ALC-LIST | جلب | POL-ALC-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/allocations` | CMD-ALC-REQUEST | إنشاء | POL-ALC-REQUEST | pool!, quantity!, window!, priority!, target!, justification | 201, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID |
| POST | `/api/v1/readiness/allocations/{id}/actions/approve` | CMD-ALC-APPROVE | سير عمل | POL-ALC-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID_STATE_TRANSITION, CAPACITY_UNAVAILABLE |
| POST | `/api/v1/readiness/allocations/{id}/actions/preempt` | CMD-ALC-PREEMPT | حذف / إنهاء | POL-ALC-PREEMPT | decision!, preempting_allocation! | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED |
| POST | `/api/v1/readiness/allocations/{id}/actions/record-consumption` | CMD-ALC-RECORD-CONSUMPTION | تعديل | POL-ALC-RECORD-CONSUMPTION | quantity!, at!, note | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID_STATE_TRANSITION, CONSUMPTION_INVALID |
| POST | `/api/v1/readiness/allocations/{id}/actions/reject` | CMD-ALC-REJECT | حذف / إنهاء | POL-ALC-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/allocations/{id}/actions/release` | CMD-ALC-RELEASE | حذف / إنهاء | POL-ALC-RELEASE | note | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_INVALID_STATE_TRANSITION |

##### `/api/v1/readiness/asset-assignments`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/asset-assignments` | CMD-ASG-ASSIGN | إنشاء | POL-ASG-ASSIGN | asset!, task, unit, window!, reservation | 201, 400, 404, 409, 422, 429, 503 | ASSET_NOT_AVAILABLE |
| POST | `/api/v1/readiness/asset-assignments/{id}/actions/cancel` | CMD-ASG-CANCEL | حذف / إنهاء | POL-ASG-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/asset-assignments/{id}/actions/return` | CMD-ASG-RETURN | حذف / إنهاء | POL-ASG-RETURN | condition_report! | 202, 400, 404, 409, 422, 429, 503 | ASSET_ASSIGNMENT_INVALID_STATE_TRANSITION, CONDITION_REPORT_REQUIRED |

##### `/api/v1/readiness/asset-availability-queries`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/asset-availability-queries` | QRY-AST-AVAILABILITY | جلب | POL-AST-AVAILABILITY | asset_types, capabilities, window!, bbox | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/asset-reservations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/asset-reservations` | CMD-RSV-HOLD | إنشاء | POL-RSV-HOLD | asset!, window!, purpose!, label! | 201, 400, 404, 409, 422, 429, 503 | ASSET_RESERVED |
| POST | `/api/v1/readiness/asset-reservations/{id}/actions/cancel` | CMD-RSV-CANCEL | حذف / إنهاء | POL-RSV-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_RESERVATION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/asset-reservations/{id}/actions/confirm` | CMD-RSV-CONFIRM | سير عمل | POL-RSV-CONFIRM | link! | 202, 400, 404, 409, 422, 429, 503 | ASSET_RESERVATION_INVALID_STATE_TRANSITION, LINK_REQUIRED |
| POST | `/api/v1/readiness/asset-reservations/{id}/actions/release` | CMD-RSV-RELEASE | حذف / إنهاء | POL-RSV-RELEASE | note | 202, 400, 404, 409, 422, 429, 503 | ASSET_RESERVATION_INVALID_STATE_TRANSITION |

##### `/api/v1/readiness/assets`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/assets` | CMD-AST-REGISTER | إنشاء | POL-AST-REGISTER | asset_type!, name!, owner_org!, custody_holder!, linked_entity, capabilities!, serial, label! | 201, 400, 404, 409, 422, 429, 503 | ASSET_INVALID |
| GET | `/api/v1/readiness/assets/{asset_id}` | QRY-AST-GET | جلب | POL-AST-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/assets/{id}/actions/dispose` | CMD-AST-DISPOSE | حذف / إنهاء | POL-AST-DISPOSE | decision!, reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED |
| POST | `/api/v1/readiness/assets/{id}/actions/fail-maintenance` | CMD-AST-FAIL-MAINTENANCE | سير عمل | POL-AST-FAIL-MAINTENANCE | maintenance_order!, reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/assets/{id}/actions/mark-unserviceable` | CMD-AST-MARK-UNSERVICEABLE | سير عمل | POL-AST-MARK-UNSERVICEABLE | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/assets/{id}/actions/reclassify` | CMD-AST-RECLASSIFY | تعديل | POL-AST-RECLASSIFY | label!, reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, CLASSIFICATION_CHANGE_NOT_AUTHORIZED |
| POST | `/api/v1/readiness/assets/{id}/actions/recover` | CMD-AST-RECOVER | سير عمل | POL-AST-RECOVER | note | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/assets/{id}/actions/report-lost` | CMD-AST-REPORT-LOST | سير عمل | POL-AST-REPORT-LOST | reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/assets/{id}/actions/return-to-service` | CMD-AST-RETURN-TO-SERVICE | سير عمل | POL-AST-RETURN-TO-SERVICE | maintenance_order! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, ASSET_NOT_SERVICEABLE |
| POST | `/api/v1/readiness/assets/{id}/actions/set-certification` | CMD-AST-SET-CERTIFICATION | تعديل | POL-AST-SET-CERTIFICATION | code!, issuer!, valid_from!, valid_to!, evidence | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, CERTIFICATION_INVALID |
| POST | `/api/v1/readiness/assets/{id}/actions/start-maintenance` | CMD-AST-START-MAINTENANCE | سير عمل | POL-AST-START-MAINTENANCE | maintenance_order! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, MAINTENANCE_ORDER_REQUIRED |
| POST | `/api/v1/readiness/assets/{id}/actions/transfer-custody` | CMD-AST-TRANSFER-CUSTODY | تعديل | POL-AST-TRANSFER-CUSTODY | new_holder!, reason! | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, CUSTODY_INVALID |
| POST | `/api/v1/readiness/assets/{id}/actions/update-condition` | CMD-AST-UPDATE-CONDITION | تعديل | POL-AST-UPDATE-CONDITION | grade!, inspector!, notes | 202, 400, 404, 409, 422, 429, 503 | ASSET_INVALID_STATE_TRANSITION, CONDITION_INVALID |

##### `/api/v1/readiness/eligibility-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/eligibility-checks` | QRY-ELIG-CHECK | جلب | POL-ELIG-CHECK | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/exercises`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/exercises` | QRY-EXR-LIST | جلب | POL-EXR-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/exercises` | CMD-EXR-PLAN | إنشاء | POL-EXR-PLAN | scenario!, objectives!, participants!, purpose!, role_ref | 201, 400, 404, 409, 422, 429, 503 | EXERCISE_INVALID |
| GET | `/api/v1/readiness/exercises/{exercise_id}` | QRY-EXR-GET | جلب | POL-EXR-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/exercises/{id}/actions/cancel` | CMD-EXR-CANCEL | حذف / إنهاء | POL-EXR-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | EXERCISE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/exercises/{id}/actions/schedule` | CMD-EXR-SCHEDULE | سير عمل | POL-EXR-SCHEDULE | window!, location!, participants! | 202, 400, 404, 409, 422, 429, 503 | EXERCISE_INVALID, EXERCISE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/exercises/{id}/actions/start` | CMD-EXR-START | سير عمل | POL-EXR-START | note | 202, 400, 404, 409, 422, 429, 503 | EXERCISE_INVALID, EXERCISE_INVALID_STATE_TRANSITION |

##### `/api/v1/readiness/logistics-requests`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/logistics-requests` | QRY-LGR-LIST | جلب | POL-LGR-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/logistics-requests` | CMD-LGR-REQUEST | إنشاء | POL-LGR-REQUEST | item_pool!, quantity!, destination!, needed_by!, priority!, justification | 201, 400, 404, 409, 422, 429, 503 | LOGISTICS_REQUEST_INVALID |
| POST | `/api/v1/readiness/logistics-requests/{id}/actions/cancel` | CMD-LGR-CANCEL | حذف / إنهاء | POL-LGR-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | LOGISTICS_REQUEST_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/logistics-requests/{id}/actions/dispatch` | CMD-LGR-DISPATCH | سير عمل | POL-LGR-DISPATCH | carrier!, ship_quantity! | 202, 400, 404, 409, 422, 429, 503 | ALLOCATION_NOT_COMMITTED, LOGISTICS_REQUEST_INVALID_STATE_TRANSITION |
| GET | `/api/v1/readiness/logistics-requests/{request_id}` | QRY-LGR-GET | جلب | POL-LGR-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/maintenance-orders`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/maintenance-orders` | QRY-MNT-SCHEDULE | جلب | POL-MNT-SCHEDULE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/maintenance-orders` | CMD-MNT-PLAN | إنشاء | POL-MNT-PLAN | asset!, kind!, window!, description! | 201, 400, 404, 409, 422, 429, 503 | MAINTENANCE_OVERLAP |
| POST | `/api/v1/readiness/maintenance-orders/{id}/actions/cancel` | CMD-MNT-CANCEL | حذف / إنهاء | POL-MNT-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/maintenance-orders/{id}/actions/complete` | CMD-MNT-COMPLETE | حذف / إنهاء | POL-MNT-COMPLETE | outcome!, work!, parts | 202, 400, 404, 409, 422, 429, 503 | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, OUTCOME_REQUIRED |
| POST | `/api/v1/readiness/maintenance-orders/{id}/actions/reschedule` | CMD-MNT-RESCHEDULE | تعديل | POL-MNT-RESCHEDULE | window!, reason! | 202, 400, 404, 409, 422, 429, 503 | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION, MAINTENANCE_OVERLAP |
| POST | `/api/v1/readiness/maintenance-orders/{id}/actions/start` | CMD-MNT-START | سير عمل | POL-MNT-START | technician! | 202, 400, 404, 409, 422, 429, 503 | MAINTENANCE_ORDER_INVALID_STATE_TRANSITION |

##### `/api/v1/readiness/persons`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/persons/{person_id}/qualifications` | QRY-QUAL-LIST | جلب | POL-QUAL-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/qualification-records`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/qualification-records` | CMD-QUAL-RECORD | إنشاء | POL-QUAL-RECORD | person!, kind!, code!, level!, valid_from!, valid_to!, issuer!, evidence | 201, 400, 404, 409, 422, 429, 503 | QUALIFICATION_INVALID |
| POST | `/api/v1/readiness/qualification-records/{id}/actions/reinstate` | CMD-QUAL-REINSTATE | سير عمل | POL-QUAL-REINSTATE | — | 202, 400, 404, 409, 422, 429, 503 | QUALIFICATION_EXPIRED, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/qualification-records/{id}/actions/renew` | CMD-QUAL-RENEW | تعديل | POL-QUAL-RENEW | valid_to!, evidence | 202, 400, 404, 409, 422, 429, 503 | QUALIFICATION_INVALID, QUALIFICATION_RECORD_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/qualification-records/{id}/actions/revoke` | CMD-QUAL-REVOKE | حذف / إنهاء | POL-QUAL-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/readiness/qualification-records/{id}/actions/suspend` | CMD-QUAL-SUSPEND | سير عمل | POL-QUAL-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | QUALIFICATION_RECORD_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/readiness/readiness-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/readiness-checks` | QRY-READINESS | جلب | POL-READINESS | subject!, role!, at! | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/resource-pools`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/resource-pools` | CMD-RPL-CREATE | إنشاء | POL-RPL-CREATE | resource_type!, name!, unit!, org_scope!, capacity!, label! | 201, 400, 404, 409, 422, 429, 503 | POOL_INVALID |
| POST | `/api/v1/readiness/resource-pools/{id}/actions/adjust-capacity` | CMD-RPL-ADJUST-CAPACITY | تعديل | POL-RPL-ADJUST-CAPACITY | capacity!, valid_from!, reason! | 202, 400, 404, 409, 422, 429, 503 | CAPACITY_BELOW_COMMITMENTS, RESOURCE_POOL_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/resource-pools/{id}/actions/close` | CMD-RPL-CLOSE | حذف / إنهاء | POL-RPL-CLOSE | reason! | 202, 400, 404, 409, 422, 429, 503 | POOL_HAS_COMMITMENTS, RESOURCE_POOL_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/resource-pools/{id}/actions/resume` | CMD-RPL-RESUME | سير عمل | POL-RPL-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | RESOURCE_POOL_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/resource-pools/{id}/actions/suspend` | CMD-RPL-SUSPEND | سير عمل | POL-RPL-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, RESOURCE_POOL_INVALID_STATE_TRANSITION |
| GET | `/api/v1/readiness/resource-pools/{pool_id}/timeline` | QRY-POL-TIMELINE | جلب | POL-POL-TIMELINE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/role-requirements`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/readiness/role-requirements` | CMD-RRQ-DEFINE | إنشاء | POL-RRQ-DEFINE | role!, requirements! | 201, 400, 404, 409, 422, 429, 503 | ROLE_REQUIREMENT_INVALID |
| POST | `/api/v1/readiness/role-requirements/{id}/actions/activate` | CMD-RRQ-ACTIVATE | سير عمل | POL-RRQ-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | ROLE_REQUIREMENT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/readiness/role-requirements/{id}/actions/edit` | CMD-RRQ-EDIT | تعديل | POL-RRQ-EDIT | requirements! | 202, 400, 404, 409, 422, 429, 503 | ROLE_REQUIREMENT_INVALID, ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/role-requirements/{id}/actions/retire` | CMD-RRQ-RETIRE | حذف / إنهاء | POL-RRQ-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, ROLE_REQUIREMENT_INVALID_STATE_TRANSITION |

##### `/api/v1/readiness/scenarios`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/scenarios` | QRY-SCN-LIST | جلب | POL-SCN-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/scenarios` | CMD-SCN-DEFINE | إنشاء | POL-SCN-DEFINE | title!, exercise_type_ref!, situation!, target_competencies!, injects! | 201, 400, 404, 409, 422, 429, 503 | SCENARIO_INVALID |
| POST | `/api/v1/readiness/scenarios/{id}/actions/activate` | CMD-SCN-ACTIVATE | سير عمل | POL-SCN-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | SCENARIO_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/readiness/scenarios/{id}/actions/edit` | CMD-SCN-EDIT | تعديل | POL-SCN-EDIT | title, situation, target_competencies, injects | 202, 400, 404, 409, 422, 429, 503 | SCENARIO_INVALID, SCENARIO_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/scenarios/{id}/actions/retire` | CMD-SCN-RETIRE | حذف / إنهاء | POL-SCN-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SCENARIO_INVALID_STATE_TRANSITION |
| GET | `/api/v1/readiness/scenarios/{scenario_id}` | QRY-SCN-GET | جلب | POL-SCN-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/shipments`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/shipments` | QRY-SHP-LIST | جلب | POL-SHP-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/shipments` | CMD-SHP-PLAN | إنشاء | POL-SHP-PLAN | logistics_request!, origin_pool!, destination!, carrier!, planned_quantity! | 201, 400, 404, 409, 422, 429, 503 | SHIPMENT_INVALID |
| POST | `/api/v1/readiness/shipments/{id}/actions/cancel` | CMD-SHP-CANCEL | حذف / إنهاء | POL-SHP-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/shipments/{id}/actions/deliver` | CMD-SHP-DELIVER | حذف / إنهاء | POL-SHP-DELIVER | delivered_quantity!, received_by!, note | 202, 400, 404, 409, 422, 429, 503 | DELIVERY_INVALID, SHIPMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/shipments/{id}/actions/depart` | CMD-SHP-DEPART | سير عمل | POL-SHP-DEPART | note | 202, 400, 404, 409, 422, 429, 503 | DEPARTURE_INVALID, SHIPMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/shipments/{id}/actions/record-checkpoint` | CMD-SHP-RECORD-CHECKPOINT | تعديل | POL-SHP-RECORD-CHECKPOINT | location!, at!, note | 202, 400, 404, 409, 422, 429, 503 | CHECKPOINT_INVALID, SHIPMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/shipments/{id}/actions/report-damage` | CMD-SHP-REPORT-DAMAGE | حذف / إنهاء | POL-SHP-REPORT-DAMAGE | damaged_quantity!, reason!, evidence | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/shipments/{id}/actions/report-lost` | CMD-SHP-REPORT-LOST | حذف / إنهاء | POL-SHP-REPORT-LOST | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SHIPMENT_INVALID_STATE_TRANSITION |
| GET | `/api/v1/readiness/shipments/{shipment_id}` | QRY-SHP-GET | جلب | POL-SHP-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/readiness/shipments/{shipment_id}/checkpoints` | QRY-SHP-TRACKING | جلب | POL-SHP-TRACKING | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/readiness/simulations`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/readiness/simulations` | QRY-SIM-LIST | جلب | POL-SIM-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/readiness/simulations` | CMD-SIM-START | نظام (داخلي) | POL-SIM-START | exercise!, scenario!, started_at! | 201, 400, 404, 409, 422, 429, 503 | SIMULATION_INVALID |
| POST | `/api/v1/readiness/simulations/{id}/actions/abort` | CMD-SIM-ABORT | حذف / إنهاء | POL-SIM-ABORT | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SIMULATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/simulations/{id}/actions/complete` | CMD-SIM-COMPLETE | حذف / إنهاء | POL-SIM-COMPLETE | — | 202, 400, 404, 409, 422, 429, 503 | EVALUATION_MISSING, SIMULATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/simulations/{id}/actions/deliver-inject` | CMD-SIM-DELIVER-INJECT | تعديل | POL-SIM-DELIVER-INJECT | inject_ref!, delivered_at!, note | 202, 400, 404, 409, 422, 429, 503 | INJECT_INVALID, SIMULATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/simulations/{id}/actions/pause` | CMD-SIM-PAUSE | سير عمل | POL-SIM-PAUSE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SIMULATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/simulations/{id}/actions/record-evaluation` | CMD-SIM-RECORD-EVALUATION | تعديل | POL-SIM-RECORD-EVALUATION | participant!, competency_code!, result!, notes | 202, 400, 404, 409, 422, 429, 503 | SEGREGATION_OF_DUTIES, SIMULATION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/readiness/simulations/{id}/actions/resume` | CMD-SIM-RESUME | سير عمل | POL-SIM-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | SIMULATION_INVALID_STATE_TRANSITION |
| GET | `/api/v1/readiness/simulations/{simulation_id}` | QRY-SIM-GET | جلب | POL-SIM-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/readiness/simulations/{simulation_id}/timeline` | QRY-SIM-TIMELINE | جلب | POL-SIM-TIMELINE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC06 — Knowledge — المعرفة والمنتجات

##### `/api/v1/knowledge/archive-packages`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/knowledge/archive-packages` | QRY-ARC-SEARCH | جلب | POL-ARC-SEARCH | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/migrate-format` | CMD-ARC-MIGRATE-FORMAT | تعديل | POL-ARC-MIGRATE-FORMAT | target_format!, reason! | 202, 400, 404, 409, 422, 429, 503 | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, FORMAT_INVALID |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/repair` | CMD-ARC-REPAIR | سير عمل | POL-ARC-REPAIR | replica_ref! | 202, 400, 404, 409, 422, 429, 503 | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, FIXITY_MISMATCH |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/retry-ingest` | CMD-ARC-RETRY-INGEST | سير عمل | POL-ARC-RETRY-INGEST | note! | 202, 400, 404, 409, 422, 429, 503 | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/archive-packages/{id}/actions/transfer` | CMD-ARC-TRANSFER | حذف / إنهاء | POL-ARC-TRANSFER | decision!, receiving_archive!, receipt! | 202, 400, 404, 409, 422, 429, 503 | ARCHIVE_PACKAGE_INVALID_STATE_TRANSITION, AUTHORITY_REQUIRED |
| POST | `/api/v1/knowledge/archive-packages/{package_id}/retrievals` | QRY-ARC-RETRIEVE | جلب | POL-ARC-RETRIEVE | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/knowledge/distributions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/knowledge/distributions` | CMD-DST-DISTRIBUTE | إنشاء | POL-DST-DISTRIBUTE | product!, recipients!, formats!, message | 201, 400, 404, 409, 422, 429, 503 | PRODUCT_NOT_APPROVED |
| POST | `/api/v1/knowledge/distributions/{id}/actions/cancel` | CMD-DST-CANCEL | حذف / إنهاء | POL-DST-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | DISTRIBUTION_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/knowledge/knowledge-objects`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/knowledge/knowledge-objects` | QRY-KNO-SEARCH | جلب | POL-KNO-SEARCH | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/knowledge/knowledge-objects` | CMD-KNO-DRAFT | إنشاء | POL-KNO-DRAFT | knowledge_type!, title!, source, revises, label! | 201, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_INVALID |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/discard` | CMD-KNO-DISCARD | حذف / إنهاء | POL-KNO-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/edit` | CMD-KNO-EDIT | تعديل | POL-KNO-EDIT | statements!, relationships | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_INVALID, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/publish` | CMD-KNO-PUBLISH | سير عمل | POL-KNO-PUBLISH | note | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/record-reuse` | CMD-KNO-RECORD-REUSE | تعديل | POL-KNO-RECORD-REUSE | target! | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, TARGET_INVALID |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/reject` | CMD-KNO-REJECT | حذف / إنهاء | POL-KNO-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/retire` | CMD-KNO-RETIRE | حذف / إنهاء | POL-KNO-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/return` | CMD-KNO-RETURN | سير عمل | POL-KNO-RETURN | reason! | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/knowledge-objects/{id}/actions/submit` | CMD-KNO-SUBMIT | سير عمل | POL-KNO-SUBMIT | — | 202, 400, 404, 409, 422, 429, 503 | KNOWLEDGE_INCOMPLETE, KNOWLEDGE_OBJECT_INVALID_STATE_TRANSITION |

##### `/api/v1/knowledge/knowledge-suggestions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/knowledge/knowledge-suggestions` | QRY-KNO-SUGGEST | جلب | POL-KNO-SUGGEST | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/knowledge/product-templates`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/knowledge/product-templates` | CMD-PTM-DEFINE | إنشاء | POL-PTM-DEFINE | code!, kind!, name! | 201, 400, 404, 409, 422, 429, 503 | TEMPLATE_INVALID |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/activate` | CMD-PTM-ACTIVATE | سير عمل | POL-PTM-ACTIVATE | sample_ref! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/edit` | CMD-PTM-EDIT | تعديل | POL-PTM-EDIT | sections! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, TEMPLATE_INVALID |
| POST | `/api/v1/knowledge/product-templates/{id}/actions/retire` | CMD-PTM-RETIRE | حذف / إنهاء | POL-PTM-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_TEMPLATE_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/knowledge/products`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/knowledge/products` | QRY-PRD-LIST | جلب | POL-PRD-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/knowledge/products` | CMD-PRD-CREATE | إنشاء | POL-PRD-CREATE | template!, parameters!, audience!, title!, revises, label! | 201, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID |
| POST | `/api/v1/knowledge/products/{id}/actions/approve` | CMD-PRD-APPROVE | سير عمل | POL-PRD-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/knowledge/products/{id}/actions/discard` | CMD-PRD-DISCARD | حذف / إنهاء | POL-PRD-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/products/{id}/actions/edit-narrative` | CMD-PRD-EDIT-NARRATIVE | تعديل | POL-PRD-EDIT-NARRATIVE | section_id!, text! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION, SECTION_NOT_EDITABLE |
| POST | `/api/v1/knowledge/products/{id}/actions/generate` | CMD-PRD-GENERATE | سير عمل | POL-PRD-GENERATE | — | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/knowledge/products/{id}/actions/return` | CMD-PRD-RETURN | سير عمل | POL-PRD-RETURN | reason! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/knowledge/products/{id}/actions/submit` | CMD-PRD-SUBMIT | سير عمل | POL-PRD-SUBMIT | — | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INCOMPLETE, PRODUCT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/knowledge/products/{id}/actions/withdraw` | CMD-PRD-WITHDRAW | حذف / إنهاء | POL-PRD-WITHDRAW | reason! | 202, 400, 404, 409, 422, 429, 503 | PRODUCT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/knowledge/products/{product_id}` | QRY-PRD-GET | جلب | POL-PRD-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/knowledge/products/{product_id}/distributions` | QRY-DST-LOG | جلب | POL-DST-LOG | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/knowledge/reconstructions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/knowledge/reconstructions` | CMD-REC-REQUEST | إنشاء | POL-REC-REQUEST | scope!, valid_at!, known_at!, purpose! | 201, 400, 404, 409, 422, 429, 503 | RECONSTRUCTION_INVALID |
| POST | `/api/v1/knowledge/reconstructions/{id}/actions/cancel` | CMD-REC-CANCEL | حذف / إنهاء | POL-REC-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, RECONSTRUCTION_INVALID_STATE_TRANSITION |
| GET | `/api/v1/knowledge/reconstructions/{reconstruction_id}/report` | QRY-REC-REPORT | جلب | POL-REC-REPORT | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |


#### BC07 — Platform Intelligence — التكامل والذكاء الاصطناعي

##### `/api/v1/ai/evaluation-suites`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/ai/evaluation-suites` | CMD-EVS-DRAFT | إنشاء | POL-EVS-DRAFT | based_on | 201, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/ai/evaluation-suites/{id}/actions/activate` | CMD-EVS-ACTIVATE | سير عمل | POL-EVS-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | EVAL_SUITE_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/ai/evaluation-suites/{id}/actions/edit` | CMD-EVS-EDIT | تعديل | POL-EVS-EDIT | sets! | 202, 400, 404, 409, 422, 429, 503 | EVAL_SUITE_INVALID_STATE_TRANSITION, SUITE_INVALID |

##### `/api/v1/ai/models`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/ai/models` | QRY-MDL-LIST | جلب | POL-MDL-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/ai/models` | CMD-MDL-REGISTER | إنشاء | POL-MDL-REGISTER | family!, version!, weights_digest!, licence!, languages!, context_tokens!, hosting!, roles! | 201, 400, 404, 409, 422, 429, 503 | MODEL_INVALID |
| POST | `/api/v1/ai/models/{id}/actions/approve` | CMD-MDL-APPROVE | سير عمل | POL-MDL-APPROVE | report! | 202, 400, 404, 409, 422, 429, 503 | EVALUATION_BELOW_THRESHOLD, MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/deprecate` | CMD-MDL-DEPRECATE | سير عمل | POL-MDL-DEPRECATE | reason! | 202, 400, 404, 409, 422, 429, 503 | MODEL_IN_ACTIVE_ROUTE, MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/fail-evaluation` | CMD-MDL-FAIL-EVALUATION | حذف / إنهاء | POL-MDL-FAIL-EVALUATION | report! | 202, 400, 404, 409, 422, 429, 503 | MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/promote` | CMD-MDL-PROMOTE | سير عمل | POL-MDL-PROMOTE | canary_report! | 202, 400, 404, 409, 422, 429, 503 | CANARY_BELOW_THRESHOLD, MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/reinstate` | CMD-MDL-REINSTATE | سير عمل | POL-MDL-REINSTATE | reason! | 202, 400, 404, 409, 422, 429, 503 | EVALUATION_TOO_OLD, MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/retire` | CMD-MDL-RETIRE | حذف / إنهاء | POL-MDL-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/stage` | CMD-MDL-STAGE | سير عمل | POL-MDL-STAGE | canary_share!, operations! | 202, 400, 404, 409, 422, 429, 503 | MODEL_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/models/{id}/actions/start-evaluation` | CMD-MDL-START-EVALUATION | سير عمل | POL-MDL-START-EVALUATION | suite! | 202, 400, 404, 409, 422, 429, 503 | MODEL_VERSION_INVALID_STATE_TRANSITION, SUITE_NOT_ACTIVE |

##### `/api/v1/ai/requests`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/ai/requests` | CMD-AIR-SUBMIT | إنشاء | POL-AIR-SUBMIT | operation!, input!, scope, purpose!, target | 201, 400, 404, 409, 422, 429, 503 | AI_OPERATION_NOT_ALLOWED |
| POST | `/api/v1/ai/requests/{id}/actions/cancel` | CMD-AIR-CANCEL | حذف / إنهاء | POL-AIR-CANCEL | — | 202, 400, 404, 409, 422, 429, 503 | AI_REQUEST_INVALID_STATE_TRANSITION |
| GET | `/api/v1/ai/requests/{request_id}` | QRY-AIR-GET | جلب | POL-AIR-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/ai/requests/{request_id}/context` | QRY-AIR-CONTEXT | جلب | POL-AIR-CONTEXT | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/ai/results`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/ai/results` | QRY-AIRS-QUEUE | جلب | POL-AIRS-QUEUE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/ai/results/{id}/actions/accept` | CMD-AIRS-ACCEPT | حذف / إنهاء | POL-AIRS-ACCEPT | note | 202, 400, 404, 409, 422, 429, 503 | AI_RESULT_INVALID_STATE_TRANSITION, OWNER_REJECTED |
| POST | `/api/v1/ai/results/{id}/actions/accept-partially` | CMD-AIRS-ACCEPT-PARTIALLY | حذف / إنهاء | POL-AIRS-ACCEPT-PARTIALLY | accepted_items!, rejected_items! | 202, 400, 404, 409, 422, 429, 503 | AI_RESULT_INVALID_STATE_TRANSITION, OWNER_REJECTED |
| POST | `/api/v1/ai/results/{id}/actions/reject` | CMD-AIRS-REJECT | حذف / إنهاء | POL-AIRS-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | AI_RESULT_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/ai/results/{id}/actions/start-review` | CMD-AIRS-START-REVIEW | سير عمل | POL-AIRS-START-REVIEW | — | 202, 400, 404, 409, 422, 429, 503 | AI_RESULT_INVALID_STATE_TRANSITION, REVIEWER_NOT_CLEARED |

##### `/api/v1/ai/routing`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/ai/routing` | QRY-RTG-ACTIVE | جلب | POL-RTG-ACTIVE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/ai/routings`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/ai/routings` | CMD-RTG-DRAFT | إنشاء | POL-RTG-DRAFT | based_on | 201, 400, 404, 409, 422, 429, 503 | DRAFT_EXISTS |
| POST | `/api/v1/ai/routings/{id}/actions/activate` | CMD-RTG-ACTIVATE | سير عمل | POL-RTG-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | AI_ROUTING_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/ai/routings/{id}/actions/discard` | CMD-RTG-DISCARD | حذف / إنهاء | POL-RTG-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | AI_ROUTING_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/ai/routings/{id}/actions/edit` | CMD-RTG-EDIT | تعديل | POL-RTG-EDIT | routes! | 202, 400, 404, 409, 422, 429, 503 | AI_ROUTING_INVALID_STATE_TRANSITION, ROUTING_INVALID |

##### `/api/v1/ai/tools`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/ai/tools` | QRY-TOL-LIST | جلب | POL-TOL-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/ai/tools` | CMD-TOL-REGISTER | إنشاء | POL-TOL-REGISTER | name!, description!, input_schema!, binding!, effect!, permission!, max_ail! | 201, 400, 404, 409, 422, 429, 503 | TOOL_INVALID |
| POST | `/api/v1/ai/tools/{id}/actions/activate` | CMD-TOL-ACTIVATE | سير عمل | POL-TOL-ACTIVATE | review_ref! | 202, 400, 404, 409, 422, 429, 503 | AI_TOOL_INVALID_STATE_TRANSITION, SECURITY_REVIEW_REQUIRED |
| POST | `/api/v1/ai/tools/{id}/actions/disable` | CMD-TOL-DISABLE | سير عمل | POL-TOL-DISABLE | reason! | 202, 400, 404, 409, 422, 429, 503 | AI_TOOL_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/ai/tools/{id}/actions/enable` | CMD-TOL-ENABLE | سير عمل | POL-TOL-ENABLE | — | 202, 400, 404, 409, 422, 429, 503 | AI_TOOL_INVALID_STATE_TRANSITION |
| POST | `/api/v1/ai/tools/{id}/actions/retire` | CMD-TOL-RETIRE | حذف / إنهاء | POL-TOL-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | AI_TOOL_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/ai/usage`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/ai/usage` | QRY-AI-USAGE | جلب | POL-AI-USAGE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/discovery/graph`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/discovery/graph/entities/{entity_id}/neighborhood` | QRY-GRAPH-NEIGHBORHOOD | جلب | POL-GRAPH-NEIGHBORHOOD | cursor, limit, depth, valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/discovery/graph/paths` | QRY-GRAPH-PATHS | جلب | POL-GRAPH-PATHS | from!, to!, max_hops, relationship_types, valid_at, known_at, max_paths | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/discovery/projection-versions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/discovery/projection-versions` | QRY-PRJ-STATUS | جلب | POL-PRJ-STATUS | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/discovery/projection-versions` | CMD-PRJ-CREATE-VERSION | إنشاء | POL-PRJ-CREATE-VERSION | kind!, tenant_group!, schema_version!, normalization_version!, reason! | 201, 400, 404, 409, 422, 429, 503 | PROJECTION_BUILD_IN_PROGRESS |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/cancel-build` | CMD-PRJ-CANCEL-BUILD | حذف / إنهاء | POL-PRJ-CANCEL-BUILD | reason! | 202, 400, 404, 409, 422, 429, 503 | PROJECTION_VERSION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/promote` | CMD-PRJ-PROMOTE | سير عمل | POL-PRJ-PROMOTE | — | 202, 400, 404, 409, 422, 429, 503 | PROJECTION_NOT_VERIFIED, PROJECTION_VERSION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/discovery/projection-versions/{id}/actions/retire` | CMD-PRJ-RETIRE | حذف / إنهاء | POL-PRJ-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | LAST_ACTIVE_PROJECTION, PROJECTION_VERSION_INVALID_STATE_TRANSITION |

##### `/api/v1/discovery/search-queries`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/discovery/search-queries` | QRY-SRCH-QUERY | جلب | POL-SRCH-QUERY | text, types!, geo, time, valid_at, filters, facets, sort, cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/discovery/suggestions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/discovery/suggestions` | QRY-SRCH-SUGGEST | جلب | POL-SRCH-SUGGEST | cursor, limit, q! | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/field/preload-packages`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/field/preload-packages` | CMD-PKG-REQUEST | إنشاء | POL-PKG-REQUEST | device!, area!, layers!, window!, level! | 201, 400, 404, 409, 422, 429, 503 | PRELOAD_NOT_ALLOWED |
| POST | `/api/v1/field/preload-packages/{id}/actions/confirm-download` | CMD-PKG-CONFIRM-DOWNLOAD | سير عمل | POL-PKG-CONFIRM-DOWNLOAD | manifest_sha256! | 202, 400, 404, 409, 422, 429, 503 | MANIFEST_MISMATCH, PRELOAD_PACKAGE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/field/preload-packages/{id}/actions/revoke` | CMD-PKG-REVOKE | حذف / إنهاء | POL-PKG-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | PRELOAD_PACKAGE_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/field/preload-packages/{package_id}` | QRY-PKG-GET | جلب | POL-PKG-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/field/sync-conflicts`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/field/sync-conflicts` | QRY-SCF-LIST | جلب | POL-SCF-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| GET | `/api/v1/field/sync-conflicts/{conflict_id}` | QRY-SCF-GET | جلب | POL-SCF-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/field/sync-conflicts/{id}/actions/assign` | CMD-SCF-ASSIGN | تعديل | POL-SCF-ASSIGN | reviewer! | 202, 400, 404, 409, 422, 429, 503 | REVIEWER_NOT_AUTHORIZED, SYNC_CONFLICT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/field/sync-conflicts/{id}/actions/discard` | CMD-SCF-DISCARD | حذف / إنهاء | POL-SCF-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SYNC_CONFLICT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/field/sync-conflicts/{id}/actions/reapply` | CMD-SCF-REAPPLY | حذف / إنهاء | POL-SCF-REAPPLY | note | 202, 400, 404, 409, 422, 429, 503 | OWNER_REJECTED, SYNC_CONFLICT_INVALID_STATE_TRANSITION |
| POST | `/api/v1/field/sync-conflicts/{id}/actions/resolve-manually` | CMD-SCF-RESOLVE-MANUALLY | حذف / إنهاء | POL-SCF-RESOLVE-MANUALLY | note!, action_ref | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SYNC_CONFLICT_INVALID_STATE_TRANSITION |

##### `/api/v1/field/sync-sessions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/field/sync-sessions` | CMD-SYN-OPEN | إنشاء | POL-SYN-OPEN | device!, device_time!, last_acked_seq!, queue_length!, queue_head_hash!, signature! | 201, 400, 404, 409, 422, 429, 503 | DEVICE_NOT_ACTIVE |
| POST | `/api/v1/field/sync-sessions/{id}/actions/upload-batch` | CMD-SYN-UPLOAD-BATCH | سير عمل | POL-SYN-UPLOAD-BATCH | envelopes!, end_of_queue! | 202, 400, 404, 409, 422, 429, 503 | SEQUENCE_GAP, SYNC_SESSION_INVALID_STATE_TRANSITION |
| GET | `/api/v1/field/sync-sessions/{session_id}/delta` | QRY-SYN-DELTA | جلب | POL-SYN-DELTA | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/integration/adapters`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/integration/adapters` | CMD-ADP-REGISTER | إنشاء | POL-ADP-REGISTER | name!, source!, service_account!, mapping! | 201, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID |
| GET | `/api/v1/integration/adapters/{adapter_id}` | QRY-ADP-GET | جلب | POL-ADP-GET | valid_at, known_at | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/integration/adapters/{id}/actions/activate` | CMD-ADP-ACTIVATE | سير عمل | POL-ADP-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/integration/adapters/{id}/actions/resume` | CMD-ADP-RESUME | سير عمل | POL-ADP-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/adapters/{id}/actions/retire` | CMD-ADP-RETIRE | حذف / إنهاء | POL-ADP-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/integration/adapters/{id}/actions/suspend` | CMD-ADP-SUSPEND | سير عمل | POL-ADP-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/integration/adapters/{id}/actions/update-mapping` | CMD-ADP-UPDATE-MAPPING | تعديل | POL-ADP-UPDATE-MAPPING | mapping!, tests! | 202, 400, 404, 409, 422, 429, 503 | ADAPTER_INVALID_STATE_TRANSITION, MAPPING_TESTS_FAILED |

##### `/api/v1/integration/connections`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/integration/connections` | QRY-CON-LIST | جلب | POL-CON-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/integration/connections` | CMD-CON-REGISTER | إنشاء | POL-CON-REGISTER | name!, system_kind!, endpoint!, protocol!, direction!, credentials_ref! | 201, 400, 404, 409, 422, 429, 503 | CONNECTION_INVALID |
| POST | `/api/v1/integration/connections/{id}/actions/activate` | CMD-CON-ACTIVATE | سير عمل | POL-CON-ACTIVATE | allow_list_entry! | 202, 400, 404, 409, 422, 429, 503 | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/integration/connections/{id}/actions/fail-test` | CMD-CON-FAIL-TEST | سير عمل | POL-CON-FAIL-TEST | errors! | 202, 400, 404, 409, 422, 429, 503 | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/connections/{id}/actions/resume` | CMD-CON-RESUME | سير عمل | POL-CON-RESUME | — | 202, 400, 404, 409, 422, 429, 503 | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/connections/{id}/actions/retire` | CMD-CON-RETIRE | حذف / إنهاء | POL-CON-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | CONNECTION_IN_USE, INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/connections/{id}/actions/suspend` | CMD-CON-SUSPEND | سير عمل | POL-CON-SUSPEND | reason! | 202, 400, 404, 409, 422, 429, 503 | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/integration/connections/{id}/actions/test` | CMD-CON-TEST | سير عمل | POL-CON-TEST | — | 202, 400, 404, 409, 422, 429, 503 | INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION |

##### `/api/v1/integration/sensor-streams`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/integration/sensor-streams` | QRY-SNS-LIST | جلب | POL-SNS-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/integration/sensor-streams` | CMD-SNS-REGISTER | إنشاء | POL-SNS-REGISTER | connection!, source!, quantity!, unit!, expected_rate!, location, linked_entity | 201, 400, 404, 409, 422, 429, 503 | STREAM_INVALID |
| POST | `/api/v1/integration/sensor-streams/{id}/actions/activate` | CMD-SNS-ACTIVATE | سير عمل | POL-SNS-ACTIVATE | — | 202, 400, 404, 409, 422, 429, 503 | CONNECTION_NOT_ACTIVE, SENSOR_STREAM_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/sensor-streams/{id}/actions/pause` | CMD-SNS-PAUSE | سير عمل | POL-SNS-PAUSE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SENSOR_STREAM_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/sensor-streams/{id}/actions/retire` | CMD-SNS-RETIRE | حذف / إنهاء | POL-SNS-RETIRE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SENSOR_STREAM_INVALID_STATE_TRANSITION |
| POST | `/api/v1/integration/sensor-streams/{id}/actions/set-quality-rules` | CMD-SNS-SET-QUALITY-RULES | تعديل | POL-SNS-SET-QUALITY-RULES | rules! | 202, 400, 404, 409, 422, 429, 503 | QUALITY_RULES_INVALID, SENSOR_STREAM_INVALID_STATE_TRANSITION |


#### BC08 — Governance — الحوكمة والأمن

##### `/api/v1/governance/audit-integrity-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/audit-integrity-checks` | QRY-AUD-VERIFY | جلب | POL-AUD-VERIFY | — | 202, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/audit-records`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/governance/audit-records` | QRY-AUD-SEARCH | جلب | POL-AUD-SEARCH | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/classification-scheme`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/governance/classification-scheme` | QRY-CLS-ACTIVE | جلب | POL-CLS-ACTIVE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/classification-schemes`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/classification-schemes` | CMD-CLS-DRAFT | إنشاء | POL-CLS-DRAFT | based_on | 201, 400, 404, 409, 422, 429, 503 | DRAFT_EXISTS |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/activate` | CMD-CLS-ACTIVATE | سير عمل | POL-CLS-ACTIVATE | effective_from! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION, SCHEME_INVALID |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/discard` | CMD-CLS-DISCARD | حذف / إنهاء | POL-CLS-DISCARD | — | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION |
| POST | `/api/v1/governance/classification-schemes/{id}/actions/edit` | CMD-CLS-EDIT | تعديل | POL-CLS-EDIT | levels!, compartments!, caveats!, audit_threshold!, default_level! | 202, 400, 404, 409, 422, 429, 503 | CLASSIFICATION_SCHEME_INVALID_STATE_TRANSITION, SCHEME_INVALID |

##### `/api/v1/governance/disposition-runs`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/disposition-runs/{id}/actions/approve` | CMD-DSP-APPROVE | سير عمل | POL-DSP-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | DISPOSITION_RUN_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/governance/disposition-runs/{id}/actions/cancel` | CMD-DSP-CANCEL | حذف / إنهاء | POL-DSP-CANCEL | reason! | 202, 400, 404, 409, 422, 429, 503 | DISPOSITION_RUN_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/governance/disposition-runs/{id}/actions/submit` | CMD-DSP-SUBMIT | سير عمل | POL-DSP-SUBMIT | note | 202, 400, 404, 409, 422, 429, 503 | DISPOSITION_RUN_INVALID_STATE_TRANSITION |
| GET | `/api/v1/governance/disposition-runs/{run_id}` | QRY-DSP-GET | جلب | POL-DSP-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/erasure-requests`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/erasure-requests` | CMD-ERS-REGISTER | إنشاء | POL-ERS-REGISTER | legal_basis!, person, entities, requester! | 201, 400, 404, 409, 422, 429, 503 | ERASURE_INVALID |
| POST | `/api/v1/governance/erasure-requests/{id}/actions/approve` | CMD-ERS-APPROVE | سير عمل | POL-ERS-APPROVE | decision_note! | 202, 400, 404, 409, 422, 429, 503 | ERASURE_REQUEST_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/governance/erasure-requests/{id}/actions/reject` | CMD-ERS-REJECT | حذف / إنهاء | POL-ERS-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | ERASURE_REQUEST_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| GET | `/api/v1/governance/erasure-requests/{request_id}` | QRY-ERS-GET | جلب | POL-ERS-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/hold-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/hold-checks` | QRY-LHD-CHECK | جلب | POL-LHD-CHECK | urns, subjects, buckets | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/legal-holds`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/governance/legal-holds` | QRY-LHD-LIST | جلب | POL-LHD-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/governance/legal-holds` | CMD-LHD-PLACE | إنشاء | POL-LHD-PLACE | name!, legal_reference!, scope! | 201, 400, 404, 409, 422, 429, 503 | HOLD_INVALID |
| POST | `/api/v1/governance/legal-holds/{id}/actions/approve-release` | CMD-LHD-APPROVE-RELEASE | حذف / إنهاء | POL-LHD-APPROVE-RELEASE | note | 202, 400, 404, 409, 422, 429, 503 | LEGAL_HOLD_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/governance/legal-holds/{id}/actions/cancel-release` | CMD-LHD-CANCEL-RELEASE | سير عمل | POL-LHD-CANCEL-RELEASE | reason! | 202, 400, 404, 409, 422, 429, 503 | LEGAL_HOLD_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/governance/legal-holds/{id}/actions/extend` | CMD-LHD-EXTEND | تعديل | POL-LHD-EXTEND | scope!, reason! | 202, 400, 404, 409, 422, 429, 503 | HOLD_INVALID, LEGAL_HOLD_INVALID_STATE_TRANSITION |
| POST | `/api/v1/governance/legal-holds/{id}/actions/request-release` | CMD-LHD-REQUEST-RELEASE | سير عمل | POL-LHD-REQUEST-RELEASE | reason! | 202, 400, 404, 409, 422, 429, 503 | LEGAL_HOLD_INVALID_STATE_TRANSITION, REASON_REQUIRED |

##### `/api/v1/governance/policy-decisions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/policy-decisions` | QRY-PDP-DECIDE | جلب | POL-PDP-DECIDE | subject!, action!, resource!, purpose!, context! | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/policy-sets`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/policy-sets` | CMD-POL-DRAFT | إنشاء | POL-POL-DRAFT | based_on | 201, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/governance/policy-sets/{id}/actions/approve` | CMD-POL-APPROVE | سير عمل | POL-POL-APPROVE | — | 202, 400, 404, 409, 422, 429, 503 | POLICY_SET_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/governance/policy-sets/{id}/actions/edit` | CMD-POL-EDIT | تعديل | POL-POL-EDIT | decision_tables!, tests! | 202, 400, 404, 409, 422, 429, 503 | POLICY_INVALID, POLICY_SET_INVALID_STATE_TRANSITION |
| POST | `/api/v1/governance/policy-sets/{id}/actions/reject` | CMD-POL-REJECT | حذف / إنهاء | POL-POL-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | POLICY_SET_INVALID_STATE_TRANSITION, REASON_REQUIRED |
| POST | `/api/v1/governance/policy-sets/{id}/actions/submit` | CMD-POL-SUBMIT | سير عمل | POL-POL-SUBMIT | effective_from! | 202, 400, 404, 409, 422, 429, 503 | POLICY_SET_INVALID_STATE_TRANSITION, POLICY_TESTS_FAILED |
| GET | `/api/v1/governance/policy-sets/{version_id}` | QRY-POL-GET | جلب | POL-POL-GET | — | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/retention-schedule`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/governance/retention-schedule` | QRY-RTS-ACTIVE | جلب | POL-RTS-ACTIVE | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |

##### `/api/v1/governance/retention-schedules`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/governance/retention-schedules` | CMD-RTS-DRAFT | إنشاء | POL-RTS-DRAFT | based_on | 201, 400, 404, 409, 422, 429, 503 | DRAFT_EXISTS |
| POST | `/api/v1/governance/retention-schedules/{id}/actions/activate` | CMD-RTS-ACTIVATE | سير عمل | POL-RTS-ACTIVATE | effective_from!, retroactive_classes | 202, 400, 404, 409, 422, 429, 503 | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION, SCHEDULE_INCOMPLETE |
| POST | `/api/v1/governance/retention-schedules/{id}/actions/discard` | CMD-RTS-DISCARD | حذف / إنهاء | POL-RTS-DISCARD | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, RETENTION_SCHEDULE_INVALID_STATE_TRANSITION |
| POST | `/api/v1/governance/retention-schedules/{id}/actions/edit` | CMD-RTS-EDIT | تعديل | POL-RTS-EDIT | rules! | 202, 400, 404, 409, 422, 429, 503 | RETENTION_SCHEDULE_INVALID_STATE_TRANSITION, SCHEDULE_INVALID |

##### `/api/v1/governance/security-exceptions`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| GET | `/api/v1/governance/security-exceptions` | QRY-EXC-LIST | جلب | POL-EXC-LIST | cursor, limit | 200, 400, 404, 409, 422, 429, 503 | — |
| POST | `/api/v1/governance/security-exceptions` | CMD-EXC-REQUEST | إنشاء | POL-EXC-REQUEST | policy_rule!, subject_scope!, justification!, starts_at!, ends_at! | 201, 400, 404, 409, 422, 429, 503 | EXCEPTION_NOT_ALLOWED |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/approve` | CMD-EXC-APPROVE | سير عمل | POL-EXC-APPROVE | note | 202, 400, 404, 409, 422, 429, 503 | SECURITY_EXCEPTION_INVALID_STATE_TRANSITION, SEGREGATION_OF_DUTIES |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/reject` | CMD-EXC-REJECT | حذف / إنهاء | POL-EXC-REJECT | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |
| POST | `/api/v1/governance/security-exceptions/{id}/actions/revoke` | CMD-EXC-REVOKE | حذف / إنهاء | POL-EXC-REVOKE | reason! | 202, 400, 404, 409, 422, 429, 503 | REASON_REQUIRED, SECURITY_EXCEPTION_INVALID_STATE_TRANSITION |


#### — — عقود عابرة

##### `/api/v1/{context}/label-checks`

| الطريقة | المسار | العملية | النوع | السياسة | المدخلات (! إلزامي) | الاستجابات | أخطاء خاصة |
|---|---|---|---|---|---|---|---|
| POST | `/api/v1/{context}/label-checks` | QRY-LABEL-CHECK | جلب | POL-LABEL-CHECK | urns!, subject_security_version | 200 | — |

<!-- END GENERATED: build_analysis_design.py -->
