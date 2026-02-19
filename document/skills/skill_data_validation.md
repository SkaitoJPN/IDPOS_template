# Skill: Data Validation

**Used by:** Quality Guardian (agent 04), Data Scientist (agent 03)  
**Purpose:** Mandatory checks before any result is passed to Story Teller. All 5 checks must pass (or exceptions must be documented).

---

## The 5-Check Quality Gate

Run every check in order. A failure stops the pipeline and routes back to the responsible agent.

### Check 1 — Row Count

```python
row_count = len(df)
print(f"Rows: {row_count:,}")

# Expected ranges (single retailer / category / quarter):
# Shopper-level: 1,000 – 500,000
# Aggregated: 10 – 10,000
# ⚠️ If 0 → query returned nothing (check filters, katakana encoding, date range)
# ⚠️ If >10M → date range or scope too wide, consider chunking
```

### Check 2 — Date Range

```python
date_col = 'sales_period_group_end_date_part'  # canonical date column
print(f"Date range: {df[date_col].min()} → {df[date_col].max()}")

# ✅ Must match intended analysis period
# ⚠️ If min/max is earlier or later than expected → date filter misapplied
# ⚠️ If only one date value → may be filtering for exact date instead of range
```

### Check 3 — Null Check (Key Columns)

```python
key_columns = ['shopper_key', date_col, 'pos_sales_amt', 'jp_prod_family_1_name']
null_counts = df[key_columns].isnull().sum()
print(null_counts)

# ✅ Expect 0 nulls in key identifier and measurement columns
# ⚠️ Nulls in product columns → possible unmatched join on prod_dim
# ⚠️ Nulls in shopper_key → unmatched shopper join (check member_ind filter)
```

### Check 4 — Duplicate Check

```python
dup_count = df.duplicated().sum()
print(f"Duplicate rows: {dup_count:,}")

# ✅ Expect 0 for transaction-level data
# ⚠️ Duplicates on shopper-period grain → GROUP BY may be missing a dimension
# If intentional (e.g., same shopper bought same variant twice), document it
```

### Check 5 — Shopper Count Sanity

```python
shopper_count = df['shopper_key'].nunique()
print(f"Unique shoppers: {shopper_count:,}")

# Expected:
# Single product / retailer / quarter: 1,000 – 20,000
# Full category / all retailers / year: 50,000 – 500,000
# ⚠️ <100 → sample too small (flag and report)
# ⚠️ >1,000,000 → scope may be too wide, or member_ind filter missing
```

---

## Statistical Validation

### Minimum Sample Size

```python
MIN_SHOPPERS = 100

if shopper_count < MIN_SHOPPERS:
    print(f"⚠️ WARNING: Sample size {shopper_count} < {MIN_SHOPPERS}. Results unreliable.")
    # — Route back to CEO to confirm scope before proceeding
```

### Outlier Detection

```python
value_col = 'pos_sales_amt'
q99 = df[value_col].quantile(0.99)
max_val = df[value_col].max()

if max_val > 10 * q99:
    print(f"⚠️ WARNING: Extreme outlier detected (max={max_val:,.0f}, P99={q99:,.0f})")
    print("Investigate before aggregating — outlier may skew averages significantly")
```

### Variance Check

```python
cv = df[value_col].std() / df[value_col].mean()  # Coefficient of variation
if cv > 1.0:
    print(f"⚠️ CAUTION: High variance (CV={cv:.2f}). Averages may be misleading — use median too.")
```

### Significance Reporting (for A/B or period comparisons)

Always report alongside any comparative finding:
- Sample size: "Based on N = X shoppers"
- Time period: "Q4 2024 vs Q4 2023"
- Confidence interval: "95% CI: ± Y%"
- Significance: "Statistically significant at p < 0.05" or "Not statistically significant (p = Z)"

---

## Order-of-Magnitude Sanity Checks

```python
# Total sales value (¥)
assert df['pos_sales_amt'].sum() > 1_000_000, \
    f"Total ¥{df['pos_sales_amt'].sum():,.0f} seems too low for this scope"

# Age range (if demographics analysis)
if 'age' in df.columns:
    assert df['age'].between(0, 100).all(), "Age values out of 0–100 range"

# Repeat rate (if trial/repeat)
if 'repeat_rate' in df.columns:
    assert df['repeat_rate'].between(0, 1).all(), "Repeat rate must be between 0 and 1"

# Lift (if market basket)
if 'lift' in df.columns:
    assert (df['lift'] > 0).all(), "Lift must be positive"
    # Typical range: 0.5 – 10; values > 20 are suspicious
    suspicious = df[df['lift'] > 20]
    if len(suspicious) > 0:
        print(f"⚠️ {len(suspicious)} rows with lift > 20 — verify basket size")
```

---

## Common Failure → Root Cause → Fix

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| 0 rows returned | Full-width katakana / wrong retailer code / wrong date format | `skill_katakana_encoder`, check retailer code map |
| Null product columns | Wrong dim table (`prod_dim_vw` instead of `prod_dim_ext_vw`) | Data Engineer corrects join |
| Shopper count implausibly high | Missing `member_ind = 'Y'` filter | Data Engineer adds loyalty filter |
| Extreme duplicate count | Missing GROUP BY dimension (e.g. retailer or date) | Data Engineer adds dimension |
| Orders of magnitude too low | Silver table used instead of Gold | Data Engineer corrects table reference |
| Repeat rate > 1 | Division error in lookback logic | Data Scientist fixes calculation |

---

## Quality Report Template

```
Quality Gate Report — [Analysis Name]
======================================
Date: [YYYY-MM-DD]
Analyst: [Name / Copilot]

Check 1  Rows:             [N]        ✅ / ⚠️ [note]
Check 2  Date range:       [start]–[end]  ✅ / ⚠️ [note]
Check 3  Nulls (key cols): [count]    ✅ / ⚠️ [note]
Check 4  Duplicates:       [count]    ✅ / ⚠️ [note]
Check 5  Unique shoppers:  [N]        ✅ / ⚠️ [note]

Statistical note: n = [X]; [any flags]
Logic checks:     [any pitfalls detected and resolved]
Exceptions:       [anything that passed with caveats]

Status: PASS / HOLD (resolve [issue] before Story Teller)
```
