# IDPOS Reference (Canonical)

**Last Updated:** 2026-02-19  
**Purpose:** Single source of truth for practical IDPOS analysis usage.

---

## 1) Canonical Data Contract

### Main fact table

- `cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw` (`idpos`)

### Main dimension tables

- `id_pos_ai_1.prod_dim_ext_vw` (`prod`)
- `id_pos_ai_1.shopper_dim_generic_vw` (`shopper`)
- `id_pos_ai_1.site_dim_vw` (`site`) — optional
- `id_pos_ai_1.site_dim_ext_vw` (`site_ext`) — optional
- `id_pos_ai_1.cust_dim_ext_vw` (`cust`) — optional

### Standard joins

```sql
FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod
  ON idpos.prod_key = prod.prod_key
LEFT JOIN id_pos_ai_1.shopper_dim_generic_vw shopper
  ON idpos.shopper_key = shopper.shopper_key
LEFT JOIN id_pos_ai_1.site_dim_vw site
  ON idpos.site_key = site.site_key
LEFT JOIN id_pos_ai_1.site_dim_ext_vw site_ext
  ON idpos.site_key = site_ext.site_key
LEFT JOIN id_pos_ai_1.cust_dim_ext_vw cust
  ON site.own_party_key = cust.cust_key
```

---

## 2) Full Column Reference

### Fact table: `loyalty_transact_fct_v1_vw`

| Column                             | Type      | Purpose                                                     |
| ---------------------------------- | --------- | ----------------------------------------------------------- |
| `prod_key`                         | bigint    | JOIN to `prod_dim_ext_vw`                                   |
| `shopper_key`                      | bigint    | JOIN to `shopper_dim_generic_vw`; also shopper ID           |
| `site_key`                         | bigint    | JOIN to `site_dim_vw` / `site_dim_ext_vw`                   |
| `sales_period_group_end_date_part` | string    | **Canonical date field** — partition key, cast to DATE      |
| `data_provider_code_part`          | string    | **Retailer filter** (`cds_8005`–`cds_8017`) — partition key |
| `pos_sales_amt`                    | decimal   | Sales value in JPY (tax included)                           |
| `pos_sales_without_tax_amt`        | decimal   | Sales value (tax excluded)                                  |
| `pos_unit_sales_qty`               | int       | Unit sales quantity                                         |
| `pos_profit_amt`                   | decimal   | Gross profit                                                |
| `shelf_price_amt`                  | decimal   | Unit selling price                                          |
| `promo_ind`                        | string    | Promotion/sale flag                                         |
| `transact_id`                      | string    | Receipt / transaction ID                                    |
| `transact_timestamp`               | timestamp | Transaction datetime                                        |
| `custom_measure_501_text`          | string    | Member class (retailer-specific, e.g. Sugi Yakkyoku)        |

### Product dim: `prod_dim_ext_vw`

**Prefer `prod_dim_ext_vw` over `prod_dim_vw`** — ext tables are standardized across retailers.

| Column                                    | Notes                                                               |
| ----------------------------------------- | ------------------------------------------------------------------- |
| `prod_key`                                | JOIN key                                                            |
| `jp_item_gtin`                            | JAN / EAN / GTIN code                                               |
| `jp_prod_name`                            | Product name (English or full-width)                                |
| `jp_prod_alter_lang_name`                 | Product name (half-width katakana)                                  |
| `jp_brand_name`                           | Brand name (English)                                                |
| `jp_brand_alter_lang_name`                | Brand name (half-width katakana)                                    |
| `jp_sub_brand_name`                       | Sub-brand name (English)                                            |
| `jp_sub_brand_alter_lang_name`            | Sub-brand name (half-width katakana) — **use for filtering**        |
| `jp_mfgr_name`                            | Manufacturer name (English)                                         |
| `jp_mfgr_alter_lang_name`                 | Manufacturer name (Japanese)                                        |
| `jp_category_name`                        | Category — English, e.g. `'Laundry'`                                |
| `jp_category_alter_lang_name`             | Category — half-width katakana                                      |
| `jp_sub_category_name`                    | Sub-category (English)                                              |
| `jp_sub_category_alter_lang_name`         | Sub-category (half-width) — e.g. `'洗濯洗剤'`                       |
| `jp_segment_name`                         | Segment name                                                        |
| `jp_sub_segment_name`                     | Sub-segment name                                                    |
| `jp_segment_1_name` … `jp_segment_6_name` | Segment detail 1–6 (volume, size details etc.)                      |
| `jp_segment_4_name`                       | **Canonical size field**                                            |
| `jp_prod_family_1_name`                   | **Canonical variant field** — English, format: `'SubBrand_Variant'` |
| `jp_prod_family_2_name`                   | Sub-brand detail name (English variant)                             |
| `jp_prod_form_name`                       | Product form (e.g. `'ﾎﾞｰﾙ'`, `'液体濃縮'`)                          |
| `jp_variety_name`                         | Variety (regular/campaign etc.)                                     |
| `jp_size_name`                            | ⚠️ Deprecated for size — use `jp_segment_4_name`                    |
| `jp_pack_size_name`                       | ⚠️ Deprecated for size — use `jp_segment_4_name`                    |

