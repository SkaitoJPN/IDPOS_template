# Skill: SQL Builder

**Used by:** Data Engineer (agent 02)  
**Purpose:** Canonical SQL patterns for IDPOS queries. Always apply the baseline filter block first, then build the analysis-specific logic on top.

---

## Baseline Filter Block (Apply to Every Query)

```sql
WHERE idpos.sales_period_group_end_date_part BETWEEN '{start_date}' AND '{end_date}'
  AND idpos.data_provider_code_part IN ({retailer_codes})      -- e.g. 'cds_8005', 'cds_8013'
  AND prod.jp_category_name = 'Laundry'                        -- adjust for category
  AND shopper.member_ind = 'Y'                                  -- loyalty members only
```

**Always filter at this level before any GROUP BY or aggregation.**

---

## Table Reference Block

```sql
FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
JOIN id_pos_ai_1.prod_dim_ext_vw                 prod    ON idpos.prod_key    = prod.prod_key
JOIN id_pos_ai_1.shopper_dim_generic_vw          shopper ON idpos.shopper_key = shopper.shopper_key
-- Optional joins:
-- JOIN id_pos_ai_1.site_dim_ext_vw              site    ON idpos.site_key    = site.site_key
-- JOIN id_pos_ai_1.cust_dim_ext_vw              cust    ON idpos.cust_key    = cust.cust_key
```

Rules:
- Always use `prod_dim_ext_vw` (not `prod_dim_vw`)
- Always use `gold_customer_loyalty` (never `silver_customer_loyalty`)
- Only add `site` and `cust` joins when analysis requires store-level or customer-level attributes

---

## Pattern 1: Basic Sales Aggregation

```sql
SELECT
    prod.jp_prod_family_1_name          AS variant,
    prod.jp_segment_4_name              AS size,
    SUM(idpos.pos_sales_amt)            AS total_sales_jpy,
    SUM(idpos.pos_unit_sales_qty)       AS total_units,
    COUNT(DISTINCT idpos.shopper_key)   AS unique_shoppers,
    COUNT(DISTINCT idpos.transact_id)   AS total_transactions
FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
JOIN id_pos_ai_1.prod_dim_ext_vw prod    ON idpos.prod_key    = prod.prod_key
JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
WHERE idpos.sales_period_group_end_date_part BETWEEN '{start_date}' AND '{end_date}'
  AND idpos.data_provider_code_part IN ('{retailer_code}')
  AND prod.jp_category_name = 'Laundry'
  AND shopper.member_ind = 'Y'
GROUP BY 1, 2
ORDER BY total_sales_jpy DESC
```

---

## Pattern 2: Source of Volume (SoV)

```sql
-- Step 1: Identify target purchasers in post-period
WITH post_purchasers AS (
    SELECT DISTINCT idpos.shopper_key
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part BETWEEN '{post_start}' AND '{post_end}'
      AND idpos.data_provider_code_part IN ('{retailer_code}')
      AND {target_product_filter}          -- e.g. prod.jp_prod_family_1_name = 'Bold Gel Ball'
      AND shopper.member_ind = 'Y'
),
-- Step 2: Look up what they bought in pre-period
pre_purchases AS (
    SELECT
        idpos.shopper_key,
        prod.jp_prod_family_1_name   AS pre_variant,
        SUM(idpos.pos_sales_amt)     AS pre_sales
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part BETWEEN '{pre_start}' AND '{pre_end}'
      AND idpos.data_provider_code_part IN ('{retailer_code}')
      AND prod.jp_category_name = 'Laundry'
      AND shopper.member_ind = 'Y'
      AND idpos.shopper_key IN (SELECT shopper_key FROM post_purchasers)
    GROUP BY 1, 2
)
SELECT pre_variant, SUM(pre_sales) AS sales, COUNT(DISTINCT shopper_key) AS shoppers
FROM pre_purchases
GROUP BY 1
ORDER BY shoppers DESC
```

---

## Pattern 3: Next Purchase (Window Function)

