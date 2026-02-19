# Skill: Visualization

**Used by:** Data Scientist (agent 03)  
**Purpose:** Match chart type to business question; write insight-driven titles; apply library and formatting standards.

---

## Chart Type Selection

| Business Question | Chart Type | Template Where Used |
|-------------------|-----------|-------------------|
| "Which is biggest?" / Ranking | Horizontal bar chart | 01, 02, 04 |
| "How did it change over time?" | Line chart | 01, 06 |
| "What is the composition / share?" | Stacked bar or donut | 01, 02 |
| "Where did shoppers flow?" | Sankey diagram | 08_Shopper Flow |
| "What overlaps between brands?" | Venn diagram | 05_Venn |
| "What's the relationship / network?" | Network graph (node-link) | 04_Co-purchase |
| "Who are the buyers? (age × gender)" | Population pyramid | 07_Demographics |
| "How are two variables correlated?" | Scatter plot | ad hoc |
| "How does a metric decompose?" | Waterfall chart | 01_C-TSR |

---

## The Title Rule

**Every chart title must state the insight, not the variable.**

```
❌ "Brand Sales"
✅ "Ariel Gel Ball Lost 15% of Sales YoY Despite Category Growth"

❌ "Venn Diagram: Brand A vs Brand B"
✅ "Only 8% of Shoppers Buy Both Ariel and Bold — Low Cannibalization Risk"

❌ "Trial and Repeat Rates"
✅ "1 in 8 New Ariel Buyers Returns — Large Pack Has 2× Higher Rate"

❌ "Shopper Flow 2024 vs 2023"
✅ "Bold Gained 12K Shoppers From Competitors While Competitors Gained 3K From Bold"

❌ "Source of Volume"
✅ "60% of New Bold Gel Ball Buyers Previously Bought Competitor Brand"
```

---

## Library Guide

| Library | When to use |
|---------|-------------|
| `plotly` | Default for all charts — interactive, supports Sankey, subplots |
| `matplotlib` | Static exports (PNG for reports), population pyramid control |
| `seaborn` | Heatmaps, correlation matrices, distribution plots |
| `networkx` | Co-purchase network graph (co-purchase template only) |
| `matplotlib_venn` | Venn diagrams (venn template only) |

---

## Chart Formatting Checklist

- [ ] Title states the **insight** (not the metric name)
- [ ] Axes labeled with units (¥, %, count, index)
- [ ] Legend is clear and positioned outside if many categories
- [ ] Color used meaningfully: warm = decline/risk, cool = growth/opportunity, neutral = reference
- [ ] Key data points labeled directly on chart (not only in legend)
- [ ] Source noted (e.g., "Source: IDPOS CDS 8005–8013, Laundry, Loyalty Members")
- [ ] Benchmark / comparison line added where possible (e.g., category average)
- [ ] Figure size set for readability (default: `figsize=(12, 6)` for bar/line)

---

## Plotly Quick Patterns

### Bar Chart (Ranking)

```python
import plotly.express as px

fig = px.bar(
    df.sort_values('total_sales_jpy', ascending=False).head(15),
    x='total_sales_jpy',
    y='variant',
    orientation='h',
    title='Top 15 Variants by Sales — [Insight Here]',
    labels={'total_sales_jpy': 'Sales (¥)', 'variant': 'Variant'},
    text='total_sales_jpy'
)
fig.update_traces(texttemplate='¥%{text:,.0f}', textposition='outside')
fig.update_layout(yaxis={'categoryorder': 'total ascending'})
fig.show()
```

### Line Chart (Trend)

```python
fig = px.line(
    df,
    x='date',
    y='value',
    color='variant',
    title='[Insight about the trend]',
    labels={'value': 'Sales (¥)', 'date': 'Week'}
)
fig.show()
```

### Sankey Diagram (Shopper Flow)

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    node=dict(
        label=node_labels,
        color=node_colors
    ),
    link=dict(
        source=source_list,
        target=target_list,
        value=value_list
    )
))
fig.update_layout(title_text='[Insight about who moved where]')
fig.show()
```

### Population Pyramid (Demographics)

```python
import matplotlib.pyplot as plt
import numpy as np

age_groups = df['age_group'].unique()
male = df[df['gender'] == 'Male']['pct'].values
female = df[df['gender'] == 'Female']['pct'].values

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(age_groups, -male, color='steelblue', label='Male')
ax.barh(age_groups, female, color='salmon', label='Female')
ax.set_xlabel('Share of Shoppers (%)')
ax.set_title('[Insight about the demographic profile]')
ax.legend()
plt.tight_layout()
plt.show()
```

---

## Insight Annotation Pattern

Always add a text annotation for the most important number:

```python
fig.add_annotation(
    x=key_x, y=key_y,
    text="← Key insight: X% above category average",
    showarrow=True,
    font=dict(size=12, color='darkred')
)
```
