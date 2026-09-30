---
id: ASYNCAPI-SLC07
type: event-contract
title: AsyncAPI — SLC-07 Domain Events
wave: W6
slice: SLC-07
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-07 Domain Events

_35 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-07 Domain Events
  version: 1.0.0
channels:
  intelligence.events:
    address: '{cell}.intelligence.events'
    messages:
      EVT-ACS-CREATED:
        $ref: '#/components/messages/EVT-ACS-CREATED'
      EVT-ACS-DEFINED:
        $ref: '#/components/messages/EVT-ACS-DEFINED'
      EVT-ACS-OPENED:
        $ref: '#/components/messages/EVT-ACS-OPENED'
      EVT-ACS-HYPOTHESIS-ADDED:
        $ref: '#/components/messages/EVT-ACS-HYPOTHESIS-ADDED'
      EVT-ACS-HYPOTHESIS-UPDATED:
        $ref: '#/components/messages/EVT-ACS-HYPOTHESIS-UPDATED'
      EVT-ACS-ASSUMPTION-ADDED:
        $ref: '#/components/messages/EVT-ACS-ASSUMPTION-ADDED'
      EVT-ACS-ASSUMPTION-RETIRED:
        $ref: '#/components/messages/EVT-ACS-ASSUMPTION-RETIRED'
      EVT-ACS-EVIDENCE-SELECTED:
        $ref: '#/components/messages/EVT-ACS-EVIDENCE-SELECTED'
      EVT-ACS-EVIDENCE-DESELECTED:
        $ref: '#/components/messages/EVT-ACS-EVIDENCE-DESELECTED'
      EVT-ACS-SCENARIO-DEFINED:
        $ref: '#/components/messages/EVT-ACS-SCENARIO-DEFINED'
      EVT-ACS-CLOSED:
        $ref: '#/components/messages/EVT-ACS-CLOSED'
      EVT-ACS-REOPENED:
        $ref: '#/components/messages/EVT-ACS-REOPENED'
      EVT-ACS-CANCELLED:
        $ref: '#/components/messages/EVT-ACS-CANCELLED'
      EVT-ACS-RECLASSIFIED:
        $ref: '#/components/messages/EVT-ACS-RECLASSIFIED'
      EVT-AMT-REGISTERED:
        $ref: '#/components/messages/EVT-AMT-REGISTERED'
      EVT-AMT-ACTIVATED:
        $ref: '#/components/messages/EVT-AMT-ACTIVATED'
      EVT-AMT-DEPRECATED:
        $ref: '#/components/messages/EVT-AMT-DEPRECATED'
      EVT-AMT-RETIRED:
        $ref: '#/components/messages/EVT-AMT-RETIRED'
      EVT-RUN-QUEUED:
        $ref: '#/components/messages/EVT-RUN-QUEUED'
      EVT-RUN-STARTED:
        $ref: '#/components/messages/EVT-RUN-STARTED'
      EVT-RUN-SUCCEEDED:
        $ref: '#/components/messages/EVT-RUN-SUCCEEDED'
      EVT-RUN-FAILED:
        $ref: '#/components/messages/EVT-RUN-FAILED'
      EVT-RUN-CANCELLED:
        $ref: '#/components/messages/EVT-RUN-CANCELLED'
      EVT-FND-RECORDED:
        $ref: '#/components/messages/EVT-FND-RECORDED'
      EVT-FND-EDITED:
        $ref: '#/components/messages/EVT-FND-EDITED'
      EVT-FND-ACCEPTED:
        $ref: '#/components/messages/EVT-FND-ACCEPTED'
      EVT-FND-WITHDRAWN:
        $ref: '#/components/messages/EVT-FND-WITHDRAWN'
      EVT-ASM-DRAFTED:
        $ref: '#/components/messages/EVT-ASM-DRAFTED'
      EVT-ASM-EDITED:
        $ref: '#/components/messages/EVT-ASM-EDITED'
      EVT-ASM-SUBMITTED:
        $ref: '#/components/messages/EVT-ASM-SUBMITTED'
      EVT-ASM-RETURNED:
        $ref: '#/components/messages/EVT-ASM-RETURNED'
      EVT-ASM-PUBLISHED:
        $ref: '#/components/messages/EVT-ASM-PUBLISHED'
      EVT-ASM-SUPERSEDED:
        $ref: '#/components/messages/EVT-ASM-SUPERSEDED'
      EVT-ASM-WITHDRAWN:
        $ref: '#/components/messages/EVT-ASM-WITHDRAWN'
      EVT-ASM-DISCARDED:
        $ref: '#/components/messages/EVT-ASM-DISCARDED'
    parameters:
      cell: {}
