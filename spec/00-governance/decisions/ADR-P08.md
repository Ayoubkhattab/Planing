---
id: ADR-P08
type: adr
title: Erasure vs Immutability
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-03
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-002
corrects:
- CR-39
verified_by:
- QAS-PRV-001
---

# ADR-P08: Erasure vs Immutability

## Context and Problem
عدم الحذف والأحداث الثابتة والأرشفة تتعارض مع الإتلاف القانوني وطلبات المحو.

## Considered Options
1. Crypto-shredding
2. Tombstones مع إزالة المحتوى
3. استثناءات قانونية موثقة

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
لا ترجيح قبل UNK-002.

## W1 Input (delegated answers)
Q18 → الخيار 1 — يُعتمد رسمياً في W3.

## Decision Outcome
**Crypto-shredding for personal data; key destruction for disposition.**
- Attributes flagged `personal_data: true` are encrypted with a per-data-subject key wrapped by the tenant key.
- Erasure = destroy the subject key → data unreadable in all stores, projections, backups and archives.
- Audit facts keep a pseudonymous subject reference.
- Legal hold blocks key destruction.

## Rationale
W1 Q18; the only option that reaches backups without rewriting them.

## Consequences
- ✅ Erasure reaches immutable stores and backups
- ⚠️ Key management becomes critical infrastructure (FM required)
- ⚠️ Search on encrypted personal fields limited to normalized tokens computed before encryption under policy

## Impact
- **security:** KMS/HSM availability is critical tier
- **legal:** UNK-002 confirmation still required before G8

## Verified By
QAS-PRV-001

## Previously Blocked By
UNK-002

## Amendment (SLC-12a, CR-51)
Implementation detail: disposition uses **class-bucket keys** (record class × trigger month) so one key destruction retires a whole bucket across stores and backups; erasure uses **subject keys**. Held records are re-wrapped under hold keys before a bucket key is destroyed. A **restore gate** replays the append-only key-destruction log on any key-store restore, closing the gap where an older key-store backup could revive destroyed keys. See `08-security/key-hierarchy-and-disposition.md`.
