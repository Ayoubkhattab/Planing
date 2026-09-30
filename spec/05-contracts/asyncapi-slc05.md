---
id: ASYNCAPI-SLC05
type: event-contract
title: AsyncAPI — SLC-05 Domain Events
wave: W6
slice: SLC-05
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-05 Domain Events

_7 messages on 1 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-05 Domain Events
  version: 1.0.0
channels:
  discovery.events:
    address: '{cell}.discovery.events'
    messages:
      EVT-PRJ-BUILD-STARTED:
        $ref: '#/components/messages/EVT-PRJ-BUILD-STARTED'
      EVT-PRJ-READY:
        $ref: '#/components/messages/EVT-PRJ-READY'
      EVT-PRJ-FAILED:
        $ref: '#/components/messages/EVT-PRJ-FAILED'
      EVT-PRJ-PROMOTED:
        $ref: '#/components/messages/EVT-PRJ-PROMOTED'
      EVT-PRJ-DEGRADED:
        $ref: '#/components/messages/EVT-PRJ-DEGRADED'
      EVT-PRJ-RECOVERED:
        $ref: '#/components/messages/EVT-PRJ-RECOVERED'
      EVT-PRJ-RETIRED:
        $ref: '#/components/messages/EVT-PRJ-RETIRED'
    parameters:
      cell: {}
operations:
  publish_discovery:
    action: send
    channel:
      $ref: '#/channels/discovery.events'
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
    EVT-PRJ-BUILD-STARTED:
      name: EVT-PRJ-BUILD-STARTED
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
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-READY:
      name: EVT-PRJ-READY
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-FAILED:
      name: EVT-PRJ-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-PROMOTED:
      name: EVT-PRJ-PROMOTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-DEGRADED:
      name: EVT-PRJ-DEGRADED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-RECOVERED:
      name: EVT-PRJ-RECOVERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-PRJ-RETIRED:
      name: EVT-PRJ-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Query router (alias switch)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
```
