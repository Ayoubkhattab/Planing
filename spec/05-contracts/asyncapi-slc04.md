---
id: ASYNCAPI-SLC04
type: event-contract
title: AsyncAPI — SLC-04 Domain Events
wave: W6
slice: SLC-04
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-04 Domain Events

_23 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-04 Domain Events
  version: 1.0.0
channels:
  information.events:
    address: '{cell}.information.events'
    messages:
      EVT-CNF-DETECTED:
        $ref: '#/components/messages/EVT-CNF-DETECTED'
      EVT-CNF-RAISED:
        $ref: '#/components/messages/EVT-CNF-RAISED'
      EVT-CNF-CLAIM-ADDED:
        $ref: '#/components/messages/EVT-CNF-CLAIM-ADDED'
      EVT-CNF-ASSIGNED:
        $ref: '#/components/messages/EVT-CNF-ASSIGNED'
      EVT-CNF-REVIEW-STARTED:
        $ref: '#/components/messages/EVT-CNF-REVIEW-STARTED'
      EVT-CNF-RESOLVED:
        $ref: '#/components/messages/EVT-CNF-RESOLVED'
      EVT-CNF-ACCEPTED:
        $ref: '#/components/messages/EVT-CNF-ACCEPTED'
      EVT-CNF-REOPENED:
        $ref: '#/components/messages/EVT-CNF-REOPENED'
      EVT-CNF-SUPERSEDED:
        $ref: '#/components/messages/EVT-CNF-SUPERSEDED'
      EVT-ER-PROPOSED:
        $ref: '#/components/messages/EVT-ER-PROPOSED'
      EVT-ER-REVIEW-STARTED:
        $ref: '#/components/messages/EVT-ER-REVIEW-STARTED'
      EVT-ER-MATCHED:
        $ref: '#/components/messages/EVT-ER-MATCHED'
      EVT-ER-NOT-MATCHED:
        $ref: '#/components/messages/EVT-ER-NOT-MATCHED'
      EVT-ER-PARKED:
        $ref: '#/components/messages/EVT-ER-PARKED'
      EVT-ER-RESUMED:
        $ref: '#/components/messages/EVT-ER-RESUMED'
      EVT-ER-SPLIT-REQUESTED:
        $ref: '#/components/messages/EVT-ER-SPLIT-REQUESTED'
      EVT-ER-MATCH-CONFIRMED:
        $ref: '#/components/messages/EVT-ER-MATCH-CONFIRMED'
      EVT-ER-SPLIT:
        $ref: '#/components/messages/EVT-ER-SPLIT'
      EVT-ER-WITHDRAWN:
        $ref: '#/components/messages/EVT-ER-WITHDRAWN'
      EVT-MRS-DRAFTED:
        $ref: '#/components/messages/EVT-MRS-DRAFTED'
      EVT-MRS-EDITED:
        $ref: '#/components/messages/EVT-MRS-EDITED'
      EVT-MRS-ACTIVATED:
        $ref: '#/components/messages/EVT-MRS-ACTIVATED'
      EVT-MRS-SUPERSEDED:
        $ref: '#/components/messages/EVT-MRS-SUPERSEDED'
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
    EVT-CNF-DETECTED:
      name: EVT-CNF-DETECTED
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
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-RAISED:
      name: EVT-CNF-RAISED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-CLAIM-ADDED:
      name: EVT-CNF-CLAIM-ADDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-ASSIGNED:
      name: EVT-CNF-ASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-REVIEW-STARTED:
      name: EVT-CNF-REVIEW-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-RESOLVED:
      name: EVT-CNF-RESOLVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-ACCEPTED:
      name: EVT-CNF-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-REOPENED:
      name: EVT-CNF-REOPENED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-CNF-SUPERSEDED:
      name: EVT-CNF-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Resolved-view materializer (SLC-05)
      - Analyst notifications
      - 'Situation membership (SLC-06: DISPUTED markers)'
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-PROPOSED:
      name: EVT-ER-PROPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-REVIEW-STARTED:
      name: EVT-ER-REVIEW-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-MATCHED:
      name: EVT-ER-MATCHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-NOT-MATCHED:
      name: EVT-ER-NOT-MATCHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-PARKED:
      name: EVT-ER-PARKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-RESUMED:
      name: EVT-ER-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-SPLIT-REQUESTED:
      name: EVT-ER-SPLIT-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-MATCH-CONFIRMED:
      name: EVT-ER-MATCH-CONFIRMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-SPLIT:
      name: EVT-ER-SPLIT
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-ER-WITHDRAWN:
      name: EVT-ER-WITHDRAWN
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Cluster maintainer (same transaction) → EVT cluster changed
      - Conflict detector (re-run on cluster change)
      - Search/Graph projections (canonical ids)
      - Situation membership (SLC-06)
      x-partition-key: tenant_id + aggregate.id
    EVT-MRS-DRAFTED:
      name: EVT-MRS-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Candidate generator (reloads ruleset)
      x-partition-key: tenant_id + aggregate.id
    EVT-MRS-EDITED:
      name: EVT-MRS-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Candidate generator (reloads ruleset)
      x-partition-key: tenant_id + aggregate.id
    EVT-MRS-ACTIVATED:
      name: EVT-MRS-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Candidate generator (reloads ruleset)
      x-partition-key: tenant_id + aggregate.id
    EVT-MRS-SUPERSEDED:
      name: EVT-MRS-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Candidate generator (reloads ruleset)
      x-partition-key: tenant_id + aggregate.id
```
