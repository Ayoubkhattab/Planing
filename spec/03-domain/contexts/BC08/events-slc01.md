---
id: EVT-CAT-BC08-SLC01
type: event-catalog
title: Domain Events — BC08 (SLC-01)
wave: W4
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---


# Domain Events — BC08 (SLC-01)

_18 events_

| الحدث | Aggregate | ينتجه | يؤثر أمنياً | المستهلكون | مفتاح التقسيم |
|---|---|---|---|---|---|
| EVT-CLS-DRAFTED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-DRAFT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-CLS-EDITED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-EDIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-CLS-ACTIVATED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-ACTIVATE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-CLS-DISCARDED | AGG-CLASSIFICATION-SCHEME | CMD-CLS-DISCARD | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-CLS-SUPERSEDED | AGG-CLASSIFICATION-SCHEME | SYS:successor activated | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-DRAFTED | AGG-POLICY-SET | CMD-POL-DRAFT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-EDITED | AGG-POLICY-SET | CMD-POL-EDIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-SUBMITTED | AGG-POLICY-SET | CMD-POL-SUBMIT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-APPROVED | AGG-POLICY-SET | CMD-POL-APPROVE | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-REJECTED | AGG-POLICY-SET | CMD-POL-REJECT | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-ACTIVATED | AGG-POLICY-SET | SYS:effective_from reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-POL-SUPERSEDED | AGG-POLICY-SET | SYS:successor activated | — | Search/Directory projection (BC01 read model); PDP bundle distributor | tenant_id + aggregate.id |
| EVT-EXC-REQUESTED | AGG-SECURITY-EXCEPTION | CMD-EXC-REQUEST | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-EXC-FIRST-APPROVED | AGG-SECURITY-EXCEPTION | CMD-EXC-APPROVE | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-EXC-ACTIVATED | AGG-SECURITY-EXCEPTION | CMD-EXC-APPROVE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-EXC-REJECTED | AGG-SECURITY-EXCEPTION | CMD-EXC-REJECT | — | Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-EXC-REVOKED | AGG-SECURITY-EXCEPTION | CMD-EXC-REVOKE | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |
| EVT-EXC-EXPIRED | AGG-SECURITY-EXCEPTION | SYS:end reached | نعم | Security-version service (EVT-SEC-VERSION-INCREMENTED); PEP decision caches; Projection security-version table; Search/Directory projection (BC01 read model) | tenant_id + aggregate.id |

المخطط: `05-contracts/asyncapi-{SFX}.md`. التسليم at-least-once عبر outbox؛ المستهلكون idempotent عبر inbox (REQ-PLT-006).
