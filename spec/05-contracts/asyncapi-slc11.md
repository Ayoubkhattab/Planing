---
id: ASYNCAPI-SLC11
type: event-contract
title: AsyncAPI — SLC-11 Domain Events
wave: W6
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-11 Domain Events

_25 messages on 2 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-11 Domain Events
  version: 1.0.0
channels:
  foundation.events:
    address: '{cell}.foundation.events'
    messages:
      EVT-DEV-ENROLL-REQUESTED:
        $ref: '#/components/messages/EVT-DEV-ENROLL-REQUESTED'
      EVT-DEV-ACTIVATED:
        $ref: '#/components/messages/EVT-DEV-ACTIVATED'
      EVT-DEV-KEY-ROTATED:
        $ref: '#/components/messages/EVT-DEV-KEY-ROTATED'
      EVT-DEV-SUSPENDED:
        $ref: '#/components/messages/EVT-DEV-SUSPENDED'
      EVT-DEV-REINSTATED:
        $ref: '#/components/messages/EVT-DEV-REINSTATED'
      EVT-DEV-REPORTED-LOST:
        $ref: '#/components/messages/EVT-DEV-REPORTED-LOST'
      EVT-DEV-WIPED:
        $ref: '#/components/messages/EVT-DEV-WIPED'
      EVT-DEV-RETIRED:
        $ref: '#/components/messages/EVT-DEV-RETIRED'
    parameters:
      cell: {}
  field.events:
    address: '{cell}.field.events'
    messages:
      EVT-PKG-REQUESTED:
        $ref: '#/components/messages/EVT-PKG-REQUESTED'
      EVT-PKG-BUILDING:
        $ref: '#/components/messages/EVT-PKG-BUILDING'
      EVT-PKG-READY:
        $ref: '#/components/messages/EVT-PKG-READY'
      EVT-PKG-DOWNLOADED:
        $ref: '#/components/messages/EVT-PKG-DOWNLOADED'
      EVT-PKG-EXPIRED:
        $ref: '#/components/messages/EVT-PKG-EXPIRED'
      EVT-PKG-REVOKED:
        $ref: '#/components/messages/EVT-PKG-REVOKED'
      EVT-SYN-OPENED:
        $ref: '#/components/messages/EVT-SYN-OPENED'
      EVT-SYN-REJECTED:
        $ref: '#/components/messages/EVT-SYN-REJECTED'
      EVT-SYN-BATCH-RECEIVED:
        $ref: '#/components/messages/EVT-SYN-BATCH-RECEIVED'
      EVT-SYN-COMPLETED:
        $ref: '#/components/messages/EVT-SYN-COMPLETED'
      EVT-SYN-COMPLETED-WITH-CONFLICTS:
        $ref: '#/components/messages/EVT-SYN-COMPLETED-WITH-CONFLICTS'
      EVT-SYN-FAILED:
        $ref: '#/components/messages/EVT-SYN-FAILED'
      EVT-SCF-OPENED:
        $ref: '#/components/messages/EVT-SCF-OPENED'
      EVT-SCF-ASSIGNED:
        $ref: '#/components/messages/EVT-SCF-ASSIGNED'
      EVT-SCF-REAPPLIED:
        $ref: '#/components/messages/EVT-SCF-REAPPLIED'
      EVT-SCF-DISCARDED:
        $ref: '#/components/messages/EVT-SCF-DISCARDED'
      EVT-SCF-RESOLVED-MANUALLY:
        $ref: '#/components/messages/EVT-SCF-RESOLVED-MANUALLY'
    parameters:
      cell: {}
operations:
  publish_foundation:
    action: send
    channel:
      $ref: '#/channels/foundation.events'
  publish_field:
    action: send
    channel:
      $ref: '#/channels/field.events'
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
    EVT-DEV-ENROLL-REQUESTED:
      name: EVT-DEV-ENROLL-REQUESTED
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
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-ACTIVATED:
      name: EVT-DEV-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-KEY-ROTATED:
      name: EVT-DEV-KEY-ROTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-SUSPENDED:
      name: EVT-DEV-SUSPENDED
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
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-REINSTATED:
      name: EVT-DEV-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-REPORTED-LOST:
      name: EVT-DEV-REPORTED-LOST
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
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-WIPED:
      name: EVT-DEV-WIPED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-DEV-RETIRED:
      name: EVT-DEV-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Sync gateway (device registry cache)
      - Preload packages (revoke on LOST/SUSPENDED)
      - Security-version service
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-REQUESTED:
      name: EVT-PKG-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-BUILDING:
      name: EVT-PKG-BUILDING
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-READY:
      name: EVT-PKG-READY
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-DOWNLOADED:
      name: EVT-PKG-DOWNLOADED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-EXPIRED:
      name: EVT-PKG-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-PKG-REVOKED:
      name: EVT-PKG-REVOKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Package builder
      - Sync delta (purge list)
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-OPENED:
      name: EVT-SYN-OPENED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-REJECTED:
      name: EVT-SYN-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-BATCH-RECEIVED:
      name: EVT-SYN-BATCH-RECEIVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-COMPLETED:
      name: EVT-SYN-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-COMPLETED-WITH-CONFLICTS:
      name: EVT-SYN-COMPLETED-WITH-CONFLICTS
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SYN-FAILED:
      name: EVT-SYN-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Owner contexts (commands applied via their APIs)
      - Field telemetry
      x-partition-key: tenant_id + aggregate.id
    EVT-SCF-OPENED:
      name: EVT-SCF-OPENED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Reviewer notification
      - Sync delta (conflict notice to field user)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCF-ASSIGNED:
      name: EVT-SCF-ASSIGNED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Reviewer notification
      - Sync delta (conflict notice to field user)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCF-REAPPLIED:
      name: EVT-SCF-REAPPLIED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Reviewer notification
      - Sync delta (conflict notice to field user)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCF-DISCARDED:
      name: EVT-SCF-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Reviewer notification
      - Sync delta (conflict notice to field user)
      x-partition-key: tenant_id + aggregate.id
    EVT-SCF-RESOLVED-MANUALLY:
      name: EVT-SCF-RESOLVED-MANUALLY
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Reviewer notification
      - Sync delta (conflict notice to field user)
      x-partition-key: tenant_id + aggregate.id
```
