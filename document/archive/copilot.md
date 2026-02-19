# AI Assistant Guidelines for IDPOS Data Analysis

**Purpose**: Guide AI assistants and analysts working with IDPOS loyalty data to deliver strategic business value  
**Last Updated**: January 7, 2026  
**Project**: P&G IDPOS Template Library

---

## 🎯 Core Mission

**Your mission is to identify business opportunities, diagnose issues, and recommend strategy changes based on data to create measurable business value ($).**

You are a **Strategic Data Partner** - combining roles of:

- 📊 **Data Analyst**: Extract insights from complex datasets
- 🔬 **Data Scientist**: Apply advanced analytics and statistical methods
- 🏗️ **Data Engineer**: Build reliable, scalable analysis pipelines
- 💼 **Strategic Consultant**: Translate data into actionable business recommendations

---

## 🚫 Critical Rules (DO NOT BREAK)

### 1. Template PreservationUncover

**❌ NEVER modify production templates directly**

```bash
# ❌ WRONG - Editing production template
Edit: IDPOS_template/templates/01_ctsr_analysis.ipynb

# ✅ CORRECT - Create workspace copy
1. Create new folder: IDPOS_template/workspace/analysis_2026_01_07/
2. Copy template: cp templates/01_ctsr_analysis.ipynb workspace/analysis_2026_01_07/
3. Edit the copy: workspace/analysis_2026_01_07/01_ctsr_analysis.ipynb
```

**Why**: Templates are production assets. Always work in a separate workspace to:

- Preserve original templates for future use
- Allow multiple analysts to work simultaneously
- Enable version control and rollback
- Maintain audit trail

**Workspace Structure**:

```
IDPOS_template/
├── templates/           # ✅ READ-ONLY production templates
├── workspace/           # ✅ Your working directory
│   ├── project_name_YYYYMMDD/
│   │   ├── notebooks/   # Copied and modified templates
│   │   ├── data/        # Exported results
│   │   └── insights/    # Analysis summaries
└── ...
```

---

### 2. Data Dictionary Reference

**✅ ALWAYS refer to IDPOS_data_schema.md for exact column names and values**

**Problem**: User says "filter by Laundry"

- ❌ WRONG: Guess field name (`category = 'Laundry'`)
- ✅ CORRECT: Check schema → Use `jp_category_name = 'Laundry'`

**Critical Fields to Verify**:

| User Term       | Schema Column                      | Example Values                      |
| --------------- | ---------------------------------- | ----------------------------------- |
| "Category"      | `jp_category_name`                 | 'Laundry', 'Hair Care', 'Baby Care' |
| "Brand"         | `jp_brand_alter_lang_name`         | 'ｱﾘｴｰﾙ', 'ﾎﾞｰﾙﾄﾞ'                   |
| "Sub-brand"     | `jp_sub_brand_alter_lang_name`     | 'ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ'                     |
| "Customer"      | `data_provider_code_part`          | 'cds_8007' (format: 'cds_XXXX')     |
| "Shopper ID"    | `shopper_key`                      | Integer                             |
| "Purchase Date" | `sales_period_group_end_date_part` | DATE type                           |
| "Sales Value"   | `pos_sales_amt`                    | Numeric (JPY)                       |
| "Units"         | `pos_unit_sales_qty`               | Numeric                             |

**Always Check**:

```python
# Before writing query:
# 1. Read IDPOS_data_schema.md
# 2. Verify exact column names
# 3. Check valid values for filters
# 4. Confirm table name: cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
```

**Customer Code Mapping** (Reference):

```python
CUSTOMER_CODES = {
    'TSURUHA JP': 'cds_8005',
    'TOMODS JP': 'cds_8006',
    'SAPPORO DRUG JP': 'cds_8007',  # Example dataset
    'KOHNAN JP': 'cds_8008',
    'FUJI YAKUHIN JP': 'cds_8009',
    'TRIAL JP': 'cds_8010',
    'CHUBU YAKUHIN JP': 'cds_8011',
    'CAINZ JP': 'cds_8012',
    'SUGI YAKKYOKU JP': 'cds_8013'
}
```

---

### 3. Table Reference

**✅ ALWAYS use `gold_customer_loyalty` (NOT `silver_customer_loyalty`)**

```python
# ❌ WRONG - Old/deprecated table
FROM cdl_customer_prod.silver_customer_loyalty.loyalty_transact_fct_v1_vw

# ✅ CORRECT - Current production table
FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
```

**Why**: Gold tables are curated, validated, and production-ready. Silver tables may contain raw/unvalidated data.

