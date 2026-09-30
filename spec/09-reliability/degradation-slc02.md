---
id: DEGRADATION-SLC02
type: degradation-matrix
title: Degradation Matrix — SLC-02
wave: W5
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Degradation Matrix — SLC-02

## matrix

_4 items_

| capability | failure | fully_available_via | degraded_mode | manual_fallback | unavailable_when |
|---|---|---|---|---|---|
| Record observation | object store down | text + location recorded; attachments deferred | attachments retried by client | — | — |
| Read entity | current table suspect | as-of path from history (slower) | — | — | — |
| Ingestion | burst | queued with backpressure | latency ↑ | — | queue full → RATE_LIMITED to sources |
| Evidence view | scanner down | metadata visible | file unavailable | — | — |

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
matrix:
- capability: Record observation
  failure: object store down
  fully_available_via: text + location recorded; attachments deferred
  degraded_mode: attachments retried by client
  manual_fallback: —
  unavailable_when: —
- capability: Read entity
  failure: current table suspect
  fully_available_via: as-of path from history (slower)
  degraded_mode: —
  manual_fallback: —
  unavailable_when: —
- capability: Ingestion
  failure: burst
  fully_available_via: queued with backpressure
  degraded_mode: latency ↑
  manual_fallback: —
  unavailable_when: queue full → RATE_LIMITED to sources
- capability: Evidence view
  failure: scanner down
  fully_available_via: metadata visible
  degraded_mode: file unavailable
  manual_fallback: —
  unavailable_when: —
```

</details>
