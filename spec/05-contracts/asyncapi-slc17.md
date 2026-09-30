---
id: ASYNCAPI-SLC17
type: event-contract
title: AsyncAPI — SLC-17 Domain Events
wave: W6
slice: SLC-17
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-17 Domain Events

_17 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-17 Domain Events
  version: 1.0.0
channels:
  operations.events:
    address: '{cell}.operations.events'
    messages:
      EVT-RIS-IDENTIFIED:
        $ref: '#/components/messages/EVT-RIS-IDENTIFIED'
      EVT-RIS-ASSESSED:
        $ref: '#/components/messages/EVT-RIS-ASSESSED'
      EVT-RIS-TREATMENT-PLANNED:
        $ref: '#/components/messages/EVT-RIS-TREATMENT-PLANNED'
      EVT-RIS-REASSESSED:
        $ref: '#/components/messages/EVT-RIS-REASSESSED'
      EVT-RIS-CLOSED:
        $ref: '#/components/messages/EVT-RIS-CLOSED'
      EVT-RIS-MATERIALIZATION-LINKED:
        $ref: '#/components/messages/EVT-RIS-MATERIALIZATION-LINKED'
      EVT-INC-REPORTED:
        $ref: '#/components/messages/EVT-INC-REPORTED'
      EVT-INC-ASSESSED:
        $ref: '#/components/messages/EVT-INC-ASSESSED'
      EVT-INC-RESPONSE-DISPATCHED:
        $ref: '#/components/messages/EVT-INC-RESPONSE-DISPATCHED'
      EVT-INC-CONTAINED:
        $ref: '#/components/messages/EVT-INC-CONTAINED'
      EVT-INC-RESOLVED:
        $ref: '#/components/messages/EVT-INC-RESOLVED'
      EVT-INC-CLOSED:
        $ref: '#/components/messages/EVT-INC-CLOSED'
      EVT-INC-CANCELLED:
        $ref: '#/components/messages/EVT-INC-CANCELLED'
      EVT-INC-ESCALATED:
        $ref: '#/components/messages/EVT-INC-ESCALATED'
      EVT-INC-DE-ESCALATED:
        $ref: '#/components/messages/EVT-INC-DE-ESCALATED'
      EVT-INC-CONTINGENCY-ACTIVATED:
        $ref: '#/components/messages/EVT-INC-CONTINGENCY-ACTIVATED'
      EVT-INC-SLA-BREACHED:
        $ref: '#/components/messages/EVT-INC-SLA-BREACHED'
    parameters:
      cell: {}
operations:
  publish_operations:
    action: send
    channel:
      $ref: '#/channels/operations.events'
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
    EVT-RIS-IDENTIFIED:
      name: EVT-RIS-IDENTIFIED
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
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-RIS-ASSESSED:
      name: EVT-RIS-ASSESSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-RIS-TREATMENT-PLANNED:
      name: EVT-RIS-TREATMENT-PLANNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-RIS-REASSESSED:
      name: EVT-RIS-REASSESSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-RIS-CLOSED:
      name: EVT-RIS-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-RIS-MATERIALIZATION-LINKED:
      name: EVT-RIS-MATERIALIZATION-LINKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Coordination cases (SLC-15، عند ارتباط النطاق)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-REPORTED:
      name: EVT-INC-REPORTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-ASSESSED:
      name: EVT-INC-ASSESSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-RESPONSE-DISPATCHED:
      name: EVT-INC-RESPONSE-DISPATCHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-CONTAINED:
      name: EVT-INC-CONTAINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-RESOLVED:
      name: EVT-INC-RESOLVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-CLOSED:
      name: EVT-INC-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-CANCELLED:
      name: EVT-INC-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-ESCALATED:
      name: EVT-INC-ESCALATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-DE-ESCALATED:
      name: EVT-INC-DE-ESCALATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-CONTINGENCY-ACTIVATED:
      name: EVT-INC-CONTINGENCY-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
    EVT-INC-SLA-BREACHED:
      name: EVT-INC-SLA-BREACHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search projection (SLC-05)
      - Notification (SLC-06)
      - اقتراحات كائن المعرفة (SLC-12، بعد الإغلاق — R3-Q5)
      x-partition-key: tenant_id + aggregate.id
```
