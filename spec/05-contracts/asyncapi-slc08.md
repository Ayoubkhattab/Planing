---
id: ASYNCAPI-SLC08
type: event-contract
title: AsyncAPI — SLC-08 Domain Events
wave: W6
slice: SLC-08
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-08 Domain Events

_33 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-08 Domain Events
  version: 1.0.0
channels:
  operations.events:
    address: '{cell}.operations.events'
    messages:
      EVT-DRQ-CREATED:
        $ref: '#/components/messages/EVT-DRQ-CREATED'
      EVT-DRQ-OPTION-ADDED:
        $ref: '#/components/messages/EVT-DRQ-OPTION-ADDED'
      EVT-DRQ-CITED:
        $ref: '#/components/messages/EVT-DRQ-CITED'
      EVT-DRQ-OPENED:
        $ref: '#/components/messages/EVT-DRQ-OPENED'
      EVT-DRQ-ESCALATED:
        $ref: '#/components/messages/EVT-DRQ-ESCALATED'
      EVT-DRQ-DECIDED:
        $ref: '#/components/messages/EVT-DRQ-DECIDED'
      EVT-DRQ-WITHDRAWN:
        $ref: '#/components/messages/EVT-DRQ-WITHDRAWN'
      EVT-DEC-RECORDED:
        $ref: '#/components/messages/EVT-DEC-RECORDED'
      EVT-DEC-SUPERSEDED:
        $ref: '#/components/messages/EVT-DEC-SUPERSEDED'
      EVT-DEC-ANNULLED:
        $ref: '#/components/messages/EVT-DEC-ANNULLED'
      EVT-PLN-CREATED:
        $ref: '#/components/messages/EVT-PLN-CREATED'
      EVT-PLN-ACTIVATED:
        $ref: '#/components/messages/EVT-PLN-ACTIVATED'
      EVT-PLN-SUSPENDED:
        $ref: '#/components/messages/EVT-PLN-SUSPENDED'
      EVT-PLN-RESUMED:
        $ref: '#/components/messages/EVT-PLN-RESUMED'
      EVT-PLN-COMPLETED:
        $ref: '#/components/messages/EVT-PLN-COMPLETED'
      EVT-PLN-CLOSED:
        $ref: '#/components/messages/EVT-PLN-CLOSED'
      EVT-PLN-CANCELLED:
        $ref: '#/components/messages/EVT-PLN-CANCELLED'
      EVT-PLN-RECLASSIFIED:
        $ref: '#/components/messages/EVT-PLN-RECLASSIFIED'
      EVT-PLN-REVIEW-FLAGGED:
        $ref: '#/components/messages/EVT-PLN-REVIEW-FLAGGED'
      EVT-PLV-DRAFTED:
        $ref: '#/components/messages/EVT-PLV-DRAFTED'
      EVT-PLV-EDITED:
        $ref: '#/components/messages/EVT-PLV-EDITED'
      EVT-PLV-SUBMITTED:
        $ref: '#/components/messages/EVT-PLV-SUBMITTED'
      EVT-PLV-RETURNED:
        $ref: '#/components/messages/EVT-PLV-RETURNED'
      EVT-PLV-BASELINED:
        $ref: '#/components/messages/EVT-PLV-BASELINED'
      EVT-PLV-REJECTED:
        $ref: '#/components/messages/EVT-PLV-REJECTED'
      EVT-PLV-MINOR-AMENDED:
        $ref: '#/components/messages/EVT-PLV-MINOR-AMENDED'
      EVT-PLV-SUPERSEDED:
        $ref: '#/components/messages/EVT-PLV-SUPERSEDED'
      EVT-PLV-DISCARDED:
        $ref: '#/components/messages/EVT-PLV-DISCARDED'
      EVT-OUT-TRACKER-CREATED:
        $ref: '#/components/messages/EVT-OUT-TRACKER-CREATED'
      EVT-OUT-TARGET-CHANGED:
        $ref: '#/components/messages/EVT-OUT-TARGET-CHANGED'
      EVT-OUT-MEASURED:
        $ref: '#/components/messages/EVT-OUT-MEASURED'
      EVT-OUT-MEASUREMENT-CORRECTED:
        $ref: '#/components/messages/EVT-OUT-MEASUREMENT-CORRECTED'
      EVT-OUT-TRACKER-CLOSED:
        $ref: '#/components/messages/EVT-OUT-TRACKER-CLOSED'
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
    EVT-DRQ-CREATED:
      name: EVT-DRQ-CREATED
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
    EVT-DRQ-OPTION-ADDED:
      name: EVT-DRQ-OPTION-ADDED
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
    EVT-DRQ-CITED:
      name: EVT-DRQ-CITED
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
    EVT-DRQ-OPENED:
      name: EVT-DRQ-OPENED
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
    EVT-DRQ-ESCALATED:
      name: EVT-DRQ-ESCALATED
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
    EVT-DRQ-DECIDED:
      name: EVT-DRQ-DECIDED
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
    EVT-DRQ-WITHDRAWN:
      name: EVT-DRQ-WITHDRAWN
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
    EVT-DEC-RECORDED:
      name: EVT-DEC-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision request (DECIDED)
      - Plans implementing it (review flag on supersede/annul)
      - Search projection (SLC-05)
      - Audit reports
      x-partition-key: tenant_id + aggregate.id
    EVT-DEC-SUPERSEDED:
      name: EVT-DEC-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision request (DECIDED)
      - Plans implementing it (review flag on supersede/annul)
      - Search projection (SLC-05)
      - Audit reports
      x-partition-key: tenant_id + aggregate.id
    EVT-DEC-ANNULLED:
      name: EVT-DEC-ANNULLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Decision request (DECIDED)
      - Plans implementing it (review flag on supersede/annul)
      - Search projection (SLC-05)
      - Audit reports
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-CREATED:
      name: EVT-PLN-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-ACTIVATED:
      name: EVT-PLN-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-SUSPENDED:
      name: EVT-PLN-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-RESUMED:
      name: EVT-PLN-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-COMPLETED:
      name: EVT-PLN-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-CLOSED:
      name: EVT-PLN-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-CANCELLED:
      name: EVT-PLN-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-RECLASSIFIED:
      name: EVT-PLN-RECLASSIFIED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Security-version service (EVT-SEC-VERSION-INCREMENTED)
      - PEP decision caches
      - Projection security-version table
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLN-REVIEW-FLAGGED:
      name: EVT-PLN-REVIEW-FLAGGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (suspend/cancel cascades)
      - Outcome trackers (close)
      - Notification (owners, assignees)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-DRAFTED:
      name: EVT-PLV-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-EDITED:
      name: EVT-PLV-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-SUBMITTED:
      name: EVT-PLV-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-RETURNED:
      name: EVT-PLV-RETURNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-BASELINED:
      name: EVT-PLV-BASELINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-REJECTED:
      name: EVT-PLV-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-MINOR-AMENDED:
      name: EVT-PLV-MINOR-AMENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-SUPERSEDED:
      name: EVT-PLV-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-PLV-DISCARDED:
      name: EVT-PLV-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task synchronizer (SPEC-PLAN §3)
      - Outcome trackers
      - Plan identity (activation)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OUT-TRACKER-CREATED:
      name: EVT-OUT-TRACKER-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Plan progress view
      - Business telemetry (OUT-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OUT-TARGET-CHANGED:
      name: EVT-OUT-TARGET-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Plan progress view
      - Business telemetry (OUT-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OUT-MEASURED:
      name: EVT-OUT-MEASURED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Plan progress view
      - Business telemetry (OUT-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OUT-MEASUREMENT-CORRECTED:
      name: EVT-OUT-MEASUREMENT-CORRECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Plan progress view
      - Business telemetry (OUT-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OUT-TRACKER-CLOSED:
      name: EVT-OUT-TRACKER-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Plan progress view
      - Business telemetry (OUT-05)
      x-partition-key: tenant_id + aggregate.id
```
