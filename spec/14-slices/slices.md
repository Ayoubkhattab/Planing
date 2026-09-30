---
id: SLICES
type: slices
title: Slice Plan
wave: W1
tier: T0
owner_role: Orchestrator
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
consumers: []
notes: HAP-02
---

# Slice Plan

> HAP-02

## slices

_18 items_

### SLC-00

- **content:** Conceptual end-to-end walkthrough (study only)
- **depends_on:** —
- **release:** W3/W9
- **status:** PROPOSED
- **g6_slc:** NOT_STARTED

### SLC-01

- **content:** Tenancy, Identity, Organization, Authorization, Audit
- **depends_on:** —
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-01/readiness.md

### SLC-02

- **content:** Source → Observation → Entity/Claim → Evidence (temporal + spatial)
- **depends_on:** SLC-01
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-02/readiness.md

### SLC-03

- **content:** Task lifecycle + Outbox + History
- **depends_on:** SLC-01
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-03/readiness.md

### SLC-04

- **content:** Conflict Management + Entity Resolution (Merge/Split)
- **depends_on:** SLC-02
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-04/readiness.md

### SLC-05

- **content:** Secured Search & Graph Projections
- **depends_on:** SLC-02
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) — ADR-P05 condition satisfied by TD-02 (W8)
- **readiness:** 14-slices/SLC-05/readiness.md

### SLC-06

- **content:** Situation + Alerts
- **depends_on:** SLC-02, SLC-05
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-06/readiness.md

### SLC-07

- **content:** Analysis Case → Run → Finding → Assessment
- **depends_on:** SLC-02
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-07/readiness.md

### SLC-08

- **content:** Decision → Plan → Version → Baseline → Tasks
- **depends_on:** SLC-03, SLC-07
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-08/readiness.md

### SLC-09

- **content:** Assets, Resources, Allocation, Reservations, Readiness (full)
- **depends_on:** SLC-03, SLC-01
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
- **readiness:** 14-slices/SLC-09/readiness.md

### SLC-10

- **content:** Grounded AI: retrieval, context packages, drafting, extraction, translation, model lifecycle, tool registry, vector projection
- **depends_on:** SLC-05
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review and first passing model evaluation
- **readiness:** 14-slices/SLC-10/readiness.md

### SLC-11

- **content:** Offline Field Capture + Sync
- **depends_on:** SLC-02, SLC-04
- **release:** R1 (observation capture + task status only)
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated) 2026-09-24
- **readiness:** 14-slices/SLC-11/readiness.md

### SLC-12

- **content:** Products, Knowledge & Lessons, Archive packages, Historical Retrieval & Reconstruction
- **depends_on:** SLC-07, SLC-08
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
- **readiness:** 14-slices/SLC-12/readiness.md

### SLC-13

- **content:** Risk & Emergency, Training, Exercises, Logistics, Communications
- **depends_on:** —
- **release:** R3
- **status:** SUPERSEDED
- **g6_slc:** SUPERSEDED — decomposed into SLC-17 (Risk & Contingency), SLC-18 (Logistics & Supply), SLC-19 (Training, Competency & Exercises); Communications not yet decomposed (UNK-022) — CR-67

### SLC-12a

- **content:** Retention schedules & legal hold (R1 portion of SLC-12)
- **depends_on:** SLC-01, SLC-03
- **release:** R1
- **status:** APPROVED_DELEGATED
- **g6_slc:** READY (delegated; legal values pending UNK-002) 2026-09-24
- **readiness:** 14-slices/SLC-12a/readiness.md

### SLC-14

- **content:** Collection requirements & planning (CAP-02.01)
- **depends_on:** SLC-02, SLC-03
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
- **readiness:** 14-slices/SLC-14/readiness.md

### SLC-15

- **content:** Coordination cases & correlation/fusion (CAP-06.03, CAP-04.04)
- **depends_on:** SLC-04, SLC-08
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
- **readiness:** 14-slices/SLC-15/readiness.md

### SLC-16

