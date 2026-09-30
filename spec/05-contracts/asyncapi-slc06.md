---
id: ASYNCAPI-SLC06
type: event-contract
title: AsyncAPI — SLC-06 Domain Events
wave: W6
slice: SLC-06
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-06 Domain Events

_30 messages on 2 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-06 Domain Events
  version: 1.0.0
channels:
  intelligence.events:
    address: '{cell}.intelligence.events'
    messages:
      EVT-SIT-CREATED:
        $ref: '#/components/messages/EVT-SIT-CREATED'
      EVT-SIT-DEFINITION-CHANGED:
        $ref: '#/components/messages/EVT-SIT-DEFINITION-CHANGED'
      EVT-SIT-ACTIVATED:
        $ref: '#/components/messages/EVT-SIT-ACTIVATED'
      EVT-SIT-PAUSED:
        $ref: '#/components/messages/EVT-SIT-PAUSED'
      EVT-SIT-RESUMED:
        $ref: '#/components/messages/EVT-SIT-RESUMED'
      EVT-SIT-CLOSED:
        $ref: '#/components/messages/EVT-SIT-CLOSED'
      EVT-SIT-RECLASSIFIED:
        $ref: '#/components/messages/EVT-SIT-RECLASSIFIED'
      EVT-ARL-DEFINED:
        $ref: '#/components/messages/EVT-ARL-DEFINED'
      EVT-ARL-EDITED:
        $ref: '#/components/messages/EVT-ARL-EDITED'
      EVT-ARL-ACTIVATED:
        $ref: '#/components/messages/EVT-ARL-ACTIVATED'
      EVT-ARL-DISABLED:
        $ref: '#/components/messages/EVT-ARL-DISABLED'
      EVT-ARL-ENABLED:
        $ref: '#/components/messages/EVT-ARL-ENABLED'
      EVT-ARL-RETIRED:
        $ref: '#/components/messages/EVT-ARL-RETIRED'
      EVT-ALR-RAISED:
        $ref: '#/components/messages/EVT-ALR-RAISED'
      EVT-ALR-REPEATED:
        $ref: '#/components/messages/EVT-ALR-REPEATED'
      EVT-ALR-ACKNOWLEDGED:
        $ref: '#/components/messages/EVT-ALR-ACKNOWLEDGED'
      EVT-ALR-ESCALATED:
        $ref: '#/components/messages/EVT-ALR-ESCALATED'
      EVT-ALR-RESOLVED:
        $ref: '#/components/messages/EVT-ALR-RESOLVED'
      EVT-ALR-DISMISSED:
        $ref: '#/components/messages/EVT-ALR-DISMISSED'
    parameters:
      cell: {}
  operations.events:
    address: '{cell}.operations.events'
    messages:
      EVT-SUB-SUBSCRIBED:
        $ref: '#/components/messages/EVT-SUB-SUBSCRIBED'
      EVT-SUB-CHANNELS-UPDATED:
        $ref: '#/components/messages/EVT-SUB-CHANNELS-UPDATED'
      EVT-SUB-PAUSED:
        $ref: '#/components/messages/EVT-SUB-PAUSED'
      EVT-SUB-RESUMED:
        $ref: '#/components/messages/EVT-SUB-RESUMED'
      EVT-SUB-ENDED:
        $ref: '#/components/messages/EVT-SUB-ENDED'
      EVT-NTF-QUEUED:
        $ref: '#/components/messages/EVT-NTF-QUEUED'
      EVT-NTF-SENT:
        $ref: '#/components/messages/EVT-NTF-SENT'
      EVT-NTF-WITHHELD:
        $ref: '#/components/messages/EVT-NTF-WITHHELD'
      EVT-NTF-FAILED:
        $ref: '#/components/messages/EVT-NTF-FAILED'
      EVT-NTF-READ:
        $ref: '#/components/messages/EVT-NTF-READ'
      EVT-NTF-EXPIRED:
        $ref: '#/components/messages/EVT-NTF-EXPIRED'
    parameters:
      cell: {}
operations:
  publish_intelligence:
    action: send
    channel:
      $ref: '#/channels/intelligence.events'
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
    EVT-SIT-CREATED:
      name: EVT-SIT-CREATED
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
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-DEFINITION-CHANGED:
      name: EVT-SIT-DEFINITION-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-ACTIVATED:
      name: EVT-SIT-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-PAUSED:
      name: EVT-SIT-PAUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-RESUMED:
      name: EVT-SIT-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-CLOSED:
      name: EVT-SIT-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SIT-RECLASSIFIED:
      name: EVT-SIT-RECLASSIFIED
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
      - Membership evaluator (reload definition)
      - Alert evaluator
      - Tile cache invalidation
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-DEFINED:
      name: EVT-ARL-DEFINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-EDITED:
      name: EVT-ARL-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-ACTIVATED:
      name: EVT-ARL-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-DISABLED:
      name: EVT-ARL-DISABLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-ENABLED:
      name: EVT-ARL-ENABLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ARL-RETIRED:
      name: EVT-ARL-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Alert evaluator (reload rules)
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-RAISED:
      name: EVT-ALR-RAISED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-REPEATED:
      name: EVT-ALR-REPEATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-ACKNOWLEDGED:
      name: EVT-ALR-ACKNOWLEDGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-ESCALATED:
      name: EVT-ALR-ESCALATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-RESOLVED:
      name: EVT-ALR-RESOLVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-ALR-DISMISSED:
      name: EVT-ALR-DISMISSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out (recipients = cleared subscribers)
      - COP (alerts layer)
      - Escalation scheduler
      x-partition-key: tenant_id + aggregate.id
    EVT-SUB-SUBSCRIBED:
      name: EVT-SUB-SUBSCRIBED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out index
      x-partition-key: tenant_id + aggregate.id
    EVT-SUB-CHANNELS-UPDATED:
      name: EVT-SUB-CHANNELS-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out index
      x-partition-key: tenant_id + aggregate.id
    EVT-SUB-PAUSED:
      name: EVT-SUB-PAUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out index
      x-partition-key: tenant_id + aggregate.id
    EVT-SUB-RESUMED:
      name: EVT-SUB-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out index
      x-partition-key: tenant_id + aggregate.id
    EVT-SUB-ENDED:
      name: EVT-SUB-ENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Notification fan-out index
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-QUEUED:
      name: EVT-NTF-QUEUED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-SENT:
      name: EVT-NTF-SENT
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-WITHHELD:
      name: EVT-NTF-WITHHELD
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-FAILED:
      name: EVT-NTF-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-READ:
      name: EVT-NTF-READ
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
    EVT-NTF-EXPIRED:
      name: EVT-NTF-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Push gateway
      - In-app inbox
      x-partition-key: tenant_id + aggregate.id
```
