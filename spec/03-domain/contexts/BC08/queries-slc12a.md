---
id: QRY-CAT-BC08-SLC12A
type: query-catalog
title: Queries — BC08 (SLC-12a)
wave: W4
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC08 (SLC-12a)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-RTS-ACTIVE | `GET /api/v1/governance/retention-schedule` | Active schedule version with rules | Archivist, Legal, Auditor | REQ-GOV-006 |
| QRY-LHD-LIST | `GET /api/v1/governance/legal-holds` | Holds by state and scope | Legal, Archivist, Auditor | REQ-GOV-007 |
| QRY-LHD-CHECK | `POST /api/v1/governance/hold-checks` | HoldCheck OHS: URNs / subjects / (class, bucket) → held? with hold ids | owner contexts (workload identity); Archivist | REQ-GOV-007 |
| QRY-DSP-GET | `GET /api/v1/governance/disposition-runs/{run_id}` | Run with candidate summary, exceptions and certificate | Archivist, Legal, Auditor | REQ-GOV-006 |
| QRY-ERS-GET | `GET /api/v1/governance/erasure-requests/{request_id}` | Request with scope counts, confirmations and certificate (no personal data) | Legal, Auditor | REQ-GOV-008 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
