---
id: ASYNCAPI-SLC03
type: event-contract
title: AsyncAPI — SLC-03 Domain Events
wave: W6
slice: SLC-03
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-03 Domain Events

_36 messages on 2 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-03 Domain Events
  version: 1.0.0
channels:
  operations.events:
    address: '{cell}.operations.events'
    messages:
      EVT-TASK-CREATED:
        $ref: '#/components/messages/EVT-TASK-CREATED'
      EVT-TASK-EDITED:
        $ref: '#/components/messages/EVT-TASK-EDITED'
      EVT-TASK-READIED:
        $ref: '#/components/messages/EVT-TASK-READIED'
      EVT-TASK-ASSIGNED:
        $ref: '#/components/messages/EVT-TASK-ASSIGNED'
      EVT-TASK-REASSIGNED:
        $ref: '#/components/messages/EVT-TASK-REASSIGNED'
      EVT-TASK-ACCEPTED:
        $ref: '#/components/messages/EVT-TASK-ACCEPTED'
      EVT-TASK-DECLINED:
        $ref: '#/components/messages/EVT-TASK-DECLINED'
      EVT-TASK-STARTED:
        $ref: '#/components/messages/EVT-TASK-STARTED'
      EVT-TASK-BLOCKED:
        $ref: '#/components/messages/EVT-TASK-BLOCKED'
      EVT-TASK-RESUMED:
        $ref: '#/components/messages/EVT-TASK-RESUMED'
      EVT-TASK-RESULT-ITEM-ADDED:
        $ref: '#/components/messages/EVT-TASK-RESULT-ITEM-ADDED'
      EVT-TASK-SUBMITTED:
        $ref: '#/components/messages/EVT-TASK-SUBMITTED'
      EVT-TASK-REVIEW-STARTED:
        $ref: '#/components/messages/EVT-TASK-REVIEW-STARTED'
      EVT-TASK-RETURNED-FOR-REWORK:
        $ref: '#/components/messages/EVT-TASK-RETURNED-FOR-REWORK'
      EVT-TASK-APPROVED:
        $ref: '#/components/messages/EVT-TASK-APPROVED'
      EVT-TASK-REJECTED:
        $ref: '#/components/messages/EVT-TASK-REJECTED'
      EVT-TASK-COMPLETED:
        $ref: '#/components/messages/EVT-TASK-COMPLETED'
      EVT-TASK-CLOSED:
        $ref: '#/components/messages/EVT-TASK-CLOSED'
      EVT-TASK-CANCELLED:
        $ref: '#/components/messages/EVT-TASK-CANCELLED'
      EVT-TASK-EXPIRED:
        $ref: '#/components/messages/EVT-TASK-EXPIRED'
      EVT-TASK-SUPERSEDED:
        $ref: '#/components/messages/EVT-TASK-SUPERSEDED'
      EVT-TASK-ESCALATED:
        $ref: '#/components/messages/EVT-TASK-ESCALATED'
      EVT-TASK-DUE-CHANGED:
        $ref: '#/components/messages/EVT-TASK-DUE-CHANGED'
      EVT-TASK-SUSPENDED:
        $ref: '#/components/messages/EVT-TASK-SUSPENDED'
      EVT-TASK-UNSUSPENDED:
        $ref: '#/components/messages/EVT-TASK-UNSUSPENDED'
      EVT-TASK-RECLASSIFIED:
        $ref: '#/components/messages/EVT-TASK-RECLASSIFIED'
      EVT-TTY-DEFINED:
        $ref: '#/components/messages/EVT-TTY-DEFINED'
      EVT-TTY-EDITED:
        $ref: '#/components/messages/EVT-TTY-EDITED'
      EVT-TTY-ACTIVATED:
        $ref: '#/components/messages/EVT-TTY-ACTIVATED'
      EVT-TTY-RETIRED:
        $ref: '#/components/messages/EVT-TTY-RETIRED'
    parameters:
      cell: {}
  readiness.events:
    address: '{cell}.readiness.events'
    messages:
      EVT-QUAL-RECORDED:
        $ref: '#/components/messages/EVT-QUAL-RECORDED'
      EVT-QUAL-RENEWED:
        $ref: '#/components/messages/EVT-QUAL-RENEWED'
      EVT-QUAL-SUSPENDED:
        $ref: '#/components/messages/EVT-QUAL-SUSPENDED'
      EVT-QUAL-REINSTATED:
        $ref: '#/components/messages/EVT-QUAL-REINSTATED'
      EVT-QUAL-REVOKED:
        $ref: '#/components/messages/EVT-QUAL-REVOKED'
      EVT-QUAL-EXPIRED:
        $ref: '#/components/messages/EVT-QUAL-EXPIRED'
    parameters:
      cell: {}
operations:
  publish_operations:
    action: send
    channel:
      $ref: '#/channels/operations.events'
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
    EVT-TASK-CREATED:
      name: EVT-TASK-CREATED
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
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-EDITED:
      name: EVT-TASK-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-READIED:
      name: EVT-TASK-READIED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-ASSIGNED:
      name: EVT-TASK-ASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-REASSIGNED:
      name: EVT-TASK-REASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-ACCEPTED:
      name: EVT-TASK-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-DECLINED:
      name: EVT-TASK-DECLINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-STARTED:
      name: EVT-TASK-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-BLOCKED:
      name: EVT-TASK-BLOCKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-RESUMED:
      name: EVT-TASK-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-RESULT-ITEM-ADDED:
      name: EVT-TASK-RESULT-ITEM-ADDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-SUBMITTED:
      name: EVT-TASK-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-REVIEW-STARTED:
      name: EVT-TASK-REVIEW-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-RETURNED-FOR-REWORK:
      name: EVT-TASK-RETURNED-FOR-REWORK
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-APPROVED:
      name: EVT-TASK-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-REJECTED:
      name: EVT-TASK-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-COMPLETED:
      name: EVT-TASK-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-CLOSED:
      name: EVT-TASK-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-CANCELLED:
      name: EVT-TASK-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-EXPIRED:
      name: EVT-TASK-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-SUPERSEDED:
      name: EVT-TASK-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-ESCALATED:
      name: EVT-TASK-ESCALATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-DUE-CHANGED:
      name: EVT-TASK-DUE-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-SUSPENDED:
      name: EVT-TASK-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-UNSUSPENDED:
      name: EVT-TASK-UNSUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TASK-RECLASSIFIED:
      name: EVT-TASK-RECLASSIFIED
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
      - Notification service (SLC-06)
      - Plan progress (SLC-08)
      - Outcome measurement (SLC-08)
      - Search projection (SLC-05)
      - Resources release (SLC-09, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-TTY-DEFINED:
      name: EVT-TTY-DEFINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task command handler cache
      x-partition-key: tenant_id + aggregate.id
    EVT-TTY-EDITED:
      name: EVT-TTY-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task command handler cache
      x-partition-key: tenant_id + aggregate.id
    EVT-TTY-ACTIVATED:
      name: EVT-TTY-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task command handler cache
      x-partition-key: tenant_id + aggregate.id
    EVT-TTY-RETIRED:
      name: EVT-TTY-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Task command handler cache
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-RECORDED:
      name: EVT-QUAL-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-RENEWED:
      name: EVT-QUAL-RENEWED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-SUSPENDED:
      name: EVT-QUAL-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-REINSTATED:
      name: EVT-QUAL-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-REVOKED:
      name: EVT-QUAL-REVOKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
    EVT-QUAL-EXPIRED:
      name: EVT-QUAL-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Eligibility cache invalidation
      - Task assignment re-check report
      x-partition-key: tenant_id + aggregate.id
```
