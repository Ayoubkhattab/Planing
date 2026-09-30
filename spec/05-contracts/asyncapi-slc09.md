---
id: ASYNCAPI-SLC09
type: event-contract
title: AsyncAPI — SLC-09 Domain Events
wave: W6
slice: SLC-09
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-09 Domain Events

_40 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-09 Domain Events
  version: 1.0.0
channels:
  readiness.events:
    address: '{cell}.readiness.events'
    messages:
      EVT-AST-REGISTERED:
        $ref: '#/components/messages/EVT-AST-REGISTERED'
      EVT-AST-CONDITION-UPDATED:
        $ref: '#/components/messages/EVT-AST-CONDITION-UPDATED'
      EVT-AST-UNSERVICEABLE:
        $ref: '#/components/messages/EVT-AST-UNSERVICEABLE'
      EVT-AST-MAINTENANCE-STARTED:
        $ref: '#/components/messages/EVT-AST-MAINTENANCE-STARTED'
      EVT-AST-RETURNED-TO-SERVICE:
        $ref: '#/components/messages/EVT-AST-RETURNED-TO-SERVICE'
      EVT-AST-CUSTODY-TRANSFERRED:
        $ref: '#/components/messages/EVT-AST-CUSTODY-TRANSFERRED'
      EVT-AST-CERTIFICATION-SET:
        $ref: '#/components/messages/EVT-AST-CERTIFICATION-SET'
      EVT-AST-REPORTED-LOST:
        $ref: '#/components/messages/EVT-AST-REPORTED-LOST'
      EVT-AST-RECOVERED:
        $ref: '#/components/messages/EVT-AST-RECOVERED'
      EVT-AST-DISPOSED:
        $ref: '#/components/messages/EVT-AST-DISPOSED'
      EVT-AST-RECLASSIFIED:
        $ref: '#/components/messages/EVT-AST-RECLASSIFIED'
      EVT-MNT-PLANNED:
        $ref: '#/components/messages/EVT-MNT-PLANNED'
      EVT-MNT-RESCHEDULED:
        $ref: '#/components/messages/EVT-MNT-RESCHEDULED'
      EVT-MNT-STARTED:
        $ref: '#/components/messages/EVT-MNT-STARTED'
      EVT-MNT-COMPLETED:
        $ref: '#/components/messages/EVT-MNT-COMPLETED'
      EVT-MNT-CANCELLED:
        $ref: '#/components/messages/EVT-MNT-CANCELLED'
      EVT-RSV-HELD:
        $ref: '#/components/messages/EVT-RSV-HELD'
      EVT-RSV-CONFIRMED:
        $ref: '#/components/messages/EVT-RSV-CONFIRMED'
      EVT-RSV-EXPIRED:
        $ref: '#/components/messages/EVT-RSV-EXPIRED'
      EVT-RSV-RELEASED:
        $ref: '#/components/messages/EVT-RSV-RELEASED'
      EVT-RSV-CANCELLED:
        $ref: '#/components/messages/EVT-RSV-CANCELLED'
      EVT-ASG-ASSIGNED:
        $ref: '#/components/messages/EVT-ASG-ASSIGNED'
      EVT-ASG-RETURNED:
        $ref: '#/components/messages/EVT-ASG-RETURNED'
      EVT-ASG-CANCELLED:
        $ref: '#/components/messages/EVT-ASG-CANCELLED'
      EVT-RPL-CREATED:
        $ref: '#/components/messages/EVT-RPL-CREATED'
      EVT-RPL-CAPACITY-ADJUSTED:
        $ref: '#/components/messages/EVT-RPL-CAPACITY-ADJUSTED'
      EVT-RPL-SUSPENDED:
        $ref: '#/components/messages/EVT-RPL-SUSPENDED'
      EVT-RPL-RESUMED:
        $ref: '#/components/messages/EVT-RPL-RESUMED'
      EVT-RPL-CLOSED:
        $ref: '#/components/messages/EVT-RPL-CLOSED'
      EVT-ALC-REQUESTED:
        $ref: '#/components/messages/EVT-ALC-REQUESTED'
      EVT-ALC-COMMITTED:
        $ref: '#/components/messages/EVT-ALC-COMMITTED'
      EVT-ALC-APPROVAL-REQUIRED:
        $ref: '#/components/messages/EVT-ALC-APPROVAL-REQUIRED'
      EVT-ALC-REJECTED:
        $ref: '#/components/messages/EVT-ALC-REJECTED'
      EVT-ALC-CONSUMED:
        $ref: '#/components/messages/EVT-ALC-CONSUMED'
      EVT-ALC-PREEMPTED:
        $ref: '#/components/messages/EVT-ALC-PREEMPTED'
      EVT-ALC-RELEASED:
        $ref: '#/components/messages/EVT-ALC-RELEASED'
      EVT-RRQ-DEFINED:
        $ref: '#/components/messages/EVT-RRQ-DEFINED'
      EVT-RRQ-EDITED:
        $ref: '#/components/messages/EVT-RRQ-EDITED'
      EVT-RRQ-ACTIVATED:
        $ref: '#/components/messages/EVT-RRQ-ACTIVATED'
      EVT-RRQ-RETIRED:
        $ref: '#/components/messages/EVT-RRQ-RETIRED'
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
    EVT-AST-REGISTERED:
      name: EVT-AST-REGISTERED
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
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-CONDITION-UPDATED:
      name: EVT-AST-CONDITION-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-UNSERVICEABLE:
      name: EVT-AST-UNSERVICEABLE
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-MAINTENANCE-STARTED:
      name: EVT-AST-MAINTENANCE-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-RETURNED-TO-SERVICE:
      name: EVT-AST-RETURNED-TO-SERVICE
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-CUSTODY-TRANSFERRED:
      name: EVT-AST-CUSTODY-TRANSFERRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-CERTIFICATION-SET:
      name: EVT-AST-CERTIFICATION-SET
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-REPORTED-LOST:
      name: EVT-AST-REPORTED-LOST
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-RECOVERED:
      name: EVT-AST-RECOVERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-DISPOSED:
      name: EVT-AST-DISPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-AST-RECLASSIFIED:
      name: EVT-AST-RECLASSIFIED
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
      - Availability view
      - Situation assets layer (SLC-06)
      - Search projection (SLC-05)
      - Reservations/assignments (flags)
      x-partition-key: tenant_id + aggregate.id
    EVT-MNT-PLANNED:
      name: EVT-MNT-PLANNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Asset (start/return via policy)
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-MNT-RESCHEDULED:
      name: EVT-MNT-RESCHEDULED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Asset (start/return via policy)
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-MNT-STARTED:
      name: EVT-MNT-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Asset (start/return via policy)
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-MNT-COMPLETED:
      name: EVT-MNT-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Asset (start/return via policy)
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-MNT-CANCELLED:
      name: EVT-MNT-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Asset (start/return via policy)
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-RSV-HELD:
      name: EVT-RSV-HELD
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-RSV-CONFIRMED:
      name: EVT-RSV-CONFIRMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-RSV-EXPIRED:
      name: EVT-RSV-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-RSV-RELEASED:
      name: EVT-RSV-RELEASED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-RSV-CANCELLED:
      name: EVT-RSV-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      x-partition-key: tenant_id + aggregate.id
    EVT-ASG-ASSIGNED:
      name: EVT-ASG-ASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Task (SLC-03)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASG-RETURNED:
      name: EVT-ASG-RETURNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Task (SLC-03)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASG-CANCELLED:
      name: EVT-ASG-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Availability view
      - Task (SLC-03)
      x-partition-key: tenant_id + aggregate.id
    EVT-RPL-CREATED:
      name: EVT-RPL-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      x-partition-key: tenant_id + aggregate.id
    EVT-RPL-CAPACITY-ADJUSTED:
      name: EVT-RPL-CAPACITY-ADJUSTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      x-partition-key: tenant_id + aggregate.id
    EVT-RPL-SUSPENDED:
      name: EVT-RPL-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      x-partition-key: tenant_id + aggregate.id
    EVT-RPL-RESUMED:
      name: EVT-RPL-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      x-partition-key: tenant_id + aggregate.id
    EVT-RPL-CLOSED:
      name: EVT-RPL-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-REQUESTED:
      name: EVT-ALC-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-COMMITTED:
      name: EVT-ALC-COMMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-APPROVAL-REQUIRED:
      name: EVT-ALC-APPROVAL-REQUIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-REJECTED:
      name: EVT-ALC-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-CONSUMED:
      name: EVT-ALC-CONSUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-PREEMPTED:
      name: EVT-ALC-PREEMPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALC-RELEASED:
      name: EVT-ALC-RELEASED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Capacity ledger
      - Task (SLC-03) notifications
      - Plan progress (SLC-08)
      x-partition-key: tenant_id + aggregate.id
    EVT-RRQ-DEFINED:
      name: EVT-RRQ-DEFINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Readiness evaluator
      - Eligibility cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RRQ-EDITED:
      name: EVT-RRQ-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Readiness evaluator
      - Eligibility cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RRQ-ACTIVATED:
      name: EVT-RRQ-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Readiness evaluator
      - Eligibility cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RRQ-RETIRED:
      name: EVT-RRQ-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Readiness evaluator
      - Eligibility cache
      x-partition-key: tenant_id + aggregate.id
```
