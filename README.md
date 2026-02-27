# IDPOS Template Library

IDPOS Loyalty Data Analysis Templates for Japan FMCG Brands.

## Overview

This repository provides a library of reusable Jupyter Notebook templates for analysing IDPOS (ID-linked Point-of-Sale) loyalty data. It is used by P&G Japan analysts to answer strategic business questions using shopper-level retail data.

## Repository Structure

```
IDPOS_template/
├── templates/       # Read-only production templates (do not edit directly)
├── workspace/       # Working directory – copy templates here before editing
└── document/        # Reference documents, agent definitions, and skill modules
    ├── IDPOS_REFERENCE.md          # Canonical schema reference (source of truth)
    ├── AI_DICTIONARY.md            # Quick routing table for AI assistants
    ├── copilot.md                  # Analysis operating principles
    ├── agents/                     # 5-agent orchestration definitions
    └── skills/                     # 6 reusable skill modules
```

## Templates

| # | Template | Business Question |
|---|----------|-------------------|
| 01 | `01_ctsr_analysis.ipynb` | What drove YoY change? (Customer-Trade-Spend-Repeat) |
| 02 | `02_sov.ipynb` | Where did new customers come from? (Source of Volume) |
| 03 | `03_next_purchase.ipynb` | What do shoppers buy next? |
| 04 | `04_copurchase.ipynb` | What should we cross-sell? (Market basket) |
| 05 | `05_venn_diagram.ipynb` | Are brands competing or complementary? |
| 06 | `06_trial_repeat.ipynb` | How do we improve retention? (Trial/Repeat) |
| 07 | `07_demographics.ipynb` | Who is our target customer? |
| 08 | `08_shopper_flow.ipynb` | Are we gaining or losing loyalty? |

## Quick Start

1. **Read** `document/IDPOS_REFERENCE.md` to understand the schema.
2. **Create** a workspace folder: `workspace/<project_name>_YYYYMMDD/`.
3. **Copy** the relevant template(s) into your workspace folder.
4. **Edit** only the copy – never the originals in `templates/`.

> ⚠️ **Templates are read-only production assets.** Always work in `workspace/`.

## Documentation

- **`document/IDPOS_REFERENCE.md`** – Schema, column names, valid filter values, SQL join contract.
- **`document/AI_DICTIONARY.md`** – Fast routing table for AI assistants.
- **`document/copilot.md`** – Full analysis guidelines and best practices.
- **`document/agents/00_system_overview.md`** – Multi-agent orchestration loop.