```sql
WITH ranked_purchases AS (
    SELECT
        idpos.shopper_key,
        idpos.sales_period_group_end_date_part  AS purchase_date,
        prod.jp_prod_family_1_name              AS variant,
        ROW_NUMBER() OVER (
            PARTITION BY idpos.shopper_key
            ORDER BY idpos.sales_period_group_end_date_part ASC
        ) AS purchase_rank
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part BETWEEN '{start_date}' AND '{end_date}'
      AND idpos.data_provider_code_part IN ('{retailer_code}')
      AND prod.jp_category_name = 'Laundry'
      AND shopper.member_ind = 'Y'
),
target_purchase AS (
    SELECT shopper_key, purchase_date AS target_date, purchase_rank AS target_rank
    FROM ranked_purchases
    WHERE {target_product_filter}
),
next_purchase AS (
    SELECT r.shopper_key, r.variant AS next_variant, r.purchase_date AS next_date
    FROM ranked_purchases r
    JOIN target_purchase t ON r.shopper_key = t.shopper_key
    WHERE r.purchase_rank = t.target_rank + 1
      AND DATEDIFF(r.purchase_date, t.target_date) <= {max_days_between}   -- default 90
)
SELECT next_variant, COUNT(DISTINCT shopper_key) AS shoppers
FROM next_purchase
GROUP BY 1
ORDER BY shoppers DESC
```

---

## Pattern 4: Trial / Repeat Classification

```sql
WITH analysis_purchasers AS (
    SELECT DISTINCT idpos.shopper_key, MIN(idpos.sales_period_group_end_date_part) AS first_purchase_in_period
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part BETWEEN '{analysis_start}' AND '{analysis_end}'
      AND idpos.data_provider_code_part IN ('{retailer_code}')
      AND {target_product_filter}
      AND shopper.member_ind = 'Y'
    GROUP BY 1
),
lookback_purchasers AS (
    SELECT DISTINCT idpos.shopper_key
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.data_provider_code_part IN ('{retailer_code}')
      AND {target_product_filter}
      AND shopper.member_ind = 'Y'
      AND idpos.sales_period_group_end_date_part < '{analysis_start}'
      AND DATEDIFF('{analysis_start}', idpos.sales_period_group_end_date_part) <= {lookback_days}  -- default 365
)
SELECT
    a.shopper_key,
    CASE WHEN l.shopper_key IS NOT NULL THEN 'Repeat' ELSE 'Trial' END AS shopper_type
FROM analysis_purchasers a
LEFT JOIN lookback_purchasers l ON a.shopper_key = l.shopper_key
```

---

## Pattern 5: Co-purchase (Market Basket)

```sql
WITH target_baskets AS (
    SELECT DISTINCT idpos.transact_id, idpos.shopper_key
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part BETWEEN '{start_date}' AND '{end_date}'
      AND idpos.data_provider_code_part IN ('{retailer_code}')
      AND {target_product_filter}
      AND shopper.member_ind = 'Y'
),
copurchase_items AS (
    SELECT t.transact_id, prod.{copurchase_granularity} AS copurchase_item
    FROM target_baskets t
    JOIN cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos ON t.transact_id = idpos.transact_id
    JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    WHERE prod.jp_category_name = 'Laundry'
      AND NOT ({target_product_filter})   -- exclude target product from co-purchase items
)
-- Further aggregation for Support / Confidence / Lift done in Python
SELECT copurchase_item, COUNT(DISTINCT transact_id) AS co_basket_count
FROM copurchase_items
GROUP BY 1
ORDER BY co_basket_count DESC
```

---

## Performance Rules

1. **Always filter partition columns in WHERE** — `sales_period_group_end_date_part` and `data_provider_code_part` are partition keys; filter these first.
2. **Start narrow for testing** — use 1-week date range to validate query before expanding to full analysis period.
3. **Only join what is needed** — avoid adding `site` or `cust` joins unless explicitly required.
4. **No SELECT \*** — always specify columns to reduce data transfer.
