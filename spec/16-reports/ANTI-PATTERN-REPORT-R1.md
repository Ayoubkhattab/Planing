---
id: ANTI-PATTERN-R1
type: anti-pattern-report
wave: W9
status: FINAL (delegated)
basis: V5§109, V6§19
---

# Anti-Pattern Re-assessment — Release 1

| النمط | عند بداية الدراسة (V6§19.3) | الآن | كيف |
|---|---|---|---|
| Premature Technology Selection | DETECTED | **RESOLVED** | ADR-P05 + TECH-DECISIONS from evidence (CR-21) |
| Premature Kubernetes | DETECTED (light) | **RESOLVED** | justified by cells, air-gapped upgrades, operators (TD-05) |
| Unmeasured Performance / Unmodeled Capacity | DETECTED | **MITIGATED** | workloads + capacity model + test strategy; measurement at pilot |
| Hidden Technical Debt | DETECTED | **RESOLVED** | technical-debt register (DEBT-001) + reversal triggers |
| Checkmark Readiness | DETECTED | **RESOLVED** | evidence-based gate reports; readiness records per slice |
| Timestamp Collapse | PARTIAL | **RESOLVED** | bitemporal model, SL-11, FIT-09 |
| God Aggregate | AT RISK | **RESOLVED** | AnalysisCase → 5 aggregates; Plan → identity + versions (CR-29) |
| Over-centralized Core / Universal Envelope Coupling | AT RISK | **MITIGATED** | envelope as logical contract; tiers per attribute; one kernel library with a fixed API |
| Event Soup | AT RISK | **RESOLVED** | ADR-P02: history authoritative, events for integration; task_events removed |
| Shared Database | AT RISK | **MITIGATED** | schema + role per context, FIT-01; separable clusters (TD-01 reversal) |
| Inference Leakage | AT RISK | **RESOLVED (by design)** | formal non-inference properties P-51..P-53, P-64; fact-level search; alert all-or-nothing |
| Language-Blind Matching | DETECTED | **RESOLVED** | language model, Arabic analyzers, ER evaluation gate |
| Maximum Rigor Everywhere | — | **AVOIDED** | importance tiers (ADR-P03) |
| Documentation Without Consumer | — | **AVOIDED** | generated catalogs/contracts/tests consumed by build |
| Shared Tile Cache Across Clearances | — | **AVOIDED** | scope-hash cache keys |
| Premature Microservices | AVOIDED | **AVOIDED** | 13 deployment units from 8 BCs with V5§97 reasons; BC05 merged into DU-08 |
| Search / Graph as Source of Truth | AVOIDED | **AVOIDED** | projections rebuildable (FIT-11) |
| AI as Authority | AVOIDED | **AVOIDED** | autonomy matrix; AIL5 forbidden |

**الخلاصة:** لا نمط مضاد بحالة DETECTED دون معالجة. أربعة بحالة MITIGATED تحتاج قياساً في Pilot لإغلاقها نهائياً.
