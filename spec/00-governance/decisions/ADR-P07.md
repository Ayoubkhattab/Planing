---
id: ADR-P07
type: adr
title: Nature of Situation
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by: []
corrects:
- CR-05
verified_by:
- QAS-PERF-006
---

# ADR-P07: Nature of Situation

## Context and Problem
PRJ§60 يصف Situation كـ View، بينما لها أوامر (UC-020..023) ومالك (PRJ§9).

## Considered Options
1. Aggregate يملك التعريف والعضوية والتنبيه، والمحتوى إسقاط
2. إسقاط خالص

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1.

## Decision Outcome
**Situation is an aggregate in BC03** owning definition (extent, window, criteria, owner, classification), membership rules, alert rules and lifecycle. Its content (member objects) is a projection; members remain owned by their contexts.

## Rationale
PRJ has commands and alerts on situations; state needs an owner (A04).

## Consequences
- ✅ Clear owner
- ✅ Content never duplicated as truth
- ⚠️ Membership evaluation is a streaming workload (WL-06)

## Impact
- **performance:** QAS-PERF-006

## Verified By
QAS-PERF-006

## Previously Blocked By
None — can be decided now.
