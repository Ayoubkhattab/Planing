---
id: SPEC-KEYS-DISPOSITION
type: component-specification
title: Key Hierarchy, Crypto-Shredding, Restore Gate, Disposition & Erasure Execution
wave: W4
slice: SLC-12a
tier: T0
status: APPROVED_DELEGATED
approved_by: Claude (acting decision owner, delegated by project owner)
approved_at: '2026-09-24'
traces: {decided_by: [ADR-P08, ADR-P04], corrects: [CR-51], requirements: [REQ-GOV-006, REQ-GOV-007, REQ-GOV-008], quality: [QAS-PRV-001]}
---

# Key Hierarchy & Disposition

## 1. هرمية المفاتيح
```text
HSM / KMS (per cell)
 └─ Tenant KEK                                  (in HSM; never exported)
     ├─ Class-Bucket DEK  (tenant, record_class, bucket = trigger month)   ← disposition unit
     │    encrypts: record content of that class whose retention trigger falls in that month
     ├─ Subject DEK       (tenant, subject)     ← erasure unit
     │    encrypts: personal_data attributes about that subject (platform person, or information entity of type person)
     │              — wherever stored, incl. BC05 qualification records of that person (CR-69)
     └─ Hold DEK          (tenant, hold)         ← re-wrap target for held records inside a bucket being destroyed
```
- البيانات الشخصية مشفرة **مرتين**: بمفتاح الموضوع (للمحو) ومفتاح فئة-الحاوية (للإتلاف). إتلاف أيهما يجعلها غير مقروءة.
- المفاتيح المشتقة (DEKs) تُخزن ملفوفة بـ KEK في مخزن مفاتيح داخل الخلية؛ الـ HSM يحمل KEKs فقط → يتسع لملايين المفاتيح (W8 input).
- ذاكرة المفاتيح في الذاكرة ≤ 10 دقائق (FM-S01-08)، وتُفرَّغ فوراً عند حدث إتلاف.

## 2. الإتلاف بالحاويات (Disposition)
```text
plan (daily):  buckets B where every record in B has trigger + period < now   (per ACTIVE schedule)
               held(B) := HoldCheck(bucket B) ∪ HoldCheck(urns in B)
approve:       two persons (INV-DSP / SoD); HoldCheck re-run
execute(B):    for r in held(B): re-wrap r's content key under Hold DEK(h)       -- INV-DSP-02
               destroy Class-Bucket DEK(B) ; append to key-destruction log
               notify owners: purge plaintext caches, projections rebuild excluding B ; write tombstones
certificate:   buckets, key ids destroyed, counts, held items excluded, time
```
- **لماذا الحاويات؟** إتلاف صف بصف في مليار ملاحظة ونسخها الاحتياطية غير عملي؛ إتلاف مفتاح واحد لكل (فئة، شهر) يصل لكل النسخ دفعة واحدة (SR-00).
- إجراء REVIEW: الحاوية لا تُتلف حتى يعتمد المراجع قائمة عناصرها أو ينقلها لفئة أطول.

## 3. المحو (Erasure)
- تحديد النطاق: مفاتيح الموضوع في BC01 (Person) وBC02 (كيانات من نوع شخص لها ادعاءات personal_data).
- التنفيذ: إتلاف مفاتيح الموضوع + سجل في سجل الإتلاف + طلب من كل سياق مالك إفراغ النسخ الواضحة (ذاكرات، فهارس) وتأكيد خلال ≤ 24 ساعة.
- حقائق التدقيق تبقى بمرجع مستعار (INV-ERS-03).

## 4. بوابة الاستعادة (Restore Gate) — CR-51
المشكلة: النسخ الاحتياطية لمخزن المفاتيح نفسه قد تحتوي مفتاحاً أُتلف لاحقاً، فاستعادتها تعيد إحياء البيانات.
الحل:
1. **سجل إتلاف المفاتيح** append-only، منفصل، مكرر، ولا يخضع للاستعادة من نسخ أقدم.
2. أي استعادة لمخزن المفاتيح تمر ببوابة: قبل فتح أي خدمة، يُعاد تطبيق سجل الإتلاف على المخزن المستعاد، فتُتلف المفاتيح المدرجة من جديد.
3. نسخ مخزن المفاتيح الاحتياطية تُحفظ ≤ 35 يوماً، فتختفي فيزيائياً بعد ذلك.
4. فحص دوري (FIT-19 مقترح): استعادة تجريبية تثبت أن أي مفتاح في السجل غير قابل للاستخدام بعد البوابة.

بهذا يصبح "غير قابل للاسترجاع فوراً" (QAS-PRV-001) صحيحاً عملياً لا نظرياً.

## 5. عقود السياقات المالكة
| العقد | الاتجاه | الغرض |
|---|---|---|
| HoldCheck (OHS، BC08) | المالك → BC08 | قبل أي محو/إتلاف/إنهاء مستأجر |
| DispositionNotice (حدث) | BC08 → المالكون | إفراغ النسخ الواضحة وإعادة بناء الإسقاطات دون الحاويات المتلفة |
| ErasureScope / ErasureConfirm (OHS) | BC08 ↔ BC01/BC02 | تحديد مفاتيح الموضوع وتأكيد الإفراغ |
