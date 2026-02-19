# Skill: Katakana Encoder

**Used by:** Data Engineer (agent 02), Quality Guardian (agent 04)  
**Purpose:** Ensure all `_alter_lang_name` column filters use half-width katakana. Full-width katakana returns 0 rows with no error.

---

## The Rule

Columns ending in `_alter_lang_name` store **half-width katakana (半角カナ)**.

```
❌ Full-width (full-size characters): ア リ エ ー ル  → returns 0 rows, no error
✅ Half-width (compact characters):  ｱﾘｴｰﾙ          → correct, returns data
```

**How to tell them apart:** Half-width characters are visually narrower and distinct.  
**How to verify:** Run `SELECT DISTINCT jp_sub_brand_alter_lang_name` with `LIMIT 10` to compare against the reference table below.

---

## P&G Brand Reference (Half-Width Katakana)

### Ariel Sub-brands

| Sub-brand (English) | `jp_sub_brand_alter_lang_name` |
|--------------------|-----------------------------|
| Ariel Gel | `ｱﾘｴｰﾙｼﾞｪﾙ` |
| Ariel Gel Ball | `ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ` |
| Ariel Mirai | `ｱﾘｴｰﾙﾐﾗｲ` |
| Ariel Powder | `ｱﾘｴｰﾙ粉末` |
| All Ariel (wildcard) | `LIKE 'ｱﾘｴｰﾙ%'` |

### Bold Sub-brands

| Sub-brand (English) | `jp_sub_brand_alter_lang_name` |
|--------------------|-----------------------------|
| Bold Gel | `ﾎﾞｰﾙﾄﾞｼﾞｪﾙ` |
| Bold Gel Ball | `ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ` |
| All Bold (wildcard) | `LIKE 'ﾎﾞｰﾙﾄﾞ%'` |

---

## `jp_prod_family_1_name` Variant Reference (English — no katakana)

The variant column uses **English** — no katakana required here.

| Variant | `jp_prod_family_1_name` |
|---------|------------------------|
| Ariel Gel Ball (standard) | `'Ariel Gel Ball'` |
| Ariel Gel Ball Indoor Dry | `'Ariel Gel Ball_Indoor Dry'` |
| Ariel Gel Ball Pro Power | `'Ariel Gel Ball_Pro Power'` |
| Bold Gel Ball (standard) | `'Bold Gel Ball'` |
| Bold Gel Ball Pink | `'Bold Gel Ball_Pink'` |
| Bold Gel Ball Blue | `'Bold Gel Ball_Blue'` |
| Bold Gel Ball WH-Tea & Fl | `'Bold Gel Ball_WH-TEA&FL'` |

Use **exact match** (`=`) for variant filters, not LIKE.

---

## Brand Reference (half-width katakana)

| Brand | `jp_brand_alter_lang_name` |
|-------|--------------------------|
| Ariel | `ｱﾘｴｰﾙ` |
| Bold | `ﾎﾞｰﾙﾄﾞ` |

---

## SQL Filter Examples

```sql
-- Single sub-brand
AND prod.jp_sub_brand_alter_lang_name = 'ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ'

-- Multiple sub-brands
AND prod.jp_sub_brand_alter_lang_name IN ('ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ', 'ｱﾘｴｰﾙｼﾞｪﾙ')

-- Wildcard (all Ariel)
AND prod.jp_sub_brand_alter_lang_name LIKE 'ｱﾘｴｰﾙ%'

-- Variant (English — use exact match)
AND prod.jp_prod_family_1_name = 'Ariel Gel Ball_Indoor Dry'

-- Category (English — no katakana needed)
AND prod.jp_category_name = 'Laundry'

-- Sub-category (half-width — detergent only, excludes gifting)
AND prod.jp_sub_category_alter_lang_name = '洗濯洗剤'
```

---

## Historical Error to Avoid

From the initiative repeat tracking analysis (Jan 2026):

```sql
-- ❌ WRONG: Used jp_prod_name with full-width Japanese text
WHERE jp_prod_name LIKE '%インドアドライ%'       -- returned partial/wrong results

-- ✅ CORRECT: Use jp_prod_family_1_name with exact English match
WHERE prod.jp_prod_family_1_name = 'Ariel Gel Ball_Indoor Dry'  -- canonical
```

**Archived in:** `document/archive/VARIANT_COLUMN_REFERENCE.md`

---

## Verification Query

When in doubt, run this to get actual values from the database:

```sql
SELECT DISTINCT
    jp_sub_brand_alter_lang_name,
    jp_brand_alter_lang_name,
    jp_prod_family_1_name,
    COUNT(*) AS sku_count
FROM id_pos_ai_1.prod_dim_ext_vw
WHERE jp_category_name = 'Laundry'
  AND jp_sub_brand_alter_lang_name LIKE 'ｱﾘｴｰﾙ%'
GROUP BY 1, 2, 3
ORDER BY sku_count DESC
LIMIT 20
```
