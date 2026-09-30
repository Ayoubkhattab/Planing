---
id: WL-SLC10
type: workload-catalog
title: Workloads — SLC-10 (recalibrate after R1 pilot)
wave: W5
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
recalibrate_after_pilot: true
---

# Workloads — SLC-10 (recalibrate after R1 pilot)

## workloads

_4 items_

| id | name | derivation | target |
|---|---|---|---|
| WL-09a | Grounded Q&A | ≈ 50 concurrent requests per cell at peak; ≈ 5 req/s | QAS-AI-003 |
| WL-10a | Batch extraction/translation | document ingest driven; ≈ 1,000 documents/day per tenant | throughput per GPU-hour (pilot) |
| WL-10b | Embeddings | = new/changed facts and document chunks (≈ claim rate + documents) | vector projection lag ≤ 5 min |
| WL-10c | Evaluation runs | per model promotion + weekly drift sample | suite run ≤ 4 h |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
workloads:
- id: WL-09a
  name: Grounded Q&A
  derivation: ≈ 50 concurrent requests per cell at peak; ≈ 5 req/s
  target: QAS-AI-003
- id: WL-10a
  name: Batch extraction/translation
  derivation: document ingest driven; ≈ 1,000 documents/day per tenant
  target: throughput per GPU-hour (pilot)
- id: WL-10b
  name: Embeddings
  derivation: = new/changed facts and document chunks (≈ claim rate + documents)
  target: vector projection lag ≤ 5 min
- id: WL-10c
  name: Evaluation runs
  derivation: per model promotion + weekly drift sample
  target: suite run ≤ 4 h
```

</details>