- **content:** Enterprise integrations (ERP, HRIS, DMS, sensors, CAP alerts)
- **depends_on:** SLC-02, SLC-01
- **release:** R2
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 pilot review and UNK-021
- **readiness:** 14-slices/SLC-16/readiness.md

**r2_order:** SLC-09 → SLC-12 → SLC-10 → SLC-14 → SLC-15 → SLC-16 (SLC-10 after SLC-12 so products/knowledge exist as AI drafting targets; integrations last because they depend on tenant systems)

### SLC-17

- **content:** Risk & Contingency (risk register, incident lifecycle, contingency plan activation via SLC-08 reuse)
- **depends_on:** SLC-08, SLC-03
- **release:** R3
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 **and** R2 pilot review (RSK-028)
- **readiness:** 14-slices/SLC-17/readiness.md

### SLC-18

- **content:** Logistics & Supply (CAP-08.03, DOM-16, BC05) — Logistics Request and Shipment reuse SLC-09's Resource Pool/Allocation directly for inventory (R3-Q3); no separate stock model
- **depends_on:** SLC-09
- **release:** R3
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 **and** R2 pilot review (RSK-028; this slice's actual technical dependency, SLC-09, is genuinely R2 and unmeasured)
- **readiness:** 14-slices/SLC-18/readiness.md

### SLC-19

- **content:** Training, Competency & Exercises (CAP-08.05, DOM-18+19) — extends SLC-03's Qualification Record and SLC-09's Role Requirement (both unmodified), stores After Action Review as an SLC-12 Knowledge Object (CR-63); adds 3 new aggregates (Scenario, Exercise, Simulation)
- **depends_on:** SLC-03, SLC-09, SLC-12
- **release:** R3
- **status:** APPROVED_DELEGATED
- **g6_slc:** DESIGN_COMPLETE — G6 held until R1 **and** R2 pilot review (RSK-028; narrowest actual exposure among the three R3 slices — see readiness.md)
- **readiness:** 14-slices/SLC-19/readiness.md

**r3_order:** SLC-17 → SLC-18 → SLC-19 (risk & contingency first — most structurally independent; logistics second — direct extension of an already-designed context; training/exercises last — depends on the most prior slices). All three R3 slices are now DESIGN COMPLETE. No G6 for any R3 slice before the R1 **and** R2 pilot reviews (RSK-028).

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
slices:
- id: SLC-00
  content: Conceptual end-to-end walkthrough (study only)
  depends_on: []
  release: W3/W9
  status: PROPOSED
  g6_slc: NOT_STARTED
- id: SLC-01
  content: Tenancy, Identity, Organization, Authorization, Audit
  depends_on: []
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-01/readiness.md
- id: SLC-02
  content: Source → Observation → Entity/Claim → Evidence (temporal + spatial)
  depends_on:
  - SLC-01
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-02/readiness.md
- id: SLC-03
  content: Task lifecycle + Outbox + History
  depends_on:
  - SLC-01
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-03/readiness.md
- id: SLC-04
  content: Conflict Management + Entity Resolution (Merge/Split)
  depends_on:
  - SLC-02
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-04/readiness.md
- id: SLC-05
  content: Secured Search & Graph Projections
  depends_on:
  - SLC-02
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) — ADR-P05 condition satisfied by TD-02 (W8)
  readiness: 14-slices/SLC-05/readiness.md
- id: SLC-06
  content: Situation + Alerts
  depends_on:
  - SLC-02
  - SLC-05
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-06/readiness.md
- id: SLC-07
  content: Analysis Case → Run → Finding → Assessment
  depends_on:
  - SLC-02
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-07/readiness.md
- id: SLC-08
  content: Decision → Plan → Version → Baseline → Tasks
  depends_on:
  - SLC-03
  - SLC-07
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-08/readiness.md
- id: SLC-09
  content: Assets, Resources, Allocation, Reservations, Readiness (full)
  depends_on:
  - SLC-03
  - SLC-01
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
  readiness: 14-slices/SLC-09/readiness.md
- id: SLC-10
  content: 'Grounded AI: retrieval, context packages, drafting, extraction, translation, model lifecycle, tool registry, vector
    projection'
  depends_on:
  - SLC-05
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review and first passing model evaluation
  readiness: 14-slices/SLC-10/readiness.md
