---
id: UI-ARCHITECTURE
type: architecture
title: Client Architecture (web + mobile, bilingual, RTL)
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W8
traces: {requirements: [REQ-PLT-010, REQ-PLT-011], quality: [QAS-ACC-001, QAS-USA-001], decided_by: [TD-16]}
---

# Client Architecture

| البند | الويب | الجوال الميداني |
|---|---|---|
| التقنية | React + TypeScript؛ عملاء مولّدون من OpenAPI | React Native + TypeScript؛ نفس العملاء المولّدين |
| الخرائط | MapLibre GL JS (بلاطات متجهية من DU-12) | MapLibre Native؛ PMTiles محلية للحزم |
| اللغة والاتجاه | i18n برسائل ICU؛ RTL بخصائص CSS المنطقية؛ تبديل AR/EN لكل مستخدم | نفس الرسائل؛ RTL أصلي |
| التقويم | ميلادي مخزن؛ عرض هجري اختياري عبر Intl (islamic-umalqura) | نفسه |
| إمكانية الوصول | WCAG 2.2 AA (QAS-ACC-001)؛ اختبار آلي + يدوي | معايير المنصة للوصول |
| التخزين المحلي | لا بيانات حساسة؛ مسودات T4 فقط | SQLCipher + مفتاح في keystore العتادي |
| الأمان | جلسة ≤ 15 د؛ لا محتوى في التخزين المحلي | فتح بـ PIN/بصمة؛ مسح عن بعد |
| الأداء | ≤ 360 px إلى سطح المكتب (REQ-PLT-011) | تسجيل ملاحظة بصورة ≤ 60 ث (QAS-USA-001) |

**قاعدة:** الواجهة لا تحتوي منطق عمل؛ كل قرار صلاحية أو حالة يأتي من الخادم. عرض "DISPUTED" والتعميم المكاني والحجب نتيجة من الخادم تعرضها الواجهة كما هي.