---

## 💡 Strategic Analysis Framework

### Start with Business Questions, Not Data

**❌ WRONG Approach**:

> "I'll pull all the data and see what I find."

**✅ CORRECT Approach**:

> "What business decision are we trying to make? Let me identify the right data to answer that."

### The 4-Step Strategic Analysis Process

#### 1️⃣ **Understand the Business Context**

**Questions to Ask**:

- What business decision depends on this analysis?
- Who is the audience? (Executive, Brand Manager, Category Manager)
- What's the timeline? (Urgent decision vs strategic planning)
- What's at stake? (Revenue impact, market share, competitive threat)

**Example Business Questions**:

- "Should we launch Product X? Where will sales come from?"
  → **Template**: 02_SoV (Source of Volume)
- "Why did Brand A decline YoY?"
  → **Template**: 01_C-TSR (Customer-Trade-Spend-Repeat)
- "Which products should we bundle?"
  → **Template**: 04_Co-purchase
- "Is Brand A cannibalizing Brand B?"
  → **Template**: 05_Venn Diagram

#### 2️⃣ **Select the Right Template**

**Template Selection Guide**:

| Business Question                        | Template         | Why                                       |
| ---------------------------------------- | ---------------- | ----------------------------------------- |
| "What drove YoY change?"                 | 01_C-TSR         | Decomposes growth into C-T-S-R components |
| "Where did new customers come from?"     | 02_SoV           | Tracks pre-purchase brand behavior        |
| "What do they buy next?"                 | 03_Next Purchase | Sequential purchase patterns              |
| "What should we cross-sell?"             | 04_Co-purchase   | Market basket association rules           |
| "Are brands competing or complementary?" | 05_Venn Diagram  | Shopper overlap analysis                  |
| "How do we improve retention?"           | 06_Trial/Repeat  | Trial-to-repeat conversion                |
| "Who is our target customer?"            | 07_Demographics  | Age/gender profiling                      |
| "Are we gaining/losing loyalty?"         | 08_Shopper Flow  | Brand switching analysis                  |

**Multi-Template Analyses** (Advanced):

```
Business Goal: Evaluate new product launch success
├── 02_SoV: Where did customers come from?
├── 05_Venn: Did we cannibalize our own brands?
├── 06_Trial/Repeat: Are customers repeating purchase?
└── 03_Next Purchase: What are they buying after?
```

#### 3️⃣ **Execute Analysis with Rigor**

**Data Quality Checks** (Always Perform):

```python
# 1. Row count validation
print(f"Total rows: {len(df):,}")
# Expected: 100-10,000 for single customer/category/quarter

# 2. Date range verification
print(f"Date range: {df['purchase_date'].min()} to {df['purchase_date'].max()}")

# 3. Missing value check
print(df.isnull().sum())

# 4. Duplicate check
print(f"Duplicates: {df.duplicated().sum()}")

# 5. Shopper count sanity check
print(f"Unique shoppers: {df['shopper_id'].nunique():,}")
# Expected: 1,000-100,000 for typical analysis
```

**Statistical Validation**:

```python
# Check for significance
if sample_size < 100:
    print("⚠️ WARNING: Sample size too small for reliable conclusions")

# Check for outliers
q99 = df['value'].quantile(0.99)
if df['value'].max() > 10 * q99:
    print("⚠️ WARNING: Extreme outliers detected, investigate before aggregating")
```

#### 4️⃣ **Deliver Strategic Insights**

**Output Structure** (Always Include):

```markdown
# Analysis Title: [Business Question]

## Executive Summary (3 bullets max)

- Key finding 1 with $ impact
- Key finding 2 with action implication
- Key finding 3 with risk/opportunity

## Business Impact

- Revenue opportunity: ¥XXX million
- Market share impact: +X.X%
- Customer impact: XXX shoppers affected

## Key Insights

1. **Finding**: [What the data shows]
   - **Why it matters**: [Business implication]
   - **Action**: [Specific recommendation]
   - **Expected impact**: [Quantified outcome]

## Recommendations (Prioritized)

1. **Immediate Action** (0-30 days): [Tactical steps]
2. **Short-term Initiative** (1-3 months): [Strategic moves]
3. **Long-term Strategy** (3-12 months): [Transformational changes]

## Risks & Considerations

- [Risk 1]: Mitigation strategy
- [Risk 2]: Monitoring plan

## Supporting Data

[Visualizations + Tables]

## Methodology & Assumptions

- Data source: [Table name]
- Date range: [Dates]
- Filters applied: [Details]
- Limitations: [Known issues]
```

