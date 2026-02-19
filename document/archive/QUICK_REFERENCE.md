# IDPOS Quick Reference Guide

**Last Updated:** 2026-01-07

## Important Notes

### Character Encoding
⚠️ **Database uses HALF-WIDTH KATAKANA (半角カナ)** - not full-width!

- Correct: `ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ` (half-width)
- Incorrect: `アリエール ジェルボール` (full-width)

---

## Customer Codes

| Code | Name | Name (Japanese) |
|------|------|-----------------|
| `cds_8005` | TSURUHA | ツルハ |
| `cds_8006` | TOMODS | トモズ |
| `cds_8007` | SAPPORO DRUG | サツドラ |
| `cds_8008` | KOHNAN | コーナン |
| `cds_8009` | FUJI YAKUHIN | 富士薬品 |
| `cds_8010` | TRIAL | トライアル |
| `cds_8011` | CHUBU YAKUHIN | 中部薬品 |
| `cds_8012` | CAINZ | カインズ |
| `cds_8013` | SUGI YAKKYOKU | スギ薬局 |

---

## Common P&G Ariel Sub-Brands

| Sub-Brand (Database Format) | Product Name | SKUs |
|-----------------------------|--------------|------|
| `ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ` | Ariel Gel Ball | 403 |
| `ｱﾘｴｰﾙｼﾞｪﾙ` | Ariel Liquid Gel | 454 |
| `ｱﾘｴｰﾙｷﾞﾌﾄ` | Ariel Gift Sets | 310 |
| `ｱﾘｴｰﾙﾐﾗｲ` | Ariel Mirai | 45 |
| `ｱﾘｴｰﾙ粉末` | Ariel Powder | 34 |
| `ｱﾘｴｰﾙ濃縮ｼﾞｪﾙ` | Ariel Concentrated Gel | 9 |
| `ｱﾘｴｰﾙ洗濯槽ｸﾘｰﾅｰ` | Ariel Washer Cleaner | 5 |
| `ｱﾘｴｰﾙｽﾌﾟﾚｰ` | Ariel Spray | 4 |

---

## Common P&G Bold Sub-Brands

| Sub-Brand (Database Format) | Product Name | SKUs |
|-----------------------------|--------------|------|
| `ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ` | Bold Gel Ball | 442 |
| `ﾎﾞｰﾙﾄﾞｼﾞｪﾙ` | Bold Liquid Gel | 382 |
| `ﾎﾞｰﾙﾄﾞｷﾞﾌﾄ` | Bold Gift Sets | 59 |

---

## Common Categories

| Category | Japanese | Note |
|----------|----------|------|
| `Laundry` | 洗濯 | Main laundry category |
| `Fabric Enhancer` | 柔軟剤 | Fabric softeners |
| `Dish Care` | 食器用洗剤 | Dishwashing |

---

## Common Sub-Categories (Laundry)

| Sub-Category | Meaning | SKUs |
|--------------|---------|------|
| `洗濯洗剤` | Laundry Detergent | 6,739 |
| `ﾗﾝﾄﾞﾘｰ_ｿﾉﾀｻﾌﾞｶﾃｺﾞﾘ` | Laundry - Other Sub-categories | 4,033 |
| `業務用` | Commercial/Business Use | 130 |

---

## Product Forms (Laundry)

| Form | Japanese | SKUs |
|------|----------|------|
| `液体非濃縮` | Liquid Non-concentrated | 2,218 |
| `ｷﾞﾌﾄ` | Gift Set | 1,147 |
| `ﾎﾞｰﾙ` | Ball/Pod | 930 |
| `液体濃縮` | Liquid Concentrated | 749 |
| `液体` | Liquid | 663 |
| `粉末` | Powder | 649 |
| `ｽﾌﾟﾚｰ･ﾐｽﾄ` | Spray/Mist | 141 |

---

## Code Examples

### Basic Product Filter
```python
# Specific product - Ariel Gel Ball
target_condition = "jp_sub_brand_alter_lang_name = 'ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ'"

# All Ariel products
target_condition = "jp_sub_brand_alter_lang_name LIKE 'ｱﾘｴｰﾙ%'"

# Multiple products
target_condition = "jp_sub_brand_alter_lang_name IN ('ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ', 'ｱﾘｴｰﾙｼﾞｪﾙ')"
```

### By Brand
```python
target_condition = "jp_brand_name = 'Ariel'"
```

### By Sub-Category
```python
target_condition = "jp_sub_category_alter_lang_name = '洗濯洗剤'"
```

### Customer Selection
```python
customer_filter = 'cds_8005'  # TSURUHA
```

### Date Range
```python
start_date = '2025-01-01'
end_date = '2025-12-31'
```

### Full Analysis Setup Example
```python
# Customer: Tsuruha, 2025, Ariel Gel Ball
customer_filter = 'cds_8005'
start_date = '2025-01-01'
end_date = '2025-12-31'
category_filter = 'Laundry'
target_condition = "jp_sub_brand_alter_lang_name = 'ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ'"
```

---

## Tips

1. **Always use half-width katakana** for Japanese product names in the database
2. **Check the full dictionary** at `data_dictionary_laundry.md` for complete lists
3. **Verify product names** exist in the database before running analysis
4. **Use LIKE operator** with `%` wildcard for broader searches
5. **Date format** is always `YYYY-MM-DD`

---

## File References

- **Full Dictionary:** `data_dictionary_laundry.md`
- **Dictionary Builder Script:** `build_data_dictionary.py`
- **Template Files:** `templates/*.ipynb`
