---
id: EVT-CAT-BC05-SLC18
type: event-catalog
title: Domain Events — BC05 (SLC-18)
wave: W4
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
---


# Domain Events — BC05 (SLC-18)

_15 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-LGR-REQUESTED | AGG-LOGISTICS-REQUEST | CMD-LGR-REQUEST | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-APPROVED | AGG-LOGISTICS-REQUEST | SYS:linked allocation committed, SYS:linked allocation committed | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-PENDING-APPROVAL | AGG-LOGISTICS-REQUEST | SYS:linked allocation requires approval | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-REJECTED | AGG-LOGISTICS-REQUEST | SYS:linked allocation rejected, SYS:linked allocation rejected | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-DISPATCHED | AGG-LOGISTICS-REQUEST | CMD-LGR-DISPATCH | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-FULFILLED | AGG-LOGISTICS-REQUEST | SYS:linked shipment delivered in full | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-PARTIALLY-FULFILLED | AGG-LOGISTICS-REQUEST | SYS:linked shipment resolved short | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-LGR-CANCELLED | AGG-LOGISTICS-REQUEST | CMD-LGR-CANCEL | — | Capacity ledger (via linked allocation, SLC-09); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-PLANNED | AGG-SHIPMENT | CMD-SHP-PLAN | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-DEPARTED | AGG-SHIPMENT | CMD-SHP-DEPART | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-CHECKPOINT-RECORDED | AGG-SHIPMENT | CMD-SHP-RECORD-CHECKPOINT | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-DELIVERED | AGG-SHIPMENT | CMD-SHP-DELIVER | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-DAMAGED | AGG-SHIPMENT | CMD-SHP-REPORT-DAMAGE | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-LOST | AGG-SHIPMENT | CMD-SHP-REPORT-LOST | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |
| EVT-SHP-CANCELLED | AGG-SHIPMENT | CMD-SHP-CANCEL | — | Logistics Request (fulfillment status); Search projection (SLC-05) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
