"""
Transform the Bold Gel Ball pricing strategy notebook into an Ariel Gel Ball version.
Uses a three-pass swap technique to consistently swap brand focus throughout the notebook.
"""
import json, copy

input_path = 'SUD_pricing_strategy.ipynb'
output_path = 'ariel_gel_ball_pricing_strategy.ipynb'

with open(input_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb_new = copy.deepcopy(nb)


def get_source(cell):
    return ''.join(cell['source'])


def set_source(cell, text):
    if not text:
        cell['source'] = []
        return
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            if line:
                result.append(line)
    cell['source'] = result


def swap_brands(text):
    """Three-pass brand swap: Bold <-> Ariel in all relevant forms."""
    # Pass 1: Replace with unique placeholders (longest patterns first)
    replacements_pass1 = [
        ('Bold Gel Ball', '___PH_01___'),
        ('Ariel Gel Ball', '___PH_02___'),
        ('ボールドジェルボール', '___PH_03___'),
        ('アリエールジェルボール', '___PH_04___'),
        ('BOLD_GB', '___PH_05___'),
        ('ARIEL_GB', '___PH_06___'),
        ('bold_', '___PH_07___'),
        ('ariel_', '___PH_08___'),
        ('to_ariel', '___PH_09___'),
        ('to_bold', '___PH_10___'),
        # Catch-all (applied AFTER specific patterns)
        ('Bold', '___PH_15___'),
        ('Ariel', '___PH_16___'),
        ('bold', '___PH_17___'),
        ('ariel', '___PH_18___'),
    ]

    for original, placeholder in replacements_pass1:
        text = text.replace(original, placeholder)

    # Pass 2: Replace placeholders with swapped values
    reverse_map = {
        '___PH_01___': 'Ariel Gel Ball',
        '___PH_02___': 'Bold Gel Ball',
        '___PH_03___': 'アリエールジェルボール',
        '___PH_04___': 'ボールドジェルボール',
        '___PH_05___': 'ARIEL_GB',
        '___PH_06___': 'BOLD_GB',
        '___PH_07___': 'ariel_',
        '___PH_08___': 'bold_',
        '___PH_09___': 'to_bold',
        '___PH_10___': 'to_ariel',
        '___PH_15___': 'Ariel',
        '___PH_16___': 'Bold',
        '___PH_17___': 'ariel',
        '___PH_18___': 'bold',
    }

    for placeholder, new_value in reverse_map.items():
        text = text.replace(placeholder, new_value)

    return text


cells = nb_new['cells']

# 0-indexed cells that need the full brand swap
# These are analysis cells that focus on Bold -> need to focus on Ariel
SWAP_CELLS = {
    13,         # Q7: asp_band_universe (Bold-specific query)
    16, 17,     # Q10, Q11 derived (Bold-specific filters)
    24,         # A-4: Unit Ratio (swap ratio direction)
    28, 29, 30, # B-2, B-3, B-4: Trial comparison (swap index direction)
    36, 37,     # C-3c, C-4: Bold-focused analysis
    38, 39,     # C-5, C-5b: Price-point productivity
    43, 44,     # D-3, D-3b: Bold post-lapse destination
    45,         # D-4: Cross-flow analysis
    46,         # E-3b: Ariel Sankey -> Bold Sankey
    48, 49, 50, 51,  # E-1 through E-3: Shopper flow
    53, 54, 55, 56, 57, 58,  # F-1 through F-6: Price point deep-dive
    60, 61,     # Strategic summary + Export
}

for i, cell in enumerate(cells):
    src = get_source(cell)
    modified = False

    if i == 0:
        # Title markdown
        src = src.replace('Bold Gel Ball Pricing Strategy', 'Ariel Gel Ball Pricing Strategy')
        modified = True

    elif i == 5:
        # Cache cell: Change OUTPUT_DIR to avoid overwriting Bold outputs
        src = src.replace("OUTPUT_DIR = Path('output')", "OUTPUT_DIR = Path('output_ariel')")
        modified = True

    elif i == 13:
        # Q7: Change cache name (brand-specific query) + apply swap
        src = src.replace("cached_query('asp_band_universe'", "cached_query('ariel_asp_band_universe'")
        src = swap_brands(src)
        modified = True

    elif i in SWAP_CELLS:
        src = swap_brands(src)
        modified = True

    # Fix cell 61 (Export): guard unguarded period_pivot reference
    if i == 61:
        old_line = "    strip_tz(period_pivot).to_excel(writer, sheet_name='C_PrePost_Renewal', index=False)"
        new_line = "    if 'period_pivot' in dir(): strip_tz(period_pivot).to_excel(writer, sheet_name='C_PrePost_Renewal', index=False)"
        src = src.replace(old_line, new_line)
        modified = True

    if modified:
        set_source(cell, src)

    # Clear all code cell outputs for clean re-execution
    if cell.get('cell_type') == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None

# Save the new notebook
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(nb_new, f, ensure_ascii=False, indent=1)

print(f'✅ Created {output_path}')
print(f'   Cells with brand swap: {len(SWAP_CELLS)}')
print(f'   Special cells: 3 (title, cache, Q7 cache name)')
print(f'   All code cell outputs cleared for clean re-execution')
