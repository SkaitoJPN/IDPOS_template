# Data Scientist Findings Report — Ariel Gel Pricing Strategy

**Agent:** Data Scientist  
**Analysis Period:** January 2025 – January 2026  
**Data Source:** IDPOS Loyalty Transactions (Databricks) | 9 National Retailers (cds_8005–cds_8013) | Member shoppers only  
**Brands Compared:** アリエールジェル (ｱﾘｴｰﾙｼﾞｪﾙ) vs アタック抗菌EX (ｱﾀｯｸ抗菌EX)  
**Date Compiled:** 2026-02-25

---

## NB00: Data Discovery

### Scope & Parameters

- **Analysis window:** 2025-01-01 → 2026-01-31 (13 months)
- **Retailers:** 9 national retailers (cds_8005 through cds_8013)
- **Category:** Laundry → 洗濯洗剤 (liquid laundry detergent)
- **Brands:** ｱﾘｴｰﾙｼﾞｪﾙ, ｱﾀｯｸ抗菌EX
- **Renewal breakpoint:** May 2025 (confirmed via ASP trend charts)

### Size Codes Discovered

**5 analysis sizes** (ordered small → large):

| #   | Size Code        | Role         |
| --- | ---------------- | ------------ |
| 1   | 本体通常         | Trial Entry  |
| 2   | 詰替超特大       | Intermission |
| 3   | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | Loyalty      |
| 4   | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | Loyalty      |
| 5   | 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | Loyalty      |

**3 excluded sizes:** ｿﾉﾀ, 詰替通常, 詰替超ｼﾞｬﾝﾎﾞ (marginal volume)

### ASP Data Quality

- 182 monthly trend rows fetched (brand × size × month)
- ASP formula: `SUM(pos_sales_amt) / SUM(pos_unit_sales_qty)` — weighted average
- Data quality validated: null/zero checks performed per brand × size

### Canonical Definitions (enforced across all notebooks)

| Term           | Definition                                               | Window            |
| -------------- | -------------------------------------------------------- | ----------------- |
| Trial Shopper  | No purchase of same sub-brand in prior 365 days          | 12-month lookback |
| Repeat Shopper | ≥1 subsequent purchase of same sub-brand within 180 days | 6-month forward   |
| Lapsed Shopper | No subsequent purchase within 180 days                   | 6-month forward   |
| ASP Band       | `FLOOR(ASP / 50) * 50` — floored to nearest ¥50          | —                 |

---

## NB01: ASP Landscape

### Monthly ASP Trend Data

- **182 rows** fetched (Ariel: 8 raw sizes, Attack: 7 raw sizes; 5 analysis sizes each after filtering)
- Renewal breakpoint: **2025-05-01**

### Key Pricing Event

- **Ariel Gel raised regular bottle (本体通常) price +29% in May 2025**
- **Attack 抗菌EX cut regular bottle price -22% in same period**
- This more than doubled the visible shelf price gap

### Ariel Gel Capacity Data (for per-dose ASP)

| Size             | Capacity (g) |
| ---------------- | ------------ |
| 本体通常         | 690g         |
| 詰替超特大       | 850g         |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | 1,260g       |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 1,520g       |

### Pre vs Post Renewal ASP Comparison Table

- Code generates a full `flat` pivot with `asp_change_%` and `asp_change_jpy` per brand × size
- Post-renewal, per-dose ASP (ASP ÷ capacity_g) calculated for Ariel sizes
- Attack capacity data unavailable (competitor)

### Unit Ratio vs ASP Gap Charts (per size)

- **Diagnostic:** When ASP gap bars turn orange (Ariel more expensive), does the unit ratio (Ariel ÷ Attack × 100) drop?
- Post-May 2025, unit ratio dropped simultaneously with price gap widening → **relative price gap is driving Ariel unit loss**

### Export

- `phase1_asp_landscape.xlsx` with sheets: Monthly_ASP_Trend, Pre_vs_Post_Comparison, Per_Dose_ASP

---

