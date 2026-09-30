---
id: LDM-SLC11
type: logical-data-model
title: Logical Data Model — SLC-11
wave: W6
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Logical Data Model — SLC-11

## BC01 — foundation
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| devices | (tenant_id, device_id) | user_id, platform, mdm_ref, state, lost_at?, version | ≤ 3 ACTIVE per user |
| device_keys | (tenant_id, device_id, key_id) | public_key, valid_from, revoked_at? | one current key |

## BC07 — field (server)
| الجدول | المفتاح | أعمدة | قيود |
|---|---|---|---|
| preload_packages | (tenant_id, package_id) | device_id, user_id, area(json), layers[], window, level, manifest(json), security_version, expires_at, state | — |
| sync_sessions | (tenant_id, session_id) | device_id, user_id, clock_offset_ms, opened_at, acked_seq, state | — |
| device_cursors | (tenant_id, device_id) | last_acked_seq, last_hash | resume point |
| applied_commands | (tenant_id, client_command_id) | device_id, seq, target_command, result (applied / conflict / rejected), applied_at | idempotency; retained ≥ 30 d |
| sync_conflicts | (tenant_id, conflict_id) | envelope(json), state_snapshot(json), owner_reason, reviewer?, state, version | — |

## Device (client) — logical, encrypted
| المخزن | المحتوى |
|---|---|
| command_queue | envelopes by seq with prev_hash chain |
| packages | preload content by manifest, encrypted per package key; purged at expiry/revocation |
| outbox_attachments | encrypted blobs awaiting upload |
| my_tasks | last delta snapshot |
