# Document Guide

This folder was reorganized to reduce duplication and improve AI/human readability.

## Start Here

1. `AI_DICTIONARY.md`  
   Fast routing: where to find the right information with minimal context.

2. `IDPOS_REFERENCE.md`  
   **Single canonical reference** for schema usage, field choices, join contract, and practical filters.

3. `copilot.md`  
   Working/analysis operating principles + pointer to agent/skill system.

## Agent & Skill System

4. `agents/`  
   5 agent definition files (CEO, Data Engineer, Data Scientist, Quality Guardian, Story Teller).  
   Start with `agents/00_system_overview.md` for the orchestration loop.

5. `skills/`  
   6 reusable skill modules invoked by agents:  
   `skill_template_selector`, `skill_sql_builder`, `skill_data_validation`,  
   `skill_visualization`, `skill_insight_delivery`, `skill_katakana_encoder`.

## Archive

- `archive/` contains case-specific or historical notes that are not canonical rules.

## Source-of-Truth Policy

| Topic | Canonical source |
|-------|----------------|
| Field/SQL decisions | `IDPOS_REFERENCE.md` |
| Agent routing | `AI_DICTIONARY.md` sections 3–4 |
| Agent behavior | `agents/` |
| Reusable logic | `skills/` |
| If documents conflict | `IDPOS_REFERENCE.md` wins |
