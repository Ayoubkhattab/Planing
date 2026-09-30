---
id: DEGRADATION-SLC01
type: degradation-matrix
title: Degradation Matrix — SLC-01
wave: W5
slice: SLC-01
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
---

# Degradation Matrix — SLC-01

## matrix

_6 items_

| capability | failure | fully_available_via | degraded_mode | manual_fallback | unavailable_when |
|---|---|---|---|---|---|
| Sign-in | IdP down | existing sessions ≤ 15 min | — | manual: none (security) | new sign-ins |
| Any request | BC01 directory down | cached SecurityContext ≤ 60 s | — | — | after 60 s |
| Any request | PDP bundle > 5 min old | — | deny writes; allow reads ≤ INTERNAL with cached bundle | — | all |
| Commands | Audit store down | full (local buffering) | — | — | if backlog > 24 h |
| Revocation | Version stream lag | direct KV reads | slower | — | — |
| Admin ops | Scheduler down | read-time validity enforcement | expiry events late | — | — |

**principle:** الأمن لا يتدهور إلى السماح؛ يتدهور إلى الرفض (fail-closed)، والتوفر يُحمى بالتخزين المؤقت القصير والنسخ المتعددة.

---

<details>
<summary>Machine-readable data (YAML) — المصدر المعتمد لهذا الملف</summary>

```yaml
matrix:
- capability: Sign-in
  failure: IdP down
  fully_available_via: existing sessions ≤ 15 min
  degraded_mode: —
  manual_fallback: 'manual: none (security)'
  unavailable_when: new sign-ins
- capability: Any request
  failure: BC01 directory down
  fully_available_via: cached SecurityContext ≤ 60 s
  degraded_mode: —
  manual_fallback: —
  unavailable_when: after 60 s
- capability: Any request
  failure: PDP bundle > 5 min old
  fully_available_via: —
  degraded_mode: deny writes; allow reads ≤ INTERNAL with cached bundle
  manual_fallback: —
  unavailable_when: all
- capability: Commands
  failure: Audit store down
  fully_available_via: full (local buffering)
  degraded_mode: —
  manual_fallback: —
  unavailable_when: if backlog > 24 h
- capability: Revocation
  failure: Version stream lag
  fully_available_via: direct KV reads
  degraded_mode: slower
  manual_fallback: —
  unavailable_when: —
- capability: Admin ops
  failure: Scheduler down
  fully_available_via: read-time validity enforcement
  degraded_mode: expiry events late
  manual_fallback: —
  unavailable_when: —
principle: الأمن لا يتدهور إلى السماح؛ يتدهور إلى الرفض (fail-closed)، والتوفر يُحمى بالتخزين المؤقت القصير والنسخ المتعددة.
```

</details>