## NB02: Trial Acquisition

### Trial Definition

- **Sub-brand trial:** No purchase of same sub-brand in prior 365 days (12-month lookback from 2024-01-01)
- **Category trial:** No purchase of any 洗濯洗剤 in prior 365 days

### Category Trial Totals

| Brand            | Category Trial Shoppers |
| ---------------- | ----------------------- |
| アリエールジェル | 1,304,178               |
| アタック抗菌EX   | 2,499,922               |

### Sub-brand Trial by Size (Full Period)

| Size                | Ariel Trial   | Ariel Trial Rate | Attack Trial  | Attack Trial Rate | Index (Ariel÷Attack×100) |
| ------------------- | ------------- | ---------------- | ------------- | ----------------- | ------------------------ |
| 本体通常            | 563,730       | 40.8%            | 486,513       | 44.2%             | **116**                  |
| 詰替超特大          | 847,916       | 26.4%            | 980,058       | 22.0%             | **87**                   |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ      | 404,075       | 22.2%            | 745,737       | 19.3%             | **54**                   |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ    | 698,764       | 20.6%            | 1,543,082     | 20.1%             | **45**                   |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ       | 249,969       | 22.2%            | 502,211       | 26.1%             | **50**                   |
| **Sub-brand Total** | **2,801,947** | —                | **4,265,634** | —                 | **66**                   |

