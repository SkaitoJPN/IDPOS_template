# Ariel Bottle Products - Repeat Rate Analysis Report

**Analysis Date**: January 7, 2026  
**Prepared for**: Sales Team  
**Purpose**: MCC Comparison

---

## Executive Summary

This analysis calculates repeat rates for Ariel bottle products across all IDPOS retailers (excluding convenience stores). The repeat rate represents the percentage of customers who made an initial purchase during the TFI (Trial/First-time purchase) period and then returned to purchase the same product again within the specified repeat period.

---

## Key Findings

### Repeat Rate Results

| Product                            | TFI Period           | Repeat Period        | TFI Shoppers | Repeat Shoppers | **Repeat Rate** |
| ---------------------------------- | -------------------- | -------------------- | ------------ | --------------- | --------------- |
| **Ariel Mirai Regular (本体通常)** | Jul 1 - Aug 31, 2025 | Jul 1 - Nov 30, 2025 | 31,278       | 1,584           | **5.06%**       |
| **Ariel Mirai Large (本体大)**     | Jul 1 - Aug 31, 2025 | Jul 1 - Nov 30, 2025 | 87,132       | 9,215           | **10.58%**      |
| **Ariel Gel (本体各種)**           | Sep 1 - Sep 30, 2025 | Sep 1 - Dec 31, 2025 | 191,751      | 22,528          | **11.75%**      |

---

## Insights

### 1. Product Performance Ranking

- **Ariel Gel** shows the highest repeat rate at **11.75%**
- **Ariel Mirai Large** has a moderate repeat rate at **10.58%**
- **Ariel Mirai Regular** has the lowest repeat rate at **5.06%**

### 2. Size Impact (Ariel Mirai)

- Large size (本体大) performs **2.1x better** than regular size (本体通常)
- Large size: 10.58% vs Regular size: 5.06%
- This suggests larger pack sizes drive better customer retention

### 3. Volume Considerations

- **Ariel Gel** has the largest customer base with 191,751 TFI shoppers
- **Ariel Mirai Large** has 87,132 TFI shoppers (2.8x more than regular size)
- Despite lower repeat rate, Ariel Mirai Regular still captures 31,278 TFI customers

---

## Methodology

### Data Scope

- **Channels**: All channels **excluding** FAMILYMART, LAWSON, SEVEN ELEVEN (convenience stores)
- **Retailers**: All 9 IDPOS retailers aggregated:
  - TSURUHA (cds_8005)
  - TOMODS (cds_8006)
  - SAPPORO DRUG (cds_8007)
  - KOHNAN (cds_8008)
  - FUJI YAKUHIN (cds_8009)
  - TRIAL (cds_8010)
  - CHUBU YAKUHIN (cds_8011)
  - CAINZ (cds_8012)
  - SUGI YAKKYOKU (cds_8013)
- **Category**: Laundry
- **Product Filter**: Sub-brand and size (jp_segment_4_name) used for segmentation
- **Gift Sets**: Excluded (only "本体" products included)

### Calculation Logic

**TFI Shoppers**:

- Unique shoppers who purchased the target product during the TFI period
- First-time or returning customers who purchased during this specific window

**Repeat Shoppers**:

- Subset of TFI shoppers who made **at least one additional purchase** of the same product
- Purchase must occur **AFTER the TFI period ends** but within the repeat period window
- Same shopper ID required (cohort-based tracking)

**Repeat Rate Formula**:

```
Repeat Rate = (Repeat Shoppers / TFI Shoppers) × 100%
```

### Period Definitions

**For Ariel Mirai (Regular & Large)**:

- TFI Period: July 1 - August 31, 2025 (2 months)
- Repeat Period: July 1 - November 30, 2025 (5 months total, includes TFI + 3 months post-TFI)
- Repeat purchases tracked: September 1 - November 30, 2025 (3 months)

**For Ariel Gel**:

- TFI Period: September 1 - September 30, 2025 (1 month)
- Repeat Period: September 1 - December 31, 2025 (4 months total, includes TFI + 3 months post-TFI)
- Repeat purchases tracked: October 1 - December 31, 2025 (3 months)

---

## Data Quality Notes

### Half-Width Katakana

- Database uses half-width katakana for product names
- Correct format: `ｱﾘｴｰﾙﾐﾗｲ` (not `アリエール ミライ`)
- Correct format: `ｱﾘｴｰﾙｼﾞｪﾙ` (not `アリエール ジェル`)

### Member ID Filtering

- Only loyalty card members included (member_ind = 'Y')
- Non-member transactions excluded to ensure accurate shopper-level tracking

### Data Source

- Table: `cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw`
- Gold layer data (validated and production-ready)

---

## MCC Comparison Readiness

These results are **ready for direct comparison** with MCC (Modern Channel - Convenience Store) data because:

1. ✅ **Same time periods** used for both TFI and repeat windows
2. ✅ **Same calculation methodology**: TFI cohort → Repeat rate within defined window
3. ✅ **Channel separation**: IDPOS excludes CVS, MCC is CVS-specific
4. ✅ **Same product definitions**: Sub-brand and size filters match
5. ✅ **Same 3-month repeat window**: Post-TFI tracking period is consistent

---

## Recommendations

### For Sales Strategy

1. **Leverage Large Pack Success**:

   - Ariel Mirai Large shows 2x better repeat rate than Regular
   - Consider promotional focus on larger pack sizes to improve customer retention

2. **Investigate Regular Pack Underperformance**:

   - 5.06% repeat rate is significantly lower than other products
   - May indicate pricing, shelf placement, or value perception issues

3. **Ariel Gel as Benchmark**:
   - 11.75% repeat rate is the highest performer
   - Use as internal benchmark for other product launches

### For MCC Comparison

When comparing with MCC data:

- Expected: MCC repeat rates may differ due to different shopping behaviors in convenience stores
- Key question: Do the same product size dynamics hold true in CVS channels?
- Look for: Whether Ariel Gel maintains leadership across both channel types

---

## Files Delivered

1. **ariel_bottle_repeat_rate_results.xlsx** - Complete analysis results with metadata
2. **analyze_repeat_rate.py** - Python script for reproduction/validation
3. **This report** - Executive summary and methodology documentation

---

## Technical Notes

**Analysis Execution**:

- Date/Time: 2026-01-07 15:06
- Environment: Databricks SQL Connector (Python)
- Workspace: `IDPOS_template/workspace/ariel_repeat_rate_20260107/`

**Query Performance**:

- All three analyses completed successfully
- No data quality issues encountered
- Results validated against expected order of magnitudes

---

## Contact

For questions about this analysis:

- **Methodology**: Refer to IDPOS template documentation
- **Data Quality**: Contact IDPOS data team
- **Results Interpretation**: Sales analytics team

---

**Report Generated**: 2026-01-07  
**Status**: ✅ Complete and ready for MCC comparison
