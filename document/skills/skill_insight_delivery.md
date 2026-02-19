# Skill: Insight Delivery

**Used by:** Story Teller (agent 05), CEO (agent 01 — for review)  
**Purpose:** Standard output structure for non-analyst-friendly analysis delivery. Every analysis must produce this format.

---

## Standard Output Structure

```markdown
# [Analysis Title]

[Plain-language restatement of the business question]

**Date:** [YYYY-MM-DD]  
**Scope:** [Retailer(s), Category, Time Period, Shopper Type]  
**Templates used:** [e.g., 02_SoV + 05_Venn + 06_Trial/Repeat]

---

## Executive Summary

- [Finding 1: What changed / what we found, with ¥ or % impact — 1 sentence]
- [Finding 2: Business implication — 1 sentence]
- [Finding 3: Biggest risk or opportunity — 1 sentence]

---

## Business Impact

| Metric                     | Value        |
| -------------------------- | ------------ |
| Revenue opportunity / risk | ¥XXX million |
| Market share impact        | +/- X.X%     |
| Shoppers affected          | XXX,XXX      |
| [Other relevant KPI]       | [Value]      |

---

## Key Insights

### [Insight 1 Title — states the finding]

- **What the data shows:** [Plain description, no jargon]
- **Why it matters:** [Business implication in ¥ or competitive terms]
- **What to do:** [Specific action]
- **Expected impact:** [Quantified: ¥, %, or shopper count]

### [Insight 2 Title]

[Same format]

### [Insight 3 Title]

[Same format]

---

## Recommendations

| Priority | Timeframe   | Action                                   | Expected Impact    |
| -------- | ----------- | ---------------------------------------- | ------------------ |
| 1        | 0–30 days   | [Specific tactical step — who does what] | [¥ / % / shoppers] |
| 2        | 1–3 months  | [Strategic initiative]                   | [¥ / % / shoppers] |
| 3        | 3–12 months | [Transformational change]                | [¥ / % / shoppers] |

---

## Risks & Limitations

- **[Risk 1]:** [What it means + mitigation]
- **[Risk 2]:** [What it means + mitigation]
- **Data limitation:** [What the data cannot tell us, and what that means for confidence in conclusions]

---

## Supporting Data

[Charts with insight-stating titles]

[Key tables — max 10 rows, sorted by most important metric]

---

## Methodology

- **Data source:** `cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw`
- **Date range:** [start] to [end]
- **Retailers:** [list]
- **Shopper type:** Loyalty program members (`member_ind = 'Y'`)
- **Category:** [Category name]
- **Key assumptions:** [List (e.g., "Trial defined as no purchase in prior 365 days")]
```

---

## Language Translation Table

Story Teller must replace analyst terms with business language:

| Analyst term            | Business language                                                |
| ----------------------- | ---------------------------------------------------------------- |
| `jp_prod_family_1_name` | "variant"                                                        |
| `member_ind = 'Y'`      | "ID"                                                             |
| `shopper_key`           | "shopper"                                                        |
| `pos_sales_amt`         | "value (¥)"                                                      |
| `transact_id`           | "purchase transaction"                                           |
| "lift = 3.2"            | "3.2× more likely to be bought together"                         |
| "p < 0.05"              | "this finding is statistically reliable"                         |
| "cohort"                | "group of shoppers"                                              |
| "first-time buyer"      | "trial shopper"                                                  |
| "repeat rate 11.75%"    | "roughly 1 in 8 new buyers returned to purchase again"           |
| "YoY -12%"              | "sales fell 12% vs the same period last year"                    |
| "IYA"                   | "vs last year"                                                   |
| "C-TSR"                 | "our growth framework (Customers × Frequency × Spend × Loyalty)" |
| "SoV"                   | "where sales came from"                                          |
| "Venn overlap 30%"      | "3 in 10 shoppers buy both products"                             |

---

## Recommendation Specificity Standard

**Generic (not accepted):**

> "Increase marketing investment."

**Specific (required):**

> "Run a loyalty coupon offer targeting the 15,200 lapsed Ariel Gel Ball shoppers at TSURUHA who last purchased >90 days ago. Offer ¥200 off on next purchase. Expected recovery: 20% reactivation = 3,040 shoppers = ¥9M in recovered sales."

A recommendation is specific enough when it answers: **Who** does **what**, for **which customers**, at **which retailer**, by **when**, producing **what outcome (¥)**.

---

## Before Delivering Checklist

- [ ] All statistical terms translated to plain language
- [ ] Every ¥ or % impact quantified (no "significant" without a number)
- [ ] Recommendations are specific (who, what, which customers, where, by when)
- [ ] Charts have insight-stating titles (not variable names)
- [ ] Limitations noted
- [ ] CEO has reviewed and approved
- [ ] Output can be read by a brand manager with no data background