- id: SLC-11
  content: Offline Field Capture + Sync
  depends_on:
  - SLC-02
  - SLC-04
  release: R1 (observation capture + task status only)
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated) 2026-09-24
  readiness: 14-slices/SLC-11/readiness.md
- id: SLC-12
  content: Products, Knowledge & Lessons, Archive packages, Historical Retrieval & Reconstruction
  depends_on:
  - SLC-07
  - SLC-08
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
  readiness: 14-slices/SLC-12/readiness.md
- id: SLC-13
  content: Risk & Emergency, Training, Exercises, Logistics, Communications
  depends_on: []
  release: R3
  status: SUPERSEDED
  g6_slc: SUPERSEDED — decomposed into SLC-17 (Risk & Contingency), SLC-18 (Logistics & Supply), SLC-19 (Training, Competency & Exercises); Communications not yet decomposed (UNK-022) — CR-67
- id: SLC-12a
  content: Retention schedules & legal hold (R1 portion of SLC-12)
  depends_on:
  - SLC-01
  - SLC-03
  release: R1
  status: APPROVED_DELEGATED
  g6_slc: READY (delegated; legal values pending UNK-002) 2026-09-24
  readiness: 14-slices/SLC-12a/readiness.md
- id: SLC-14
  content: Collection requirements & planning (CAP-02.01)
  depends_on:
  - SLC-02
  - SLC-03
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
  readiness: 14-slices/SLC-14/readiness.md
- id: SLC-15
  content: Coordination cases & correlation/fusion (CAP-06.03, CAP-04.04)
  depends_on:
  - SLC-04
  - SLC-08
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review (RSK-027)
  readiness: 14-slices/SLC-15/readiness.md
- id: SLC-16
  content: Enterprise integrations (ERP, HRIS, DMS, sensors, CAP alerts)
  depends_on:
  - SLC-02
  - SLC-01
  release: R2
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 pilot review and UNK-021
  readiness: 14-slices/SLC-16/readiness.md
- id: SLC-17
  content: Risk & Contingency (risk register, incident lifecycle, contingency plan activation via SLC-08 reuse)
  depends_on:
  - SLC-08
  - SLC-03
  release: R3
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 and R2 pilot review (RSK-028)
  readiness: 14-slices/SLC-17/readiness.md
- id: SLC-18
  content: Logistics & Supply (CAP-08.03, DOM-16, BC05) — Logistics Request and Shipment reuse SLC-09's Resource Pool/Allocation
    directly for inventory (R3-Q3); no separate stock model
  depends_on:
  - SLC-09
  release: R3
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 and R2 pilot review (RSK-028; this slice's actual technical dependency,
    SLC-09, is genuinely R2 and unmeasured)
  readiness: 14-slices/SLC-18/readiness.md
- id: SLC-19
  content: Training, Competency & Exercises (CAP-08.05, DOM-18+19) — extends SLC-03's Qualification Record and SLC-09's
    Role Requirement (both unmodified), stores After Action Review as an SLC-12 Knowledge Object (CR-63); adds 3 new
    aggregates (Scenario, Exercise, Simulation)
  depends_on:
  - SLC-03
  - SLC-09
  - SLC-12
  release: R3
  status: APPROVED_DELEGATED
  g6_slc: DESIGN_COMPLETE — G6 held until R1 and R2 pilot review (RSK-028; narrowest actual exposure among the three
    R3 slices)
  readiness: 14-slices/SLC-19/readiness.md
r2_order: SLC-09 → SLC-12 → SLC-10 → SLC-14 → SLC-15 → SLC-16 (SLC-10 after SLC-12 so products/knowledge exist as AI drafting
  targets; integrations last because they depend on tenant systems)
r3_order: SLC-17 → SLC-18 → SLC-19 (risk & contingency first — most structurally independent; logistics second — direct
  extension of an already-designed context; training/exercises last — depends on the most prior slices). All three R3
  slices are now DESIGN COMPLETE. No G6 for any R3 slice before the R1 and R2 pilot reviews (RSK-028).
```

</details>
