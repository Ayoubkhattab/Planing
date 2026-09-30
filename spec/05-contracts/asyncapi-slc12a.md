---
id: ASYNCAPI-SLC12A
type: event-contract
title: AsyncAPI — SLC-12a Domain Events
wave: W6
slice: SLC-12a
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-12a Domain Events

_25 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-12a Domain Events
  version: 1.0.0
channels:
  governance.events:
    address: '{cell}.governance.events'
    messages:
      EVT-RTS-DRAFTED:
        $ref: '#/components/messages/EVT-RTS-DRAFTED'
      EVT-RTS-EDITED:
        $ref: '#/components/messages/EVT-RTS-EDITED'
      EVT-RTS-ACTIVATED:
        $ref: '#/components/messages/EVT-RTS-ACTIVATED'
      EVT-RTS-DISCARDED:
        $ref: '#/components/messages/EVT-RTS-DISCARDED'
      EVT-RTS-SUPERSEDED:
        $ref: '#/components/messages/EVT-RTS-SUPERSEDED'
      EVT-LHD-PLACED:
        $ref: '#/components/messages/EVT-LHD-PLACED'
      EVT-LHD-EXTENDED:
        $ref: '#/components/messages/EVT-LHD-EXTENDED'
      EVT-LHD-RELEASE-REQUESTED:
        $ref: '#/components/messages/EVT-LHD-RELEASE-REQUESTED'
      EVT-LHD-RELEASED:
        $ref: '#/components/messages/EVT-LHD-RELEASED'
      EVT-LHD-RELEASE-CANCELLED:
        $ref: '#/components/messages/EVT-LHD-RELEASE-CANCELLED'
      EVT-DSP-PLANNED:
        $ref: '#/components/messages/EVT-DSP-PLANNED'
      EVT-DSP-SUBMITTED:
        $ref: '#/components/messages/EVT-DSP-SUBMITTED'
      EVT-DSP-APPROVED:
        $ref: '#/components/messages/EVT-DSP-APPROVED'
      EVT-DSP-EXECUTING:
        $ref: '#/components/messages/EVT-DSP-EXECUTING'
      EVT-DSP-COMPLETED:
        $ref: '#/components/messages/EVT-DSP-COMPLETED'
      EVT-DSP-COMPLETED-WITH-EXCEPTIONS:
        $ref: '#/components/messages/EVT-DSP-COMPLETED-WITH-EXCEPTIONS'
      EVT-DSP-CANCELLED:
        $ref: '#/components/messages/EVT-DSP-CANCELLED'
      EVT-ERS-RECEIVED:
        $ref: '#/components/messages/EVT-ERS-RECEIVED'
      EVT-ERS-SCOPED:
        $ref: '#/components/messages/EVT-ERS-SCOPED'
      EVT-ERS-APPROVED:
        $ref: '#/components/messages/EVT-ERS-APPROVED'
      EVT-ERS-REJECTED:
        $ref: '#/components/messages/EVT-ERS-REJECTED'
      EVT-ERS-BLOCKED:
        $ref: '#/components/messages/EVT-ERS-BLOCKED'
      EVT-ERS-UNBLOCKED:
        $ref: '#/components/messages/EVT-ERS-UNBLOCKED'
      EVT-ERS-EXECUTING:
        $ref: '#/components/messages/EVT-ERS-EXECUTING'
      EVT-ERS-COMPLETED:
        $ref: '#/components/messages/EVT-ERS-COMPLETED'
    parameters:
      cell: {}
operations:
  publish_governance:
    action: send
    channel:
      $ref: '#/channels/governance.events'
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
    EVT-RTS-DRAFTED:
      name: EVT-RTS-DRAFTED
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
      - Disposition planner
      - Key-bucket policy (class period sizing)
      x-partition-key: tenant_id + aggregate.id
    EVT-RTS-EDITED:
      name: EVT-RTS-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Disposition planner
      - Key-bucket policy (class period sizing)
      x-partition-key: tenant_id + aggregate.id
    EVT-RTS-ACTIVATED:
      name: EVT-RTS-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Disposition planner
      - Key-bucket policy (class period sizing)
      x-partition-key: tenant_id + aggregate.id
    EVT-RTS-DISCARDED:
      name: EVT-RTS-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Disposition planner
      - Key-bucket policy (class period sizing)
      x-partition-key: tenant_id + aggregate.id
    EVT-RTS-SUPERSEDED:
      name: EVT-RTS-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Disposition planner
      - Key-bucket policy (class period sizing)
      x-partition-key: tenant_id + aggregate.id
    EVT-LHD-PLACED:
      name: EVT-LHD-PLACED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - HoldCheck cache (all owners)
      - Disposition planner
      - Erasure executor
      x-partition-key: tenant_id + aggregate.id
    EVT-LHD-EXTENDED:
      name: EVT-LHD-EXTENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - HoldCheck cache (all owners)
      - Disposition planner
      - Erasure executor
      x-partition-key: tenant_id + aggregate.id
    EVT-LHD-RELEASE-REQUESTED:
      name: EVT-LHD-RELEASE-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - HoldCheck cache (all owners)
      - Disposition planner
      - Erasure executor
      x-partition-key: tenant_id + aggregate.id
    EVT-LHD-RELEASED:
      name: EVT-LHD-RELEASED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - HoldCheck cache (all owners)
      - Disposition planner
      - Erasure executor
      x-partition-key: tenant_id + aggregate.id
    EVT-LHD-RELEASE-CANCELLED:
      name: EVT-LHD-RELEASE-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - HoldCheck cache (all owners)
      - Disposition planner
      - Erasure executor
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-PLANNED:
      name: EVT-DSP-PLANNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-SUBMITTED:
      name: EVT-DSP-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-APPROVED:
      name: EVT-DSP-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-EXECUTING:
      name: EVT-DSP-EXECUTING
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-COMPLETED:
      name: EVT-DSP-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-COMPLETED-WITH-EXCEPTIONS:
      name: EVT-DSP-COMPLETED-WITH-EXCEPTIONS
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DSP-CANCELLED:
      name: EVT-DSP-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (bucket key destruction)
      - Owner contexts (purge plaintext caches, projections)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-RECEIVED:
      name: EVT-ERS-RECEIVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-SCOPED:
      name: EVT-ERS-SCOPED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-APPROVED:
      name: EVT-ERS-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-REJECTED:
      name: EVT-ERS-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-BLOCKED:
      name: EVT-ERS-BLOCKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-UNBLOCKED:
      name: EVT-ERS-UNBLOCKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-EXECUTING:
      name: EVT-ERS-EXECUTING
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
    EVT-ERS-COMPLETED:
      name: EVT-ERS-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Key manager (subject key destruction)
      - BC01 / BC02 / BC05 (scope + confirmation)
      - Projections (purge)
      x-partition-key: tenant_id + aggregate.id
```
