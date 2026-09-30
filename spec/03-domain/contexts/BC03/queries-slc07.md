---
id: QRY-CAT-BC03-SLC07
type: query-catalog
title: Queries — BC03 (SLC-07)
wave: W4
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC03 (SLC-07)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-ACS-GET | `GET /api/v1/intelligence/analysis-cases/{case_id}` | Case with question, scope, hypotheses, assumptions, visible selections, scenarios | case label rule; selections filtered | REQ-ANL-001 |
| QRY-ACS-LIST | `GET /api/v1/intelligence/analysis-cases` | Cases by owner, state, extent | allowed_scope | REQ-ANL-001 |
| QRY-RUN-GET | `GET /api/v1/intelligence/analysis-runs/{run_id}` | Run with pins, parameters, steps, status, artifacts, reproduction report | run label rule | REQ-ANL-002 |
| QRY-RUN-ARTIFACT | `POST /api/v1/intelligence/analysis-runs/{run_id}/artifact-grants` | Short-lived download target for a result artifact | run label rule; audited | REQ-ANL-002 |
| QRY-SCN-COMPARE | `GET /api/v1/intelligence/analysis-cases/{case_id}/scenario-comparison` | Side-by-side results of runs per scenario with differing inputs | case label rule | REQ-ANL-007 |
| QRY-FND-LIST | `GET /api/v1/intelligence/analysis-cases/{case_id}/findings` | Findings with sources | label rule | REQ-ANL-005 |
| QRY-ASM-GET | `GET /api/v1/intelligence/assessments/{assessment_id}` | Assessment version (default: current PUBLISHED; or version / known_at) | label rule; REDACT obligation for uncleared citations | REQ-ANL-008 |
| QRY-ASM-VERSIONS | `GET /api/v1/intelligence/assessments/{assessment_id}/versions` | Version history with states and times | label rule | REQ-ANL-006 |
| QRY-AMT-LIST | `GET /api/v1/intelligence/analysis-methods` | Methods and versions | any analyst | REQ-ANL-002 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
