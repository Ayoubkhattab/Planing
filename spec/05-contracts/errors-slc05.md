---
id: ERRORS-SLC05
type: error-catalog
title: Error Catalog — SLC-05
wave: W6
slice: SLC-05
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Error Catalog — SLC-05

`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند مورد لا يحق للمستدعي رؤيته: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5 كما عدّله ADR-P19). يُعاد `403` لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء، أو لأمر إنشاء مرفوض. التزام `mfa` غير مستوفى يُعاد `401 MFA_STEP_UP_REQUIRED` ويُعاد الطلب بعد المصادقة المعززة بنفس `Idempotency-Key`؛ قرار `REQUIRE_APPROVAL` يُعاد `403 APPROVAL_REQUIRED` ويسمي `details.approver` دور المعتمِد. ترويسة `Retry-After` ترافق 429 و503 القابل لإعادة المحاولة (CR-78).

| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |
|---|---|---|---|---|
| `AUTHZ_DENIED` | 403→404 | لا | 4 | CMD-PRJ-CANCEL-BUILD, CMD-PRJ-CREATE-VERSION, CMD-PRJ-PROMOTE, CMD-PRJ-RETIRE |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 4 | CMD-PRJ-CANCEL-BUILD, CMD-PRJ-CREATE-VERSION, CMD-PRJ-PROMOTE, CMD-PRJ-RETIRE |
| `LAST_ACTIVE_PROJECTION` | 422 | لا | 1 | CMD-PRJ-RETIRE |
| `PROJECTION_BUILD_IN_PROGRESS` | 422 | لا | 1 | CMD-PRJ-CREATE-VERSION |
| `PROJECTION_NOT_VERIFIED` | 422 | لا | 1 | CMD-PRJ-PROMOTE |
| `PROJECTION_VERSION_INVALID_STATE_TRANSITION` | 409 | لا | 3 | CMD-PRJ-CANCEL-BUILD, CMD-PRJ-PROMOTE, CMD-PRJ-RETIRE |
| `REASON_REQUIRED` | 422 | لا | 1 | CMD-PRJ-CANCEL-BUILD |
| `VALIDATION_FAILED` | 400 | لا | 4 | CMD-PRJ-CANCEL-BUILD, CMD-PRJ-CREATE-VERSION, CMD-PRJ-PROMOTE, CMD-PRJ-RETIRE |
| `VERSION_CONFLICT` | 409 | نعم | 4 | CMD-PRJ-CANCEL-BUILD, CMD-PRJ-CREATE-VERSION, CMD-PRJ-PROMOTE, CMD-PRJ-RETIRE |
| `NOT_FOUND` | 404 | لا | — | platform-wide |
| `RATE_LIMITED` | 429 | نعم | — | platform-wide |
| `AUDIT_UNAVAILABLE` | 503 | لا | — | platform-wide |
| `SEGREGATION_OF_DUTIES` | 422 | لا | — | platform-wide |
| `POLICY_ENGINE_UNAVAILABLE` | 503 (request denied) | نعم | — | platform-wide |
| `UNAUTHENTICATED` | 401 | لا | — | platform-wide |
| `MFA_STEP_UP_REQUIRED` | 401 | نعم | — | platform-wide |
| `APPROVAL_REQUIRED` | 403 | لا | — | platform-wide |
| `PAYLOAD_TOO_LARGE` | 413 | لا | — | platform-wide |
| `UNSUPPORTED_MEDIA_TYPE` | 415 | لا | — | platform-wide |
| `DEPENDENCY_UNAVAILABLE` | 503 | نعم | — | platform-wide |
