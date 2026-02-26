# Handover Document — Ariel Gel Pricing Strategy Analysis

**Date:** 2026-02-20  
**Branch:** `feature/ariel-gel-strategy-v2`  
**Repo:** https://github.com/SkaitoJPN/IDPOS_template  
**Workspace:** `c:\Users\sugimoto.k.1\OneDrive - Procter and Gamble\work\01_analysis\python\IDPOS_template\workspace\ariel_gel_pricing_strategy_20260219\`

---

## runsubagent

> **"runsubagent Data Engineer + Data Scientist for P&G Japan laundry analysis. The workspace is an IDPOS Databricks analysis project for Ariel Gel pricing strategy."**

Or simply paste this document and say: _"Continue from this handover document."_

---

## What Was Completed (Previous Session)

All 20 notebook edits across 5 notebooks are **DONE**. No code changes needed.

| #     | Notebook                       | Change                                                                                                                                                |
| ----- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1-4   | 01_asp_landscape.ipynb         | SIZE_ORDER/EXCLUDED_SIZES params; filter+order Ariel & Attack charts; new combined Ariel+Attack ASP chart                                             |
| 5-9   | 02_trial_acquisition.ipynb     | SIZE_ORDER params; filter cell 11; new combined trial chart; outlier clipping cell 17 (5th–95th pct); MIN_OBS_FREQ=5 + ascending axis cell 19         |
| 10-12 | 03_trial_repeat.ipynb          | SIZE_ORDER params; filter+reorder migration heatmap + new Attack heatmap; new ASP 50JPY bin chart                                                     |
| 13-16 | 04_lapse_analysis.ipynb        | SIZE_ORDER params; filter lapse-by-size; **BUG FIX** 100% lapse rate (scan to LAPSE_CUTOFF_DATE, remove HAVING); new Attack lapse + destination cells |
| 17-20 | 05_shopper_universe_flow.ipynb | SIZE_ORDER params; filter funnel data; order funnel charts; new Attack Sankey                                                                         |

---

## What Needs to Be Done Next

### Step 1 — Run Notebooks in Order (Databricks connect required)

Run each notebook **top to bottom** in this order:

```
1. 01_asp_landscape.ipynb       → outputs: phase1_asp_landscape.xlsx
2. 02_trial_acquisition.ipynb   → outputs: phase2_trial_acquisition.xlsx
3. 03_trial_repeat.ipynb        → outputs: phase3_trial_repeat.xlsx  ← required by notebook 05
4. 04_lapse_analysis.ipynb      → outputs: phase4_lapse_analysis.xlsx
5. 05_shopper_universe_flow.ipynb → reads phase3 + phase4 xlsx for Attack Sankey
```

**Critical verification for notebook 04:**  
After running cell that queries `all_at_risk_query`, check the print output:

```
✅ XXXX at-risk shoppers fetched
   Lapsed: XXXX  Retained: XXXX
```

Retained count should be **non-zero** (the bug fix). Previously 100% lapsed because retained shoppers were excluded. Expected lapse rate for 詰替超特大 ≈ 50–60%, NOT 100%.

### Step 2 — Push to GitHub

```powershell
$env:PATH = "C:\Program Files\GitHub CLI;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;$env:PATH"
cd "c:\Users\sugimoto.k.1\OneDrive - Procter and Gamble\work\01_analysis\python\IDPOS_template"
git add workspace/ariel_gel_pricing_strategy_20260219/*.ipynb
git commit -m "feat: size filter/order + combined charts + lapse bug fix + Attack comparison"
git push origin feature/ariel-gel-strategy-v2
```

### Step 3 — Optional: Update 1-Pager HTML

After running all notebooks, if the numbers changed (especially lapse rates), update `ARIEL_GEL_1PAGER.html` with revised lapse rate figures.

---

## Key Parameters (All Notebooks)

```python
ARIEL_GEL   = 'ｱﾘｴｰﾙｼﾞｪﾙ'
ATTACK_EX   = 'ｱﾀｯｸ抗菌EX'
ANALYSIS_START    = '2025-01-01'
ANALYSIS_END      = '2026-01-31'
RENEWAL_MONTH     = '2025-05-01'
LAPSE_CUTOFF_DATE = '2025-07-31'
LAPSE_WINDOW_DAYS = 180

SIZE_ORDER     = ['本体通常', '詰替超特大', '詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ', '詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ', '詰替ﾒｶﾞｼﾞｬﾝﾎﾞ']
EXCLUDED_SIZES = ['ｿﾉﾀ', '詰替通常', '詰替超ｼﾞｬﾝﾎﾞ']
```

---

## Data Source

- **Database:** Databricks (`cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw`)
- **Retailers:** 9 national retailers (`cds_8005` – `cds_8013`)
- **Credentials:** `.env` file at repo root (`../../.env` relative to analysis folder)
- **Python env:** Databricks Connect + pandas + plotly + numpy + openpyxl

---

## Known Issues / Watch Points

| Issue                | Detail                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 05 Attack Sankey     | Reads `phase3_trial_repeat.xlsx` — run notebook 03 first or cell will print a graceful fallback message and skip                                              |
| 04 Lapse bug (FIXED) | Bug was: scan window `ANALYSIS_END` + `HAVING MAX(date) <= LAPSE_CUTOFF_DATE` excluded retained shoppers. Fix: scan to `LAPSE_CUTOFF_DATE`, removed `HAVING`. |
| 02 cell 17 outliers  | Per-size 5th–95th percentile clipping on weighted_asp scatter — verify trendlines look reasonable after running                                               |

---

## Files in Analysis Folder

```
01_asp_landscape.ipynb          ← MODIFIED
02_trial_acquisition.ipynb      ← MODIFIED
03_trial_repeat.ipynb           ← MODIFIED
04_lapse_analysis.ipynb         ← MODIFIED (+ bug fix)
05_shopper_universe_flow.ipynb  ← MODIFIED
ANALYSIS_REPORT.md
STRATEGY_MEMO.md
ARIEL_GEL_1PAGER.html
```
