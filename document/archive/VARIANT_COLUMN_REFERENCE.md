# Variant Column Reference

**IMPORTANT**: This document records the correct columns for variant-level and size-level analysis in IDPOS data.

## Key Information

### Variant Column Name

- **Column**: `jp_prod_family_1_name`
- **Table**: `id_pos_ai_1.prod_dim_ext_vw`
- **Usage**: Use this column to filter product variants, NOT jp_prod_name

### Size Column Name

- **Column**: `jp_segment_4_name`
- **Table**: `id_pos_ai_1.prod_dim_ext_vw`
- **Usage**: Use this column for size/pack size information
- **Date Added**: January 23, 2026
- **Note**: Do NOT use jp_pack_size_name or jp_size_name - use jp_segment_4_name!

### Valid Variant Values

#### Ariel Gel Ball Variants

1. `Ariel Gel Ball` - Base/All variants
2. `Ariel Gel Ball_Indoor Dry` - Indoor Dry variant
3. `Ariel Gel Ball_Pro Power` - Pro Power variant

#### Bold Gel Ball Variants

1. `Bold Gel Ball_Blue` - Blue variant
2. `Bold Gel Ball_Pink` - Pink variant
3. `Bold Gel_WH-TEA&FL` - White Tea & Flower variant

## Historical Notes

- **Date**: January 16, 2026
- **Context**: Second reminder about this column
- **Previous attempts**: Incorrectly tried to filter using jp_prod_name with LIKE patterns
- **Correct approach**: Direct equality match on jp_prod_family_1_name

## Query Pattern

```sql
-- Correct variant filtering
WHERE p.jp_prod_family_1_name = 'Ariel Gel Ball_Indoor Dry'

-- NOT this (incorrect):
-- WHERE p.jp_prod_name LIKE '%インドアドライ%'
```
