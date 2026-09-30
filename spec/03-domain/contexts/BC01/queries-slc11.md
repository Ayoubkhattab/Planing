---
id: QRY-CAT-BC01-SLC11
type: query-catalog
title: Queries — BC01 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC01 (SLC-11)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-DEV-LIST | `GET /api/v1/foundation/devices` | Devices of a user (self) or in scope (Administrator) | self; Administrator in scope | REQ-OFF-005 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
