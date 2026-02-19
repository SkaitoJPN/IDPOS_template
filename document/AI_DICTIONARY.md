# AI Dictionary (Minimal Routing)

**Last Updated:** 2026-02-19  
**Goal:** help AI find the right document with minimal tokens.

---

## 1) Where to Look First

| Need                                  | Open                              | Why                                     |
| ------------------------------------- | --------------------------------- | --------------------------------------- |
| Column/table/filter decisions         | `IDPOS_REFERENCE.md`              | Canonical source of truth               |
| Quick navigation across docs          | `AI_DICTIONARY.md`                | This map                                |
| Working principles and delivery style | `copilot.md`                      | Analysis behavior and quality standards |
| Historical/project-specific notes     | `archive/CONVERSATION_SUMMARY.md` | Context only, not canonical             |
| Implementation logic                  | `templates/*.ipynb`               | Ground-truth analysis patterns          |

---

## 2) Canonical Defaults (Fast Recall)

- Fact table: `cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw`
- Date: `sales_period_group_end_date_part`
- Retailer code: `data_provider_code_part`
- Loyalty shopper: `shopper.member_ind = 'Y'`
- Category default: `jp_category_name = 'Laundry'`
- Variant: `jp_prod_family_1_name`
- Size: `jp_segment_4_name`

---

## 3) Agent Routing

| Agent | File | Open when... |
|-------|------|--------------|
| CEO | `agents/01_ceo.md` | Clarifying business question, selecting analysis, reviewing deliverable |
| Data Engineer | `agents/02_data_engineer.md` | Writing SQL, validating columns/tables, encoding filters |
| Data Scientist | `agents/03_data_scientist.md` | Setting up workspace, running templates, building charts |
| Quality Guardian | `agents/04_quality_guardian.md` | Validating results, checking logic, catching pitfalls |
| Story Teller | `agents/05_storyteller.md` | Writing executive narrative, iterating on CEO feedback |
| System overview | `agents/00_system_overview.md` | Understanding orchestration loop and handoff triggers |

---

## 4) Skill Routing

| Skill | File | Use when... |
|-------|------|-------------|
| Template Selector | `skills/skill_template_selector.md` | Mapping business question to template(s) |
| SQL Builder | `skills/skill_sql_builder.md` | Writing any IDPOS query |
| Data Validation | `skills/skill_data_validation.md` | Running quality gate on results |
| Visualization | `skills/skill_visualization.md` | Choosing chart type, writing insight titles |
| Insight Delivery | `skills/skill_insight_delivery.md` | Structuring the final output narrative |
| Katakana Encoder | `skills/skill_katakana_encoder.md` | Filtering by sub-brand or brand name |

---

## 5) Duplication Rule

- Do not create separate schema/variant/quick-reference copies.
- Keep operational truth only in `IDPOS_REFERENCE.md`.
