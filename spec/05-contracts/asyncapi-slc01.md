---
id: ASYNCAPI-SLC01
type: event-contract
title: AsyncAPI — SLC-01 Domain Events
wave: W6
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-01 Domain Events

_79 messages on 3 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-01 Domain Events
  version: 1.0.0
channels:
  foundation.events:
    address: '{cell}.foundation.events'
    messages:
      EVT-TEN-PROVISIONING-STARTED:
        $ref: '#/components/messages/EVT-TEN-PROVISIONING-STARTED'
      EVT-TEN-ACTIVATED:
        $ref: '#/components/messages/EVT-TEN-ACTIVATED'
      EVT-TEN-PROVISIONING-FAILED:
        $ref: '#/components/messages/EVT-TEN-PROVISIONING-FAILED'
      EVT-TEN-SUSPENDED:
        $ref: '#/components/messages/EVT-TEN-SUSPENDED'
      EVT-TEN-REACTIVATED:
        $ref: '#/components/messages/EVT-TEN-REACTIVATED'
      EVT-TEN-MIGRATION-STARTED:
        $ref: '#/components/messages/EVT-TEN-MIGRATION-STARTED'
      EVT-TEN-MIGRATED:
        $ref: '#/components/messages/EVT-TEN-MIGRATED'
      EVT-TEN-DECOMMISSION-STARTED:
        $ref: '#/components/messages/EVT-TEN-DECOMMISSION-STARTED'
      EVT-TEN-DECOMMISSIONED:
        $ref: '#/components/messages/EVT-TEN-DECOMMISSIONED'
      EVT-TEN-QUOTAS-UPDATED:
        $ref: '#/components/messages/EVT-TEN-QUOTAS-UPDATED'
      EVT-ORG-CREATED:
        $ref: '#/components/messages/EVT-ORG-CREATED'
      EVT-ORG-RENAMED:
        $ref: '#/components/messages/EVT-ORG-RENAMED'
      EVT-ORG-UNIT-ADDED:
        $ref: '#/components/messages/EVT-ORG-UNIT-ADDED'
      EVT-ORG-UNIT-RENAMED:
        $ref: '#/components/messages/EVT-ORG-UNIT-RENAMED'
      EVT-ORG-UNIT-MOVED:
        $ref: '#/components/messages/EVT-ORG-UNIT-MOVED'
      EVT-ORG-UNIT-DEACTIVATED:
        $ref: '#/components/messages/EVT-ORG-UNIT-DEACTIVATED'
      EVT-ORG-DEACTIVATED:
        $ref: '#/components/messages/EVT-ORG-DEACTIVATED'
      EVT-ORG-REACTIVATED:
        $ref: '#/components/messages/EVT-ORG-REACTIVATED'
      EVT-PER-REGISTERED:
        $ref: '#/components/messages/EVT-PER-REGISTERED'
      EVT-PER-DETAILS-UPDATED:
        $ref: '#/components/messages/EVT-PER-DETAILS-UPDATED'
      EVT-PER-DEACTIVATED:
        $ref: '#/components/messages/EVT-PER-DEACTIVATED'
      EVT-PER-REACTIVATED:
        $ref: '#/components/messages/EVT-PER-REACTIVATED'
      EVT-PER-ERASED:
        $ref: '#/components/messages/EVT-PER-ERASED'
      EVT-USR-PROVISIONED:
        $ref: '#/components/messages/EVT-USR-PROVISIONED'
      EVT-USR-IDENTITY-LINKED:
        $ref: '#/components/messages/EVT-USR-IDENTITY-LINKED'
      EVT-USR-IDENTITY-UNLINKED:
        $ref: '#/components/messages/EVT-USR-IDENTITY-UNLINKED'
      EVT-USR-PERSON-LINKED:
        $ref: '#/components/messages/EVT-USR-PERSON-LINKED'
      EVT-USR-ACTIVATED:
        $ref: '#/components/messages/EVT-USR-ACTIVATED'
      EVT-USR-LOCKED:
        $ref: '#/components/messages/EVT-USR-LOCKED'
      EVT-USR-UNLOCKED:
        $ref: '#/components/messages/EVT-USR-UNLOCKED'
      EVT-USR-DISABLED:
        $ref: '#/components/messages/EVT-USR-DISABLED'
      EVT-USR-ENABLED:
        $ref: '#/components/messages/EVT-USR-ENABLED'
      EVT-USR-CLOSED:
        $ref: '#/components/messages/EVT-USR-CLOSED'
      EVT-SVC-CREATED:
        $ref: '#/components/messages/EVT-SVC-CREATED'
      EVT-SVC-CREDENTIAL-ROTATED:
        $ref: '#/components/messages/EVT-SVC-CREDENTIAL-ROTATED'
      EVT-SVC-DISABLED:
        $ref: '#/components/messages/EVT-SVC-DISABLED'
      EVT-SVC-ENABLED:
        $ref: '#/components/messages/EVT-SVC-ENABLED'
      EVT-SVC-CLOSED:
        $ref: '#/components/messages/EVT-SVC-CLOSED'
      EVT-ROL-DEFINED:
        $ref: '#/components/messages/EVT-ROL-DEFINED'
      EVT-ROL-PERMISSIONS-CHANGED:
        $ref: '#/components/messages/EVT-ROL-PERMISSIONS-CHANGED'
      EVT-ROL-ACTIVATED:
        $ref: '#/components/messages/EVT-ROL-ACTIVATED'
      EVT-ROL-RETIRED:
        $ref: '#/components/messages/EVT-ROL-RETIRED'
      EVT-RAS-ASSIGNED:
        $ref: '#/components/messages/EVT-RAS-ASSIGNED'
      EVT-RAS-REVOKED:
        $ref: '#/components/messages/EVT-RAS-REVOKED'
      EVT-RAS-EXPIRED:
        $ref: '#/components/messages/EVT-RAS-EXPIRED'
      EVT-AUT-GRANT-REQUESTED:
        $ref: '#/components/messages/EVT-AUT-GRANT-REQUESTED'
      EVT-AUT-GRANTED:
        $ref: '#/components/messages/EVT-AUT-GRANTED'
      EVT-AUT-GRANT-REJECTED:
        $ref: '#/components/messages/EVT-AUT-GRANT-REJECTED'
      EVT-AUT-DELEGATED:
        $ref: '#/components/messages/EVT-AUT-DELEGATED'
      EVT-AUT-SUSPENDED:
        $ref: '#/components/messages/EVT-AUT-SUSPENDED'
      EVT-AUT-RESUMED:
        $ref: '#/components/messages/EVT-AUT-RESUMED'
      EVT-AUT-REVOKED:
        $ref: '#/components/messages/EVT-AUT-REVOKED'
      EVT-AUT-EXPIRED:
        $ref: '#/components/messages/EVT-AUT-EXPIRED'
      EVT-CLR-REQUESTED:
        $ref: '#/components/messages/EVT-CLR-REQUESTED'
      EVT-CLR-GRANTED:
        $ref: '#/components/messages/EVT-CLR-GRANTED'
      EVT-CLR-MODIFIED:
        $ref: '#/components/messages/EVT-CLR-MODIFIED'
      EVT-CLR-SUSPENDED:
        $ref: '#/components/messages/EVT-CLR-SUSPENDED'
      EVT-CLR-REINSTATED:
        $ref: '#/components/messages/EVT-CLR-REINSTATED'
      EVT-CLR-REVOKED:
        $ref: '#/components/messages/EVT-CLR-REVOKED'
      EVT-CLR-EXPIRED:
        $ref: '#/components/messages/EVT-CLR-EXPIRED'
    parameters:
      cell: {}
  governance.events:
    address: '{cell}.governance.events'
    messages:
      EVT-CLS-DRAFTED:
        $ref: '#/components/messages/EVT-CLS-DRAFTED'
      EVT-CLS-EDITED:
        $ref: '#/components/messages/EVT-CLS-EDITED'
      EVT-CLS-ACTIVATED:
        $ref: '#/components/messages/EVT-CLS-ACTIVATED'
      EVT-CLS-DISCARDED:
        $ref: '#/components/messages/EVT-CLS-DISCARDED'
      EVT-CLS-SUPERSEDED:
        $ref: '#/components/messages/EVT-CLS-SUPERSEDED'
      EVT-POL-DRAFTED:
        $ref: '#/components/messages/EVT-POL-DRAFTED'
      EVT-POL-EDITED:
        $ref: '#/components/messages/EVT-POL-EDITED'
      EVT-POL-SUBMITTED:
        $ref: '#/components/messages/EVT-POL-SUBMITTED'
      EVT-POL-APPROVED:
        $ref: '#/components/messages/EVT-POL-APPROVED'
      EVT-POL-REJECTED:
        $ref: '#/components/messages/EVT-POL-REJECTED'
      EVT-POL-ACTIVATED:
        $ref: '#/components/messages/EVT-POL-ACTIVATED'
      EVT-POL-SUPERSEDED:
        $ref: '#/components/messages/EVT-POL-SUPERSEDED'
      EVT-EXC-REQUESTED:
        $ref: '#/components/messages/EVT-EXC-REQUESTED'
      EVT-EXC-FIRST-APPROVED:
        $ref: '#/components/messages/EVT-EXC-FIRST-APPROVED'
      EVT-EXC-ACTIVATED:
        $ref: '#/components/messages/EVT-EXC-ACTIVATED'
      EVT-EXC-REJECTED:
        $ref: '#/components/messages/EVT-EXC-REJECTED'
      EVT-EXC-REVOKED:
        $ref: '#/components/messages/EVT-EXC-REVOKED'
      EVT-EXC-EXPIRED:
        $ref: '#/components/messages/EVT-EXC-EXPIRED'
    parameters:
      cell: {}
  security.versions:
    address: '{cell}.security.versions'
    messages:
      EVT-SEC-VERSION-INCREMENTED:
        $ref: '#/components/messages/EVT-SEC-VERSION-INCREMENTED'
    parameters:
      cell: {}
