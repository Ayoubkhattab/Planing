---
id: ASYNCAPI-SLC14
type: event-contract
title: AsyncAPI — SLC-14 Domain Events
wave: W6
slice: SLC-14
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-14 Domain Events

_16 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-14 Domain Events
  version: 1.0.0
channels:
  information.events:
    address: '{cell}.information.events'
    messages:
      EVT-CRQ-DRAFTED:
        $ref: '#/components/messages/EVT-CRQ-DRAFTED'
      EVT-CRQ-EDITED:
        $ref: '#/components/messages/EVT-CRQ-EDITED'
      EVT-CRQ-SUBMITTED:
        $ref: '#/components/messages/EVT-CRQ-SUBMITTED'
      EVT-CRQ-APPROVED:
        $ref: '#/components/messages/EVT-CRQ-APPROVED'
      EVT-CRQ-REJECTED:
        $ref: '#/components/messages/EVT-CRQ-REJECTED'
      EVT-CRQ-AMENDED:
        $ref: '#/components/messages/EVT-CRQ-AMENDED'
      EVT-CRQ-FULFILMENT-UPDATED:
        $ref: '#/components/messages/EVT-CRQ-FULFILMENT-UPDATED'
      EVT-CRQ-SATISFIED:
        $ref: '#/components/messages/EVT-CRQ-SATISFIED'
      EVT-CRQ-EXPIRED:
        $ref: '#/components/messages/EVT-CRQ-EXPIRED'
      EVT-CRQ-CANCELLED:
        $ref: '#/components/messages/EVT-CRQ-CANCELLED'
      EVT-CPL-CREATED:
        $ref: '#/components/messages/EVT-CPL-CREATED'
      EVT-CPL-ACTIVITY-ADDED:
        $ref: '#/components/messages/EVT-CPL-ACTIVITY-ADDED'
      EVT-CPL-ACTIVITY-REMOVED:
        $ref: '#/components/messages/EVT-CPL-ACTIVITY-REMOVED'
      EVT-CPL-ACTIVATED:
        $ref: '#/components/messages/EVT-CPL-ACTIVATED'
      EVT-CPL-COMPLETED:
        $ref: '#/components/messages/EVT-CPL-COMPLETED'
      EVT-CPL-CANCELLED:
        $ref: '#/components/messages/EVT-CPL-CANCELLED'
    parameters:
      cell: {}
operations:
  publish_information:
    action: send
    channel:
      $ref: '#/channels/information.events'
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
    EVT-CRQ-DRAFTED:
      name: EVT-CRQ-DRAFTED
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
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-EDITED:
      name: EVT-CRQ-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-SUBMITTED:
      name: EVT-CRQ-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-APPROVED:
      name: EVT-CRQ-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-REJECTED:
      name: EVT-CRQ-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-AMENDED:
      name: EVT-CRQ-AMENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-FULFILMENT-UPDATED:
      name: EVT-CRQ-FULFILMENT-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-SATISFIED:
      name: EVT-CRQ-SATISFIED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-EXPIRED:
      name: EVT-CRQ-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRQ-CANCELLED:
      name: EVT-CRQ-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Matching engine (reload EEIs)
      - Collection board
      - Search projection (SLC-05)
      - Notification (requester)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-CREATED:
      name: EVT-CPL-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-ACTIVITY-ADDED:
      name: EVT-CPL-ACTIVITY-ADDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-ACTIVITY-REMOVED:
      name: EVT-CPL-ACTIVITY-REMOVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-ACTIVATED:
      name: EVT-CPL-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-COMPLETED:
      name: EVT-CPL-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
    EVT-CPL-CANCELLED:
      name: EVT-CPL-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task creation (SLC-03)
      - Notification (units)
      x-partition-key: tenant_id + aggregate.id
```
