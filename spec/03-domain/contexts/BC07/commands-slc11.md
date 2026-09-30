---
id: CMD-CAT-BC07-SLC11
type: command-catalog
title: Commands — BC07 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Commands — BC07 (SLC-11)

_9 commands_

| الأمر | Aggregate | HTTP | داخلي | الفاعل | السياسة | الحمولة (! إلزامي) | الأحداث | الأخطاء |
|---|---|---|---|---|---|---|---|---|
| CMD-PKG-REQUEST | AGG-PRELOAD-PACKAGE | `POST /api/v1/field/preload-packages` | لا | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-REQUEST | `device!:urn area!:object layers!:array window!:Interval level!:string` | EVT-PKG-REQUESTED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRELOAD_NOT_ALLOWED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PKG-CONFIRM-DOWNLOAD | AGG-PRELOAD-PACKAGE | `POST /api/v1/field/preload-packages/{id}/actions/confirm-download` | لا | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-CONFIRM-DOWNLOAD | `manifest_sha256!:string` | EVT-PKG-DOWNLOADED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, MANIFEST_MISMATCH, PRELOAD_PACKAGE_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-PKG-REVOKE | AGG-PRELOAD-PACKAGE | `POST /api/v1/field/preload-packages/{id}/actions/revoke` | لا | field user (request, confirm download, revoke) · Administrator / Security Officer (revoke) | POL-PKG-REVOKE | `reason!:string` | EVT-PKG-REVOKED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, PRELOAD_PACKAGE_INVALID_STATE_TRANSITION, REASON_REQUIRED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SYN-OPEN | AGG-SYNC-SESSION | `POST /api/v1/field/sync-sessions` | لا | field device + user (open, upload) | POL-SYN-OPEN | `device!:urn device_time!:date-time last_acked_seq!:integer queue_length!:integer queue_head_hash!:string signature!:string` | EVT-SYN-OPENED | AUTHZ_DENIED, DEVICE_NOT_ACTIVE, IDEMPOTENCY_KEY_REUSED, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SYN-UPLOAD-BATCH | AGG-SYNC-SESSION | `POST /api/v1/field/sync-sessions/{id}/actions/upload-batch` | لا | field device + user (open, upload) | POL-SYN-UPLOAD-BATCH | `envelopes!:array end_of_queue!:boolean` | EVT-SYN-BATCH-RECEIVED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, SEQUENCE_GAP, SYNC_SESSION_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCF-ASSIGN | AGG-SYNC-CONFLICT | `POST /api/v1/field/sync-conflicts/{id}/actions/assign` | لا | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-ASSIGN | `reviewer!:urn` | EVT-SCF-ASSIGNED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REVIEWER_NOT_AUTHORIZED, SYNC_CONFLICT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCF-REAPPLY | AGG-SYNC-CONFLICT | `POST /api/v1/field/sync-conflicts/{id}/actions/reapply` | لا | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-REAPPLY | `note:string` | EVT-SCF-REAPPLIED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, OWNER_REJECTED, SYNC_CONFLICT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCF-DISCARD | AGG-SYNC-CONFLICT | `POST /api/v1/field/sync-conflicts/{id}/actions/discard` | لا | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-DISCARD | `reason!:string` | EVT-SCF-DISCARDED | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SYNC_CONFLICT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |
| CMD-SCF-RESOLVE-MANUALLY | AGG-SYNC-CONFLICT | `POST /api/v1/field/sync-conflicts/{id}/actions/resolve-manually` | لا | reviewer: task owner/Planner, Analyst for observations (assign, reapply, discard, resolve) | POL-SCF-RESOLVE-MANUALLY | `note!:string action_ref:urn` | EVT-SCF-RESOLVED-MANUALLY | AUTHZ_DENIED, IDEMPOTENCY_KEY_REUSED, REASON_REQUIRED, SYNC_CONFLICT_INVALID_STATE_TRANSITION, VALIDATION_FAILED, VERSION_CONFLICT |

**مشترك لكل الأوامر:** `Idempotency-Key` إلزامي؛ `If-Match` إلزامي لغير أوامر الإنشاء؛ `X-Purpose` و`X-Correlation-Id` إلزاميان؛ الاستجابة `202` مع `ResourceRef {urn, id, version, state}` أو `201` للإنشاء.

---

<details>
<summary>Machine-readable data (YAML)</summary>

