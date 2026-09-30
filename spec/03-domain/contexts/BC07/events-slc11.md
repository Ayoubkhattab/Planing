---
id: EVT-CAT-BC07-SLC11
type: event-catalog
title: Domain Events — BC07 (SLC-11)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC07 (SLC-11)

_17 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-PKG-REQUESTED | AGG-PRELOAD-PACKAGE | CMD-PKG-REQUEST | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-PKG-BUILDING | AGG-PRELOAD-PACKAGE | SYS:build started | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-PKG-READY | AGG-PRELOAD-PACKAGE | SYS:build finished | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-PKG-DOWNLOADED | AGG-PRELOAD-PACKAGE | CMD-PKG-CONFIRM-DOWNLOAD | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-PKG-EXPIRED | AGG-PRELOAD-PACKAGE | SYS:expires_at reached | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-PKG-REVOKED | AGG-PRELOAD-PACKAGE | SYS:user security_version changed or device not ACTIVE, CMD-PKG-REVOKE | — | Package builder; Sync delta (purge list) | tenant_id + aggregate.id |
| EVT-SYN-OPENED | AGG-SYNC-SESSION | CMD-SYN-OPEN | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SYN-REJECTED | AGG-SYNC-SESSION | SYS:device LOST or SUSPENDED at handshake | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SYN-BATCH-RECEIVED | AGG-SYNC-SESSION | CMD-SYN-UPLOAD-BATCH | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SYN-COMPLETED | AGG-SYNC-SESSION | SYS:all uploaded commands processed without conflict | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SYN-COMPLETED-WITH-CONFLICTS | AGG-SYNC-SESSION | SYS:all processed with ≥ 1 sync conflict | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SYN-FAILED | AGG-SYNC-SESSION | SYS:idle timeout (5 min) or transport loss | — | Owner contexts (commands applied via their APIs); Field telemetry | tenant_id + aggregate.id |
| EVT-SCF-OPENED | AGG-SYNC-CONFLICT | SYS:stale state-changing command | — | Reviewer notification; Sync delta (conflict notice to field user) | tenant_id + aggregate.id |
| EVT-SCF-ASSIGNED | AGG-SYNC-CONFLICT | CMD-SCF-ASSIGN | — | Reviewer notification; Sync delta (conflict notice to field user) | tenant_id + aggregate.id |
| EVT-SCF-REAPPLIED | AGG-SYNC-CONFLICT | CMD-SCF-REAPPLY | — | Reviewer notification; Sync delta (conflict notice to field user) | tenant_id + aggregate.id |
| EVT-SCF-DISCARDED | AGG-SYNC-CONFLICT | CMD-SCF-DISCARD | — | Reviewer notification; Sync delta (conflict notice to field user) | tenant_id + aggregate.id |
| EVT-SCF-RESOLVED-MANUALLY | AGG-SYNC-CONFLICT | CMD-SCF-RESOLVE-MANUALLY | — | Reviewer notification; Sync delta (conflict notice to field user) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
