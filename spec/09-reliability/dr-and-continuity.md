---
id: DR-CONTINUITY
type: architecture
title: Disaster Recovery, Backups & Business Continuity
tier: T2
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
wave: W8
traces: {requirements: [REQ-PLT-004, REQ-PLT-012], quality: [QAS-AVL-001, QAS-AVL-002, QAS-AVL-003, QAS-REC-001, QAS-REC-002, QAS-REC-003, QAS-PRV-002], corrects: [CR-54]}
---

# Disaster Recovery & Continuity

## 1. طبقات الخدمة لكل وحدة
| الطبقة | الوحدات | التوفر | RPO | RTO |
|---|---|---|---|---|
| critical | DU-01, 02, 03, 04, 05, 07, 08 (المهام), 10 | 99.9 % | ≤ 5 د | ≤ 1 س |
| important | DU-06, 09, 12, 13 | 99.5 % | ≤ 15 د | ≤ 4 س |
| standard | DU-11، التقارير | 99 % | ≤ 24 س | ≤ 24 س |

## 2. الحماية لكل مخزن
| المخزن | داخل الموقع | إلى موقع DR (نفس الولاية) | اختبار |
|---|---|---|---|
| PostgreSQL | replica متزامن + replica غير متزامن | WAL shipping مستمر؛ تأخر ≤ 5 د؛ نسخة كاملة يومية | استعادة أسبوعية آلية + تدريب DR ربعي |
| Kafka | replication factor 3 | MirrorMaker 2 للمواضيع الحرجة | إعادة تشغيل المستهلكين من نقاط المزامنة |
| OpenSearch | replicas | **لقطات كل 15 د إلى object storage** | استعادة لقطة ≤ 4 س |
| Object storage | erasure coding | نسخ غير متزامن | عينات تحقق hash |
| Key store (OpenBao + DEKs) | HA | نسخ + **سجل الإتلاف** | بوابة الاستعادة (FIT-19) |
| Valkey | replicas | لا حاجة (يُعاد بناؤه من BC01) | — |

## 3. تصحيح (CR-54)
التصميم السابق اعتبر فهارس البحث "قابلة لإعادة البناء" فقط. لكن إعادة البناء الكاملة تصل إلى 24 ساعة (QAS-REL-004)، بينما RTO لطبقة "important" 4 ساعات. الحل: **لقطات OpenSearch كل 15 دقيقة** تُستعاد في DR ضمن 4 ساعات، ثم يُلحق الفرق من Kafka؛ إعادة البناء الكاملة تبقى لتغييرات المخطط فقط.

## 4. استمرارية العمل
| الموقف | الاستمرارية |
|---|---|
| انقطاع الموقع الرئيسي | الانتقال إلى DR ضمن RTO |
| انقطاع الشبكة للميدان | العمل دون اتصال 72 س (SLC-11) |
| تعطل البحث | الأوامر والقراءات المباشرة والخرائط مستمرة |
| تعطل الإشعارات | صندوق الوارد داخل التطبيق + سحب |
| تعطل IdP | الجلسات الحالية ≤ 15 د؛ إجراء طوارئ بحسابات break-glass بشخصين |