```yaml
commands:
- id: CMD-PKG-REQUEST
  aggregate: AGG-PRELOAD-PACKAGE
  bc: BC07
  transitions:
  - from:
    - ∅
    to: REQUESTED
    guard: device ACTIVE; area polygon ≤ tenant max area; layers; time window; requested
      level ≤ tenant offline max level (default INTERNAL, POL-OFFLINE-PRELOAD)
    event: EVT-PKG-REQUESTED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRELOAD_NOT_ALLOWED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/field/preload-packages
  internal: false
  policy: POL-PKG-REQUEST
  actors: field user (request, confirm download, revoke) · Administrator / Security
    Officer (revoke)
  payload: device!:urn area!:object layers!:array window!:Interval level!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-PKG-CONFIRM-DOWNLOAD
  aggregate: AGG-PRELOAD-PACKAGE
  bc: BC07
  transitions:
  - from:
    - READY
    to: DOWNLOADED
    guard: device acknowledges manifest hash
    event: EVT-PKG-DOWNLOADED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - MANIFEST_MISMATCH
  - PRELOAD_PACKAGE_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/preload-packages/{id}/actions/confirm-download
  internal: false
  policy: POL-PKG-CONFIRM-DOWNLOAD
  actors: field user (request, confirm download, revoke) · Administrator / Security
    Officer (revoke)
  payload: manifest_sha256!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-PKG-REVOKE
  aggregate: AGG-PRELOAD-PACKAGE
  bc: BC07
  transitions:
  - from:
    - REQUESTED
    - BUILDING
    - READY
    - DOWNLOADED
    to: REVOKED
    guard: user, Administrator or Security Officer; reason
    event: EVT-PKG-REVOKED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - PRELOAD_PACKAGE_INVALID_STATE_TRANSITION
  - REASON_REQUIRED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/preload-packages/{id}/actions/revoke
  internal: false
  policy: POL-PKG-REVOKE
  actors: field user (request, confirm download, revoke) · Administrator / Security
    Officer (revoke)
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SYN-OPEN
  aggregate: AGG-SYNC-SESSION
  bc: BC07
  transitions:
  - from:
    - ∅
    to: OPEN
    guard: device ACTIVE; user authenticated (fresh token); device signature on handshake;
      clock offset measured (server − device); resumes after last acknowledged seq
    event: EVT-SYN-OPENED
  errors:
  - AUTHZ_DENIED
  - DEVICE_NOT_ACTIVE
  - IDEMPOTENCY_KEY_REUSED
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: true
  http:
  - POST
  - /api/v1/field/sync-sessions
  internal: false
  policy: POL-SYN-OPEN
  actors: field device + user (open, upload)
  payload: device!:urn device_time!:date-time last_acked_seq!:integer queue_length!:integer
    queue_head_hash!:string signature!:string
  offline_capable: false
  idempotency_key: required
  expected_version: not applicable (creation)
- id: CMD-SYN-UPLOAD-BATCH
  aggregate: AGG-SYNC-SESSION
  bc: BC07
  transitions:
  - from:
    - OPEN
    - APPLYING
    to: APPLYING
    guard: ≤ 200 commands; contiguous seq after last acknowledged; each envelope signed
      by device key; batch hash chain continues
    event: EVT-SYN-BATCH-RECEIVED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - SEQUENCE_GAP
  - SYNC_SESSION_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/sync-sessions/{id}/actions/upload-batch
  internal: false
  policy: POL-SYN-UPLOAD-BATCH
  actors: field device + user (open, upload)
  payload: envelopes!:array end_of_queue!:boolean
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCF-ASSIGN
  aggregate: AGG-SYNC-CONFLICT
  bc: BC07
  transitions:
  - from:
    - OPEN
    to: '='
    guard: assignee authorized on the target
    event: EVT-SCF-ASSIGNED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REVIEWER_NOT_AUTHORIZED
  - SYNC_CONFLICT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/sync-conflicts/{id}/actions/assign
  internal: false
  policy: POL-SCF-ASSIGN
  actors: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply,
    discard, resolve)'
  payload: reviewer!:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCF-REAPPLY
  aggregate: AGG-SYNC-CONFLICT
  bc: BC07
  transitions:
  - from:
    - OPEN
    to: RESOLVED_APPLIED
    guard: reviewer re-sends the original intent against the current version; owner-context
      accepts (its guards still apply)
    event: EVT-SCF-REAPPLIED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - OWNER_REJECTED
  - SYNC_CONFLICT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/sync-conflicts/{id}/actions/reapply
  internal: false
  policy: POL-SCF-REAPPLY
  actors: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply,
    discard, resolve)'
  payload: note:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCF-DISCARD
  aggregate: AGG-SYNC-CONFLICT
  bc: BC07
  transitions:
  - from:
    - OPEN
    to: RESOLVED_DISCARDED
    guard: reason; field user notified
    event: EVT-SCF-DISCARDED
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SYNC_CONFLICT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/sync-conflicts/{id}/actions/discard
  internal: false
  policy: POL-SCF-DISCARD
  actors: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply,
    discard, resolve)'
  payload: reason!:string
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
- id: CMD-SCF-RESOLVE-MANUALLY
  aggregate: AGG-SYNC-CONFLICT
  bc: BC07
  transitions:
  - from:
    - OPEN
    to: RESOLVED_MANUAL
    guard: note + reference to the alternative action taken
    event: EVT-SCF-RESOLVED-MANUALLY
  errors:
  - AUTHZ_DENIED
  - IDEMPOTENCY_KEY_REUSED
  - REASON_REQUIRED
  - SYNC_CONFLICT_INVALID_STATE_TRANSITION
  - VALIDATION_FAILED
  - VERSION_CONFLICT
  creates: false
  http:
  - POST
  - /api/v1/field/sync-conflicts/{id}/actions/resolve-manually
  internal: false
  policy: POL-SCF-RESOLVE-MANUALLY
  actors: 'reviewer: task owner/Planner, Analyst for observations (assign, reapply,
    discard, resolve)'
  payload: note!:string action_ref:urn
  offline_capable: false
  idempotency_key: required
  expected_version: required (If-Match)
```

</details>