operations:
  publish_foundation:
    action: send
    channel:
      $ref: '#/channels/foundation.events'
  publish_governance:
    action: send
    channel:
      $ref: '#/channels/governance.events'
  publish_security:
    action: send
    channel:
      $ref: '#/channels/security.versions'
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
    EVT-TEN-PROVISIONING-STARTED:
      name: EVT-TEN-PROVISIONING-STARTED
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
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-ACTIVATED:
      name: EVT-TEN-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-PROVISIONING-FAILED:
      name: EVT-TEN-PROVISIONING-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-SUSPENDED:
      name: EVT-TEN-SUSPENDED
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
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-REACTIVATED:
      name: EVT-TEN-REACTIVATED
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
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-MIGRATION-STARTED:
      name: EVT-TEN-MIGRATION-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-MIGRATED:
      name: EVT-TEN-MIGRATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-DECOMMISSION-STARTED:
      name: EVT-TEN-DECOMMISSION-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-DECOMMISSIONED:
      name: EVT-TEN-DECOMMISSIONED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-TEN-QUOTAS-UPDATED:
      name: EVT-TEN-QUOTAS-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Provisioning saga / cell controller
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-CREATED:
      name: EVT-ORG-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-RENAMED:
      name: EVT-ORG-RENAMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-UNIT-ADDED:
      name: EVT-ORG-UNIT-ADDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-UNIT-RENAMED:
      name: EVT-ORG-UNIT-RENAMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-UNIT-MOVED:
      name: EVT-ORG-UNIT-MOVED
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
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-UNIT-DEACTIVATED:
      name: EVT-ORG-UNIT-DEACTIVATED
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
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-DEACTIVATED:
      name: EVT-ORG-DEACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-ORG-REACTIVATED:
      name: EVT-ORG-REACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - All contexts' org-scope read models
      x-partition-key: tenant_id + aggregate.id
    EVT-PER-REGISTERED:
      name: EVT-PER-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-PER-DETAILS-UPDATED:
      name: EVT-PER-DETAILS-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-PER-DEACTIVATED:
      name: EVT-PER-DEACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-PER-REACTIVATED:
      name: EVT-PER-REACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-PER-ERASED:
      name: EVT-PER-ERASED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-PROVISIONED:
      name: EVT-USR-PROVISIONED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-IDENTITY-LINKED:
      name: EVT-USR-IDENTITY-LINKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-IDENTITY-UNLINKED:
      name: EVT-USR-IDENTITY-UNLINKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-PERSON-LINKED:
      name: EVT-USR-PERSON-LINKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-ACTIVATED:
      name: EVT-USR-ACTIVATED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-LOCKED:
      name: EVT-USR-LOCKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-UNLOCKED:
      name: EVT-USR-UNLOCKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-DISABLED:
      name: EVT-USR-DISABLED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-ENABLED:
      name: EVT-USR-ENABLED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-USR-CLOSED:
      name: EVT-USR-CLOSED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SVC-CREATED:
      name: EVT-SVC-CREATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SVC-CREDENTIAL-ROTATED:
      name: EVT-SVC-CREDENTIAL-ROTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SVC-DISABLED:
      name: EVT-SVC-DISABLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SVC-ENABLED:
      name: EVT-SVC-ENABLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SVC-CLOSED:
      name: EVT-SVC-CLOSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-ROL-DEFINED:
      name: EVT-ROL-DEFINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-ROL-PERMISSIONS-CHANGED:
      name: EVT-ROL-PERMISSIONS-CHANGED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-ROL-ACTIVATED:
      name: EVT-ROL-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-ROL-RETIRED:
      name: EVT-ROL-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-RAS-ASSIGNED:
      name: EVT-RAS-ASSIGNED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-RAS-REVOKED:
      name: EVT-RAS-REVOKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-RAS-EXPIRED:
      name: EVT-RAS-EXPIRED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-GRANT-REQUESTED:
      name: EVT-AUT-GRANT-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-GRANTED:
      name: EVT-AUT-GRANTED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-GRANT-REJECTED:
      name: EVT-AUT-GRANT-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-DELEGATED:
      name: EVT-AUT-DELEGATED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-SUSPENDED:
      name: EVT-AUT-SUSPENDED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-RESUMED:
      name: EVT-AUT-RESUMED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-REVOKED:
      name: EVT-AUT-REVOKED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-AUT-EXPIRED:
      name: EVT-AUT-EXPIRED
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
      - Search/Directory projection (BC01 read model)
      - Notification (delegates informed on revoke/expire)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-REQUESTED:
      name: EVT-CLR-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-GRANTED:
      name: EVT-CLR-GRANTED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-MODIFIED:
      name: EVT-CLR-MODIFIED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-SUSPENDED:
      name: EVT-CLR-SUSPENDED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-REINSTATED:
      name: EVT-CLR-REINSTATED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-REVOKED:
      name: EVT-CLR-REVOKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLR-EXPIRED:
      name: EVT-CLR-EXPIRED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLS-DRAFTED:
      name: EVT-CLS-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-CLS-EDITED:
      name: EVT-CLS-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-CLS-ACTIVATED:
      name: EVT-CLS-ACTIVATED
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
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-CLS-DISCARDED:
      name: EVT-CLS-DISCARDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-CLS-SUPERSEDED:
      name: EVT-CLS-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-DRAFTED:
      name: EVT-POL-DRAFTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-EDITED:
      name: EVT-POL-EDITED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-SUBMITTED:
      name: EVT-POL-SUBMITTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-APPROVED:
      name: EVT-POL-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-REJECTED:
      name: EVT-POL-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-ACTIVATED:
      name: EVT-POL-ACTIVATED
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
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-POL-SUPERSEDED:
      name: EVT-POL-SUPERSEDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      - PDP bundle distributor
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-REQUESTED:
      name: EVT-EXC-REQUESTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-FIRST-APPROVED:
      name: EVT-EXC-FIRST-APPROVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-ACTIVATED:
      name: EVT-EXC-ACTIVATED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-REJECTED:
      name: EVT-EXC-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-REVOKED:
      name: EVT-EXC-REVOKED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-EXC-EXPIRED:
      name: EVT-EXC-EXPIRED
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
      - Search/Directory projection (BC01 read model)
      x-partition-key: tenant_id + aggregate.id
    EVT-SEC-VERSION-INCREMENTED:
      name: EVT-SEC-VERSION-INCREMENTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload:
              type: object
              required:
              - subject_urn
              - security_version
              - cause_event_id
              properties:
                subject_urn:
                  type: string
                security_version:
                  type: integer
                cause_event_id:
                  type: string
      x-consumers:
      - All PEPs
      - Projection security-version tables
      - SecurityContext cache
      x-partition-key: tenant_id + subject_urn
```
