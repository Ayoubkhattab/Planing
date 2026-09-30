---
id: QRY-CAT-BC04-SLC17
type: query-catalog
title: Queries — BC04 (SLC-17)
wave: W4
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Queries — BC04 (SLC-17)

| الاستعلام | HTTP | يعيد | من يحق له (السياسة قبل الاسترجاع — SL-09) | المتطلب |
|---|---|---|---|---|
| QRY-RIS-GET | `GET /api/v1/operations/risks/{risk_id}` | Risk بنطاقه المرئي للطالب | مالك النطاق؛ مدير المخاطر | REQ-RCM-014 |
| QRY-RIS-REGISTER | `GET /api/v1/operations/risks` | سجل المخاطر مصفّى بالفئة/النطاق/الدرجة | allowed_scope | REQ-RCM-014 |
| QRY-INC-GET | `GET /api/v1/operations/incidents/{incident_id}` | Incident بنطاقه المرئي للطالب | allowed_scope | REQ-RCM-015 |
| QRY-INC-LIST | `GET /api/v1/operations/incidents` | حوادث مصفّاة بالفئة/الخطورة/الحالة/النطاق | allowed_scope | REQ-RCM-015 |
| QRY-INC-RECOVERY-STATUS | `GET /api/v1/operations/incidents/{incident_id}/recovery-status` | تقدم التعافي المحسوب من مهام خطة الاستمرارية المرتبطة مقابل زمن بدء الحادثة (RTO/RPO تقديرية) | القائد؛ مالك الاستمرارية | REQ-RCM-016 |

كل استعلام: PEP يطلب قرار PDP بـ `action=view` ونوع المورد والنطاق، ويطبق `allowed_scope` قبل القراءة (ADR-P06). القوائم بمؤشر (cursor).
