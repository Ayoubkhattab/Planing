---
id: ERRORS-SLC14
type: error-catalog
title: Error Catalog — SLC-14
wave: W6
slice: SLC-14
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Error Catalog — SLC-14

`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند مورد لا يحق للمستدعي رؤيته: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5 كما عدّله ADR-P19). يُعاد `403` لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء، أو لأمر إنشاء مرفوض. التزام `mfa` غير مستوفى يُعاد `401 MFA_STEP_UP_REQUIRED` ويُعاد الطلب بعد المصادقة المعززة بنفس `Idempotency-Key`؛ قرار `REQUIRE_APPROVAL` يُعاد `403 APPROVAL_REQUIRED` ويسمي `details.approver` دور المعتمِد. ترويسة `Retry-After` ترافق 429 و503 القابل لإعادة المحاولة (CR-78).

| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |
|---|---|---|---|---|
| `ACTIVITY_ALREADY_TASKED` | 422 | لا | 1 | CMD-CPL-REMOVE-ACTIVITY |
| `ACTIVITY_INVALID` | 422 | لا | 1 | CMD-CPL-ADD-ACTIVITY |
| `AUTHZ_DENIED` | 403→404 | لا | 14 | CMD-CPL-ACTIVATE, CMD-CPL-ADD-ACTIVITY, CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CPL-CREATE, CMD-CPL-REMOVE-ACTIVITY, CMD-CRQ-AMEND, CMD-CRQ-APPROVE, CMD-CRQ-CANCE… |
| `COLLECTION_PLAN_INVALID_STATE_TRANSITION` | 409 | لا | 5 | CMD-CPL-ACTIVATE, CMD-CPL-ADD-ACTIVITY, CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CPL-REMOVE-ACTIVITY |
| `COLLECTION_REQUIREMENT_INVALID_STATE_TRANSITION` | 409 | لا | 7 | CMD-CRQ-AMEND, CMD-CRQ-APPROVE, CMD-CRQ-CANCEL, CMD-CRQ-EDIT, CMD-CRQ-MARK-SATISFIED, CMD-CRQ-REJECT, CMD-CRQ-SUBMIT |
| `FULFILMENT_INSUFFICIENT` | 422 | لا | 1 | CMD-CRQ-MARK-SATISFIED |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 14 | CMD-CPL-ACTIVATE, CMD-CPL-ADD-ACTIVITY, CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CPL-CREATE, CMD-CPL-REMOVE-ACTIVITY, CMD-CRQ-AMEND, CMD-CRQ-APPROVE, CMD-CRQ-CANCE… |
| `PLAN_EMPTY` | 422 | لا | 1 | CMD-CPL-ACTIVATE |
| `REASON_REQUIRED` | 422 | لا | 4 | CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CRQ-CANCEL, CMD-CRQ-REJECT |
| `REQUIREMENT_INCOMPLETE` | 422 | لا | 1 | CMD-CRQ-SUBMIT |
| `REQUIREMENT_INVALID` | 422 | لا | 3 | CMD-CRQ-AMEND, CMD-CRQ-DRAFT, CMD-CRQ-EDIT |
| `REQUIREMENT_NOT_APPROVED` | 422 | لا | 1 | CMD-CPL-CREATE |
| `SEGREGATION_OF_DUTIES` | 422 | لا | 1 | CMD-CRQ-APPROVE |
| `VALIDATION_FAILED` | 400 | لا | 14 | CMD-CPL-ACTIVATE, CMD-CPL-ADD-ACTIVITY, CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CPL-CREATE, CMD-CPL-REMOVE-ACTIVITY, CMD-CRQ-AMEND, CMD-CRQ-APPROVE, CMD-CRQ-CANCE… |
| `VERSION_CONFLICT` | 409 | نعم | 14 | CMD-CPL-ACTIVATE, CMD-CPL-ADD-ACTIVITY, CMD-CPL-CANCEL, CMD-CPL-COMPLETE, CMD-CPL-CREATE, CMD-CPL-REMOVE-ACTIVITY, CMD-CRQ-AMEND, CMD-CRQ-APPROVE, CMD-CRQ-CANCE… |
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
