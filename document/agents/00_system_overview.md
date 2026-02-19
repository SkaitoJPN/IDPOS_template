# Agent System Overview

**Last Updated:** 2026-02-19  
**Purpose:** Defines the multi-agent orchestration model for IDPOS analysis. Read this first before activating any agent.

---

## Agent Roster

| # | Agent | Role | Primary Skill(s) |
|---|-------|------|-----------------|
| 01 | CEO | Strategy, scoping, non-analyst review | `skill_template_selector`, `skill_insight_delivery` |
| 02 | Data Engineer | SQL, schema, data access | `skill_sql_builder`, `skill_katakana_encoder` |
| 03 | Data Scientist | Code, templates, visualization, ML | `skill_template_selector`, `skill_visualization` |
| 04 | Quality Guardian | Accuracy, validation, pitfall detection | `skill_data_validation` |
| 05 | Story Teller | Non-analyst narrative, exec communication | `skill_insight_delivery` |

---

## Orchestration Loop

```
1. [CEO] Clarify business question, decision, audience, timeline
        ↓
2. [CEO] Select analysis type → invoke skill_template_selector
        ↓
3a. [Data Engineer] Write SQL, validate schema → invoke skill_sql_builder + skill_katakana_encoder
3b. [Data Scientist] Copy template to workspace/, configure parameters
   (3a and 3b run in parallel)
        ↓
4. [Data Scientist] Execute analysis, build visualizations → invoke skill_visualization
        ↓
5. [Quality Guardian] Run 5-check gate + statistical validation → invoke skill_data_validation
        ↓
6. [Story Teller] Write non-analyst narrative → invoke skill_insight_delivery
        ↓
7. [CEO] Review as non-analyst. If unclear/jargon-heavy → send back to Story Teller with specific critique
        ↓
8. [Story Teller] Revise based on CEO feedback
        ↓
9. Deliver
```

---

## Handoff Triggers

| From → To | Trigger condition |
|-----------|-------------------|
| CEO → Data Engineer + Data Scientist | Business question confirmed, template selected |
| Data Engineer → Data Scientist | SQL query validated and ready to run |
| Data Scientist → Quality Guardian | Analysis result produced (DataFrame / chart ready) |
| Quality Guardian → Story Teller | All 5 checks passed (or exceptions documented) |
| Story Teller → CEO | First draft narrative complete |
| CEO → Story Teller | Non-analyst review finds jargon, missing ¥ impact, or unclear action |
| Story Teller → Delivery | CEO approves narrative as "any stakeholder could understand this" |

---

## Hard Rules (All Agents Must Obey)

1. **Templates are read-only.** Never edit `templates/*.ipynb` directly. Always copy to `workspace/project_name_YYYYMMDD/`.
2. **Gold table only.** Always use `gold_customer_loyalty`, never `silver_customer_loyalty`.
3. **IDPOS_REFERENCE.md is truth.** For any column, table, or filter decision — check `document/IDPOS_REFERENCE.md` first.

---

## Document Routing

| Need | Document |
|------|----------|
| Schema, columns, SQL contract | `document/IDPOS_REFERENCE.md` |
| Quick routing table | `document/AI_DICTIONARY.md` |
| Agent identities + responsibilities | `document/agents/` (this folder) |
| Reusable instruction modules | `document/skills/` |
| Analysis behavior, delivery style | `document/copilot.md` |
| Historical project notes | `document/archive/CONVERSATION_SUMMARY.md` |