### Shopper dim: `shopper_dim_generic_vw`

Note: also has `data_provider_code_part` column — use same retailer filter when pre-filtering.

| Column              | Notes                                                          |
| ------------------- | -------------------------------------------------------------- |
| `shopper_key`       | JOIN key                                                       |
| `member_ind`        | Loyalty member flag — **always filter `= 'Y'`**                |
| `gender_code`       | `'0'`=Not Registered, `'1'`=Male, `'2'`=Female                 |
| `age`               | Age group in 10s (0, 10, 20, … 90); calculated from birth date |
| `birth_year`        | Birth year                                                     |
| `birth_month`       | Birth month                                                    |
| `communication_ind` | DM opt-in flag                                                 |
| `post_code`         | Zip / postal code                                              |

### Site dims: `site_dim_vw` / `site_dim_ext_vw`

**Prefer `site_dim_ext_vw`** for store attributes — standardized across retailers.

| Column                               | Table             | Notes                                                           |
| ------------------------------------ | ----------------- | --------------------------------------------------------------- |
| `site_key`                           | both              | JOIN key                                                        |
| `own_party_key`                      | `site_dim_vw`     | Used to JOIN `cust_dim_ext_vw` (via `own_party_key = cust_key`) |
| `site_name`                          | `site_dim_vw`     | Store name                                                      |
| `cust_site_level_1_name` … `_6_name` | `site_dim_vw`     | Area hierarchy names                                            |
| `jp_site_name`                       | `site_dim_ext_vw` | Store name (English)                                            |
| `jp_site_alter_lang_name`            | `site_dim_ext_vw` | Store name (Japanese)                                           |
| `jp_store_format_desc`               | `site_dim_ext_vw` | Store format                                                    |
| `jp_site_state_name`                 | `site_dim_ext_vw` | Prefecture                                                      |

### Optional: `calendar_dim_vw`

Join on `idpos.sales_period_group_end_date_part = cal.day_date` for calendar attributes.

### Optional: `cust_dim_ext_vw`

Join via: `site_dim_vw.own_party_key = cust_dim_ext_vw.cust_key`

| Column                                       | Notes                            |
| -------------------------------------------- | -------------------------------- |
| `jp_cust_lvl_1_name` / `_2_name` / `_3_name` | CHQ / RHQ1 / RHQ2 name (English) |
| `jp_cust_lvl_1_alter_lang_name`              | CHQ name (Japanese)              |
| `jp_cust_channel_name`                       | Channel (outlet type)            |
| `jp_cust_sub_channel_name`                   | Sub-channel                      |
| `jp_cust_team_name`                          | Organization (G30/Electro/EMG)   |

---

## 3) Canonical Field Choices (Critical)

| Use case               | Canonical field                    | Rule                                                         |
| ---------------------- | ---------------------------------- | ------------------------------------------------------------ |
| Date filter            | `sales_period_group_end_date_part` | Use for analysis period filtering                            |
| Retailer filter        | `data_provider_code_part`          | Use `cds_XXXX` codes                                         |
| Loyalty shopper filter | `shopper.member_ind`               | Use `= 'Y'`                                                  |
| Category               | `jp_category_name`                 | Laundry default: `'Laundry'`                                 |
| Sub-brand targeting    | `jp_sub_brand_alter_lang_name`     | **Half-width katakana** — see Section 4                      |
| Variant                | `jp_prod_family_1_name`            | English string, format: `'Brand_Variant'` — exact match only |
| Size                   | `jp_segment_4_name`                | Display above variant name                                   |
| Product ID             | `jp_item_gtin`                     | Keep consistent within one analysis                          |
| Sales value            | `pos_sales_amt`                    | JPY                                                          |
| Units                  | `pos_unit_sales_qty`               | Numeric                                                      |

---

## 4) Katakana Encoding (Critical for Correct Filtering)

**Rule:** Columns ending in `_alter_lang_name` store **half-width katakana (半角カナ)** in the actual database.

- ✅ CORRECT (half-width): `'ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ'`
- ❌ WRONG (full-width): `'アリエールジェルボール'`

Template example values that use full-width (e.g. `'アリエール'`, `'ボールド'`) are **illustrative only** and will likely return 0 rows. Always use half-width for actual queries.

### Known valid half-width values

**P&G Ariel sub-brands** (`jp_sub_brand_alter_lang_name`):

| English label  | Half-width katakana value |
| -------------- | ------------------------- |
| Ariel Gel      | `ｱﾘｴｰﾙｼﾞｪﾙ`               |
| Ariel Gel Ball | `ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ`           |
| Ariel Gift     | `ｱﾘｴｰﾙｷﾞﾌﾄ`               |
| Ariel Mirai    | `ｱﾘｴｰﾙﾐﾗｲ`                |
| Ariel Powder   | `ｱﾘｴｰﾙ粉末`               |

**P&G Bold sub-brands** (`jp_sub_brand_alter_lang_name`):

