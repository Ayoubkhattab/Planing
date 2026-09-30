---
id: WL-SLC19
type: workload-catalog
title: Workloads — SLC-19
wave: W5
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
recalibrate_after_pilot: true
---

# Workloads — SLC-19

استُنتجت هذه الأعباء تحليلياً بلا أي قياس فعلي — كسائر شرائح R3 (RSK-028)؛ **كل رقم أدناه إشاري بحت** ويُعاد اشتقاقه بالكامل بعد التجربة، لا يُعاير فقط. خلافاً لـ SLC-18، اعتماد هذه الشريحة على بنية شرائح أخرى غير مقاسة محدود بحقل مرجعي واحد لكل من SLC-03 وSLC-12 (لا آلية تنافس أو دفتر سعة مشترك)، انظر `03-domain/contexts/BC05/training-exercise-spec.md` §6.

## workloads

_3 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-19a | Scenario define/edit/activate/retire commands | نادرة نسبياً — أنشطة تصميم/اعتماد إدارية لا تشغيلية؛ تقدير أولي ≤ 0.1/s لكل خلية | authoring latency p95 (يُعاد اشتقاقه بعد Pilot R1) |
| WL-19b | Exercise plan/schedule/start/cancel commands | متوسطة التكرار — جدولة تدريب دورية، ليست حدثاً مستمراً؛ تقدير أولي ≤ 0.5/s لكل خلية | scheduling command p95 (يُعاد اشتقاقه بعد Pilot R1) |
| WL-19c | Simulation inject-delivery and evaluation commands | الأعلى تكراراً في هذه الشريحة — أثناء تمرين حي، حقن وتقييمات متتالية على مدى نافذة تنفيذ قصيرة؛ تقدير أولي ≤ 3/s لكل محاكاة نشطة | inject/evaluation write p95 (يُعاد اشتقاقه بعد Pilot R1 وR2) |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-19a
  name: Scenario define/edit/activate/retire commands
  derivation: نادرة نسبياً — أنشطة تصميم/اعتماد إدارية لا تشغيلية؛ تقدير أولي ≤ 0.1/s لكل خلية — إشاري، غير مقاس
  target: authoring latency p95 (يُعاد اشتقاقه بعد Pilot R1)
- id: WL-19b
  name: Exercise plan/schedule/start/cancel commands
  derivation: متوسطة التكرار — جدولة تدريب دورية، ليست حدثاً مستمراً؛ تقدير أولي ≤ 0.5/s لكل خلية — إشاري، غير مقاس
  target: scheduling command p95 (يُعاد اشتقاقه بعد Pilot R1)
- id: WL-19c
  name: Simulation inject-delivery and evaluation commands
  derivation: الأعلى تكراراً في هذه الشريحة — أثناء تمرين حي، حقن وتقييمات متتالية على مدى نافذة تنفيذ قصيرة؛ تقدير أولي ≤ 3/s لكل محاكاة نشطة — إشاري، غير مقاس
  target: inject/evaluation write p95 (يُعاد اشتقاقه بعد Pilot R1 وR2)
```

</details>