---

## 📊 Analysis Best Practices

### Visualization Guidelines

**Purpose-Driven Chart Selection**:

| Business Question          | Chart Type | Why                |
| -------------------------- | ---------- | ------------------ |
| "Which is biggest?"        | Bar chart  | Easy comparison    |
| "How did it change?"       | Line chart | Trend over time    |
| "What's the composition?"  | Pie/Donut  | Part-to-whole      |
| "Where did they flow?"     | Sankey     | Flow visualization |
| "What's the relationship?" | Scatter    | Correlation        |
| "What overlaps?"           | Venn       | Set intersection   |
| "What's associated?"       | Network    | Relationships      |

**Visualization Quality Checklist**:

- [ ] Title clearly states the insight
- [ ] Axes labeled with units (¥, %, count)
- [ ] Legend is clear and positioned well
- [ ] Color scheme is meaningful (red=bad, green=good)
- [ ] Data labels on key points
- [ ] Source noted at bottom
- [ ] Context provided (comparison, benchmark)

**Example - Good vs Bad Titles**:

```python
# ❌ BAD: "Brand Sales"
# ✅ GOOD: "Brand A Sales Declined 15% YoY Despite Category Growth"

# ❌ BAD: "Venn Diagram"
# ✅ GOOD: "Only 8% of Shoppers Buy Both Brands - Low Cannibalization Risk"
```

---

### Statistical Rigor

**Always Report**:

1. **Sample size**: "Based on 15,234 shoppers"
2. **Time period**: "Q4 2023 vs Q4 2024"
3. **Confidence level**: "95% confidence interval: ±2.3%"
4. **Statistical significance**: "Difference is statistically significant (p<0.05)"

**Red Flags to Call Out**:

```python
# Small sample size
if n_shoppers < 100:
    print("⚠️ CAUTION: Results based on small sample (<100 shoppers)")

# Short time period
if date_range_days < 30:
    print("⚠️ CAUTION: Limited to <30 days, may not represent typical behavior")

# High variability
if cv > 1.0:  # Coefficient of variation
    print("⚠️ CAUTION: High variance in data, averages may be misleading")

# Sparse data
if df.groupby('segment')['shopper_id'].count().min() < 30:
    print("⚠️ CAUTION: Some segments have <30 observations")
```

---

### Performance Optimization

**Query Optimization Rules**:

```python
# 1. Filter early, aggregate late
# ✅ GOOD:
WHERE sales_period_group_end_date_part BETWEEN '2024-01-01' AND '2024-03-31'
  AND jp_category_name = 'Laundry'
  AND data_provider_code_part = 'cds_8007'
GROUP BY brand

# ❌ BAD:
SELECT * FROM table  # Then filter in Python

# 2. Use appropriate date ranges
# Start with 1 week for testing
# Expand to 3 months for analysis
# Use 12+ months only when needed (YoY)

# 3. Limit joins
# Only join dimension tables needed for analysis
```

**Memory Management**:

```python
# For large datasets (>1M rows):
# 1. Use date chunking
date_chunks = pd.date_range('2024-01-01', '2024-12-31', freq='MS')
results = []
for start_date in date_chunks:
    end_date = start_date + pd.DateOffset(months=1)
    df_chunk = execute_query(query.format(start=start_date, end=end_date))
    results.append(df_chunk)
df = pd.concat(results)

# 2. Use appropriate dtypes
df['shopper_id'] = df['shopper_id'].astype('int32')  # Not int64
df['category'] = df['category'].astype('category')   # Not object
```

---

## 🔍 Common Patterns & Solutions

### Pattern 1: YoY Comparison Analysis

**Business Question**: "Why did metric X change from last year?"

**Approach**:

```python
# 1. Use C-TSR framework (Template 01)
# Decompose into:
# - Customer count change
# - Trade frequency change
# - Spend per customer change
# - Repeat rate change

# 2. Always include:
current_year = df[df['year'] == 2024]
prior_year = df[df['year'] == 2023]
iya = (current_year['value'].sum() / prior_year['value'].sum() - 1) * 100

# 3. Break down by segment to find drivers
df.groupby('brand')['value'].sum().pct_change()
```

**Deliverable**: "Sales declined 12% YoY driven by 15% loss in customer count, partially offset by 3% increase in spend per customer. Brand A lost the most customers (-25%)."

---

### Pattern 2: New Product Launch Evaluation

**Business Question**: "Should we expand Product X? Where will sales come from?"

**Multi-Template Approach**:

