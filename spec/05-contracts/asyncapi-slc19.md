---
id: ASYNCAPI-SLC19
type: event-contract
title: AsyncAPI — SLC-19 Domain Events
wave: W6
slice: SLC-19
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-29'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-19 Domain Events

_17 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-19 Domain Events
  version: 1.0.0
channels:
  readiness.events:
    address: '{cell}.readiness.events'
    messages:
      EVT-SCN-DEFINED:
        $ref: '#/components/messages/EVT-SCN-DEFINED'
      EVT-SCN-EDITED:
        $ref: '#/components/messages/EVT-SCN-EDITED'
      EVT-SCN-ACTIVATED:
        $ref: '#/components/messages/EVT-SCN-ACTIVATED'
      EVT-SCN-RETIRED:
        $ref: '#/components/messages/EVT-SCN-RETIRED'
      EVT-EXR-PLANNED:
        $ref: '#/components/messages/EVT-EXR-PLANNED'
      EVT-EXR-SCHEDULED:
        $ref: '#/components/messages/EVT-EXR-SCHEDULED'
      EVT-EXR-STARTED:
        $ref: '#/components/messages/EVT-EXR-STARTED'
      EVT-EXR-COMPLETED:
        $ref: '#/components/messages/EVT-EXR-COMPLETED'
      EVT-EXR-ABORTED:
        $ref: '#/components/messages/EVT-EXR-ABORTED'
      EVT-EXR-CANCELLED:
        $ref: '#/components/messages/EVT-EXR-CANCELLED'
      EVT-SIM-STARTED:
        $ref: '#/components/messages/EVT-SIM-STARTED'
      EVT-SIM-INJECT-DELIVERED:
        $ref: '#/components/messages/EVT-SIM-INJECT-DELIVERED'
      EVT-SIM-EVALUATION-RECORDED:
        $ref: '#/components/messages/EVT-SIM-EVALUATION-RECORDED'
      EVT-SIM-PAUSED:
        $ref: '#/components/messages/EVT-SIM-PAUSED'
      EVT-SIM-RESUMED:
        $ref: '#/components/messages/EVT-SIM-RESUMED'
      EVT-SIM-COMPLETED:
        $ref: '#/components/messages/EVT-SIM-COMPLETED'
      EVT-SIM-ABORTED:
        $ref: '#/components/messages/EVT-SIM-ABORTED'
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
    EVT-SCN-DEFINED:
      name: EVT-SCN-DEFINED
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
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCN-EDITED:
      name: EVT-SCN-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCN-ACTIVATED:
      name: EVT-SCN-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Exercise (frozen scenario reference on plan)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCN-RETIRED:
      name: EVT-SCN-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-PLANNED:
      name: EVT-EXR-PLANNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-SCHEDULED:
      name: EVT-EXR-SCHEDULED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-STARTED:
      name: EVT-EXR-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Simulation (creation trigger)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-COMPLETED:
      name: EVT-EXR-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-ABORTED:
      name: EVT-EXR-ABORTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXR-CANCELLED:
      name: EVT-EXR-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-STARTED:
      name: EVT-SIM-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Exercise (IN_PROGRESS trigger)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-INJECT-DELIVERED:
      name: EVT-SIM-INJECT-DELIVERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-EVALUATION-RECORDED:
      name: EVT-SIM-EVALUATION-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Qualification Record (optional evidence source, SLC-03 — unmodified)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-PAUSED:
      name: EVT-SIM-PAUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-RESUMED:
      name: EVT-SIM-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-COMPLETED:
      name: EVT-SIM-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Exercise (COMPLETED trigger)
      - Knowledge Object (optional AAR terminal source, SLC-12 — CR-63)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIM-ABORTED:
      name: EVT-SIM-ABORTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Exercise (ABORTED trigger)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
```
