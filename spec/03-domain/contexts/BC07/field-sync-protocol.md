---
id: SPEC-FIELD-SYNC
type: component-specification
title: Field Synchronization Protocol (ADR-P09)
wave: W4
slice: SLC-11
tier: T1
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P09, ADR-P01], corrects: [CR-49, CR-50], requirements: [REQ-OFF-001, REQ-OFF-002, REQ-OFF-003, REQ-OFF-004, REQ-OFF-005, REQ-OFF-006], quality: [QAS-OFF-001, QAS-SEC-007]}
---

# Field Synchronization Protocol

## 1. على الجهاز (دون اتصال)
| البند | القاعدة |
|---|---|
| الفتح | فتح التطبيق بـ PIN/بصمة يفك مفتاح التخزين المحلي (مرتبط بالمستخدم والجهاز)؛ لا بيانات مقروءة دون فتح (QAS-SEC-007) |
| الالتقاط | الأوامر المسموحة فقط (x-offline-capable في SLC-02/SLC-03)؛ كل أمر يُضاف لطابور بـ seq متتالي، `client_command_id` (ULID)، `device_time`، `base_version` للأوامر المغيرة للحالة، وتوقيع بمفتاح الجهاز، وسلسلة hash (`prev_hash`) |
| المعرّفات | الكائنات الجديدة (ملاحظات، أدلة، مرفقات) تأخذ ULID يولده الجهاز (`client_id`) — آمن من التصادم ويجعل الإنشاء idempotent (CR-50) |
| الحد الزمني | بعد 72 ساعة بلا اتصال (R1؛ 7 أيام في التصميم): **الالتقاط يستمر**، لكن **قراءة البيانات المحملة مسبقاً تتوقف** (انتهاء الحزمة) — الالتقاط قيّم، وقراءة بيانات حساسة قديمة خطر |
| المرفقات | تُحفظ مشفرة محلياً وتُرفع بعد الاتصال عبر أهداف رفع مباشرة قابلة للاستئناف |

## 2. المصافحة
```text
device → CMD-SYN-OPEN {device, device_time Td, last_acked_seq, queue_length, queue_head_hash, signature}
server:  verify device ACTIVE (else REJECTED + WIPE/STOP), user token fresh, signature
         clock_offset = Ts_receive − Td  (round-trip corrected on the second exchange)
         return session_id, acked_seq, server_time
```

## 3. الرفع والتطبيق
```text
for each batch (≤ 200, contiguous seq):
  verify signatures and hash chain; gap → SEQUENCE_GAP (device resends from acked_seq+1)
  for each envelope in seq order:
     if client_command_id already applied → skip (idempotent)                       -- REQ-OFF-006
     if device lost_at ≤ device_time corrected → open sync conflict (INV-SCF-03)
     cmd := owner-context command with:
              SecurityContext = user's (delegated), Idempotency-Key = client_command_id
              observed_at / device times = device_time + clock_offset (raw device_time kept)
              recorded_from = server receipt (owner assigns)                         -- REQ-OFF-003
     if cmd is append-only (RECORD, INITIATE/COMPLETE-UPLOAD, EVD-REGISTER, ATTACH-EVIDENCE, ADD-RESULT-ITEM):
          apply; owner guards still apply (e.g. task must be IN_PROGRESS/BLOCKED)
     else (state-changing):
          apply only if base_version = current version; else → AGG-SYNC-CONFLICT (CF-05) -- REQ-OFF-004, no LWW
     owner rejects for a guard (not version) → conflict with the owner's reason
  ack highest contiguous processed seq
```
- ترتيب التطبيق هو ترتيب الجهاز. أمر لاحق يعتمد على نتيجة أمر سابق (مثلاً START ثم SUBMIT) يُطبق بالترتيب نفسه، فتتطابق `base_version` المتوقعة إذا لم يتغير شيء على الخادم.
- انحراف ساعة > 5 دقائق → علامة DEVICE_CLOCK_SUSPECT في جودة البيانات (INV-OBS-04).

## 4. التنزيل (Delta)
بعد الرفع: تغييرات مهام المستخدم (نسخة ملخصة ومرئية فقط)، حالة الحزم، قائمة purge (حزم منتهية/ملغاة، كائنات فقد المستخدم صلاحيتها)، إشعارات التعارضات، وتعليمات (CONTINUE / STOP / WIPE / REAUTHENTICATE).

## 5. التعارضات (CR-49)
- CF-05 **لا** يمر عبر محرك تعارض الادعاءات في BC02. الملاحظات إلحاقية ولا تتعارض؛ ادعاءاتها المشتقة تدخل محرك BC02 (CF-01..04) كأي ادعاء.
- CF-05 خاص بالأوامر المغيرة للحالة المتقادمة، ويُمثل بـ AGG-SYNC-CONFLICT مع الأمر الأصلي ولقطة الحالة الحالية وسبب الرفض.
- المراجع يعيد التطبيق على الإصدار الحالي، أو يهمل، أو يحل يدوياً؛ وفي كل الحالات حراسات المالك سارية (INV-SCF-02).

## 6. الأداء والتوسع (QAS-OFF-001)
- 1,000 أمر في طابور بعد 72 ساعة على رابط 1 Mbps: ≤ 10 دقائق (الأوامر صغيرة؛ المرفقات منفصلة ومستأنفة).
- بوابة المزامنة عديمة الحالة؛ حد معدل لكل جهاز؛ طابور عند عاصفة إعادة الاتصال (FM-S03-04) مع أولوية للأجهزة الأقدم انقطاعاً.