operations:
  publish_intelligence:
    action: send
    channel:
      $ref: '#/channels/intelligence.events'
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
    EVT-ACS-CREATED:
      name: EVT-ACS-CREATED
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
    EVT-ACS-DEFINED:
      name: EVT-ACS-DEFINED
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
    EVT-ACS-OPENED:
      name: EVT-ACS-OPENED
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
    EVT-ACS-HYPOTHESIS-ADDED:
      name: EVT-ACS-HYPOTHESIS-ADDED
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
    EVT-ACS-HYPOTHESIS-UPDATED:
      name: EVT-ACS-HYPOTHESIS-UPDATED
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
    EVT-ACS-ASSUMPTION-ADDED:
      name: EVT-ACS-ASSUMPTION-ADDED
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
    EVT-ACS-ASSUMPTION-RETIRED:
      name: EVT-ACS-ASSUMPTION-RETIRED
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
    EVT-ACS-EVIDENCE-SELECTED:
      name: EVT-ACS-EVIDENCE-SELECTED
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
    EVT-ACS-EVIDENCE-DESELECTED:
      name: EVT-ACS-EVIDENCE-DESELECTED
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
    EVT-ACS-SCENARIO-DEFINED:
      name: EVT-ACS-SCENARIO-DEFINED
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
    EVT-ACS-CLOSED:
      name: EVT-ACS-CLOSED
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
    EVT-ACS-REOPENED:
      name: EVT-ACS-REOPENED
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
    EVT-ACS-CANCELLED:
      name: EVT-ACS-CANCELLED
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
    EVT-ACS-RECLASSIFIED:
      name: EVT-ACS-RECLASSIFIED
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
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-AMT-REGISTERED:
      name: EVT-AMT-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler (image allow-list)
      x-partition-key: tenant_id + aggregate.id
    EVT-AMT-ACTIVATED:
      name: EVT-AMT-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler (image allow-list)
      x-partition-key: tenant_id + aggregate.id
    EVT-AMT-DEPRECATED:
      name: EVT-AMT-DEPRECATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler (image allow-list)
      x-partition-key: tenant_id + aggregate.id
    EVT-AMT-RETIRED:
      name: EVT-AMT-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler (image allow-list)
      x-partition-key: tenant_id + aggregate.id
    EVT-RUN-QUEUED:
      name: EVT-RUN-QUEUED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler / compute workers
      - Lineage writer (BC02 LineageRecord)
      - Case owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-RUN-STARTED:
      name: EVT-RUN-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler / compute workers
      - Lineage writer (BC02 LineageRecord)
      - Case owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-RUN-SUCCEEDED:
      name: EVT-RUN-SUCCEEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler / compute workers
      - Lineage writer (BC02 LineageRecord)
      - Case owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-RUN-FAILED:
      name: EVT-RUN-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler / compute workers
      - Lineage writer (BC02 LineageRecord)
      - Case owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-RUN-CANCELLED:
      name: EVT-RUN-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Job scheduler / compute workers
      - Lineage writer (BC02 LineageRecord)
      - Case owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-FND-RECORDED:
      name: EVT-FND-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Assessment review flags
      x-partition-key: tenant_id + aggregate.id
    EVT-FND-EDITED:
      name: EVT-FND-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Assessment review flags
      x-partition-key: tenant_id + aggregate.id
    EVT-FND-ACCEPTED:
      name: EVT-FND-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Assessment review flags
      x-partition-key: tenant_id + aggregate.id
    EVT-FND-WITHDRAWN:
      name: EVT-FND-WITHDRAWN
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Assessment review flags
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-DRAFTED:
      name: EVT-ASM-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-EDITED:
      name: EVT-ASM-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-SUBMITTED:
      name: EVT-ASM-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-RETURNED:
      name: EVT-ASM-RETURNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-PUBLISHED:
      name: EVT-ASM-PUBLISHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-SUPERSEDED:
      name: EVT-ASM-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-WITHDRAWN:
      name: EVT-ASM-WITHDRAWN
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
    EVT-ASM-DISCARDED:
      name: EVT-ASM-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Decision requests (SLC-08: pinned references)'
      - Situation membership (assessment layer)
      - Search projection (SLC-05)
      - Products (SLC-12, R2)
      x-partition-key: tenant_id + aggregate.id
```
