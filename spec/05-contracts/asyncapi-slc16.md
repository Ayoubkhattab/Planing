---
id: ASYNCAPI-SLC16
type: event-contract
title: AsyncAPI — SLC-16 Domain Events
wave: W6
slice: SLC-16
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-16 Domain Events

_25 messages on 3 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-16 Domain Events
  version: 1.0.0
channels:
  integration.events:
    address: '{cell}.integration.events'
    messages:
      EVT-CON-REGISTERED:
        $ref: '#/components/messages/EVT-CON-REGISTERED'
      EVT-CON-TEST-STARTED:
        $ref: '#/components/messages/EVT-CON-TEST-STARTED'
      EVT-CON-ACTIVATED:
        $ref: '#/components/messages/EVT-CON-ACTIVATED'
      EVT-CON-TEST-FAILED:
        $ref: '#/components/messages/EVT-CON-TEST-FAILED'
      EVT-CON-DEGRADED:
        $ref: '#/components/messages/EVT-CON-DEGRADED'
      EVT-CON-RECOVERED:
        $ref: '#/components/messages/EVT-CON-RECOVERED'
      EVT-CON-SUSPENDED:
        $ref: '#/components/messages/EVT-CON-SUSPENDED'
      EVT-CON-RESUMED:
        $ref: '#/components/messages/EVT-CON-RESUMED'
      EVT-CON-RETIRED:
        $ref: '#/components/messages/EVT-CON-RETIRED'
      EVT-SNS-REGISTERED:
        $ref: '#/components/messages/EVT-SNS-REGISTERED'
      EVT-SNS-QUALITY-RULES-SET:
        $ref: '#/components/messages/EVT-SNS-QUALITY-RULES-SET'
      EVT-SNS-ACTIVATED:
        $ref: '#/components/messages/EVT-SNS-ACTIVATED'
      EVT-SNS-PAUSED:
        $ref: '#/components/messages/EVT-SNS-PAUSED'
      EVT-SNS-STALE:
        $ref: '#/components/messages/EVT-SNS-STALE'
      EVT-SNS-RETIRED:
        $ref: '#/components/messages/EVT-SNS-RETIRED'
    parameters:
      cell: {}
  foundation.events:
    address: '{cell}.foundation.events'
    messages:
      EVT-HRS-PROPOSED:
        $ref: '#/components/messages/EVT-HRS-PROPOSED'
      EVT-HRS-APPROVED:
        $ref: '#/components/messages/EVT-HRS-APPROVED'
      EVT-HRS-REJECTED:
        $ref: '#/components/messages/EVT-HRS-REJECTED'
      EVT-HRS-SUPERSEDED:
        $ref: '#/components/messages/EVT-HRS-SUPERSEDED'
      EVT-HRS-EXPIRED:
        $ref: '#/components/messages/EVT-HRS-EXPIRED'
    parameters:
      cell: {}
  intelligence.events:
    address: '{cell}.intelligence.events'
    messages:
      EVT-CAP-PREPARED:
        $ref: '#/components/messages/EVT-CAP-PREPARED'
      EVT-CAP-SENT:
        $ref: '#/components/messages/EVT-CAP-SENT'
      EVT-CAP-FAILED:
        $ref: '#/components/messages/EVT-CAP-FAILED'
      EVT-CAP-RETRY:
        $ref: '#/components/messages/EVT-CAP-RETRY'
      EVT-CAP-CANCELLED:
        $ref: '#/components/messages/EVT-CAP-CANCELLED'
    parameters:
      cell: {}
operations:
  publish_integration:
    action: send
    channel:
      $ref: '#/channels/integration.events'
  publish_foundation:
    action: send
    channel:
      $ref: '#/channels/foundation.events'
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
    EVT-CON-REGISTERED:
      name: EVT-CON-REGISTERED
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
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-TEST-STARTED:
      name: EVT-CON-TEST-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-ACTIVATED:
      name: EVT-CON-ACTIVATED
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
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-TEST-FAILED:
      name: EVT-CON-TEST-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-DEGRADED:
      name: EVT-CON-DEGRADED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-RECOVERED:
      name: EVT-CON-RECOVERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-SUSPENDED:
      name: EVT-CON-SUSPENDED
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
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-RESUMED:
      name: EVT-CON-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-CON-RETIRED:
      name: EVT-CON-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Egress gateway (allow-list)
      - Adapters (bind/unbind)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-REGISTERED:
      name: EVT-SNS-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-QUALITY-RULES-SET:
      name: EVT-SNS-QUALITY-RULES-SET
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-ACTIVATED:
      name: EVT-SNS-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-PAUSED:
      name: EVT-SNS-PAUSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-STALE:
      name: EVT-SNS-STALE
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-SNS-RETIRED:
      name: EVT-SNS-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Ingestion workers (SLC-02 batches)
      - Operations alerting
      x-partition-key: tenant_id + aggregate.id
    EVT-HRS-PROPOSED:
      name: EVT-HRS-PROPOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Role assignments / users (BC01)
      - Security Officer notification (leave)
      x-partition-key: tenant_id + aggregate.id
    EVT-HRS-APPROVED:
      name: EVT-HRS-APPROVED
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
      - Role assignments / users (BC01)
      - Security Officer notification (leave)
      x-partition-key: tenant_id + aggregate.id
    EVT-HRS-REJECTED:
      name: EVT-HRS-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Role assignments / users (BC01)
      - Security Officer notification (leave)
      x-partition-key: tenant_id + aggregate.id
    EVT-HRS-SUPERSEDED:
      name: EVT-HRS-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Role assignments / users (BC01)
      - Security Officer notification (leave)
      x-partition-key: tenant_id + aggregate.id
    EVT-HRS-EXPIRED:
      name: EVT-HRS-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Role assignments / users (BC01)
      - Security Officer notification (leave)
      x-partition-key: tenant_id + aggregate.id
    EVT-CAP-PREPARED:
      name: EVT-CAP-PREPARED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - CAP gateway
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-CAP-SENT:
      name: EVT-CAP-SENT
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - CAP gateway
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-CAP-FAILED:
      name: EVT-CAP-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - CAP gateway
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-CAP-RETRY:
      name: EVT-CAP-RETRY
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - CAP gateway
      - Audit
      x-partition-key: tenant_id + aggregate.id
    EVT-CAP-CANCELLED:
      name: EVT-CAP-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - CAP gateway
      - Audit
      x-partition-key: tenant_id + aggregate.id
```
