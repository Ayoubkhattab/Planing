---
id: ASYNCAPI-SLC10
type: event-contract
title: AsyncAPI — SLC-10 Domain Events
wave: W6
slice: SLC-10
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-10 Domain Events

_37 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-10 Domain Events
  version: 1.0.0
channels:
  ai.events:
    address: '{cell}.ai.events'
    messages:
      EVT-AIR-RECEIVED:
        $ref: '#/components/messages/EVT-AIR-RECEIVED'
      EVT-AIR-REFUSED:
        $ref: '#/components/messages/EVT-AIR-REFUSED'
      EVT-AIR-RETRIEVING:
        $ref: '#/components/messages/EVT-AIR-RETRIEVING'
      EVT-AIR-CONTEXT-SEALED:
        $ref: '#/components/messages/EVT-AIR-CONTEXT-SEALED'
      EVT-AIR-INSUFFICIENT-EVIDENCE:
        $ref: '#/components/messages/EVT-AIR-INSUFFICIENT-EVIDENCE'
      EVT-AIR-COMPLETED:
        $ref: '#/components/messages/EVT-AIR-COMPLETED'
      EVT-AIR-FAILED:
        $ref: '#/components/messages/EVT-AIR-FAILED'
      EVT-AIR-CANCELLED:
        $ref: '#/components/messages/EVT-AIR-CANCELLED'
      EVT-AIRS-PROPOSED:
        $ref: '#/components/messages/EVT-AIRS-PROPOSED'
      EVT-AIRS-REVIEW-STARTED:
        $ref: '#/components/messages/EVT-AIRS-REVIEW-STARTED'
      EVT-AIRS-ACCEPTED:
        $ref: '#/components/messages/EVT-AIRS-ACCEPTED'
      EVT-AIRS-PARTIALLY-ACCEPTED:
        $ref: '#/components/messages/EVT-AIRS-PARTIALLY-ACCEPTED'
      EVT-AIRS-REJECTED:
        $ref: '#/components/messages/EVT-AIRS-REJECTED'
      EVT-MDL-REGISTERED:
        $ref: '#/components/messages/EVT-MDL-REGISTERED'
      EVT-MDL-EVALUATION-STARTED:
        $ref: '#/components/messages/EVT-MDL-EVALUATION-STARTED'
      EVT-MDL-APPROVED:
        $ref: '#/components/messages/EVT-MDL-APPROVED'
      EVT-MDL-EVALUATION-FAILED:
        $ref: '#/components/messages/EVT-MDL-EVALUATION-FAILED'
      EVT-MDL-STAGED:
        $ref: '#/components/messages/EVT-MDL-STAGED'
      EVT-MDL-PROMOTED:
        $ref: '#/components/messages/EVT-MDL-PROMOTED'
      EVT-MDL-DRIFT-DETECTED:
        $ref: '#/components/messages/EVT-MDL-DRIFT-DETECTED'
      EVT-MDL-DEPRECATED:
        $ref: '#/components/messages/EVT-MDL-DEPRECATED'
      EVT-MDL-REINSTATED:
        $ref: '#/components/messages/EVT-MDL-REINSTATED'
      EVT-MDL-RETIRED:
        $ref: '#/components/messages/EVT-MDL-RETIRED'
      EVT-RTG-DRAFTED:
        $ref: '#/components/messages/EVT-RTG-DRAFTED'
      EVT-RTG-EDITED:
        $ref: '#/components/messages/EVT-RTG-EDITED'
      EVT-RTG-ACTIVATED:
        $ref: '#/components/messages/EVT-RTG-ACTIVATED'
      EVT-RTG-DISCARDED:
        $ref: '#/components/messages/EVT-RTG-DISCARDED'
      EVT-RTG-SUPERSEDED:
        $ref: '#/components/messages/EVT-RTG-SUPERSEDED'
      EVT-TOL-REGISTERED:
        $ref: '#/components/messages/EVT-TOL-REGISTERED'
      EVT-TOL-ACTIVATED:
        $ref: '#/components/messages/EVT-TOL-ACTIVATED'
      EVT-TOL-DISABLED:
        $ref: '#/components/messages/EVT-TOL-DISABLED'
      EVT-TOL-ENABLED:
        $ref: '#/components/messages/EVT-TOL-ENABLED'
      EVT-TOL-RETIRED:
        $ref: '#/components/messages/EVT-TOL-RETIRED'
      EVT-EVS-DRAFTED:
        $ref: '#/components/messages/EVT-EVS-DRAFTED'
      EVT-EVS-EDITED:
        $ref: '#/components/messages/EVT-EVS-EDITED'
      EVT-EVS-ACTIVATED:
        $ref: '#/components/messages/EVT-EVS-ACTIVATED'
      EVT-EVS-SUPERSEDED:
        $ref: '#/components/messages/EVT-EVS-SUPERSEDED'
    parameters:
      cell: {}