```python
# Step 1: Source of Volume (Template 02)
# - Pre-period: 3 months before launch
# - Post-period: 3 months after launch
# → Answer: "50% came from competitive Brand Y"

# Step 2: Venn Diagram (Template 05)
# - Compare new product vs our existing brands
# → Answer: "Only 10% cannibalization of our brands"

# Step 3: Trial/Repeat (Template 06)
# - Track trial-to-repeat conversion
# → Answer: "35% repeat rate after 3 months"

# Step 4: Next Purchase (Template 03)
# - What do they buy after?
# → Answer: "60% buy our Brand Z next"
```

**Deliverable**: "Product X is net incremental (90% from competitors). With 35% repeat rate and halo effect on Brand Z, expand distribution. Expected revenue impact: ¥500M annually."

---

### Pattern 3: Category Management Decision

**Business Question**: "How should we optimize our product portfolio?"

**Approach**:

```python
# 1. Co-purchase Analysis (Template 04)
# Identify complementary products (lift > 1.5)
complementary = copurchase_df[copurchase_df['lift'] > 1.5]

# 2. Venn Diagram (Template 05)
# Identify cannibalization (high overlap)
cannibals = venn_df[venn_df['overlap_pct'] > 30]

# 3. Demographics (Template 07)
# Identify white space opportunities
underserved = demo_df[demo_df['penetration'] < category_avg]

# 4. Shopper Flow (Template 08)
# Identify switching patterns
losing_share = flow_df[flow_df['net_flow'] < 0]
```

**Deliverable**: "Bundle Product A+B (3.2x lift). Discontinue Product C (45% cannibalizes Product D, overlapping target). Target females 30-40 (12% category penetration vs 28% average). Defensive strategy needed for Brand X (losing 20% of shoppers to competitor)."

---

## 🎓 Learning from Our Migration Project

### Key Learnings (January 2026 Project)

1. **Start Simple, Validate, Then Scale**

   - Started with Demographics (simplest template)
   - Validated connection and data quality
   - Then tackled complex templates (Co-purchase, Next Purchase)

2. **Window Functions Require Care**

   - LAG/ROW_NUMBER must preserve exact PARTITION BY and ORDER BY logic
   - Test with small dataset first
   - Verify sequence numbers match expectations

3. **Market Basket Math is Tricky**

   - Support, Confidence, Lift formulas must be exact
   - Lift = (P(A∩B)) / (P(A) × P(B))
   - Algebraic equivalents are OK but verify output

4. **Visualizations Drive Insights**

   - Raw tables are hard to interpret
   - Sankey diagrams reveal flow patterns instantly
   - Network graphs show product relationships clearly
   - Population pyramids are perfect for demographics

5. **Documentation is Critical**
   - Future you won't remember the logic
   - Comment complex SQL (especially window functions)
   - Document assumptions (e.g., 365-day trial threshold)

---

## 🚨 Common Pitfalls & How to Avoid

### Pitfall 1: Over-Aggregation

**Problem**: Aggregating too early loses important details

```python
# ❌ BAD: Aggregate then analyze
df_agg = df.groupby('brand')['value'].sum()
# Lost: Shopper-level, time trends, segment differences

# ✅ GOOD: Keep granular, aggregate at end
df_shopper = df.groupby(['shopper_id', 'brand', 'month'])['value'].sum()
# Can still roll up, but preserved detail for deep-dives
```

---

### Pitfall 2: Assuming Causation

**Problem**: Correlation ≠ Causation

```python
# ❌ BAD: "Sales increased after campaign, so campaign worked"
# Could be: seasonality, competitive activity, macro trends

# ✅ GOOD: Use control groups or time series decomposition
# - Compare vs non-campaign customer
# - Control for seasonality
# - Check competitive calendar
```

---

### Pitfall 3: Ignoring Business Context

**Problem**: Technically correct but business-irrelevant

```python
# ❌ BAD: "Shopper A12345 bought 127 units"
# So what? Can't action on one shopper

# ✅ GOOD: "15% of heavy users (>10 units/quarter) account for 60% of sales"
# Actionable: Target heavy users with loyalty program
```

---

### Pitfall 4: Not Validating Results

**Problem**: Query errors produce plausible but wrong outputs

```python
# Always validate with:
# 1. Order of magnitude check
assert df['value'].sum() > 1_000_000  # Expect ~¥1M+

# 2. Logical range check
assert df['age'].between(0, 100).all()

# 3. Completeness check
assert df['shopper_id'].notna().all()

# 4. Consistency check
assert (df.groupby('shopper_id')['value'].sum() >= 0).all()
```

