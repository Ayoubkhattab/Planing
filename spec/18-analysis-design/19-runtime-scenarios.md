---
id: AD-19-RUNTIME-SCENARIOS
type: runtime-scenarios
title: "سيناريوهات التشغيل — مخططات التسلسل للمسارات الحرجة"
status: DRAFT
phase: "Phase 3.8 — 18-analysis-design (المرحلة 4)"
sources: [03-domain/contexts/BC*/aggregates/AGG-*.md, 03-domain/contexts/BC*/events-*.md, 08-security/authorization-model.md, 08-security/key-hierarchy-and-disposition.md, 00-governance/decisions/ADR-P06.md, 00-governance/decisions/ADR-P09.md, 00-governance/decisions/ADR-P17.md, 00-governance/decisions/ADR-P19.md, 02-requirements/quality-scenarios.md, 12-solution/deployment-units.md]
---

# سيناريوهات التشغيل (Runtime Scenarios)

كيف تتعاون الوحدات في المسارات الحرجة، خطوة بخطوة. المسار العام للأمر والاستعلام والحدث في `11-hexagonal-reference.md` §3–§4؛ هنا اثنا عشر مسارًا محددًا، اختيرت لأنها تحمل أصعب ضمانات النظام: التخويل قبل الوصول، الاتساق، عدم الإفصاح، الإلغاء الفوري، الزمن الحرج، العمل دون اتصال، المحو والإتلاف.

**قراءة المخططات:** المشاركون وحدات النشر (`12-components.md`)؛ كل رسالة أمر أو حدث أو استعلام بمعرّفه في المواصفات. التسميات في المخططات بالإنجليزية لتُرسم بلا أخطاء؛ الشرح بالعربية تحتها. ما لا تذكره المصادر صراحة معلَّم **[Derived]**.

| # | السيناريو | الضمانات | الوحدات |
|---|---|---|---|
| 1 | إسناد مهمة | خط الأوامر كاملًا، استدعاء سياق آخر، فشل مغلق | DU-01، DU-08 |
| 2 | اعتماد خطة بمصادقة معززة | `401` ثم إعادة المحاولة، فصل المهام، فحص السلطة | DU-01، DU-08، DU-02 |
| 3 | بحث مؤمَّن | `allowed_scope` قبل العدّ، إعادة فحص النتائج | DU-01، DU-09 |
| 4 | من الملاحظة إلى التنبيه | ≤ 5 ثوانٍ طرفًا لطرف | DU-05، DU-07، DU-06، DU-08 |
| 5 | سحب الصلاحية | نافذ في الطلب التالي | DU-02، كل الوحدات |
| 6 | المزامنة الميدانية | لا «آخر كتابة تفوز»، تعارض صريح | DU-10، الوحدات المالكة |
| 7 | من القرار إلى المهام | تتبع التنفيذ إلى قراره | DU-08، DU-02 |
| 8 | محو صاحب بيانات | غير قابل للاسترجاع في كل النسخ | DU-03، DU-02، DU-04، DU-14 |
| 9 | الإتلاف اليومي | لا إتلاف لمجمَّد | DU-03 |
| 10 | تهيئة مستأجر | ساغا قابلة للتعويض | DU-02، DU-03 |
| 11 | طلب ذكاء اصطناعي (R2) | استرجاع بصلاحيات الطالب، إسناد كل عبارة | DU-16، DU-09 |
| 12 | استعادة مخزن المفاتيح | المفتاح المُتلَف يبقى مُتلَفًا | DU-03 |

---

## 1. إسناد مهمة — `CMD-TASK-ASSIGN`

```mermaid
sequenceDiagram
  autonumber
  actor P as Planner
  participant G as DU-01 Gateway
  participant O as DU-08 Operations
  participant R as BC05 EligibilityCheck
  participant DB as PostgreSQL operations
  P->>G: POST tasks/id/actions/assign + Idempotency-Key + If-Match
  G->>O: signed SecurityContext
  O->>O: tenant scope + coarse authorization
  O->>DB: idempotency check, load AGG-TASK
  O->>O: full authorization POL-TASK-ASSIGN with task attributes
  O->>O: If-Match version check
  O->>R: EligibilityCheck(assignee, task type, now)
  R-->>O: ELIGIBLE or CONDITIONALLY_ELIGIBLE
  O->>O: guard: assignee ACTIVE, clearance >= task label
  O->>DB: commit state + history + EVT-TASK-ASSIGNED + audit + idempotency record
  O-->>G: 202 ResourceRef
  G-->>P: 202
```

