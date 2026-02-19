# Skill: Template Selector

**Used by:** CEO (agent 01), Data Scientist (agent 03)  
**Purpose:** Map a business question to the correct template(s). Select single-template or multi-template combination.

---

## Decision Table: Business Question → Template

| Business Question | Template | Core Method |
|-------------------|----------|-------------|
| "What drove YoY change?" | `01_ctsr_analysis` | C×T×S×R decomposition |
| "Where did new customers come from?" | `02_sov` | Pre/post purchase comparison |
| "What do shoppers buy after our product?" | `03_next_purchase` | Window function sequential purchase |
| "Which products should we cross-sell / bundle?" | `04_copurchase` | Market basket (Support, Confidence, Lift) |
| "Are two brands cannibalizing each other?" | `05_venn_diagram` | Shopper overlap analysis |
| "How do we improve retention?" | `06_trial_repeat` | Trial-to-repeat conversion (365-day lookback) |
| "Who is our target customer?" | `07_demographics` | Age × gender profile |
| "Are we gaining or losing loyalty over time?" | `08_shopper_flow` | Sankey diagram of brand switching |

---

## Multi-Template Combinations

### New Product Launch Evaluation
```
02_SoV          → Where did new buyers come from? (competitive switching)
05_Venn         → Did we cannibalize our own portfolio?
06_Trial/Repeat → Are new buyers returning?
03_Next Purchase → What do they buy after the new product?
```

### YoY Change Root Cause
```
01_C-TSR        → Decompose into Customers / Trades / Spend / Repeat
08_Shopper Flow → Are shoppers leaving to competitors?
07_Demographics → Has the buyer profile shifted?
```

### Portfolio Optimization
```
04_Co-purchase  → What products are bought together? (Lift > 1.5 = strong association)
05_Venn         → Is there overlap >30%? (cannibalization signal)
07_Demographics → Are there underserved segments?
08_Shopper Flow → Which products are losing shoppers?
```

---

## Template Location

All templates are in `templates/` and are **read-only**.

```
templates/
  01_ctsr_analysis.ipynb
  02_sov.ipynb
  03_next_purchase.ipynb
  04_copurchase.ipynb
  05_venn_diagram.ipynb
  06_trial_repeat.ipynb
  07_demographics.ipynb
  08_shopper_flow.ipynb
```

Always copy the selected template to:
```
workspace/project_name_YYYYMMDD/
```

---

## Decision Tree (for ambiguous questions)

```
Is the question about change over time?
  Yes → Does it compare YoY? → 01_C-TSR
  Yes → Does it compare two periods of brand loyalty? → 08_Shopper Flow

Is the question about a new product?
  Yes → Run: 02_SoV + 05_Venn + 06_Trial/Repeat + 03_Next Purchase

Is the question about who buys?
  Yes → 07_Demographics

Is the question about what they buy together?
  Yes → 04_Co-purchase

Is the question about retention or repeat buying?
  Yes → 06_Trial/Repeat

Is the question about where buyers came from?
  Yes → 02_SoV
```

---

## Note on Template 04 and 05 Dependencies

- `04_copurchase` requires `networkx` package (`pip install networkx`)
- `05_venn_diagram` requires `matplotlib_venn` package (`pip install matplotlib_venn`)
