---
id: ERRORS-SLC16
type: error-catalog
title: Error Catalog — SLC-16
wave: W6
slice: SLC-16
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Error Catalog — SLC-16

`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند مورد لا يحق للمستدعي رؤيته: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5 كما عدّله ADR-P19). يُعاد `403` لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء، أو لأمر إنشاء مرفوض. التزام `mfa` غير مستوفى يُعاد `401 MFA_STEP_UP_REQUIRED` ويُعاد الطلب بعد المصادقة المعززة بنفس `Idempotency-Key`؛ قرار `REQUIRE_APPROVAL` يُعاد `403 APPROVAL_REQUIRED` ويسمي `details.approver` دور المعتمِد. ترويسة `Retry-After` ترافق 429 و503 القابل لإعادة المحاولة (CR-78).

| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |
|---|---|---|---|---|
| `AUTHZ_DENIED` | 403→404 | لا | 18 | CMD-CAP-CANCEL, CMD-CAP-PREPARE, CMD-CAP-RELEASE, CMD-CAP-RETRY, CMD-CON-ACTIVATE, CMD-CON-FAIL-TEST, CMD-CON-REGISTER, CMD-CON-RESUME, CMD-CON-RETIRE, CMD-CON-… |
| `CAP_MESSAGE_INVALID_STATE_TRANSITION` | 409 | لا | 3 | CMD-CAP-CANCEL, CMD-CAP-RELEASE, CMD-CAP-RETRY |
| `CONNECTION_INVALID` | 422 | لا | 1 | CMD-CON-REGISTER |
| `CONNECTION_IN_USE` | 422 | لا | 1 | CMD-CON-RETIRE |
| `CONNECTION_NOT_ACTIVE` | 422 | لا | 1 | CMD-SNS-ACTIVATE |
| `HR_SYNC_PROPOSAL_INVALID_STATE_TRANSITION` | 409 | لا | 2 | CMD-HRS-APPROVE, CMD-HRS-REJECT |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 18 | CMD-CAP-CANCEL, CMD-CAP-PREPARE, CMD-CAP-RELEASE, CMD-CAP-RETRY, CMD-CON-ACTIVATE, CMD-CON-FAIL-TEST, CMD-CON-REGISTER, CMD-CON-RESUME, CMD-CON-RETIRE, CMD-CON-… |
| `INTEGRATION_CONNECTION_INVALID_STATE_TRANSITION` | 409 | لا | 6 | CMD-CON-ACTIVATE, CMD-CON-FAIL-TEST, CMD-CON-RESUME, CMD-CON-RETIRE, CMD-CON-SUSPEND, CMD-CON-TEST |
| `OWNER_REJECTED` | 422 | لا | 1 | CMD-HRS-APPROVE |
| `QUALITY_RULES_INVALID` | 422 | لا | 1 | CMD-SNS-SET-QUALITY-RULES |
| `REASON_REQUIRED` | 422 | لا | 5 | CMD-CAP-CANCEL, CMD-CON-SUSPEND, CMD-HRS-REJECT, CMD-SNS-PAUSE, CMD-SNS-RETIRE |
| `RELEASE_NOT_ALLOWED` | 422 | لا | 1 | CMD-CAP-PREPARE |
| `SEGREGATION_OF_DUTIES` | 422 | لا | 2 | CMD-CAP-RELEASE, CMD-CON-ACTIVATE |
| `SENSOR_STREAM_INVALID_STATE_TRANSITION` | 409 | لا | 4 | CMD-SNS-ACTIVATE, CMD-SNS-PAUSE, CMD-SNS-RETIRE, CMD-SNS-SET-QUALITY-RULES |
| `STREAM_INVALID` | 422 | لا | 1 | CMD-SNS-REGISTER |
| `VALIDATION_FAILED` | 400 | لا | 18 | CMD-CAP-CANCEL, CMD-CAP-PREPARE, CMD-CAP-RELEASE, CMD-CAP-RETRY, CMD-CON-ACTIVATE, CMD-CON-FAIL-TEST, CMD-CON-REGISTER, CMD-CON-RESUME, CMD-CON-RETIRE, CMD-CON-… |
| `VERSION_CONFLICT` | 409 | نعم | 18 | CMD-CAP-CANCEL, CMD-CAP-PREPARE, CMD-CAP-RELEASE, CMD-CAP-RETRY, CMD-CON-ACTIVATE, CMD-CON-FAIL-TEST, CMD-CON-REGISTER, CMD-CON-RESUME, CMD-CON-RETIRE, CMD-CON-… |
| `NOT_FOUND` | 404 | لا | — | platform-wide |
| `RATE_LIMITED` | 429 | نعم | — | platform-wide |
| `AUDIT_UNAVAILABLE` | 503 | لا | — | platform-wide |
| `POLICY_ENGINE_UNAVAILABLE` | 503 (request denied) | نعم | — | platform-wide |
| `UNAUTHENTICATED` | 401 | لا | — | platform-wide |
| `MFA_STEP_UP_REQUIRED` | 401 | نعم | — | platform-wide |
| `APPROVAL_REQUIRED` | 403 | لا | — | platform-wide |
| `PAYLOAD_TOO_LARGE` | 413 | لا | — | platform-wide |
| `UNSUPPORTED_MEDIA_TYPE` | 415 | لا | — | platform-wide |
| `DEPENDENCY_UNAVAILABLE` | 503 | نعم | — | platform-wide |