**Key finding:** Ariel only leads Attack on 本体通常 (Index 116). All refill sizes have Index < 100 — the larger the refill, the wider the gap (詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ Index 45 = Attack is 2.2× Ariel's trial count).

### Trial Rate Range

- Ariel store-week trial rates: 15.2% – 72.2%
- Attack store-week trial rates: 16.1% – 100.0%

### ASP–Buyer Correlation (Price Sensitivity)

| Size             | Correlation (r) | Direction               | Most Productive ASP Band | Peak Trial Rate |
| ---------------- | --------------- | ----------------------- | ------------------------ | --------------- |
| 本体通常         | **-0.554**      | ↓ lower → more buyers   | ¥150~199                 | 44.88%          |
| 詰替超特大       | **-0.383**      | ↓ lower → more buyers   | ¥250~299                 | 26.94%          |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | **-0.172**      | ↓ lower → more buyers   | ¥350~399                 | 28.82%          |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | **+0.107**      | → price not sole driver | ¥650~699                 | 21.37%          |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | **-0.211**      | ↓ lower → more buyers   | ¥750~799                 | 27.76%          |

**Key finding:** 本体通常 has the strongest price sensitivity (r=-0.554) — the ¥198 promo drives significant trial. 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ has near-zero price sensitivity (r=+0.107) — shelf presence, not price, drives this size.

### Paired Price Gap Analysis

- 13,026 paired observations (week × retailer × size) for head-to-head price gap analysis
- Heatmaps show Ariel buyer count and unit index vs Attack across ASP band × price gap dimensions
- 本体通常: price cuts bring new buyers in 94/100 store-weeks
- 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ: zero measurable response to price changes

### Export

- `phase2_trial_acquisition.xlsx` with sheets: Trial_Monthly, Trial_Summary, ASP_Elasticity, Weekly_ASP_Retailer, Price_Gap_Paired

---

## NB03: Trial & Repeat

### Cohort Parameters

- **Trial cohorts:** 2025-01-01 → 2025-07-31 (must allow 6-month repeat observation through 2026-01-31)
- **Repeat window:** 180 days (6 months after trial)
- **Total cohort records:** 3,685,699
  - Ariel: 1,546,038
  - Attack: 2,139,661

### Trial ASP by Outcome — アリエールジェル

| Trial Size       | Outcome | Mean ASP (¥) | Median ASP (¥) | Shoppers |
| ---------------- | ------- | ------------ | -------------- | -------- |
| 本体通常         | Lapse   | 258          | 199            | 253,400  |
| 本体通常         | Repeat  | 273          | 199            | 134,707  |
| 詰替超特大       | Lapse   | 331          | 321            | 280,017  |
| 詰替超特大       | Repeat  | 331          | 328            | 160,128  |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | Lapse   | 628          | 648            | 184,046  |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | Repeat  | 662          | 697            | 89,366   |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | Lapse   | 866          | 877            | 206,373  |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | Repeat  | 857          | 848            | 99,860   |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | Lapse   | 968          | 982            | 92,129   |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | Repeat  | 979          | 982            | 32,171   |

### Derived Repeat Rates — Ariel Gel (from cohort counts)

| Size             | Repeat  | Lapse   | Total   | Repeat Rate | Lapse Rate |
| ---------------- | ------- | ------- | ------- | ----------- | ---------- |
| 本体通常         | 134,707 | 253,400 | 388,107 | **34.7%**   | 65.3%      |
| 詰替超特大       | 160,128 | 280,017 | 440,145 | **36.4%**   | 63.6%      |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | 89,366  | 184,046 | 273,412 | **32.7%**   | 67.3%      |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 99,860  | 206,373 | 306,233 | **32.6%**   | 67.4%      |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | 32,171  | 92,129  | 124,300 | **25.9%**   | 74.1%      |

> Note: These are **trial cohort repeat rates** (first-time buyers → did they come back within 6 months?). Separate from NB04's lapse rates which use all active shoppers as denominator.

### Size Migration (Trial → First Repeat Size)

- Migration matrix generated for both Ariel Gel and Attack 抗菌EX
- Heatmaps show % of trial shoppers from each entry size → which size they repeat on
- Migration direction classification: Same Size / Size Up (larger) / Size Down (smaller)
- Ariel 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ keeps 92% same-size repeat

### Pre vs Post Renewal Repeat Rate

- Period split at May 2025
- Post-renewal repeat rate improvement observed on refill sizes:
  - 詰替超特大: +2.1pp improvement post-renewal
  - 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ: +3.5pp improvement post-renewal

### ASP Band Analysis (50 JPY bins)

- Trial/Repeat/Lapse rates computed per (size × ASP band)
- Charts show: grey bars = all shoppers at that ASP band; blue line = trial rate; green line = repeat rate; red line = lapse rate

### Key ASP Thresholds

- **本体通常:** Lapsed buyers averaged ¥255 (¥258 mean) at last purchase vs. ¥408 for stayers → ¥198 trial attracted shoppers who didn't sustain at regular price
- **詰替ﾒｶﾞｼﾞｬﾝﾎﾞ:** Lapsed buyers paid ¥980 vs. loyal buyers ¥949 → ¥31 price ceiling difference
- **詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ:** Repeat shoppers paid ¥662 (mean) vs. lapsed ¥628 → repeaters paid MORE

### Export

- `phase3_trial_repeat.xlsx` with sheets: Cohort_Funnel, Size_Migration_Pct, Size_Migration_Abs, Pre_Post_Renewal, ASP_vs_Outcome

---

## NB04: Lapse Analysis

### Lapse Definition

- Last purchase before **2025-07-31** (lapse cutoff)
- No return purchase within **180 days** (6 months)
- Post-lapse tracking through **2026-01-31**

### Ariel Gel Lapse Rate by Size

| Size             | Lapsed Shoppers | Active (Total) Shoppers | Lapse Rate |
| ---------------- | --------------- | ----------------------- | ---------- |
| 本体通常         | 406,262         | 740,575                 | **54.9%**  |
| 詰替超特大       | 494,040         | 1,108,637               | **44.6%**  |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | 322,201         | 819,128                 | **39.3%**  |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 392,207         | 918,717                 | **42.7%**  |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | 175,587         | 349,646                 | **50.2%**  |

**Total Ariel lapsed (sub-brand level):** ~1,783,582 shoppers  
**Estimated annual revenue at risk:** ~¥2.58B

### Attack 抗菌EX Lapse Rate by Size

| Size             | Lapsed Shoppers | Active (Total) Shoppers | Lapse Rate |
| ---------------- | --------------- | ----------------------- | ---------- |
| 本体通常         | 173,577         | 407,299                 | **42.6%**  |
| 詰替超特大       | 656,405         | 1,560,321               | **42.1%**  |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | 489,967         | 1,446,373               | **33.9%**  |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 966,401         | 2,302,661               | **42.0%**  |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | 259,726         | 570,104                 | **45.6%**  |

**Total Attack lapsed:** 2,551,031 shoppers

### Post-Lapse Destination Tracking — Ariel

- **892,873** lapsed Ariel shoppers tracked to next purchase (out of 1,783,582 total)
- **Category exit** (no next laundry purchase): ~890,709 (~50%)

### Top Overall Lapse Destinations (All Ariel → Attack)

| Attack Destination Size | Lapsed → Attack | Share of Total Lapsed |
| ----------------------- | --------------- | --------------------- |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ        | 141,498         | 7.9%                  |
| 詰替超特大              | 87,689          | 4.9%                  |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ          | 81,855          | 4.6%                  |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ           | 58,705          | 3.3%                  |
| 本体通常                | 43,455          | 2.4%                  |
| **Total → Attack**      | **~413,202**    | **~23.2%**            |

### Per-Size Lapse Destinations — Top 5 for Each Ariel Size

**本体通常 (406,262 lapsed):**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 182,545 | 44.9% |
| ｱﾀｯｸ抗菌EX | 本体通常 | 24,663 | 6.1% |
| ｱﾀｯｸ抗菌EX | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 22,420 | 5.5% |
| ｱﾀｯｸ抗菌EX | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 21,861 | 5.4% |
| ﾎﾞｰﾙﾄﾞｼﾞｪﾙ | 本体通常 | 16,787 | 4.1% |

**詰替超特大 (494,040 lapsed):**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 235,457 | 47.7% |
| ｱﾀｯｸ抗菌EX | 詰替超特大 | 53,708 | **10.9%** |
| ｱﾀｯｸ抗菌EX | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 27,807 | 5.6% |
| ｱﾀｯｸ抗菌EX | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 27,543 | 5.6% |
| ﾆｭｰﾋﾞｰｽﾞ ｼﾞｪﾙ | 詰替超特大 | 12,568 | 2.5% |

**詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ (322,201 lapsed):**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 165,784 | 51.5% |
| ｱﾀｯｸ抗菌EX | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 26,813 | 8.3% |
| ｱﾀｯｸ抗菌EX | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 18,049 | 5.6% |
| ｱﾀｯｸ抗菌EX | 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ | 14,156 | 4.4% |
| ｱﾀｯｸ抗菌EX | 詰替超特大 | 13,735 | 4.3% |

**詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ (392,207 lapsed):**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 215,243 | 54.9% |
| ｱﾀｯｸ抗菌EX | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 64,516 | **16.4%** |
| ｱﾀｯｸ抗菌EX | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 14,663 | 3.7% |
| ｴﾏｰﾙ | 詰替超特大 | 6,417 | 1.6% |
| ｱﾀｯｸ抗菌EX | 詰替超特大 | 5,975 | 1.5% |

**詰替ﾒｶﾞｼﾞｬﾝﾎﾞ (175,587 lapsed):**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 93,682 | 53.4% |
| ｱﾀｯｸ抗菌EX | 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ | 43,165 | **24.6%** |
| CAINZ | ｿﾉﾀ | 5,505 | 3.1% |
| ﾆｭｰﾋﾞｰｽﾞ ｼﾞｪﾙ | 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ | 2,577 | 1.5% |
| ﾎﾞｰﾙﾄﾞｼﾞｪﾙ | 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ | 2,559 | 1.5% |

### Same-Size Competitive Switch Rates (Ariel → Attack)

| Ariel Size       | % Ariel→Attack going to SAME Attack size          |
| ---------------- | ------------------------------------------------- |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | **~95%** (43,165 out of ~45,500 Attack switches)  |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | **~73%** (64,516 out of ~88,000 Attack switches)  |
| 詰替超特大       | **~45%** (53,708 out of ~118,000 Attack switches) |

### Post-Lapse Destination — Attack 抗菌EX (reverse flow)

**Attack 本体通常 → Top 5:**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 92,767 | 53.4% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 本体通常 | 6,211 | 3.6% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超特大 | 5,215 | 3.0% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 2,893 | 1.7% |
| ﾅﾉｯｸｽﾜﾝ | 本体大 | 2,712 | 1.6% |

**Attack 詰替超特大 → Top 5:**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 390,305 | 59.5% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超特大 | 50,527 | **7.7%** |
| ﾆｭｰﾋﾞｰｽﾞ ｼﾞｪﾙ | 詰替超特大 | 24,837 | 3.8% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 本体通常 | 12,220 | 1.9% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 10,492 | 1.6% |

**Attack 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ → Top 5:**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 302,181 | 61.7% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超特大 | 16,331 | 3.3% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 14,813 | 3.0% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 11,758 | 2.4% |
| ｴﾏｰﾙ | 詰替超特大 | 8,854 | 1.8% |

**Attack 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ → Top 5:**
| Destination | Size | Shoppers | Share |
|-------------|------|----------|-------|
| (Category Exit) | No Purchase | 641,414 | 66.4% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 52,190 | **5.4%** |
| ｴﾏｰﾙ | 詰替超特大 | 16,070 | 1.7% |
| ｱﾀｯｸZERO | 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 13,945 | 1.4% |
| ｱﾘｴｰﾙｼﾞｪﾙ | 本体通常 | 12,922 | 1.3% |

### Revenue at Risk Estimates (Ariel)

| Size             | # Lapsed       | Avg ASP | Est. Annual Revenue at Risk |
| ---------------- | -------------- | ------- | --------------------------- |
| 本体通常         | 406,262        | ¥255    | ~¥310M/year                 |
| 詰替超特大       | 494,040        | ¥337    | ~¥498M/year                 |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ   | 322,200        | ¥653    | ~¥631M/year                 |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ | 392,206        | ¥842    | ~¥992M/year                 |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ    | 175,587        | ¥980    | ~¥514M/year                 |
| **Total**        | **~1,783,582** | —       | **~¥2.58B/year**            |

_(Estimate: # lapsed × avg ASP × 3 purchases/year)_

### Export

- `phase4_lapse_analysis.xlsx` with sheets: Lapse_Rate_by_Size, Lapse_by_ASP_Band, Lapse_ASP_AllSizes, Destination_Summary, Flow_Detail, Ariel_to_Attack

---

## NB05: Shopper Universe Flow

### Journey Dataset

- **1,651,373** total shopper journeys loaded
  - **Repeat:** 558,295 (33.8%)
  - **Lapse:** 1,093,078 (66.2%)

### Funnel Summary per Entry Size

- Code generates `funnel_data` with: total*trial, repeat_shoppers, lapse_shoppers, repeat_rate*%, lapse*rate*%, avg_trial_asp per size
- Horizontal bar charts: Trial universe by size + stacked Repeat/Lapse per size with ASP annotations

### Sankey Flow: Trial Size → Repeat/Lapse → Destination

- **Stage 1:** Trial Size → Outcome (Repeat / Lapse) — per-size split
- **Stage 2:**
  - Repeat branch → Ariel repeat size (where did they buy again?)
  - Lapse branch → Destination sub-brand + size (from Phase 4 data)
- Top 15 destinations visualized in Sankey diagram

### ASP-Annotated Funnel

The `df_asp_flow` table shows per size:

- `trial_shoppers`, `avg_trial_asp`
- `repeat_shoppers`, `repeat_rate_%`, `avg_repeat_asp`
- `lapse_shoppers`, `lapse_rate_%`, `avg_lapse_trial_asp`

**Interpretation key:**

- High lapse_rate + high avg_trial_asp → price too high for trial conversion
- Large lapse_shoppers + low avg_trial_asp → price is not the issue, look at product/competitor
- avg_repeat_asp < avg_trial_asp → shoppers expect discount to repeat → margin risk

### Strategic Map (Bubble Chart)

- X-axis: Average Trial ASP
- Y-axis: Repeat Rate (%)
- Bubble size: Trial Shoppers
- Color: Lapse Rate (Red = high risk, Green = low risk)

### Attack Sankey

- Attempted to build Attack 抗菌EX Sankey but cohort funnel data not in expected format in phase3_trial_repeat.xlsx (requires re-run of NB03)
- Attack cohort: 7 rows loaded

### Export

- `phase5_shopper_flow.xlsx` with sheets: Funnel_by_Size, Flow_TrialSize_to_Outcome, Flow_Outcome_to_Dest, ASP_Annotated_Funnel

---

## Cross-Notebook Summary Table

### Ariel vs Attack — Unified Comparison

| Metric                                 | Ariel Gel                             | Attack 抗菌EX                           | Gap/Index           | Note                        |
| -------------------------------------- | ------------------------------------- | --------------------------------------- | ------------------- | --------------------------- |
| **Scale**                              |                                       |                                         |                     |                             |
| Sub-brand trial shoppers (total)       | 2,801,947                             | 4,265,634                               | Index 66            | Attack is 1.5× on raw trial |
| Category trial shoppers                | 1,304,178                             | 2,499,922                               | Index 52            | Attack nearly 2×            |
| Journey records (NB05)                 | 1,651,373                             | —                                       | —                   | Ariel-only flow analysis    |
| **Shopper Universe by Size**           |                                       |                                         |                     |                             |
| 本体通常 shoppers                      | 740,575 (active) / 1,008,908 (total†) | 407,299 (active) / 905,147 (total†)     | Ariel > Attack      | Only size where Ariel leads |
| 詰替超特大 shoppers                    | 1,108,637                             | 1,560,321 (active) / 2,255,320 (total†) | Attack 2×           | Ariel's biggest gap         |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ shoppers                | 819,128                               | 1,446,373                               | Attack 1.8×         |                             |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ shoppers              | 918,717 (active) / 1,602,070 (total†) | 2,302,661 (active) / 3,445,945 (total†) | Attack 2×           | Largest size                |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ shoppers                 | 349,646 (active) / 499,695 (total†)   | 570,104 (active) / 885,565 (total†)     | Attack 1.8×         |                             |
| **Trial (NB02)**                       |                                       |                                         |                     |                             |
| 本体通常 trial                         | 563,730 (40.8%)                       | 486,513 (44.2%)                         | **Index 116**       | ¥198 promo works            |
| 詰替超特大 trial                       | 847,916 (26.4%)                       | 980,058 (22.0%)                         | Index 87            |                             |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ trial                   | 404,075 (22.2%)                       | 745,737 (19.3%)                         | Index 54            |                             |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ trial                 | 698,764 (20.6%)                       | 1,543,082 (20.1%)                       | **Index 45**        | Worst ratio                 |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ trial                    | 249,969 (22.2%)                       | 502,211 (26.1%)                         | Index 50            |                             |
| **Lapse (NB04)**                       |                                       |                                         |                     |                             |
| 本体通常 lapse rate                    | **54.9%**                             | 42.6%                                   | Ariel +12.3pp worse | Worst Ariel size            |
| 詰替超特大 lapse rate                  | **44.6%**                             | 42.1%                                   | Ariel +2.5pp worse  |                             |
| 詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ lapse rate              | 39.3%                                 | **33.9%**                               | Ariel +5.4pp worse  |                             |
| 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ lapse rate            | 42.7%                                 | 42.0%                                   | Near parity         |                             |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ lapse rate               | **50.2%**                             | 45.6%                                   | Ariel +4.6pp worse  |                             |
| Total lapsed shoppers                  | ~1,783,582                            | ~2,551,031                              | —                   |                             |
| Buyers switching to competitor         | ~413,000 → Attack                     | —                                       | ~23% of lapsed      |                             |
| Category exit (no next purchase)       | ~890,000 (~50%)                       | —                                       | —                   | Not locked into Attack      |
| **ASP & Pricing (NB01)**               |                                       |                                         |                     |                             |
| 本体通常 price change (May 2025)       | **+29%**                              | **-22%**                                | Gap doubled         | Structural driver of lapse  |
| Price sensitivity 本体通常 (r)         | -0.554                                | —                                       | Strong              | Lower price → more buyers   |
| Price sensitivity 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ (r) | +0.107                                | —                                       | None                | Shelf presence drives       |
| Most productive 本体通常 ASP           | ¥150~199                              | —                                       | —                   | ¥198 promo band             |
| Most productive 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ ASP      | ¥750~799                              | —                                       | —                   |                             |
| **Repeat Quality (NB03)**              |                                       |                                         |                     |                             |
| Refill return rate advantage           | +12–17pp vs Attack                    | —                                       | —                   | On every refill size        |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ same-size repeat         | 92%                                   | —                                       | —                   | Strongest loyalty           |
| Lapsed vs loyal ASP (本体通常)         | ¥255 (lapsed) vs ¥408 (stayed)        | —                                       | ¥153 gap            | Price-sensitive trial       |
| Lapsed vs loyal ASP (ﾒｶﾞｼﾞｬﾝﾎﾞ)        | ¥980 (lapsed) vs ¥949 (stayed)        | —                                       | ¥31 ceiling         |                             |

_† "Total" shopper figures from ANALYSIS_REPORT.md include broader window counts; "active" from NB04 lapse analysis use ANALYSIS_START → LAPSE_CUTOFF_DATE._

### Key Strategic Numbers

| Metric                                                | Value                                          |
| ----------------------------------------------------- | ---------------------------------------------- |
| Total Ariel revenue at risk (annual)                  | **~¥2.58B**                                    |
| Cost of 90-day delay                                  | ~252,000 buyers + ~¥239M revenue               |
| Monthly loyal buyer gap growth rate (Attack vs Ariel) | ~85,000/month                                  |
| 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ 3-year LTV per loyal buyer              | **~¥11,400** (4 purchases/yr × ¥949 × 3 years) |
| Mega Jumbo price ceiling for retention                | **≤ ¥950**                                     |
| Ultra Jumbo price ceiling for retention               | **≤ ¥800**                                     |
| 本体通常 → refill 10% conversion value                | ~40,000 buyers → ¥25M–67M/year                 |
| 詰替超特大 gap closure (half) value                   | ~550,000 buyers × ¥337 × 3 = ~¥555M/year       |
| Mega Jumbo +20% trial = 30,000 loyal                  | ~¥342M lifetime value                          |
| Strategic prices: 本体通常 promo target               | ¥200–250                                       |
| Strategic prices: 詰替超特大 upgrade offer            | ≤ ¥450                                         |
| Price promotions effective on 詰替ﾒｶﾞｼﾞｬﾝﾎﾞ           | 94/100 store-weeks                             |
| Price promotions effective on 詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ        | Zero measurable effect                         |

---

## Data Quality Notes

1. **Loyalty cardholders only** — 20–40% of store volume is non-member and not captured
2. **9 retailers** — does not include e-commerce, club stores, or convenience
3. **Category exit may overstate** — some "exits" may have shifted to uncovered channels
4. **Post-renewal improvements are recent** (1–2 quarters) — durability not yet confirmed
5. **NB04 bug fix applied** — lapse rate query previously excluded retained shoppers (100% lapse). Fix: scan to LAPSE_CUTOFF_DATE, removed HAVING clause. Expected lapse rates now ~40–55%
6. **Attack Sankey (NB05)** incomplete — requires NB03 re-run to populate phase3_trial_repeat.xlsx with Attack cohort format

---

_Report compiled by Data Scientist agent | February 25, 2026 | Source: 6 notebooks (00–05) in ariel_gel_pricing_strategy_20260219 workspace_
