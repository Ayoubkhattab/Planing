---
id: ASYNCAPI-SLC15
type: event-contract
title: AsyncAPI — SLC-15 Domain Events
wave: W6
slice: SLC-15
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-15 Domain Events

_19 messages on 2 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-15 Domain Events
  version: 1.0.0
channels:
  operations.events:
    address: '{cell}.operations.events'
    messages:
      EVT-CRD-OPENED:
        $ref: '#/components/messages/EVT-CRD-OPENED'
      EVT-CRD-PARTICIPANT-ADDED:
        $ref: '#/components/messages/EVT-CRD-PARTICIPANT-ADDED'
      EVT-CRD-PARTICIPANT-REMOVED:
        $ref: '#/components/messages/EVT-CRD-PARTICIPANT-REMOVED'
      EVT-CRD-ACTIVATED:
        $ref: '#/components/messages/EVT-CRD-ACTIVATED'
      EVT-CRD-RESPONSIBILITY-ASSIGNED:
        $ref: '#/components/messages/EVT-CRD-RESPONSIBILITY-ASSIGNED'
      EVT-CRD-RESPONSIBILITY-UPDATED:
        $ref: '#/components/messages/EVT-CRD-RESPONSIBILITY-UPDATED'
      EVT-CRD-DECISION-REQUESTED:
        $ref: '#/components/messages/EVT-CRD-DECISION-REQUESTED'
      EVT-CRD-DECISION-RECORDED:
        $ref: '#/components/messages/EVT-CRD-DECISION-RECORDED'
      EVT-CRD-CLOSED:
        $ref: '#/components/messages/EVT-CRD-CLOSED'
      EVT-CRD-CANCELLED:
        $ref: '#/components/messages/EVT-CRD-CANCELLED'
    parameters:
      cell: {}
  information.events:
    address: '{cell}.information.events'
    messages:
      EVT-CRP-PROPOSED:
        $ref: '#/components/messages/EVT-CRP-PROPOSED'
      EVT-CRP-REVIEW-STARTED:
        $ref: '#/components/messages/EVT-CRP-REVIEW-STARTED'
      EVT-CRP-ACCEPTED:
        $ref: '#/components/messages/EVT-CRP-ACCEPTED'
      EVT-CRP-REJECTED:
        $ref: '#/components/messages/EVT-CRP-REJECTED'
      EVT-CRP-EXPIRED:
        $ref: '#/components/messages/EVT-CRP-EXPIRED'
      EVT-CRR-DEFINED:
        $ref: '#/components/messages/EVT-CRR-DEFINED'
      EVT-CRR-EDITED:
        $ref: '#/components/messages/EVT-CRR-EDITED'
      EVT-CRR-ACTIVATED:
        $ref: '#/components/messages/EVT-CRR-ACTIVATED'
      EVT-CRR-RETIRED:
        $ref: '#/components/messages/EVT-CRR-RETIRED'
    parameters:
      cell: {}
operations:
  publish_operations:
    action: send
    channel:
      $ref: '#/channels/operations.events'
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
    EVT-CRD-OPENED:
      name: EVT-CRD-OPENED
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
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-PARTICIPANT-ADDED:
      name: EVT-CRD-PARTICIPANT-ADDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-PARTICIPANT-REMOVED:
      name: EVT-CRD-PARTICIPANT-REMOVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-ACTIVATED:
      name: EVT-CRD-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-RESPONSIBILITY-ASSIGNED:
      name: EVT-CRD-RESPONSIBILITY-ASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-RESPONSIBILITY-UPDATED:
      name: EVT-CRD-RESPONSIBILITY-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-DECISION-REQUESTED:
      name: EVT-CRD-DECISION-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-DECISION-RECORDED:
      name: EVT-CRD-DECISION-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-CLOSED:
      name: EVT-CRD-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRD-CANCELLED:
      name: EVT-CRD-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision requests (SLC-08)
      - Notification (participants)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CRP-PROPOSED:
      name: EVT-CRP-PROPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)
      - Rule evaluation feedback
      x-partition-key: tenant_id + aggregate.id
    EVT-CRP-REVIEW-STARTED:
      name: EVT-CRP-REVIEW-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)
      - Rule evaluation feedback
      x-partition-key: tenant_id + aggregate.id
    EVT-CRP-ACCEPTED:
      name: EVT-CRP-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)
      - Rule evaluation feedback
      x-partition-key: tenant_id + aggregate.id
    EVT-CRP-REJECTED:
      name: EVT-CRP-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)
      - Rule evaluation feedback
      x-partition-key: tenant_id + aggregate.id
    EVT-CRP-EXPIRED:
      name: EVT-CRP-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner commands on acceptance (BC02 events/relationships, SLC-04 ER)
      - Rule evaluation feedback
      x-partition-key: tenant_id + aggregate.id
    EVT-CRR-DEFINED:
      name: EVT-CRR-DEFINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Correlation engine
      x-partition-key: tenant_id + aggregate.id
    EVT-CRR-EDITED:
      name: EVT-CRR-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Correlation engine
      x-partition-key: tenant_id + aggregate.id
    EVT-CRR-ACTIVATED:
      name: EVT-CRR-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Correlation engine
      x-partition-key: tenant_id + aggregate.id
    EVT-CRR-RETIRED:
      name: EVT-CRR-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Correlation engine
      x-partition-key: tenant_id + aggregate.id
```