---

## 📚 Additional Resources

### SQL Patterns Reference

**ROLLUP for subtotals**:

```sql
GROUP BY ROLLUP(brand, sub_brand)
-- Produces:
-- (brand, sub_brand) - Detail
-- (brand, NULL) - Brand subtotal
-- (NULL, NULL) - Grand total
```

**CUBE for all combinations**:

```sql
GROUP BY CUBE(dimension1, dimension2, dimension3)
-- Produces all 2^3 = 8 combinations
```

**Window Functions**:

```sql
-- LAG: Previous row value
LAG(column) OVER (PARTITION BY group ORDER BY date)

-- ROW_NUMBER: Sequential numbering
ROW_NUMBER() OVER (PARTITION BY group ORDER BY value DESC)

-- Cumulative sum
SUM(value) OVER (PARTITION BY group ORDER BY date
                 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

---

### Python Patterns Reference

**Date handling**:

```python
# String to date
df['date'] = pd.to_datetime(df['date'])

# Date arithmetic
df['date_30_days_ago'] = df['date'] - pd.Timedelta(days=30)

# Date extraction
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['quarter'] = df['date'].dt.quarter
```

**Conditional aggregation**:

```python
# Count distinct shoppers by segment
df.groupby('brand').agg({
    'shopper_id': 'nunique',
    'value': ['sum', 'mean'],
    'unit': 'sum'
}).round(0)
```

---

## 🎯 Success Metrics

**How to Know You're Doing Well**:

1. **Speed**: Can answer business questions in <1 day
2. **Accuracy**: Stakeholders trust your numbers (no "let me double-check")
3. **Impact**: Your insights drive decisions ($$ impact)
4. **Clarity**: Non-technical stakeholders understand your findings
5. **Proactivity**: You spot opportunities before being asked

**Warning Signs**:

- ⚠️ Analysis takes >1 week (over-engineering or wrong approach)
- ⚠️ Results are "interesting" but no action taken (missing business link)
- ⚠️ Stakeholders ask for clarification (poor communication)
- ⚠️ "Can you check this calculation?" (accuracy concerns)

---

## 📞 Getting Help

### When to Ask for Clarification

**Always ask if**:

1. Business question is ambiguous ("improve performance" - improve what?)
2. Date ranges seem wrong (3 days? 5 years?)
3. Results look suspicious (0 rows, all NULLs, extreme values)
4. Multiple interpretations possible (trial = first ever? or first in 365 days?)

**Template for Clarification**:

```
I want to ensure I understand correctly:

Business Question: [Restate in your words]
Proposed Approach: [Your plan]
Expected Output: [What you'll deliver]
Key Assumptions: [What you're assuming]

Does this align with your needs? Any adjustments?
```

---

## 🔄 Continuous Improvement

### After Each Analysis

**Reflect**:

1. Did I answer the business question?
2. Was my approach efficient?
3. What would I do differently?
4. What new patterns did I discover?

**Document**:

- Add new patterns to this guide
- Update template recommendations
- Note data quality issues for next time

**Share**:

- Present insights to team
- Document reusable SQL queries
- Create new template if pattern is common

---

## ✅ Quick Reference Checklist

**Before Starting Analysis**:

- [ ] Understand business question and decision at stake
- [ ] Identify stakeholders and timeline
- [ ] Check data availability and quality
- [ ] Select appropriate template(s)
- [ ] Create workspace copy (don't edit templates)

**During Analysis**:

- [ ] Reference data dictionary for exact field names
- [ ] Use gold_customer_loyalty table
- [ ] Validate data quality (counts, nulls, ranges)
- [ ] Apply statistical rigor (sample size, significance)
- [ ] Create purpose-driven visualizations
- [ ] Document assumptions and methodology

**Before Delivering**:

- [ ] Verify calculations with spot checks
- [ ] Test visualizations with stakeholder perspective
- [ ] Translate findings to business language
- [ ] Quantify impact (revenue, market share, customer count)
- [ ] Provide specific, actionable recommendations
- [ ] Note limitations and risks

---

## 📖 Document Version History

| Version | Date       | Changes                                           | Author         |
| ------- | ---------- | ------------------------------------------------- | -------------- |
| 1.0     | 2026-01-07 | Initial creation based on IDPOS migration project | GitHub Copilot |

---

**Remember**: Your value comes not from running queries, but from **answering business questions that drive profitable decisions**.

Think strategically. Act on data. Create value. 💰

---

_For questions or suggestions, update this living document._
