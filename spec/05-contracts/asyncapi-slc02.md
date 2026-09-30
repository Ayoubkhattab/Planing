---
id: ASYNCAPI-SLC02
type: event-contract
title: AsyncAPI — SLC-02 Domain Events
wave: W6
slice: SLC-02
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
format: AsyncAPI 3.0
---

# AsyncAPI — SLC-02 Domain Events

_64 messages on 2 channels. Envelope = PRJ§14 EventEnvelope + security labels. Delivery at-least-once via outbox; consumers idempotent via inbox._

```yaml
asyncapi: 3.0.0
info:
  title: SLC-02 Domain Events
  version: 1.0.0
channels:
  information.events:
    address: '{cell}.information.events'
    messages:
      EVT-SRC-REGISTERED:
        $ref: '#/components/messages/EVT-SRC-REGISTERED'
      EVT-SRC-RELIABILITY-RATED:
        $ref: '#/components/messages/EVT-SRC-RELIABILITY-RATED'
      EVT-SRC-PROFILE-UPDATED:
        $ref: '#/components/messages/EVT-SRC-PROFILE-UPDATED'
      EVT-SRC-PROTECTION-CHANGED:
        $ref: '#/components/messages/EVT-SRC-PROTECTION-CHANGED'
      EVT-SRC-RECLASSIFIED:
        $ref: '#/components/messages/EVT-SRC-RECLASSIFIED'
      EVT-SRC-SUSPENDED:
        $ref: '#/components/messages/EVT-SRC-SUSPENDED'
      EVT-SRC-REINSTATED:
        $ref: '#/components/messages/EVT-SRC-REINSTATED'
      EVT-SRC-RETIRED:
        $ref: '#/components/messages/EVT-SRC-RETIRED'
      EVT-OBS-RECORDED:
        $ref: '#/components/messages/EVT-OBS-RECORDED'
      EVT-OBS-AMENDED:
        $ref: '#/components/messages/EVT-OBS-AMENDED'
      EVT-OBS-EVIDENCE-ATTACHED:
        $ref: '#/components/messages/EVT-OBS-EVIDENCE-ATTACHED'
      EVT-OBS-RECLASSIFIED:
        $ref: '#/components/messages/EVT-OBS-RECLASSIFIED'
      EVT-OBS-VALIDATED:
        $ref: '#/components/messages/EVT-OBS-VALIDATED'
      EVT-OBS-REJECTED:
        $ref: '#/components/messages/EVT-OBS-REJECTED'
      EVT-ENT-REGISTERED:
        $ref: '#/components/messages/EVT-ENT-REGISTERED'
      EVT-ENT-TYPE-CHANGED:
        $ref: '#/components/messages/EVT-ENT-TYPE-CHANGED'
      EVT-ENT-RECLASSIFIED:
        $ref: '#/components/messages/EVT-ENT-RECLASSIFIED'
      EVT-ENT-RETIRED:
        $ref: '#/components/messages/EVT-ENT-RETIRED'
      EVT-ENT-REINSTATED:
        $ref: '#/components/messages/EVT-ENT-REINSTATED'
      EVT-RWE-REGISTERED:
        $ref: '#/components/messages/EVT-RWE-REGISTERED'
      EVT-RWE-TYPE-CHANGED:
        $ref: '#/components/messages/EVT-RWE-TYPE-CHANGED'
      EVT-RWE-RECLASSIFIED:
        $ref: '#/components/messages/EVT-RWE-RECLASSIFIED'
      EVT-RWE-RETIRED:
        $ref: '#/components/messages/EVT-RWE-RETIRED'
      EVT-RWE-REINSTATED:
        $ref: '#/components/messages/EVT-RWE-REINSTATED'
      EVT-REL-REGISTERED:
        $ref: '#/components/messages/EVT-REL-REGISTERED'
      EVT-REL-RECLASSIFIED:
        $ref: '#/components/messages/EVT-REL-RECLASSIFIED'
      EVT-REL-RETIRED:
        $ref: '#/components/messages/EVT-REL-RETIRED'
      EVT-REL-REINSTATED:
        $ref: '#/components/messages/EVT-REL-REINSTATED'
      EVT-CLM-ASSERTED:
        $ref: '#/components/messages/EVT-CLM-ASSERTED'
      EVT-CLM-CORRECTED:
        $ref: '#/components/messages/EVT-CLM-CORRECTED'
      EVT-CLM-CHANGED:
        $ref: '#/components/messages/EVT-CLM-CHANGED'
      EVT-CLM-RETRACTED:
        $ref: '#/components/messages/EVT-CLM-RETRACTED'
      EVT-CLM-ASSESSED:
        $ref: '#/components/messages/EVT-CLM-ASSESSED'
      EVT-CLM-RECLASSIFIED:
        $ref: '#/components/messages/EVT-CLM-RECLASSIFIED'
      EVT-EVD-REGISTERED:
        $ref: '#/components/messages/EVT-EVD-REGISTERED'
      EVT-EVD-LOCATOR-UPDATED:
        $ref: '#/components/messages/EVT-EVD-LOCATOR-UPDATED'
      EVT-EVD-SEALED:
        $ref: '#/components/messages/EVT-EVD-SEALED'
      EVT-EVD-CUSTODY-TRANSFERRED:
        $ref: '#/components/messages/EVT-EVD-CUSTODY-TRANSFERRED'
      EVT-EVD-RECLASSIFIED:
        $ref: '#/components/messages/EVT-EVD-RECLASSIFIED'
      EVT-EVD-WITHDRAWN:
        $ref: '#/components/messages/EVT-EVD-WITHDRAWN'
      EVT-EVL-LINKED:
        $ref: '#/components/messages/EVT-EVL-LINKED'
      EVT-EVL-UNLINKED:
        $ref: '#/components/messages/EVT-EVL-UNLINKED'
      EVT-ATT-UPLOAD-INITIATED:
        $ref: '#/components/messages/EVT-ATT-UPLOAD-INITIATED'
      EVT-ATT-UPLOADED:
        $ref: '#/components/messages/EVT-ATT-UPLOADED'
      EVT-ATT-STORED:
        $ref: '#/components/messages/EVT-ATT-STORED'
      EVT-ATT-QUARANTINED:
        $ref: '#/components/messages/EVT-ATT-QUARANTINED'
      EVT-ATT-EXPIRED:
        $ref: '#/components/messages/EVT-ATT-EXPIRED'
      EVT-ATT-ERASED:
        $ref: '#/components/messages/EVT-ATT-ERASED'
      EVT-IMP-RECEIVED:
        $ref: '#/components/messages/EVT-IMP-RECEIVED'
      EVT-IMP-PROCESSING-STARTED:
        $ref: '#/components/messages/EVT-IMP-PROCESSING-STARTED'
      EVT-IMP-COMPLETED:
        $ref: '#/components/messages/EVT-IMP-COMPLETED'
      EVT-IMP-COMPLETED-WITH-QUARANTINE:
        $ref: '#/components/messages/EVT-IMP-COMPLETED-WITH-QUARANTINE'
      EVT-IMP-FAILED:
        $ref: '#/components/messages/EVT-IMP-FAILED'
      EVT-IMP-REPROCESSING:
        $ref: '#/components/messages/EVT-IMP-REPROCESSING'
      EVT-IMP-QUARANTINE-ACCEPTED:
        $ref: '#/components/messages/EVT-IMP-QUARANTINE-ACCEPTED'
      EVT-IMP-CANCELLED:
        $ref: '#/components/messages/EVT-IMP-CANCELLED'
      EVT-EXT-MAPPED:
        $ref: '#/components/messages/EVT-EXT-MAPPED'
      EVT-EXT-ENDED:
        $ref: '#/components/messages/EVT-EXT-ENDED'
    parameters:
      cell: {}
  integration.events:
    address: '{cell}.integration.events'
    messages:
      EVT-ADP-REGISTERED:
        $ref: '#/components/messages/EVT-ADP-REGISTERED'
      EVT-ADP-MAPPING-UPDATED:
        $ref: '#/components/messages/EVT-ADP-MAPPING-UPDATED'
      EVT-ADP-ACTIVATED:
        $ref: '#/components/messages/EVT-ADP-ACTIVATED'
      EVT-ADP-SUSPENDED:
        $ref: '#/components/messages/EVT-ADP-SUSPENDED'
      EVT-ADP-RESUMED:
        $ref: '#/components/messages/EVT-ADP-RESUMED'
      EVT-ADP-RETIRED:
        $ref: '#/components/messages/EVT-ADP-RETIRED'
    parameters:
      cell: {}
operations:
  publish_information:
    action: send
    channel:
      $ref: '#/channels/information.events'
  publish_integration:
    action: send
    channel:
      $ref: '#/channels/integration.events'
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
    EVT-SRC-REGISTERED:
      name: EVT-SRC-REGISTERED
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
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-RELIABILITY-RATED:
      name: EVT-SRC-RELIABILITY-RATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-PROFILE-UPDATED:
      name: EVT-SRC-PROFILE-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-PROTECTION-CHANGED:
      name: EVT-SRC-PROTECTION-CHANGED
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
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-RECLASSIFIED:
      name: EVT-SRC-RECLASSIFIED
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
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-SUSPENDED:
      name: EVT-SRC-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-REINSTATED:
      name: EVT-SRC-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-SRC-RETIRED:
      name: EVT-SRC-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-RECORDED:
      name: EVT-OBS-RECORDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-AMENDED:
      name: EVT-OBS-AMENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-EVIDENCE-ATTACHED:
      name: EVT-OBS-EVIDENCE-ATTACHED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-RECLASSIFIED:
      name: EVT-OBS-RECLASSIFIED
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
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-VALIDATED:
      name: EVT-OBS-VALIDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-OBS-REJECTED:
      name: EVT-OBS-REJECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Derived-claim processor (position summarization)
      - Situation membership (SLC-06)
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ENT-REGISTERED:
      name: EVT-ENT-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - ER candidate generator (SLC-04)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ENT-TYPE-CHANGED:
      name: EVT-ENT-TYPE-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - ER candidate generator (SLC-04)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ENT-RECLASSIFIED:
      name: EVT-ENT-RECLASSIFIED
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
      - ER candidate generator (SLC-04)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ENT-RETIRED:
      name: EVT-ENT-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - ER candidate generator (SLC-04)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ENT-REINSTATED:
      name: EVT-ENT-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - ER candidate generator (SLC-04)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-RWE-REGISTERED:
      name: EVT-RWE-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-RWE-TYPE-CHANGED:
      name: EVT-RWE-TYPE-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-RWE-RECLASSIFIED:
      name: EVT-RWE-RECLASSIFIED
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
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-RWE-RETIRED:
      name: EVT-RWE-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-RWE-REINSTATED:
      name: EVT-RWE-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-REL-REGISTERED:
      name: EVT-REL-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-REL-RECLASSIFIED:
      name: EVT-REL-RECLASSIFIED
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
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-REL-RETIRED:
      name: EVT-REL-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-REL-REINSTATED:
      name: EVT-REL-REINSTATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-ASSERTED:
      name: EVT-CLM-ASSERTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-CORRECTED:
      name: EVT-CLM-CORRECTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-CHANGED:
      name: EVT-CLM-CHANGED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-RETRACTED:
      name: EVT-CLM-RETRACTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-ASSESSED:
      name: EVT-CLM-ASSESSED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-CLM-RECLASSIFIED:
      name: EVT-CLM-RECLASSIFIED
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
      - Current-view maintainer (async materialized resolved views)
      - Conflict detector (SLC-04)
      - Situation membership (SLC-06)
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-REGISTERED:
      name: EVT-EVD-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-LOCATOR-UPDATED:
      name: EVT-EVD-LOCATOR-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-SEALED:
      name: EVT-EVD-SEALED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-CUSTODY-TRANSFERRED:
      name: EVT-EVD-CUSTODY-TRANSFERRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-RECLASSIFIED:
      name: EVT-EVD-RECLASSIFIED
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
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVD-WITHDRAWN:
      name: EVT-EVD-WITHDRAWN
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - 'Verification re-evaluator (on WITHDRAWN: issues CMD-CLM-ASSESS as system
        identity for linked claims, recomputing verification from remaining SUPPORTS
        links)'
      - Search projection (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVL-LINKED:
      name: EVT-EVL-LINKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-EVL-UNLINKED:
      name: EVT-EVL-UNLINKED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Search/Graph projections (SLC-05)
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-UPLOAD-INITIATED:
      name: EVT-ATT-UPLOAD-INITIATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-UPLOADED:
      name: EVT-ATT-UPLOADED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-STORED:
      name: EVT-ATT-STORED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-QUARANTINED:
      name: EVT-ATT-QUARANTINED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-EXPIRED:
      name: EVT-ATT-EXPIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-ATT-ERASED:
      name: EVT-ATT-ERASED
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
      - Content scanner
      - Evidence registrar
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-RECEIVED:
      name: EVT-IMP-RECEIVED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-PROCESSING-STARTED:
      name: EVT-IMP-PROCESSING-STARTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-COMPLETED:
      name: EVT-IMP-COMPLETED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-COMPLETED-WITH-QUARANTINE:
      name: EVT-IMP-COMPLETED-WITH-QUARANTINE
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-FAILED:
      name: EVT-IMP-FAILED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-REPROCESSING:
      name: EVT-IMP-REPROCESSING
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-QUARANTINE-ACCEPTED:
      name: EVT-IMP-QUARANTINE-ACCEPTED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-IMP-CANCELLED:
      name: EVT-IMP-CANCELLED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      - Adapter owner notification
      x-partition-key: tenant_id + aggregate.id
    EVT-EXT-MAPPED:
      name: EVT-EXT-MAPPED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker cache
      x-partition-key: tenant_id + aggregate.id
    EVT-EXT-ENDED:
      name: EVT-EXT-ENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker cache
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-REGISTERED:
      name: EVT-ADP-REGISTERED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-MAPPING-UPDATED:
      name: EVT-ADP-MAPPING-UPDATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-ACTIVATED:
      name: EVT-ADP-ACTIVATED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-SUSPENDED:
      name: EVT-ADP-SUSPENDED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-RESUMED:
      name: EVT-ADP-RESUMED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
    EVT-ADP-RETIRED:
      name: EVT-ADP-RETIRED
      contentType: application/json
      payload:
        allOf:
        - $ref: '#/components/schemas/EventEnvelope'
        - type: object
          properties:
            payload: *id001
      x-consumers:
      - Import worker
      x-partition-key: tenant_id + aggregate.id
```
