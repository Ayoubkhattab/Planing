---
id: ADR-P11
type: adr
title: Policy Engine & Representation
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-05
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by: []
corrects:
- CR-33
verified_by:
- QAS-SEC-005
---

# ADR-P11: Policy Engine & Representation

## Context and Problem
PRJ§77 يذكر Policy Engine دون تمثيل للسياسات.

## Considered Options
1. لغة سياسات تصريحية بمحرك متخصص
2. جداول قرار مفسرة داخلياً

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
جداول قرار محايدة في الدراسة، والمحرك في W8.

## Decision Outcome
**Policies are versioned data evaluated by a Policy Decision Point; every service has a Policy Enforcement Point.** Policies are specified as decision tables (`08-security/authorization-model.md`). The engine/language is selected in W8 (ADR-P05 family). Fail-closed.

## Rationale
Keeps policy independent of code and of engine choice.

## Consequences
- ✅ Policies testable as tables
- ⚠️ Engine choice deferred

## Impact
- —

## Verified By
QAS-SEC-005

## Previously Blocked By
None — can be decided now.