| الخطوة | التفصيل | المصدر |
|---|---|---|
| 3–6 | خطوات الخط 1–7 (ADR-P17)؛ المهمة غير المرئية → `404`، المرئية دون إذن → `403` | ADR-P17، ADR-P19 |
| 7–8 | استدعاء OHS متزامن لـBC05 (في R1 داخل DU-08 نفسها، ومن R2 في DU-14) | `03-domain/context-map.md`، `12-components.md` §2 |
| 9 | الشرط في جدول انتقالات AGG-TASK | AGG-TASK |
| 10 | معاملة واحدة (FIT-04) | ADR-P02 |

**مسارات الفشل:** غير مؤهل → `ASSIGNEE_NOT_ELIGIBLE` (422)؛ BC05 غير متاح → يُرفض الأمر مغلقًا (THR-S03-04؛ الرمز **[Missing]**، CR-78)؛ حالة غير READY → `TASK_INVALID_STATE_TRANSITION` (409)؛ مهمة معلقة → `TASK_SUSPENDED`. **الجودة:** p95 ≤ 300 مللي ث (QAS-PERF-001).

## 2. اعتماد خطة بمصادقة معززة — `CMD-PLV-APPROVE`

```mermaid
sequenceDiagram
  autonumber
  actor A as Approver
  participant G as DU-01 Gateway
  participant O as DU-08 Operations
  participant F as DU-02 Foundation
  participant K as Keycloak
  A->>G: POST plan-versions/id/actions/approve + Idempotency-Key K1
  G->>O: SecurityContext with auth strength
  O->>O: coarse authz, idempotency, load AGG-PLAN-VERSION
  O->>O: full authz POL-PLV-APPROVE, SoD approver != author
  O->>O: obligation mfa not satisfied
  O-->>A: 401 MFA_STEP_UP_REQUIRED with acr challenge
  A->>K: step-up authentication
  K-->>A: token with higher acr
  A->>G: same request, same Idempotency-Key K1
  G->>O: SecurityContext with stronger auth
  O->>O: coarse authz, idempotency, load, full authz, mfa satisfied
  O->>F: AuthorityCheck(approver, plan-approval, scope, now)
  F-->>O: authorized
  O->>O: If-Match, transition IN_REVIEW to BASELINED
  O->>O: commit + EVT-PLV-BASELINED
  O-->>A: 202 ResourceRef
```

نفس `Idempotency-Key` في المحاولة الثانية آمن لأن المحاولة الأولى لم تُنفِّذ شيئًا (ADR-P19). المؤلف نفسه → `SEGREGATION_OF_DUTIES` (422) قبل طلب MFA (الخطوة 5 قبل 6). فحص السلطة شرط في جدول الانتقالات (AGG-PLAN-VERSION) يُنفَّذ في الخطوة 8 **[Derived]** من موضعه في الشرط. **الأثر اللاحق:** `EVT-PLV-BASELINED` يستهلكه مُزامِن المهام ومتتبعو النتائج وتفعيل الخطة والبحث (السيناريو 7).

## 3. بحث مؤمَّن — `QRY-SRCH-QUERY`

```mermaid
sequenceDiagram
  autonumber
  actor U as Analyst
  participant G as DU-01 Gateway
  participant D as DU-09 Discovery
  participant PDP as OPA embedded
  participant OS as OpenSearch
  participant OW as Owner contexts LabelCheck
  U->>G: POST discovery/search-queries
  G->>D: SecurityContext
  D->>PDP: partial evaluation for search
  PDP-->>D: allowed_scope filter
  D->>OS: query AND allowed_scope, then counts and facets
  OS-->>D: page of hits
  D->>D: re-check security_version of subject
  D->>OW: batched LabelCheck for the page
  OW-->>D: visible subset
  D-->>U: 200 page without hidden items
```

`allowed_scope` يُطبَّق داخل الاستعلام **قبل** العدّ والأوجه والترتيب، فلا يكشف عدد أو وجه وجود كائن مخفي (ADR-P06، THR-005). إعادة الفحص (CR-47) تغلق فجوة تأخر الإسقاط بعد سحب صلاحية (THR-006). **الجودة:** 0 إفصاح في حزمة الاستدلال (QAS-SEC-002، QAS-SEC-011)؛ ميزانية زمن البحث في `07-quality/` (QAS-PERF-003).

