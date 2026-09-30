---
id: ADR-P02
type: adr
title: Persistence Style
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- WL-04
corrects:
- CR-16
verified_by:
- QAS-REL-001
- FIT-04
---

# ADR-P02: Persistence Style

## Context and Problem
PRJ§70 يعرّف task_history وtask_events وoutbox معاً دون تحديد المرجع لإعادة البناء التاريخي.

## Considered Options
1. State + History + Outbox
2. Event Sourcing
3. مختلط حسب الـ Aggregate

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1 افتراضياً؛ history هو مرجع الإعادة، والأحداث للتكامل.

## Decision Outcome
**State-stored + append-only history + transactional outbox. No event sourcing.**
- Source of truth for history: bitemporal claim records (T1) and immutable version records (T2).
- Domain events are published via outbox for integration and projections; they are **not** the source of truth and may be pruned by retention.
- The separate `task_events` table in PRJ§70 is dropped (CR-16); `task_history` is the authoritative history.

## Rationale
Simplest model satisfying ADR-P01 and outbox reliability; avoids event-sourcing complexity for a small team (ASM-008).

## Consequences
- ✅ One authoritative history per aggregate
- ✅ Projections rebuildable from source of truth
- ⚠️ Event replay alone cannot rebuild state (by design)

## Impact
- **operations:** lower complexity
- **reliability:** outbox guarantees at-least-once

## Verified By
QAS-REL-001, FIT-04

## Previously Blocked By
WL-04
