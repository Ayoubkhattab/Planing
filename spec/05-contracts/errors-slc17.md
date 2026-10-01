---
id: ERRORS-SLC17
type: error-catalog
title: Error Catalog — SLC-17
wave: W6
slice: SLC-17
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Error Catalog — SLC-17

`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند مورد لا يحق للمستدعي رؤيته: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5 كما عدّله ADR-P19). يُعاد `403` لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء، أو لأمر إنشاء مرفوض. التزام `mfa` غير مستوفى يُعاد `401 MFA_STEP_UP_REQUIRED` ويُعاد الطلب بعد المصادقة المعززة بنفس `Idempotency-Key`؛ قرار `REQUIRE_APPROVAL` يُعاد `403 APPROVAL_REQUIRED` ويسمي `details.approver` دور المعتمِد. ترويسة `Retry-After` ترافق 429 و503 القابل لإعادة المحاولة (CR-78).

| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |
|---|---|---|---|---|
| `AUTHZ_DENIED` | 403→404 | لا | 15 | CMD-INC-ACTIVATE-CONTINGENCY, CMD-INC-ASSESS, CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE, CMD-INC-DISPATCH-RESPONSE, CMD-INC-ESCALATE, … |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 15 | CMD-INC-ACTIVATE-CONTINGENCY, CMD-INC-ASSESS, CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE, CMD-INC-DISPATCH-RESPONSE, CMD-INC-ESCALATE, … |
| `INCIDENT_INVALID` | 422 | لا | 2 | CMD-INC-ASSESS, CMD-INC-REPORT |
| `INCIDENT_INVALID_STATE_TRANSITION` | 409 | لا | 9 | CMD-INC-ACTIVATE-CONTINGENCY, CMD-INC-ASSESS, CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE, CMD-INC-DISPATCH-RESPONSE, CMD-INC-ESCALATE, … |
| `PLAN_LINK_INVALID` | 422 | لا | 1 | CMD-INC-ACTIVATE-CONTINGENCY |
| `RATIONALE_REQUIRED` | 422 | لا | 1 | CMD-RIS-CLOSE |
| `REASON_REQUIRED` | 422 | لا | 4 | CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE |
| `RESPONSE_REQUIRED` | 422 | لا | 1 | CMD-INC-DISPATCH-RESPONSE |
| `RESPONSE_TASKS_OPEN` | 422 | لا | 1 | CMD-INC-RESOLVE |
| `RISK_INVALID` | 422 | لا | 1 | CMD-RIS-IDENTIFY |
| `RISK_INVALID_STATE_TRANSITION` | 409 | لا | 4 | CMD-RIS-ASSESS, CMD-RIS-CLOSE, CMD-RIS-PLAN-TREATMENT, CMD-RIS-REASSESS |
| `SEGREGATION_OF_DUTIES` | 422 | لا | 2 | CMD-RIS-ASSESS, CMD-RIS-REASSESS |
| `SEVERITY_MUST_INCREASE` | 422 | لا | 1 | CMD-INC-ESCALATE |
| `TREATMENT_INVALID` | 422 | لا | 1 | CMD-RIS-PLAN-TREATMENT |
| `VALIDATION_FAILED` | 400 | لا | 15 | CMD-INC-ACTIVATE-CONTINGENCY, CMD-INC-ASSESS, CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE, CMD-INC-DISPATCH-RESPONSE, CMD-INC-ESCALATE, … |
| `VERSION_CONFLICT` | 409 | نعم | 15 | CMD-INC-ACTIVATE-CONTINGENCY, CMD-INC-ASSESS, CMD-INC-CANCEL, CMD-INC-CLOSE, CMD-INC-CONTAIN, CMD-INC-DE-ESCALATE, CMD-INC-DISPATCH-RESPONSE, CMD-INC-ESCALATE, … |
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