## 4. من الملاحظة إلى التنبيه — ≤ 5 ثوانٍ

```mermaid
sequenceDiagram
  autonumber
  actor S as Sensor or field user
  participant I as DU-05 Ingestion
  participant K as Kafka information.events
  participant E as DU-07 Evaluators
  participant N as DU-06 Intelligence
  participant OP as DU-08 Operations
  S->>I: CMD-OBS-RECORD
  I->>I: pipeline, commit + EVT-OBS-RECORDED in outbox
  I-->>S: 201
  I->>K: CDC relay EVT-OBS-RECORDED
  K->>E: consume, inbox dedupe
  E->>E: situation membership + alert rule condition
  E->>N: internal command for SYS rule condition met
  N->>N: AGG-ALERT created RAISED, label = max(rule, object)
  N->>K: EVT-ALR-RAISED
  K->>OP: notification fan-out to cleared subscribers
  OP-->>S: push or in-app notification
```

المُقيِّم في DU-07 لا يملك بيانات؛ ينشئ التنبيه بأمر داخلي على عقد DU-06 بهوية عبء عمل (`12-components.md` §2). التنبيه لا يصل إلى مستخدم غير مصرَّح بعلامته ولا يغيّر عدّاده (QAS-SEC-012). **الجودة:** p95 ≤ 5 ثوانٍ طرفًا لطرف (QAS-PERF-005)؛ أثناء الذروة 0 أحداث مفقودة والتنبيه الحرج p95 ≤ 30 ثانية (QAS-SCAL-002). **التكرار:** الحدث نفسه مرتين لا ينشئ تنبيهين (inbox، ونافذة إزالة التكرار في AGG-ALERT).

## 5. سحب الصلاحية — نافذ في الطلب التالي

```mermaid
sequenceDiagram
  autonumber
  actor SO as Security Officer
  participant F as DU-02 Foundation
  participant SV as Security-version service
  participant T as Kafka security.versions
  participant X as Any unit PEP
  participant P as Projection security-version tables
  actor U as Affected user
  SO->>F: CMD-CLR-SUSPEND
  F->>F: commit + EVT-CLR-SUSPENDED (security-affecting)
  F->>SV: consume
  SV->>T: EVT-SEC-VERSION-INCREMENTED (priority topic)
  T->>X: invalidate cached ALLOW decisions for subject
  T->>P: update subject security_version
  U->>X: next request
  X->>X: decision cache miss, PDP re-evaluates
  X-->>U: 404 or 403
```

قرارات ALLOW المخزنة ≤ 60 ثانية مفتاحها يتضمن `security_version`، فرفع الإصدار يبطلها فورًا؛ ونتائج البحث تُعاد فحصها بالإصدار، فلا يعيد إسقاط متأخر كائنًا بعد السحب (`authorization-model.md` §5، ADR-P06). **الجودة:** نافذ في الطلب التالي في كل المسارات بغض النظر عن تأخر الفهارس (QAS-SEC-003)؛ تأخر قناة الإصدارات > 2 ثانية ينبّه (`observability-slc01.md`).

## 6. المزامنة الميدانية — `AGG-SYNC-SESSION`

```mermaid
sequenceDiagram
  autonumber
  actor FU as Field device
  participant S as DU-10 Field sync
  participant OW as Owner unit DU-05 or DU-08
  participant C as AGG-SYNC-CONFLICT
  FU->>S: CMD-SYN-OPEN signed handshake, fresh token
  S->>S: device ACTIVE, measure clock offset
  S-->>FU: OPEN, last acknowledged seq
  FU->>S: CMD-SYN-UPLOAD-BATCH up to 200 signed envelopes
  S->>S: contiguous seq, hash chain, signatures
  loop each CommandEnvelope
    S->>OW: target command with base_version, client_command_id
    alt applied or already applied
      OW-->>S: ResourceRef
    else base_version stale or rejected
      S->>C: open sync conflict
    end
  end
  S-->>FU: COMPLETED or COMPLETED_WITH_CONFLICTS
```