operations:
  publish_ai:
    action: send
    channel:
      $ref: '#/channels/ai.events'
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
    EVT-AIR-RECEIVED:
      name: EVT-AIR-RECEIVED
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
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-REFUSED:
      name: EVT-AIR-REFUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-RETRIEVING:
      name: EVT-AIR-RETRIEVING
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-CONTEXT-SEALED:
      name: EVT-AIR-CONTEXT-SEALED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-INSUFFICIENT-EVIDENCE:
      name: EVT-AIR-INSUFFICIENT-EVIDENCE
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-COMPLETED:
      name: EVT-AIR-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-FAILED:
      name: EVT-AIR-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIR-CANCELLED:
      name: EVT-AIR-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - AI result creator (reviewable operations)
      - Usage accounting
      - Audit (encrypted prompt/output log)
      x-partition-key: tenant_id + aggregate.id
    EVT-AIRS-PROPOSED:
      name: EVT-AIRS-PROPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (effects on acceptance)
      - Evaluation feedback store
      x-partition-key: tenant_id + aggregate.id
    EVT-AIRS-REVIEW-STARTED:
      name: EVT-AIRS-REVIEW-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (effects on acceptance)
      - Evaluation feedback store
      x-partition-key: tenant_id + aggregate.id
    EVT-AIRS-ACCEPTED:
      name: EVT-AIRS-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (effects on acceptance)
      - Evaluation feedback store
      x-partition-key: tenant_id + aggregate.id
    EVT-AIRS-PARTIALLY-ACCEPTED:
      name: EVT-AIRS-PARTIALLY-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (effects on acceptance)
      - Evaluation feedback store
      x-partition-key: tenant_id + aggregate.id
    EVT-AIRS-REJECTED:
      name: EVT-AIRS-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (effects on acceptance)
      - Evaluation feedback store
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-REGISTERED:
      name: EVT-MDL-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-EVALUATION-STARTED:
      name: EVT-MDL-EVALUATION-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-APPROVED:
      name: EVT-MDL-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-EVALUATION-FAILED:
      name: EVT-MDL-EVALUATION-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-STAGED:
      name: EVT-MDL-STAGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-PROMOTED:
      name: EVT-MDL-PROMOTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-DRIFT-DETECTED:
      name: EVT-MDL-DRIFT-DETECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-DEPRECATED:
      name: EVT-MDL-DEPRECATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-REINSTATED:
      name: EVT-MDL-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-MDL-RETIRED:
      name: EVT-MDL-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Inference servers (load/unload)
      - Routing validation
      x-partition-key: tenant_id + aggregate.id
    EVT-RTG-DRAFTED:
      name: EVT-RTG-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Model router
      - PEP cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RTG-EDITED:
      name: EVT-RTG-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Model router
      - PEP cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RTG-ACTIVATED:
      name: EVT-RTG-ACTIVATED
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
      - Model router
      - PEP cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RTG-DISCARDED:
      name: EVT-RTG-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Model router
      - PEP cache
      x-partition-key: tenant_id + aggregate.id
    EVT-RTG-SUPERSEDED:
      name: EVT-RTG-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Model router
      - PEP cache
      x-partition-key: tenant_id + aggregate.id
    EVT-TOL-REGISTERED:
      name: EVT-TOL-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Tool gateway
      x-partition-key: tenant_id + aggregate.id
    EVT-TOL-ACTIVATED:
      name: EVT-TOL-ACTIVATED
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
      - Tool gateway
      x-partition-key: tenant_id + aggregate.id
    EVT-TOL-DISABLED:
      name: EVT-TOL-DISABLED
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
      - Tool gateway
      x-partition-key: tenant_id + aggregate.id
    EVT-TOL-ENABLED:
      name: EVT-TOL-ENABLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Tool gateway
      x-partition-key: tenant_id + aggregate.id
    EVT-TOL-RETIRED:
      name: EVT-TOL-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Tool gateway
      x-partition-key: tenant_id + aggregate.id
    EVT-EVS-DRAFTED:
      name: EVT-EVS-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Evaluation runner
      x-partition-key: tenant_id + aggregate.id
    EVT-EVS-EDITED:
      name: EVT-EVS-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Evaluation runner
      x-partition-key: tenant_id + aggregate.id
    EVT-EVS-ACTIVATED:
      name: EVT-EVS-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Evaluation runner
      x-partition-key: tenant_id + aggregate.id
    EVT-EVS-SUPERSEDED:
      name: EVT-EVS-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Evaluation runner
      x-partition-key: tenant_id + aggregate.id
```
