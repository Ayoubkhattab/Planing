---
id: ADR-P09
type: adr
title: Field Synchronization
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-009
corrects:
- CR-13
verified_by:
- QAS-OFF-001
---

# ADR-P09: Field Synchronization

## Context and Problem
PRJ§110 يختبر المزامنة دون تصميم لها.

## Considered Options
1. إرسال الأوامر المسجلة وإعادة تطبيقها مع Conflict Engine
2. CRDT لأنواع محددة
3. نسخ قراءة فقط

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1 + 2 لأنواع محدودة؛ LWW ممنوع لـ T1/T2.

## W1 Input (delegated answers)
Q9 → الخيار 1 + 2 — يُعتمد رسمياً في W3.

## Decision Outcome
**Command queue on device; server-side replay with conflict routing.**
- Each offline command carries `client_command_id` (idempotency), `base_version`, `device_time`, `device_id`, `clock_offset` (measured at sync handshake).
- Append-only commands (new observation, new attachment) never conflict.
- State-changing commands apply only if `base_version` = current; otherwise a conflict case is opened (BC02 conflict model) — no last-write-wins for T1/T2.
- LWW is allowed only for T4 data (UI preferences).

## Rationale
W1 Q9; consistent with no silent overwrite.

## Consequences
- ✅ Deterministic, auditable sync
- ✅ Idempotent resume
- ⚠️ Field users may see 'pending review' on some updates

## Impact
- **usability:** conflict UX needed in SLC-11

## Verified By
QAS-OFF-001

## Previously Blocked By
UNK-009
