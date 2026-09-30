---
id: QRY-CAT-BC05-SLC03
type: query-catalog
title: Queries — BC05 (SLC-03)
wave: W4
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC05 (SLC-03)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-QUAL-LIST | `GET /api/v1/readiness/persons/{person_id}/qualifications` | Qualification records as of t | Manager/Resource Manager in scope; self | REQ-RDY-001 |
| QRY-ELIG-CHECK | `POST /api/v1/readiness/eligibility-checks` | EligibilityCheck(person, task_type version, at) → status + reasons | Planner/Manager in scope; internal BC04 (workload identity) | REQ-RDY-002 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
