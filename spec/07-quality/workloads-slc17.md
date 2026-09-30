---
id: WL-SLC17
type: workload-catalog
title: Workloads — SLC-17
wave: W5
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
recalibrate_after_pilot: true
---

# Workloads — SLC-17

استُنتجت هذه الأعباء تحليلياً بلا أي قياس فعلي (R3 صُمِّم قبل Pilot R1 وR2 — RSK-028)؛ **كل رقم أدناه إشاري بحت** ويُعاد اشتقاقه بالكامل بعد التجربة، لا يُعاير فقط.

## workloads

_2 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-17a | Incident commands | نادرة نسبياً مقارنة بـ WL-01 (المهام العامة)؛ تقدير أولي ≤ 1/s لكل خلية | dispatch p95 حسب severity (QAS-RCM-001، يُعاد اشتقاقه) |
| WL-17b | Risk register commands | إدارية، دفعية غالباً (مراجعات دورية)؛ تقدير أولي ≤ 0.1/s | استعلام السجل ضمن أهداف WL-01 العامة |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-17a
  name: Incident commands
  derivation: نادرة نسبياً مقارنة بـ WL-01 (المهام العامة)؛ تقدير أولي ≤ 1/s لكل خلية — إشاري، غير مقاس
  target: dispatch p95 حسب severity (QAS-RCM-001، يُعاد اشتقاقه بعد Pilot)
- id: WL-17b
  name: Risk register commands
  derivation: إدارية، دفعية غالباً (مراجعات دورية)؛ تقدير أولي ≤ 0.1/s — إشاري، غير مقاس
  target: استعلام السجل ضمن أهداف WL-01 العامة
```

</details>
