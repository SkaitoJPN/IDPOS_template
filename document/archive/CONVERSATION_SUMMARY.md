# Conversation Summary - Initiative Repeat Tracking Analysis (Archived)

This file is archived as project-specific discussion history.

## Critical Points Raised by User

### 1. Variant Column

- Column: `jp_prod_family_1_name` (not `jp_prod_name`)
- Table: `id_pos_ai_1.prod_dim_ext_vw`
- Usage: direct equality matching preferred

### 2. Size Display Requirement

- Size source: `jp_segment_4_name`

### 3. Performance Optimization

- Consolidate repeated queries into minimal extraction passes

### 4. Brand Switching Requirement

- Follow next-purchase template logic
- Must identify first purchase after trial date

### 5. Analysis Context

- Category: Laundry
- Retailers: `cds_8005` to `cds_8013` (excluding CVS as needed)
- Loyalty shoppers only: `member_ind = 'Y'`
- Japanese names often in half-width katakana

---

For active operational rules, use:

- `../IDPOS_REFERENCE.md`
- `../AI_DICTIONARY.md`
