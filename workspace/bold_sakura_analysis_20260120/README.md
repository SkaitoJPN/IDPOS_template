# Bold Sakura Analysis - December 2025

## Project Overview

**Analysis Date:** 2026/01/20  
**Objective:** Evaluate Bold Sakura performance and establish next year launch strategy

## Background

- December 2025: Bold Sakura launched
- Initiative objective: Trial user acquisition
- Bold Gel Ball Sakura performed well in 2024 → expanded to Bold Gel

## Key Questions

1. What is Bold's December status? (Value IYA, Unit IYA, Value Share)
2. How much did Bold Sakura contribute?
3. Did Bold Gel acquire unique users? (SoV analysis)
4. Should we continue Bold Gel Sakura next year? (Store distribution analysis)

## Hypothesis

- H1: Total Bold (Gel + Gel Ball) is flat vs YA because Bold Gel underperforms
- H2: Bold Gel acquired unique users despite flat value share → success

## Product Information

### Bold Sakura GTIN Codes

| Product              | GTIN          | Type     |
| -------------------- | ------------- | -------- |
| Bold Gel Ball Sakura | 4987176344250 | Gel Ball |
| Bold Gel Ball Sakura | 4987176344229 | Gel Ball |
| Bold Gel Ball Sakura | 4987176344236 | Gel Ball |
| Bold Gel Sakura      | 4987176349668 | Gel      |
| Bold Gel Sakura      | 4987176349682 | Gel      |
| Bold Gel Sakura      | 4987176349712 | Gel      |

### Sub-brand Names (half-width katakana)

- Bold Gel Ball: `ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ`
- Bold Gel: `ﾎﾞｰﾙﾄﾞｼﾞｪﾙ`

## Analysis Structure

### 1. Total Bold December Status

- Value IYA (Index Year Ago)
- Unit IYA
- Value Share (National & Channel)

### 2. Bold Sakura Contribution

- Sakura vs Regular contribution
- Gel Ball Sakura vs Gel Sakura breakdown

### 3. SoV (Source of Volume) Analysis

- Compare TY vs YA Bold Sakura shopper acquisition
- Identify unique user acquisition by Bold Gel Sakura

### 4. Store Level Distribution Analysis

- Gel Ball Only stores vs Both products stores
- Performance comparison to determine next year strategy

## Files

- `bold_sakura_analysis.ipynb` - Main analysis notebook
- `bold_sakura_analysis_YYYYMMDD.xlsx` - Output results

## Data Sources

- Transaction: `cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw`
- Product: `id_pos_ai_1.prod_dim_ext_vw`
- Site: `id_pos_ai_1.site_dim_ext_vw`
- Customer: `id_pos_ai_1.cust_dim_ext_vw`
