---
id: ASYNCAPI-SLC12
type: event-contract
title: AsyncAPI — SLC-12 Domain Events
wave: W6
slice: SLC-12
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-12 Domain Events

_42 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-12 Domain Events
  version: 1.0.0
channels:
  knowledge.events:
    address: '{cell}.knowledge.events'
    messages:
      EVT-PTM-DEFINED:
        $ref: '#/components/messages/EVT-PTM-DEFINED'
      EVT-PTM-EDITED:
        $ref: '#/components/messages/EVT-PTM-EDITED'
      EVT-PTM-ACTIVATED:
        $ref: '#/components/messages/EVT-PTM-ACTIVATED'
      EVT-PTM-RETIRED:
        $ref: '#/components/messages/EVT-PTM-RETIRED'
      EVT-PRD-CREATED:
        $ref: '#/components/messages/EVT-PRD-CREATED'
      EVT-PRD-GENERATION-STARTED:
        $ref: '#/components/messages/EVT-PRD-GENERATION-STARTED'
      EVT-PRD-GENERATED:
        $ref: '#/components/messages/EVT-PRD-GENERATED'
      EVT-PRD-GENERATION-FAILED:
        $ref: '#/components/messages/EVT-PRD-GENERATION-FAILED'
      EVT-PRD-NARRATIVE-EDITED:
        $ref: '#/components/messages/EVT-PRD-NARRATIVE-EDITED'
      EVT-PRD-SUBMITTED:
        $ref: '#/components/messages/EVT-PRD-SUBMITTED'
      EVT-PRD-RETURNED:
        $ref: '#/components/messages/EVT-PRD-RETURNED'
      EVT-PRD-APPROVED:
        $ref: '#/components/messages/EVT-PRD-APPROVED'
      EVT-PRD-SUPERSEDED:
        $ref: '#/components/messages/EVT-PRD-SUPERSEDED'
      EVT-PRD-WITHDRAWN:
        $ref: '#/components/messages/EVT-PRD-WITHDRAWN'
      EVT-PRD-DISCARDED:
        $ref: '#/components/messages/EVT-PRD-DISCARDED'
      EVT-DST-STARTED:
        $ref: '#/components/messages/EVT-DST-STARTED'
      EVT-DST-COMPLETED:
        $ref: '#/components/messages/EVT-DST-COMPLETED'
      EVT-DST-COMPLETED-WITH-EXCLUSIONS:
        $ref: '#/components/messages/EVT-DST-COMPLETED-WITH-EXCLUSIONS'
      EVT-DST-CANCELLED:
        $ref: '#/components/messages/EVT-DST-CANCELLED'
      EVT-KNO-DRAFTED:
        $ref: '#/components/messages/EVT-KNO-DRAFTED'
      EVT-KNO-EDITED:
        $ref: '#/components/messages/EVT-KNO-EDITED'
      EVT-KNO-SUBMITTED:
        $ref: '#/components/messages/EVT-KNO-SUBMITTED'
      EVT-KNO-RETURNED:
        $ref: '#/components/messages/EVT-KNO-RETURNED'
      EVT-KNO-PUBLISHED:
        $ref: '#/components/messages/EVT-KNO-PUBLISHED'
      EVT-KNO-REJECTED:
        $ref: '#/components/messages/EVT-KNO-REJECTED'
      EVT-KNO-REUSED:
        $ref: '#/components/messages/EVT-KNO-REUSED'
      EVT-KNO-SUPERSEDED:
        $ref: '#/components/messages/EVT-KNO-SUPERSEDED'
      EVT-KNO-RETIRED:
        $ref: '#/components/messages/EVT-KNO-RETIRED'
      EVT-KNO-DISCARDED:
        $ref: '#/components/messages/EVT-KNO-DISCARDED'
      EVT-ARC-INGEST-STARTED:
        $ref: '#/components/messages/EVT-ARC-INGEST-STARTED'
      EVT-ARC-ARCHIVED:
        $ref: '#/components/messages/EVT-ARC-ARCHIVED'
      EVT-ARC-INGEST-FAILED:
        $ref: '#/components/messages/EVT-ARC-INGEST-FAILED'
      EVT-ARC-INTEGRITY-FAILED:
        $ref: '#/components/messages/EVT-ARC-INTEGRITY-FAILED'
      EVT-ARC-REPAIRED:
        $ref: '#/components/messages/EVT-ARC-REPAIRED'
      EVT-ARC-FORMAT-MIGRATED:
        $ref: '#/components/messages/EVT-ARC-FORMAT-MIGRATED'
      EVT-ARC-TRANSFERRED:
        $ref: '#/components/messages/EVT-ARC-TRANSFERRED'
      EVT-ARC-DISPOSED:
        $ref: '#/components/messages/EVT-ARC-DISPOSED'
      EVT-REC-REQUESTED:
        $ref: '#/components/messages/EVT-REC-REQUESTED'
      EVT-REC-STARTED:
        $ref: '#/components/messages/EVT-REC-STARTED'
      EVT-REC-COMPLETED:
        $ref: '#/components/messages/EVT-REC-COMPLETED'
      EVT-REC-FAILED:
        $ref: '#/components/messages/EVT-REC-FAILED'
      EVT-REC-CANCELLED:
        $ref: '#/components/messages/EVT-REC-CANCELLED'
    parameters:
      cell: {}