| English label | Half-width katakana value |
| ------------- | ------------------------- |
| Bold Gel Ball | `ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ`          |
| Bold Gel      | `ﾎﾞｰﾙﾄﾞｼﾞｪﾙ`              |
| Bold Gift     | `ﾎﾞｰﾙﾄﾞｷﾞﾌﾄ`              |

### Known valid `jp_prod_family_1_name` variant values

These are **English strings**, not katakana:

| Variant                   | `jp_prod_family_1_name` value |
| ------------------------- | ----------------------------- |
| Ariel Gel Ball (all)      | `'Ariel Gel Ball'`            |
| Ariel Gel Ball Indoor Dry | `'Ariel Gel Ball_Indoor Dry'` |
| Ariel Gel Ball Pro Power  | `'Ariel Gel Ball_Pro Power'`  |
| Bold Gel Ball (all)       | `'Bold Gel Ball'`             |
| Bold Gel Ball Pink        | `'Bold Gel Ball_Pink'`        |
| Bold Gel Ball Blue        | `'Bold Gel Ball_Blue'`        |
| Bold Gel Ball WH-TEA&FL   | `'Bold Gel Ball_WH-TEA&FL'`   |

Format rule: `'<SubBrand> <ProductLine>'` or `'<SubBrand>_<Variant>'`

---

## 5) Retailer Code Map

| `data_provider_code_part` | English Name  | Japanese Name |
| ------------------------- | ------------- | ------------- |
| `cds_8005`                | TSURUHA       | ツルハ        |
| `cds_8006`                | TOMODS        | トモズ        |
| `cds_8007`                | SAPPORO DRUG  | サツドラ      |
| `cds_8008`                | KOHNAN        | コーナン      |
| `cds_8009`                | TRIAL         | トライアル    |
| `cds_8010`                | FUJI YAKUHIN  | 富士薬品      |
| `cds_8011`                | CHUBU YAKUHIN | 中部薬品      |
| `cds_8012`                | CAINZ         | カインズ      |
| `cds_8013`                | SUGI YAKKYOKU | スギ薬局      |
| `cds_8017`                | ARCLANDS      | アークランズ  |

> ⚠️ Note: `cds_8009` = TRIAL, `cds_8010` = FUJI YAKUHIN. Some older code has these swapped — verify with the table above.

---

## 6) Practical Baseline Filters

```sql
WHERE idpos.sales_period_group_end_date_part BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'
  AND idpos.data_provider_code_part IN ('cds_8005', 'cds_8006', 'cds_8007')
  AND shopper.member_ind = 'Y'
  AND prod.jp_category_name = 'Laundry'
```

---

## 7) Reusable Analysis Patterns

### SoV (pre/post)

1. Build one `base` table.
2. Split into pre and post periods.
3. Join by shopper key.

### Next Purchase

1. Identify trial date per shopper.
2. Find first purchase after trial (`ROW_NUMBER` by shopper/date).
3. Use first valid next purchase only.

### Trial / Repeat

- Use lookback (often 365-day) or lag-based classification by shopper.

### NTC extraction

- Standard pattern: `LEFT JOIN pre ... WHERE pre.id IS NULL`

---

## 8) Template Linkage

Use these notebooks as implementation templates:

- `templates/01_ctsr_analysis.ipynb`
- `templates/02_sov.ipynb`
- `templates/03_next_purchase.ipynb`
- `templates/04_copurchase.ipynb`
- `templates/05_venn_diagram.ipynb`
- `templates/06_trial_repeat.ipynb`
- `templates/07_demographics.ipynb`
- `templates/08_shopper_flow.ipynb`

---

## 9) Category Names (`jp_category_name`)

| `jp_category_name` | `jp_category_alter_lang_name` | Common user terms |
| ------------------ | ----------------------------- | ----------------- |
| `Air Care`         | `ｴｱｹｱ`                        | エア、Air         |
| `Appliances`       | `ｱﾌﾟﾗｲｱﾝｽ`                    | エレ、エレクトロ  |
| `Baby Care`        | `ﾍﾞﾋﾞｰｹｱ`                     | ベビー、Baby      |
| `Dish Care`        | `ﾃﾞｨｯｼｭｹｱ`                    | ディッシュ、Dish  |
| `Fabric Enhancer`  | `柔軟剤`                      | FE                |
| `Feminine Care`    | `ﾌｪﾐﾆﾝｹｱ`                     | フェミ、Femi care |
| `Hair Care`        | `ﾍｱｹｱ`                        | ヘア、Hair        |
| `Kitchen Cleaning` | `ｷｯﾁﾝｸﾘｰﾆﾝｸﾞ`                 |                   |
| `Laundry`          | `ﾗﾝﾄﾞﾘｰ`                      |                   |
| `Oral Care`        | `ｵｰﾗﾙｹｱ`                      | Oral              |
| `Shave Care`       | `ｶﾐｿﾘ`                        | シェーブ、Shave   |

For Laundry sub-category filter: `jp_sub_category_alter_lang_name = '洗濯洗剤'` (detergent only; excludes gifting/other)

---

## 10) Conflict Policy

If any file conflicts with this document, use this priority:

1. `IDPOS_REFERENCE.md` (this file)
2. `AI_DICTIONARY.md`
3. Other notes/archive
