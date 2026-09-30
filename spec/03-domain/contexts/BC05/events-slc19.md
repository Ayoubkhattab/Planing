---
id: EVT-CAT-BC05-SLC19
type: event-catalog
title: Domain Events — BC05 (SLC-19)
wave: W4
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
---


# Domain Events — BC05 (SLC-19)

_17 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-SCN-DEFINED | AGG-SCENARIO | CMD-SCN-DEFINE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SCN-EDITED | AGG-SCENARIO | CMD-SCN-EDIT | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SCN-ACTIVATED | AGG-SCENARIO | CMD-SCN-ACTIVATE | — | Exercise (frozen scenario reference on plan); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SCN-RETIRED | AGG-SCENARIO | CMD-SCN-RETIRE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-PLANNED | AGG-EXERCISE | CMD-EXR-PLAN | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-SCHEDULED | AGG-EXERCISE | CMD-EXR-SCHEDULE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-STARTED | AGG-EXERCISE | CMD-EXR-START | — | Simulation (creation trigger); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-COMPLETED | AGG-EXERCISE | SYS:linked simulation completed | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-ABORTED | AGG-EXERCISE | SYS:linked simulation aborted | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-EXR-CANCELLED | AGG-EXERCISE | CMD-EXR-CANCEL | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-STARTED | AGG-SIMULATION | CMD-SIM-START | — | Exercise (IN_PROGRESS trigger); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-INJECT-DELIVERED | AGG-SIMULATION | CMD-SIM-DELIVER-INJECT | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-EVALUATION-RECORDED | AGG-SIMULATION | CMD-SIM-RECORD-EVALUATION | — | Qualification Record (optional evidence source, SLC-03 — unmodified, evidence:urn already generic); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-PAUSED | AGG-SIMULATION | CMD-SIM-PAUSE | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-RESUMED | AGG-SIMULATION | CMD-SIM-RESUME | — | Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-COMPLETED | AGG-SIMULATION | CMD-SIM-COMPLETE | — | Exercise (COMPLETED trigger); Knowledge Object (optional AAR terminal source, SLC-12 — CR-63); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SIM-ABORTED | AGG-SIMULATION | CMD-SIM-ABORT | — | Exercise (ABORTED trigger); Search projection (SLC-05) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