operations:
  publish_knowledge:
    action: send
    channel:
      $ref: '#/channels/knowledge.events'
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
    EVT-PTM-DEFINED:
      name: EVT-PTM-DEFINED
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
      - Product generator
      x-partition-key: tenant_id + aggregate.id
    EVT-PTM-EDITED:
      name: EVT-PTM-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Product generator
      x-partition-key: tenant_id + aggregate.id
    EVT-PTM-ACTIVATED:
      name: EVT-PTM-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Product generator
      x-partition-key: tenant_id + aggregate.id
    EVT-PTM-RETIRED:
      name: EVT-PTM-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Product generator
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-CREATED:
      name: EVT-PRD-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-GENERATION-STARTED:
      name: EVT-PRD-GENERATION-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-GENERATED:
      name: EVT-PRD-GENERATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-GENERATION-FAILED:
      name: EVT-PRD-GENERATION-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-NARRATIVE-EDITED:
      name: EVT-PRD-NARRATIVE-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-SUBMITTED:
      name: EVT-PRD-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-RETURNED:
      name: EVT-PRD-RETURNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-APPROVED:
      name: EVT-PRD-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-SUPERSEDED:
      name: EVT-PRD-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-WITHDRAWN:
      name: EVT-PRD-WITHDRAWN
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-PRD-DISCARDED:
      name: EVT-PRD-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Distribution
      - Search projection (SLC-05)
      - Notification (reviewers)
      x-partition-key: tenant_id + aggregate.id
    EVT-DST-STARTED:
      name: EVT-DST-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification (recipients)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DST-COMPLETED:
      name: EVT-DST-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification (recipients)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DST-COMPLETED-WITH-EXCLUSIONS:
      name: EVT-DST-COMPLETED-WITH-EXCLUSIONS
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification (recipients)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-DST-CANCELLED:
      name: EVT-DST-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification (recipients)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-DRAFTED:
      name: EVT-KNO-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-EDITED:
      name: EVT-KNO-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-SUBMITTED:
      name: EVT-KNO-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-RETURNED:
      name: EVT-KNO-RETURNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-PUBLISHED:
      name: EVT-KNO-PUBLISHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-REJECTED:
      name: EVT-KNO-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-REUSED:
      name: EVT-KNO-REUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-SUPERSEDED:
      name: EVT-KNO-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-RETIRED:
      name: EVT-KNO-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-KNO-DISCARDED:
      name: EVT-KNO-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Knowledge suggestion index
      - Search projection (SLC-05)
      - Business telemetry (OUT-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-INGEST-STARTED:
      name: EVT-ARC-INGEST-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-ARCHIVED:
      name: EVT-ARC-ARCHIVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-INGEST-FAILED:
      name: EVT-ARC-INGEST-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-INTEGRITY-FAILED:
      name: EVT-ARC-INTEGRITY-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-REPAIRED:
      name: EVT-ARC-REPAIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-FORMAT-MIGRATED:
      name: EVT-ARC-FORMAT-MIGRATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-TRANSFERRED:
      name: EVT-ARC-TRANSFERRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-ARC-DISPOSED:
      name: EVT-ARC-DISPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Archive catalogue
      - Disposition (SLC-12a)
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-REC-REQUESTED:
      name: EVT-REC-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Requester notification
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-REC-STARTED:
      name: EVT-REC-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Requester notification
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-REC-COMPLETED:
      name: EVT-REC-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Requester notification
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-REC-FAILED:
      name: EVT-REC-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Requester notification
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-REC-CANCELLED:
      name: EVT-REC-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Requester notification
      - Audit
      x-partition-key: tenant_id + aggregate.id
```