الأوامر الميدانية تُنفَّذ بالصلاحيات **الحالية** لا صلاحيات لحظة الالتقاط (QAS-OFF-002)؛ `client_command_id` يجعل إعادة الرفع آمنة؛ تعارض بيانات T1/T2 لا يُحل بـ«آخر كتابة تفوز» بل بقضية صريحة (ADR-P09، FIT-15). جهاز مفقود أو موقوف عند المصافحة → `REJECTED` مع أمر مسح أو إيقاف فقط. فجوة في التسلسل → `SEQUENCE_GAP`؛ انقطاع أو خمول 5 دقائق → `FAILED` وتستأنف الجلسة التالية من آخر تسلسل مؤكد (REQ-OFF-006). عدد الأوامر المسموحة دون اتصال (6 أو 12) **[Needs Review]** (S-09، `20-integration-design.md`).

## 7. من القرار إلى المهام

```mermaid
sequenceDiagram
  autonumber
  actor M as Manager with authority
  participant O as DU-08 Operations
  participant F as DU-02 Foundation
  actor PL as Planner
  M->>O: CMD-DEC-RECORD
  O->>F: AuthorityCheck(actor, decision type, scope, at)
  F-->>O: authorized with grant chain
  O->>O: commit + EVT-DEC-RECORDED
  PL->>O: CMD-PLN-CREATE implementing the decision
  PL->>O: CMD-PLV-DRAFT, EDIT, SUBMIT
  Note over O: approval as in scenario 2
  O->>O: EVT-PLV-BASELINED
  O->>O: task synchronizer creates tasks for task_generating activities
  O->>O: plan activated by SYS first version baselined
```

القرار لا يُسجَّل إلا إن حمل صاحبه سلطة نافذة لحظة القرار (BRL-003، REQ-FND-009)؛ الخطة تشير إلى القرار الذي تنفّذه، والمهمة إلى نشاط الخطة، فيُتتبع التنفيذ إلى قراره (`06-process-models.md` تيار VS03). مُزامِن المهام من مستهلكي `EVT-PLV-BASELINED` (SPEC-PLAN §3)؛ تحرير الموارد عند اكتمال المهمة عبر أحداث BC04 إلى BC05.

## 8. محو صاحب بيانات — `AGG-ERASURE-REQUEST`

```mermaid
sequenceDiagram
  autonumber
  actor PO as Privacy officer
  actor LA as Legal authority
  participant GV as DU-03 Governance
  participant OW as Owners BC01 BC02 BC05
  participant KS as Key store and HSM
  PO->>GV: CMD-ERS-REGISTER with legal basis
  GV->>OW: ErasureScope
  OW-->>GV: subject keys located
  Note over GV: SYS subject scope resolved, SCOPED
  LA->>GV: CMD-ERS-APPROVE, approver != registrar, mfa
  GV->>GV: HoldCheck
  alt hold matches subject
    GV->>GV: BLOCKED_BY_HOLD until hold released
  else no hold
    GV->>KS: destroy subject DEKs, append destruction log
    GV->>OW: purge plaintext caches and projections
    OW-->>GV: ErasureConfirm within 24 h
    GV->>GV: COMPLETED, certificate issued
  end
```

إتلاف مفتاح الموضوع يجعل البيانات الشخصية غير مقروءة في المخازن والإسقاطات والنسخ الاحتياطية والأرشيف دفعة واحدة؛ حقائق التدقيق تبقى بمرجع مستعار (INV-ERS-03). **الجودة:** المخازن والإسقاطات ≤ 24 ساعة، والنسخ غير قابلة للاسترجاع فورًا (QAS-PRV-001؛ REQ-GOV-008).

## 9. الإتلاف اليومي — `AGG-DISPOSITION-RUN`

```mermaid
sequenceDiagram
  autonumber
  participant SCH as DU-03 scheduler
  participant GV as DU-03 Governance
  actor AR as Archivist
  actor RL as Records or Legal authority
  participant KS as Key store
  participant OW as Owner contexts
  SCH->>GV: SYS scheduled evaluation daily
  GV->>GV: PLANNED: buckets past retention, held items listed
  AR->>GV: CMD-DSP-SUBMIT
  RL->>GV: CMD-DSP-APPROVE, approver != submitter, HoldCheck re-run
  GV->>KS: re-wrap held items under hold keys
  GV->>KS: destroy bucket keys, append destruction log
  GV->>OW: DispositionNotice: purge caches, rebuild projections, tombstones
  GV->>GV: COMPLETED with certificate, or COMPLETED_WITH_EXCEPTIONS
```

الإتلاف بالحاوية (فئة، شهر) يصل إلى كل النسخ بإتلاف مفتاح واحد (`key-hierarchy-and-disposition.md` §2). **الجودة:** المرشحون ≤ ساعة، و0 سجلات مجمَّدة مُتلَفة (QAS-GOV-001). الحاويات الفاشلة تُعاد في التشغيل التالي.

