---
id: PROVENANCE-LINEAGE
type: architecture
title: Provenance & Lineage
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
traces: {requirements: [REQ-INF-005, REQ-INF-035, REQ-ANL-002, REQ-DEC-003], quality: [QAS-TRC-001, QAS-TRC-002]}
---

# Provenance & Lineage

## 1. النموذج (متوافق مع W3C PROV)
| PROV | عندنا |
|---|---|
| Entity | أي كائن بإصدار (Claim، Dataset version، Finding، Assessment version، Product version) |
| Activity | Transformation run: import batch، analysis run، AI run، reconstruction job |
| Agent | User، Service Account، Adapter، Model |

```text
LineageRecord
  id, activity_type, activity_ref
  inputs[]    {urn, version | known_at}
  outputs[]   {urn, version}
  transformation {code, version}      e.g. adapter mapping v3, algorithm v1.2, normalization v2, CRS transform
  agent_ref, started_at, ended_at, parameters_ref
```

## 2. القواعد
- كل كائن مشتق له سجل lineage واحد على الأقل (QAS-TRC-001).
- المدخلات تُشار إليها **بإصدار** أو بـ `known_at`، حتى تكون إعادة الإنتاج ممكنة بعد تغير البيانات (QAS-TRC-002).
- مخرجات AI المستخدمة في قرار: lineage يشمل context package وmodel وmodel version (BRL-009).
- الاستعلام الخلفي: من قرار إلى المصادر، مع احترام الصلاحيات: العقد غير المصرح بها تظهر كـ "مصدر محجوب" فقط إن سمحت السياسة بإظهار وجودها، وإلا يُقطع المسار دون إشارة.
