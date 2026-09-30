---
id: QRY-CAT-BC07-SLC11
type: query-catalog
title: Queries — BC07 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC07 (SLC-11)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-PKG-GET | `GET /api/v1/field/preload-packages/{package_id}` | Package manifest and download target (signed, ≤ 5 min) | package owner device + user | REQ-OFF-002 |
| QRY-SYN-DELTA | `GET /api/v1/field/sync-sessions/{session_id}/delta` | Server → device: my task changes, package updates, purge list, conflict notices, wipe/stop instruction | device + user of the session | REQ-OFF-001 |
| QRY-SCF-LIST | `GET /api/v1/field/sync-conflicts` | Open sync conflicts by target type, assignee | reviewers authorized on targets | REQ-OFF-004 |
| QRY-SCF-GET | `GET /api/v1/field/sync-conflicts/{conflict_id}` | Original envelope, current state snapshot, owner rejection reason | reviewer authorized on target | REQ-OFF-004 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