## 10. تهيئة مستأجر — ساغا BC01

```mermaid
sequenceDiagram
  autonumber
  actor PO as Platform Operator
  participant F as DU-02 Foundation
  participant ST as Provisioning steps
  participant GV as DU-03 Governance
  PO->>F: CMD-TEN-PROVISION
  F->>F: PROVISIONING
  loop each step, idempotent
    F->>ST: isolation, keys, classification scheme, default roles, quotas, audit stream
    ST-->>F: step confirmed
  end
  alt all steps confirmed
    F->>F: CMD-TEN-COMPLETE-PROVISIONING (internal) ACTIVE
  else a step failed
    F->>ST: compensate completed steps
    F->>F: CMD-TEN-FAIL-PROVISIONING (internal) PROVISIONING_FAILED
    PO->>F: CMD-TEN-RETRY-PROVISIONING
  end
```

الساغا الوحيدة في النظام (`11-hexagonal-reference.md` §3)؛ كل خطوة أمر مستقل يمر بالخط نفسه، وجدول `tenant_provisioning_steps` يجعل الخطوة idempotent. لا بيانات للمستأجر قبل اكتمال حد العزل والمخطط والأدوار وتيار التدقيق (REQ-FND-003). **الجودة:** آلية بالكامل ≤ ساعة دون تغيير كود أو مخطط (QAS-SCAL-003). المستأجر المخصص أو السيادي في خلية خاصة (REQ-FND-004).

## 11. طلب ذكاء اصطناعي (R2) — `AGG-AI-REQUEST`

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant AI as DU-16 AI Serving
  participant PDP as OPA
  participant D as DU-09 secured projections
  participant M as vLLM
  U->>AI: CMD-AIR-SUBMIT operation, purpose
  AI->>PDP: user, ai operation, scope, autonomy level
  alt denied
    AI-->>U: REFUSED
  else allowed
    AI->>D: authorized hybrid retrieval as the user
    D-->>AI: visible context items
    AI->>AI: seal context package: URN + version + label, hash
    AI->>M: generate within token budget
    M-->>AI: draft output
    AI->>AI: citation check: every statement cites a context item
    AI-->>U: COMPLETED, label = max(context labels), or INSUFFICIENT_EVIDENCE
  end
```

الذكاء الاصطناعي يقرأ الإسقاطات المؤمنة بصلاحيات الطالب فقط، ولا أدوات كتابة في R2: أدوات الاقتراح تنشئ نتائج AI فقط (TB-08، `13-project-structure.md` §4). العبارة غير المسندة تُحذف؛ فإن لم يبق جواب → `INSUFFICIENT_EVIDENCE`. **الجودة:** 0 استرجاع غير مصرَّح و0 تسرب بين المستأجرين في حزم الحقن (QAS-AI-004).

## 12. استعادة مخزن المفاتيح — بوابة الاستعادة

```mermaid
sequenceDiagram
  autonumber
  actor OP as Operator
  participant KS as Key store
  participant DL as Destruction log, WORM copy
  participant SVC as All services
  OP->>KS: restore backup older than a destruction
  KS->>DL: read full destruction log
  DL-->>KS: destroyed key ids
  KS->>KS: destroy listed keys again
  KS-->>OP: gate passed
  OP->>SVC: start services
```

سجل الإتلاف append-only ومكرر ولا يُستعاد من نسخ أقدم؛ لا تُفتح خدمة قبل اجتياز البوابة؛ نسخ مخزن المفاتيح ≤ 35 يومًا (CR-51). **الجودة:** المفتاح المُتلَف غير قابل للاستخدام قبل أن تقرأ أي خدمة بيانات (QAS-PRV-002، FIT-19).

---

## 13. ما لا تغطيه هذه السيناريوهات

| المسار | أين |
|---|---|
| مسار الأمر والاستعلام والحدث العام | `11-hexagonal-reference.md` §3–§4 |
| كل انتقال حالة ورفضه | `08-state-models.md`، `05-user-stories/` |
| الاستيراد والمحوّلات | `20-integration-design.md` |
| التمارين والمحاكاة والإمداد (R3) | `06-process-models.md` تيارات VS04 وVS05 |
| تعافي الخلية من الكوارث | `09-reliability/dr-and-continuity.md`، `22-deployment-design.md` |
