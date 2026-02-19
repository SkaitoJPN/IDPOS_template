# Ariel Bottle Products - Repeat Rate Analysis
# Purpose: Calculate repeat rates for Ariel bottle products per sales team request
# Date: 2026-01-07

from databricks import sql
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path='../../.env')

# Connect to Databricks
print("Connecting to Databricks...")
connection = sql.connect(
    server_hostname=os.getenv("DATABRICKS_HOST"),
    http_path=os.getenv("DATABRICKS_HTTP_PATH"),
    access_token=os.getenv("DATABRICKS_TOKEN")
)

# Analysis configurations
configs = [
    {
        'product_name': 'Ariel Mirai Regular (本体通常)',
        'sub_brand': 'ｱﾘｴｰﾙﾐﾗｲ',
        'size_filter': '本体通常',
        'size_filter_repeat': '%',  # Same size for repeat
        'tfi_start': '2025-07-01',
        'tfi_end': '2025-08-31',
        'repeat_start': '2025-07-01',
        'repeat_end': '2025-11-30'
    },
    {
        'product_name': 'Ariel Mirai Large (本体大)',
        'sub_brand': 'ｱﾘｴｰﾙﾐﾗｲ',
        'size_filter': '本体大',
        'size_filter_repeat': '%',  # Same size for repeat
        'tfi_start': '2025-07-01',
        'tfi_end': '2025-08-31',
        'repeat_start': '2025-07-01',
        'repeat_end': '2025-11-30'
    },
    {
        'product_name': 'Ariel Gel (本体通常)',
        'sub_brand': 'ｱﾘｴｰﾙｼﾞｪﾙ',
        'size_filter': '本体通常',
        'size_filter_repeat': '%',  # Allow ANY size for repeat purchases (本体, 詰替, etc.)
        'tfi_start': '2025-09-01',
        'tfi_end': '2025-09-30',
        'repeat_start': '2025-09-01',
        'repeat_end': '2025-12-31'
    }
]

# Customer codes (all IDPOS retailers, excluding CVS)
customers = "'cds_8005', 'cds_8006', 'cds_8007', 'cds_8008', 'cds_8009', 'cds_8010', 'cds_8011', 'cds_8012', 'cds_8013'"

results = []

print("\nProcessing analyses...")
print("=" * 80)

for config in configs:
    print(f"\nAnalyzing: {config['product_name']}")
    print(f"TFI Period: {config['tfi_start']} to {config['tfi_end']}")
    print(f"Repeat Period: {config['repeat_start']} to {config['repeat_end']}")
    
    query = f"""
    WITH tfi_purchasers AS (
        SELECT DISTINCT
            idpos.shopper_key AS shopper_id
        FROM
            cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
            LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
            LEFT JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
        WHERE
            jp_category_name = 'Laundry'
            AND jp_sub_brand_alter_lang_name = '{config['sub_brand']}'
            AND jp_segment_4_name LIKE '{config['size_filter']}'
            AND idpos.data_provider_code_part IN ({customers})
            AND sales_period_group_end_date_part BETWEEN '{config['tfi_start']}' AND '{config['tfi_end']}'
            AND shopper.member_ind = 'Y'
    ),
    repeat_purchasers AS (
        SELECT DISTINCT
            idpos.shopper_key AS shopper_id
        FROM
            cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
            LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
            LEFT JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
            INNER JOIN tfi_purchasers tfi ON idpos.shopper_key = tfi.shopper_id
        WHERE
            jp_category_name = 'Laundry'
            AND jp_sub_brand_alter_lang_name = '{config['sub_brand']}'
            AND jp_segment_4_name LIKE '{config['size_filter_repeat']}'
            AND idpos.data_provider_code_part IN ({customers})
            AND sales_period_group_end_date_part > '{config['tfi_end']}'
            AND sales_period_group_end_date_part <= '{config['repeat_end']}'
            AND shopper.member_ind = 'Y'
    )
    SELECT
        (SELECT COUNT(DISTINCT shopper_id) FROM tfi_purchasers) AS tfi_shoppers,
        (SELECT COUNT(DISTINCT shopper_id) FROM repeat_purchasers) AS repeat_shoppers
    """
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        
        tfi_shoppers = result[0] if result[0] else 0
        repeat_shoppers = result[1] if result[1] else 0
        repeat_rate = (repeat_shoppers / tfi_shoppers * 100) if tfi_shoppers > 0 else 0
        
        results.append({
            'Product': config['product_name'],
            'TFI Period': f"{config['tfi_start']} to {config['tfi_end']}",
            'Repeat Period': f"{config['repeat_start']} to {config['repeat_end']}",
            'TFI Shoppers': tfi_shoppers,
            'Repeat Shoppers': repeat_shoppers,
            'Repeat Rate (%)': round(repeat_rate, 2)
        })
        
        print(f"  ✓ TFI Shoppers: {tfi_shoppers:,}")
        print(f"  ✓ Repeat Shoppers: {repeat_shoppers:,}")
        print(f"  ✓ Repeat Rate: {repeat_rate:.2f}%")

connection.close()

# Create results dataframe
df_results = pd.DataFrame(results)

print("\n" + "=" * 80)
print("FINAL RESULTS SUMMARY")
print("=" * 80)
print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"Channels: All channels excluding FAMILYMART, LAWSON, SEVEN ELEVEN")
print(f"Customers: All 9 IDPOS retailers aggregated")
print("\n")
print(df_results.to_string(index=False))

# Export to Excel
output_file = 'ariel_bottle_repeat_rate_results.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_results.to_excel(writer, sheet_name='Results', index=False)
    
    # Add metadata sheet
    metadata = pd.DataFrame({
        'Item': ['Analysis Date', 'Category', 'Channels Excluded', 'Retailers', 'Logic'],
        'Value': [
            datetime.now().strftime('%Y-%m-%d %H:%M'),
            'Laundry',
            'FAMILYMART, LAWSON, SEVEN ELEVEN',
            '9 IDPOS retailers (cds_8005 to cds_8013)',
            'TFI: First purchase in period | Repeat: Same shopper purchased again after TFI period'
        ]
    })
    metadata.to_excel(writer, sheet_name='Metadata', index=False)

print(f"\n✓ Results exported to: {output_file}")
print("\nReady for MCC comparison!")
