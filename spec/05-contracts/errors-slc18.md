---
id: ERRORS-SLC18
type: error-catalog
title: Error Catalog — SLC-18
wave: W6
slice: SLC-18
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---

# Error Catalog — SLC-18

`AUTHZ_DENIED` لا يُعاد للعميل كما هو عند مورد لا يحق للمستدعي رؤيته: يُعاد `NOT_FOUND` بنفس الشكل (ADR-P06 §5 كما عدّله ADR-P19). يُعاد `403` لمورد يحق للمستخدم رؤيته دون تنفيذ الإجراء، أو لأمر إنشاء مرفوض. التزام `mfa` غير مستوفى يُعاد `401 MFA_STEP_UP_REQUIRED` ويُعاد الطلب بعد المصادقة المعززة بنفس `Idempotency-Key`؛ قرار `REQUIRE_APPROVAL` يُعاد `403 APPROVAL_REQUIRED` ويسمي `details.approver` دور المعتمِد. ترويسة `Retry-After` ترافق 429 و503 القابل لإعادة المحاولة (CR-78).

| الرمز | HTTP | retryable | عدد الأوامر | الأوامر |
|---|---|---|---|---|
| `ALLOCATION_NOT_COMMITTED` | 422 | لا | 1 | CMD-LGR-DISPATCH |
| `AUTHZ_DENIED` | 403→404 | لا | 10 | CMD-LGR-CANCEL, CMD-LGR-DISPATCH, CMD-LGR-REQUEST, CMD-SHP-CANCEL, CMD-SHP-DELIVER, CMD-SHP-DEPART, CMD-SHP-PLAN, CMD-SHP-RECORD-CHECKPOINT, CMD-SHP-REPORT-DAMA… |
| `CHECKPOINT_INVALID` | 422 | لا | 1 | CMD-SHP-RECORD-CHECKPOINT |
| `DELIVERY_INVALID` | 422 | لا | 1 | CMD-SHP-DELIVER |
| `DEPARTURE_INVALID` | 422 | لا | 1 | CMD-SHP-DEPART |
| `IDEMPOTENCY_KEY_REUSED` | 422 | لا | 10 | CMD-LGR-CANCEL, CMD-LGR-DISPATCH, CMD-LGR-REQUEST, CMD-SHP-CANCEL, CMD-SHP-DELIVER, CMD-SHP-DEPART, CMD-SHP-PLAN, CMD-SHP-RECORD-CHECKPOINT, CMD-SHP-REPORT-DAMA… |
| `LOGISTICS_REQUEST_INVALID` | 422 | لا | 1 | CMD-LGR-REQUEST |
| `LOGISTICS_REQUEST_INVALID_STATE_TRANSITION` | 409 | لا | 2 | CMD-LGR-CANCEL, CMD-LGR-DISPATCH |
| `REASON_REQUIRED` | 422 | لا | 4 | CMD-LGR-CANCEL, CMD-SHP-CANCEL, CMD-SHP-REPORT-DAMAGE, CMD-SHP-REPORT-LOST |
| `SHIPMENT_INVALID` | 422 | لا | 1 | CMD-SHP-PLAN |
| `SHIPMENT_INVALID_STATE_TRANSITION` | 409 | لا | 6 | CMD-SHP-CANCEL, CMD-SHP-DELIVER, CMD-SHP-DEPART, CMD-SHP-RECORD-CHECKPOINT, CMD-SHP-REPORT-DAMAGE, CMD-SHP-REPORT-LOST |
| `VALIDATION_FAILED` | 400 | لا | 10 | CMD-LGR-CANCEL, CMD-LGR-DISPATCH, CMD-LGR-REQUEST, CMD-SHP-CANCEL, CMD-SHP-DELIVER, CMD-SHP-DEPART, CMD-SHP-PLAN, CMD-SHP-RECORD-CHECKPOINT, CMD-SHP-REPORT-DAMA… |
| `VERSION_CONFLICT` | 409 | نعم | 10 | CMD-LGR-CANCEL, CMD-LGR-DISPATCH, CMD-LGR-REQUEST, CMD-SHP-CANCEL, CMD-SHP-DELIVER, CMD-SHP-DEPART, CMD-SHP-PLAN, CMD-SHP-RECORD-CHECKPOINT, CMD-SHP-REPORT-DAMA… |
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
