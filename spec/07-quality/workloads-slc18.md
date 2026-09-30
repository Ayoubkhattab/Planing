---
id: WL-SLC18
type: workload-catalog
title: Workloads — SLC-18
wave: W5
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Workloads — SLC-18

استُنتجت هذه الأعباء تحليلياً بلا أي قياس فعلي (SLC-18 تعتمد مباشرة على AGG-RESOURCE-POOL/AGG-ALLOCATION من SLC-09/R2 غير المقاس بعد — RSK-028، انظر `03-domain/contexts/BC05/logistics-spec.md` §8)؛ **كل رقم أدناه إشاري بحت** ويُعاد اشتقاقه بالكامل بعد التجربة، لا يُعاير فقط.

## workloads

_2 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-18a | Logistics request commands | أقل تكراراً من WL-01 العامة؛ يتشارك دفتر السعة مع WL-09 (SLC-09)؛ تقدير أولي ≤ 0.5/s لكل خلية | dispatch/approve p95 يتشارك ميزانية زمن SPEC-ALLOCATION §1 (يُعاد اشتقاقه بعد Pilot R2) |
| WL-18b | Shipment tracking commands (checkpoints) | الأعلى تكراراً في هذه الشريحة — تحديثات موقع دورية أثناء النقل؛ تقدير أولي ≤ 2/s لكل شحنة نشطة | كتابة نقطة تتبع p95 (يُعاد اشتقاقه بعد Pilot R1 وR2) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-18a
  name: Logistics request commands
  derivation: أقل تكراراً من WL-01 العامة؛ يتشارك دفتر السعة مع WL-09 (SLC-09)؛ تقدير أولي ≤ 0.5/s لكل خلية — إشاري، غير مقاس
  target: dispatch/approve p95 يتشارك ميزانية زمن SPEC-ALLOCATION §1 (يُعاد اشتقاقه بعد Pilot R2)
- id: WL-18b
  name: Shipment tracking commands (checkpoints)
  derivation: الأعلى تكراراً في هذه الشريحة — تحديثات موقع دورية أثناء النقل؛ تقدير أولي ≤ 2/s لكل شحنة نشطة — إشاري، غير مقاس
  target: كتابة نقطة تتبع p95 (يُعاد اشتقاقه بعد Pilot R1 وR2)
```

</details>
