---
id: ADR-P06
type: adr
title: Security Inside Projections
status: APPROVED_DELEGATED
wave: W3
deciders: HAP-05
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
blocked_by:
- UNK-006
corrects:
- CR-11
- CR-17
verified_by:
- QAS-SEC-002
- QAS-SEC-003
- QAS-SEC-004
- FIT-03
---

# ADR-P06: Security Inside Projections

## Context and Problem
Authorization Before Retrieval (PRJ§5) غير منعكس في تصميم الفهارس والمتجهات والـ Tiles والـ Cache.

## Considered Options
1. تصفية وقت الاستعلام بسمات أمنية مفهرسة
2. فهارس مجزأة حسب التصنيف/المستأجر
3. مزيج

## Initial Engineering Leaning (NOT a decision — V6 rule 75)
يُحسم بعد UNK-006؛ متطلبات منع الاستدلال إلزامية في كل الخيارات.

## W1 Input (delegated answers)
Q16 → Compartments تفرض تصفية مفهرسة + تقسيم للمستويات العليا — يُعتمد رسمياً في W3.

## Decision Outcome
**Pre-filtering with security labels + authoritative re-check.**
1. Every projection document (search, vector, graph, tile feature) carries labels: `tenant, level, compartments[], caveats[], org_scope, security_version`.
2. The PDP converts the caller's authorization into an **allowed-scope filter** that the query engine applies **before** scoring, counting and faceting.
3. Returned hits are re-checked against an authoritative **security-version table** (fast key-value) so revocations apply on the next request regardless of index lag (REQ-GOV-004).
4. Counts, facets, suggestions and 'did you mean' are computed only over the pre-filtered set. No 'N results hidden' messages.
5. Not-found and forbidden return the same response shape and status.
6. Map tiles: cache key = tile + layer + security-scope hash; operational layers above the lowest level are never shared-cached; base layers explicitly marked unclassified may be shared.

## Rationale
Post-filtering leaks existence via counts/facets/timing (A21); pre-filtering alone misses fast revocation.

## Consequences
- ✅ Closes inference channels
- ✅ Revocation effective immediately
- ⚠️ Extra key-value lookup per result page (bounded by page size)

## Impact
- **performance:** ≤ 1 batched lookup per page
- **security:** meets QAS-SEC-002..004

## Verified By
QAS-SEC-002, QAS-SEC-003, QAS-SEC-004, FIT-03

## Previously Blocked By
UNK-006

## Amendment (SLC-05, CR-47)
Step 3 is implemented as follows: **subjects** — the BC01 security-version key-value store (unchanged); **objects** — a batched `LabelCheck` call to each owning context for the returned page (OHS contract in `05-contracts/openapi-discovery-slc05.md`). No central object-label table is maintained, so no context writes into another context's store. Search indexes facts with their own labels so hidden claim values cannot match (SPEC-DISCOVERY §3.1).
