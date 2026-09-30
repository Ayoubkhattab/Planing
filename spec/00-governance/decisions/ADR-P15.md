---
id: ADR-P15
type: adr
title: Language & Entity Matching
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-04
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-011
corrects:
- CR-18
verified_by:
- QAS-USA-002
---

# ADR-P15: Language & Entity Matching

## Context and Problem
لا معالجة للعربية في البحث ومطابقة الكيانات.

## Considered Options
1. تخزين الأصل + صيغ مطبّعة ومنقحرة للمطابقة + محللات عربية
2. الاعتماد على محرك البحث الافتراضي

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
الخيار 1.

## W1 Input (delegated answers)
Q15 → الخيار 1 — يُعتمد رسمياً في W3.

## Decision Outcome
**Store original + normalized + transliterated + phonetic forms**, per `04-information/language-model.md`. Original never modified. Normalization is deterministic and versioned.

## Rationale
W1 Q15; QAS-USA-002.

## Consequences
- ✅ Arabic-aware matching and search
- ⚠️ Normalization version upgrades require re-indexing (projection rebuild)

## Impact
- —

## Verified By
QAS-USA-002

## Previously Blocked By
UNK-011
