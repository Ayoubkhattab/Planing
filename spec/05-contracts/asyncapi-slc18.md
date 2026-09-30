---
id: ASYNCAPI-SLC18
type: event-contract
title: AsyncAPI — SLC-18 Domain Events
wave: W6
slice: SLC-18
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-27'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-18 Domain Events

_15 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-18 Domain Events
  version: 1.0.0
channels:
  readiness.events:
    address: '{cell}.readiness.events'
    messages:
      EVT-LGR-REQUESTED:
        $ref: '#/components/messages/EVT-LGR-REQUESTED'
      EVT-LGR-APPROVED:
        $ref: '#/components/messages/EVT-LGR-APPROVED'
      EVT-LGR-PENDING-APPROVAL:
        $ref: '#/components/messages/EVT-LGR-PENDING-APPROVAL'
      EVT-LGR-REJECTED:
        $ref: '#/components/messages/EVT-LGR-REJECTED'
      EVT-LGR-DISPATCHED:
        $ref: '#/components/messages/EVT-LGR-DISPATCHED'
      EVT-LGR-FULFILLED:
        $ref: '#/components/messages/EVT-LGR-FULFILLED'
      EVT-LGR-PARTIALLY-FULFILLED:
        $ref: '#/components/messages/EVT-LGR-PARTIALLY-FULFILLED'
      EVT-LGR-CANCELLED:
        $ref: '#/components/messages/EVT-LGR-CANCELLED'
      EVT-SHP-PLANNED:
        $ref: '#/components/messages/EVT-SHP-PLANNED'
      EVT-SHP-DEPARTED:
        $ref: '#/components/messages/EVT-SHP-DEPARTED'
      EVT-SHP-CHECKPOINT-RECORDED:
        $ref: '#/components/messages/EVT-SHP-CHECKPOINT-RECORDED'
      EVT-SHP-DELIVERED:
        $ref: '#/components/messages/EVT-SHP-DELIVERED'
      EVT-SHP-DAMAGED:
        $ref: '#/components/messages/EVT-SHP-DAMAGED'
      EVT-SHP-LOST:
        $ref: '#/components/messages/EVT-SHP-LOST'
      EVT-SHP-CANCELLED:
        $ref: '#/components/messages/EVT-SHP-CANCELLED'
    parameters:
      cell: {}
operations:
  publish_readiness:
    action: send
    channel:
      $ref: '#/channels/readiness.events'
components:
  schemas:
    EventEnvelope:
      type: object
      required:
      - event_id
      - event_type
      - event_version
      - producer
      - aggregate
      - occurred_at
      - recorded_at
      - tenant_id
      - correlation_id
      - payload
      properties:
        event_id:
          type: string
        event_type:
          type: string
        event_version:
          type: integer
        producer:
          type: string
        aggregate:
          type: object
          properties:
            type:
              type: string
            id:
              type: string
            version:
              type: integer
        occurred_at:
          type: string
          format: date-time
        recorded_at:
          type: string
          format: date-time
        tenant_id:
          type: string
        correlation_id:
          type: string
        causation_id:
          type:
          - string
          - 'null'
        security:
          type: object
          description: labels of the aggregate (ADR-P06)
        payload:
          type: object
  messages:
    EVT-LGR-REQUESTED:
      name: EVT-LGR-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: &id001
              type: object
              required:
              - aggregate_urn
              - from_state
              - to_state
              properties:
                aggregate_urn:
                  type: string
                from_state:
                  type:
                  - string
                  - 'null'
                to_state:
                  type: string
                actor:
                  type: string
                reason:
                  type:
                  - string
                  - 'null'
                changes:
                  type: object
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-APPROVED:
      name: EVT-LGR-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-PENDING-APPROVAL:
      name: EVT-LGR-PENDING-APPROVAL
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-REJECTED:
      name: EVT-LGR-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-DISPATCHED:
      name: EVT-LGR-DISPATCHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-FULFILLED:
      name: EVT-LGR-FULFILLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-PARTIALLY-FULFILLED:
      name: EVT-LGR-PARTIALLY-FULFILLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-LGR-CANCELLED:
      name: EVT-LGR-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger (via linked allocation, SLC-09)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-PLANNED:
      name: EVT-SHP-PLANNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-DEPARTED:
      name: EVT-SHP-DEPARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-CHECKPOINT-RECORDED:
      name: EVT-SHP-CHECKPOINT-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-DELIVERED:
      name: EVT-SHP-DELIVERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-DAMAGED:
      name: EVT-SHP-DAMAGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-LOST:
      name: EVT-SHP-LOST
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SHP-CANCELLED:
      name: EVT-SHP-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Logistics Request (fulfillment status)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
```
