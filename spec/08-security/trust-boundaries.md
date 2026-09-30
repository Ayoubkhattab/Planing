---
id: TRUST-BOUNDARIES
type: security-model
title: Trust Boundary Model
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W3
tier: T0
---

# Trust Boundary Model

```mermaid
flowchart TB
  U[User / Browser / Mobile] -- TB-01 --> GW[Edge Gateway / BFF]
  FD[(Field device store)] -. TB-07 .- U
  GW -- TB-02 --> APP[Context applications]
  APP -- TB-03 --> DB[(Operational stores)]
  APP -- TB-04 --> PRJ[(Projections: search, graph, vector, tiles)]
  APP -- PDP call --> PDP[Policy Decision Point]
  APP -- TB-05 --> CELL2[Other cell]
  ADP[Adapters / ACL] -- TB-06 --> EXT[External systems]
  AI[AI runtime - R2] -- TB-08 --> PRJ
  OPS[Operator / admin plane] -- TB-09 --> APP
  DB -- TB-10 --> BK[(Backups / Archive)]
```

| TB | الحد | ما يعبره | الضوابط الإلزامية |
|---|---|---|---|
| TB-01 | المستخدم ↔ البوابة | طلبات مصادقة | OIDC/SAML، TLS 1.3، رموز قصيرة العمر، حماية CSRF، حدود معدل |
| TB-02 | البوابة ↔ التطبيقات | SecurityContext موقّع | mTLS + هوية عبء العمل؛ التطبيقات لا تثق بترويسات غير موقّعة |
| TB-03 | التطبيق ↔ المخازن | استعلامات | حساب خدمة لكل سياق؛ RLS كحاجز ثان؛ لا وصول عابر للسياقات (FIT-01) |
| TB-04 | التطبيق ↔ الإسقاطات | استعلام بفلتر | فلتر النطاق المسموح إلزامي + إعادة فحص (ADR-P06)؛ الإسقاط لا يُسأل مباشرة من الواجهة |
| TB-05 | خلية ↔ خلية | لا شيء افتراضياً | لا مسار بيانات؛ الترحيل فقط بتصدير/استيراد معتمد |
| TB-06 | المنصة ↔ الأنظمة الخارجية | بيانات واردة | ACL، تحقق مخطط، حجر، lineage؛ لا ثقة تلقائية (BRL-013) |
| TB-07 | مخزن الجهاز الميداني | بيانات محلية | تشفير، انتهاء صلاحية، مسح عن بعد، ربط بالجهاز |
| TB-08 | AI ↔ البيانات والأدوات | سياق واسترجاع | صلاحيات المستخدم الطالب فقط، AIL، سجل Context Package (R2) |
| TB-09 | مستوى التشغيل ↔ بيانات المستأجر | إدارة | المشغل لا يقرأ بيانات المستأجر؛ Break-glass بموافقة شخصين ومدة وتدقيق |
| TB-10 | المخازن ↔ النسخ والأرشيف | نسخ | مشفرة بمفاتيح المستأجر؛ الاستعادة عملية مدققة |
