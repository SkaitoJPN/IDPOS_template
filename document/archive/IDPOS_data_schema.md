
### テーブル定義とキー情報

#### loyalty_transact_fct_v1_vw
- **shopper_key** (キー)
- **prod_key** (キー)
- **site_key** (キー)
- **Purchased Date**: time_period_end_date_part
- **Time**: transact_timestamp
- **Receipt ID**: transact_id (キー)
- **Sales Unit**: pos_unit_sales_qty
- **Sales Value**: pos_sales_amt
- **Sales Value without Tax**: pos_sales_without_tax_amt
- **Profit**: pos_profit_amt
- **Unit Price**: shelf_price_amt
- **Sale Flag**: promo_ind
- **Discount Quantity**: promo_pos_unit_sales_qty
- **Discount Amount**: promo_pos_val_sales_amt
- **Detailed Tax Classification**: custom_measure_001_val
- **Item Tax Rate**: custom_measure_002_val
- **Detailed Tax Amount**: custom_measure_003_val
- **aka_kuro_kbn**: custom_measure_004_val
- **Products Eligible for Points**: custom_measure_005_val
- **Transaction Order**: line_item_entry_seq_num (numeric)
- **Register Account ID**: register_account_id
- **Member Class**: custom_measure_501_text

#### shopper_dim_generic_vw
- **shopper_id**
- **shopper_key** (キー)
- **Shopper ID**: shopper_extern_id / member_id / membership_id
- **Belong Code**: attr_002_text
- **attr_100_text**
- **Member Flag/Indicator**: member_ind
- **Zip Code**: post_code
- **Age**: age
- **Gender**: gender_code
- **Birth Year**: birth_year
- **DM flag**: communication_ind
- **Birth Month**: birth_month
- **Occupation**: attr_002_text
- **Type of Occupation**: attr_003_text

#### prod_dim
- **Product Code/JAN Code**: prod_id
- **prod_key** (キー)
- **Product Name**: prod_name / cust_prod_name / prod_long_name
- **Wholesaler name**: cust_supply_name
- **Wholesaler code**: cust_supply_id
- **Customer Product level 5 Name**: cust_prod_level_5_name
- **Customer Product level 4 Name**: cust_prod_level_4_name
- **Customer Product level 3 Name**: cust_prod_level_3_name
- **Customer Product level 2 Name**: cust_prod_level_2_name
- **Customer Product level 1 Name**: cust_prod_level_1_name
- **Customer Product level 5 Code**: cust_prod_level_5_id
- **Customer Product level 4 Code**: cust_prod_level_4_id
- **Customer Product level 3 Code**: cust_prod_level_3_id
- **Customer Product level 2 Code**: cust_prod_level_2_id
- **Customer Product level 1 Code**: cust_prod_level_1_id
- **Retailer Name**: retailer_name
- **Product Group**: customer_product_attribute_60_value
- **Maker Code**: customer_product_attribute_01_text
- **Make Name**: customer_product_attribute_02_text
- **Master Cost Price**: cost_price
- **Order End Date**: mdm_obsolete_date
- **Order Start Date**: cust_prod_eff_date

#### site_dim_vw
- **Store Code**: site_id
- **site_key** (キー)
- **site geo key**: site_geo_key
- **Store Name**: site_name
- **Area Name 3 Name**: cust_site_level_3_name
- **Area Name 2 Name**: cust_site_level_2_name
- **Area Name**: cust_site_level_1_name
- **Area Code 3 Code**: cust_site_level_3_id
- **Area Code 2 Code**: cust_site_level_2_id
- **Area Code**: cust_site_level_1_id
- **Shope Type**: site_type_name
- **store number**: site_num
- **Address**: site_street_address
- **Zip Code**: site_post_code
- **Phone Num**: site_phone_num
- **Open Date**: open_date
- **Close Date**: close_date

#### cust_dim_ext_vw
- **jp_cust_id**: string, Officially maintained: Y, Definition: FN code
- **jp_cust_name**: string, Officially maintained: Y, Definition: FN name
- **jp_cust_channel_name**: string, Officially maintained: Y, Definition: Outlet (Channel_name)
- **jp_cust_sub_channel_name**: string, Officially maintained: Y, Definition: "Outlet (Channel_name) for that CHQ. For example, if RHQ level is SM and CHQ level is GMS like AEON case, GMS is set for this column"
- **jp_cust_team_id**: string, Officially maintained: Y, Definition: Cluster1 (G30/Electro/EMG)
- **jp_cust_team_name**: string, Officially maintained: Y, Definition: Organization2 from Census
- **jp_cust_sub_team_name**: string, Officially maintained: Y, Definition: Organization3 from Census
- **jp_cust_parent_group_name**: string, Officially maintained: Y, Definition: Identification of Retailer (RT) or Wholesaler (WS)
- **jp_cust_lvl_1_id**: string, Officially maintained: Y, Definition: GCDB XXHC (CHQ)
- **jp_cust_lvl_1_name**: string, Officially maintained: Y, Definition: CHQ name in English
- **jp_cust_lvl_1_alter_lang_name**: string, Officially maintained: Y, Definition: CHQ name in Japanese
- **jp_cust_lvl_2_id**: string, Officially maintained: Y, Definition: GCDB XX12 (RHQ1)
- **jp_cust_lvl_2_name**: string, Officially maintained: Y, Definition: RHQ1 name in English
- **jp_cust_lvl_2_alter_lang_name**: string, Officially maintained: Y, Definition: RHQ1 name in Japanese
- **jp_cust_lvl_3_name**: string, Officially maintained: Y, Definition: RHQ2 name in English
- **jp_cust_lvl_3_alter_lang_name**: string, Officially maintained: Y, Definition: RHQ2 name in Japanese
- **jp_cust_lvl_3_id**: string, Officially maintained: Y, Definition: GCDB XX12 (RHQ)
- **jp_local_category_name**: string, Officially maintained: Y, Definition: Zakka Direct Call
- **jp_local_sub_category_name**: string, Officially maintained: Y, Definition: Gillette Direct Call
- **jp_org_type_id**: string, Officially maintained: Y, Definition: Define CHQ/RHQ1/RHQ2/Site
- **jp_sales_parent_team_id**: string, Officially maintained: Y, Definition: "Store num of POS (System backend use)"
- **jp_cust_lvl_2_role_name**: string, Officially maintained: Y, Definition: Cluster2 (Detail of G30/Electro/EMG)
- **jp_cust_lvl_3_role_name**: string, Officially maintained: Y, Definition: Sub-Outlet (Sub channel name)
- **jp_local_store_id**: string, Officially maintained: Y, Definition: Planet ID (only for RT)
- **jp_local_sub_sub_team**: string, Officially maintained: Y, Definition: Organization5 from Census
- **jp_local_fn_code_2**: string, Officially maintained: Y, Definition: "FN code for next HY. This field is used for developing Division score card for next HY. As cust master is maintained one month delay vs Census for business tracking purpose, we need next HY information."
- **jp_local_fn_name_2**: string, Officially maintained: Y, Definition: "FN name for next HY. This field is used for developing Division score card for next HY. As cust master is maintained one month delay vs Census for business tracking purpose, we need next HY information."
- **jp_local_zakka_dc_nc_2**: string, Officially maintained: Y, Definition: "Zakka Direct Call for next HY. This field is used for developing Division score card for next HY. As cust master is maintained one month delay vs Census for business tracking purpose, we need next HY information."
- **jp_local_gillette_dc_nc_2**: string, Officially maintained: Y, Definition: "Gillette Direct Call for next HY. This field is used for developing Division score card for next HY. As cust master is maintained one month delay vs Census for business tracking purpose, we need next HY information."
- **jp_local_zakka_organization_code**: string, Officially maintained: Y, Definition: "Org Code for Zakka. If Sector retail, pick up first two digit from Org code"
- **jp_local_electro_organization_code**: string, Officially maintained: Y, Definition: "Org Code for Electro. If Sector retail, pick up first two digit from Org code"
- **jp_local_electro_direct_call**: string, Officially maintained: Y, Definition: Electro Direct Call
- **jp_local_electro_direct_call_2**: string, Officially maintained: Y, Definition: "Electro Direct Call for next HY. This field is used for developing Division score card for next HY. As cust master is maintained one month delay vs Census for business tracking purpose, we need next HY information."
- **jp_local_electro_team**: string, Officially maintained: Y, Definition: Organization2 from Census for Electro
- **jp_local_electro_sub_team**: string, Officially maintained: Y, Definition: Organization3 from Census for Electro
- **jp_local_electro_sub_sub_team**: string, Officially maintained: Y, Definition: Organization5 from Census for Electro

---

## テーブル: cust_dim_ext_vw（顧客マスタ拡張ビュー）

| カラム名                            | データ型         | 概要・用途                                                                   |
|-------------------------------------|-----------------|----------------------------------------------------------------------------|
| jp_cust_id                          | string          | 顧客コード。DC CHQ/MVWS Census管理                                          |
| jp_cust_name                        | string          | 顧客名。DC CHQ/MVWS Census管理                                             |
| jp_cust_channel_name                | string          | チャネル名（アウトレット）。DC CHQ/MVWS Census                             |
| jp_cust_sub_channel_name            | string          | サブチャネル名。例: RHQ=SM, CHQ=GMSの場合=GMS                              |
| jp_cust_team_id                     | string          | 組織1（G30/Electro/EMG）。DC CHQ/MVWS Census                               |
| jp_cust_team_name                   | string          | 組織2。Census由来                                                          |
| jp_cust_sub_team_name               | string          | 組織3。Census由来                                                          |
| jp_cust_parent_group_name           | string          | 小売/卸判別                                                                |
| jp_cust_lvl_1_id                    | string          | CHQ管理ID。DC CHQ/MVWS Census                                              |
| jp_cust_lvl_1_name                  | string          | CHQ名（英語）。SAP                                                         |
| jp_cust_lvl_1_alter_lang_name       | string          | CHQ名（日本語）。DC CHQ/MVWS Census                                        |
| jp_cust_lvl_2_id                    | string          | RHQ1管理ID。DC CHQ/MVWS Census                                             |
| jp_cust_lvl_2_name                  | string          | RHQ1名（英語）。SAP                                                        |
| jp_cust_lvl_2_alter_lang_name       | string          | RHQ1名（日本語）。DC CHQ/MVWS Census                                       |
| jp_cust_lvl_3_name                  | string          | RHQ2名（英語）。SAP                                                        |
| jp_cust_lvl_3_alter_lang_name       | string          | RHQ2名（日本語）。DC CHQ/MVWS Census                                       |
| jp_cust_lvl_3_id                    | string          | RHQ管理ID。COINS                                                           |
| jp_local_category_name              | string          | 雑貨DCコール。DC CHQ/MVWS Census                                           |
| jp_local_sub_category_name          | string          | Gillette DCコール                                                          |
| jp_org_type_id                      | string          | CHQ/RHQ1/RHQ2/Site定義                                                     |
| jp_sales_parent_team_id             | string          | POSデータ店舗番号（システム内部用）                                        |
| jp_cust_lvl_2_role_name             | string          | クラスター2：G30/Electro/EMG詳細                                           |
| jp_cust_lvl_3_role_name             | string          | サブアウトレット/サブチャネル名                                            |
| jp_local_store_id                   | string          | PlanetID（小売用）COINS管理                                                |
| jp_local_sub_sub_team               | string          | 組織5。Census                                                              |
| jp_local_fn_code_2                  | string          | 次期HY用FNコード                                                           |
| jp_local_fn_name_2                  | string          | 次期HY用FN名                                                               |
| jp_local_zakka_dc_nc_2              | string          | 次期HY用Zakka DCコール                                                     |
| jp_local_gillette_dc_nc_2           | string          | 次期HY用Gillette DCコール                                                  |
| jp_local_zakka_organization_code     | string          | Zakka用組織コード                                                          |
| jp_local_electro_organization_code  | string          | Electro組織コード                                                          |
| jp_local_electro_direct_call        | string          | Electro DCコール                                                           |
| jp_local_electro_direct_call_2      | string          | 次期HY用Electro DCコール                                                   |
| jp_local_electro_team               | string          | Electro用組織2                                                             |
| jp_local_electro_sub_team           | string          | Electro用組織3                                                             |
| jp_local_electro_sub_sub_team       | string          | Electro用組織5                                                             |

---

## テーブル: site_dim_ext_vw（店舗マスタ拡張ビュー）

| カラム名                          | データ型          | 概要・用途                                          |
|-----------------------------------|------------------|---------------------------------------------------|
| jp_site_id                        | string           | ローカルサイトID（RTID）。SAP管理                 |
| jp_site_name                      | string           | 店舗名（英語）SAP管理                             |
| jp_site_alter_lang_name           | string           | 店舗名（日本語）                                  |
| jp_site_type_name                 | string           | 店舗/EC/その他の区別                              |
| jp_store_kbd_cluster_name         | string           | LEGO                                              |
| jp_store_lego_cluster_name        | string           | LEGOクラスター                                    |
| jp_site_city_name                 | string           | 住所（市区町村）                                  |
| jp_site_street_address            | string           | 住所（番地）                                      |
| jp_site_state_name                | string           | 住所（都道府県）                                  |
| jp_site_post_code                 | string           | 郵便番号                                          |
| jp_site_country_name              | string           | 固定値："Japan"                                   |
| jp_site_phone_num                 | string           | 電話番号                                          |
| jp_site_region_name               | string           | 地域                                              |
| jp_nielsen_area_id                | string           | Nielsenエリア                                     |
| jp_lego_channel_name              | string           | LEGOチャネルクラスター                            |
| jp_direct_ship_ind                | string           | 直送可否インジケータ                              |
| jp_trax_ind                       | string           | Trax対象店舗なら”Y”、それ以外は"N"                |
| jp_trax_avail                     | string           | Trax対象店舗なら”Qualified”、それ以外は"-"        |
| jp_site_supervising_agency_name   | string           | MDS代理店名                                       |
| jp_agent_agency_name              | string           | Other Coverage                                    |
| jp_sdo_region_name                | string           | SDOエリア                                         |
| jp_site_audit_agency_name         | string           | MDSマネージャ名                                   |
| jp_store_coverage_id              | string           | カバレッジID                                      |
| jp_visiting_org_name              | string           | User Company                                      |
| jp_visiting_agent_1_id            | string           | SVエリア                                          |
| jp_visiting_agent_2_id            | string           | MDSエリア                                         |
| jp_visiting_agent_3_id            | string           | アカウントロールオーナー                          |
| jp_site_post_2_code               | string           | 郵便番号（JIS形式）                               |
| jp_site_longitude                 | decimal(19,8)    | 経度                                              |
| jp_site_latitude                  | decimal(19,8)    | 緯度                                              |
| jp_visits_per_month_pg_qty        | decimal(19,8)    | 月別訪問回数                                      |
| jp_visits_freq_trgt_qty           | decimal(19,8)    | レギュラーチェッカーフラグ                        |

---

## テーブル: prod_dim_ext_vw（商品マスタ拡張ビュー）

| カラム名                                      | データ型       | 概要・用途                                |
|-----------------------------------------------|---------------|-----------------------------------------|
| jp_brand_name                                 | string        | ブランド名（英語）                       |
| jp_brand_alter_lang_name                      | string        | ブランド名（日本語）                     |
| jp_product_sector_name                        | string        | プロダクトセクター名                     |
| jp_sub_sector_name                            | string        | プロダクトサブセクター名                 |
| jp_mfgr_name                                  | string        | 製造社名（英語）                         |
| jp_mfgr_alter_lang_name                       | string        | 製造社名（日本語）                       |
| jp_category_name                              | string        | カテゴリ名（英語）                       |
| jp_category_alter_lang_name                   | string        | カテゴリ名（日本語）                     |
| jp_sub_category_name                          | string        | サブカテゴリ名（英語）                   |
| jp_sub_category_alter_lang_name               | string        | サブカテゴリ名（日本語）                 |
| jp_segment_name                               | string        | セグメント名                             |
| jp_sub_segment_name                           | string        | サブセグメント名                         |
| jp_sub_brand_name                             | string        | サブブランド名（英語）                   |
| jp_sub_brand_alter_lang_name                  | string        | サブブランド名（日本語）                 |
| jp_prod_name                                  | string        | 商品名（英語）                           |
| jp_prod_alter_lang_name                       | string        | 商品名（日本語）                         |
| jp_item_gtin                                  | string        | JAN/EAN/GTINコード                       |
| jp_prod_family_1_name                         | string        | サブブランド詳細名（日本語）             |
| jp_prod_family_2_name                         | string        | サブブランド詳細名（英語）               |
| jp_size_name                                  | string        | サイズ                                  |
| jp_prod_form_name                             | string        | フォーム                                 |
| jp_variety_name                               | string        | 種類（レギュラー/キャンペーン等）        |
| jp_kbd_category_name                          | string        | KBDカテゴリ情報                          |
| jp_segment_1_name 〜 jp_segment_6_name        | string        | セグメント1〜6（体積/サイズ詳細等）      |
| jp_prod_type_name                             | string        | モデル番号(Electroのみ)                  |
| jp_kbd_sub_category_name                      | string        | KBDサブカテゴリ情報                      |
| jp_pack_size_name                             | string        | パックサイズ                             |
| jp_sdo_category_name                          | string        | ゴールデンポイント分けカテゴリ           |
| jp_business_unit_category_english_name         | string        | 棚割カテゴリ情報                         |
| jp_size_group_01_name, jp_size_group_02_name   | string        | ショッパーセグメント                     |
| jp_fpc_gcas_kataban                           | string        | モデル番号(Electroのみ)                  |
| jp_6mp_sku_group_sheet_name                   | string        | Nozomi 1H用ブランド名                    |
| jp_6mp_sku_group_code, ...                    | string        | 他Nozomi専用カラム等                     |
| jp_pg_item_status_code                        | string        | Zakka/Electro/Overlap SKU                |
| jp_fpc_gcas_sos_eos_timing_val                | string        | EAR施策タイミング                        |
| jp_local_pos_share_flag                       | string        | POSシェアIn/Outフラグ                    |
| jp_local_trax_flag                            | string        | TraxシェアIn/Outフラグ                   |
| jp_item_height/width/depth                    | decimal(19,8) | 商品高さ/幅/奥行き（Trax対応SKU用）      |

## テーブル: loyalty_transact_fct_v1_vw（購買トランザクション）

| カラム名                        | データ型    | 概要・用途                                                                                   |
|---------------------------------|------------|----------------------------------------------------------------------------------------------|
| shopper_key                     | bigint     | 購買者一意キー（Shopper_ID単位）                                                             |
| prod_key                        | bigint     | 商品一意キー（Prod_ID単位）                                                                  |
| site_key                        | bigint     | 店舗一意キー（Site_ID単位）                                                                  |
| data_provider_code_part         | string     | データ提供事業者識別子のパーティションキー（例: cds_8007 など。SSID連動）                    |
| sales_period_group_end_date_part| string     | 購買日パーティションキー（小売業者ごとに列が異なる場合あり）                                 |
| transact_timestamp              | timestamp  | トランザクション日時                                                                        |
| transact_id                     | string     | レシート番号・トランザクションID                                                            |
| pos_unit_sales_qty              | int        | 売上数量                                                                                     |
| pos_sales_amt                   | decimal    | 売上金額（税込）                                                                            |
| pos_sales_without_tax_amt       | decimal    | 売上金額（税抜）                                                                            |
| pos_profit_amt                  | decimal    | 粗利金額                                                                                    |
| shelf_price_amt                 | decimal    | 単価（売単価）                                                                              |
| promo_ind                       | string     | セール/プロモーション区分                                                                   |
| promo_pos_unit_sales_qty        | int        | プロモーション値引数量                                                                      |
| promo_pos_val_sales_amt         | decimal    | プロモーション値引金額                                                                      |
| custom_measure_001_val          | string     | 詳細税区分                                                                                  |
| custom_measure_002_val          | string     | 商品毎税率                                                                                   |
| custom_measure_003_val          | decimal    | 詳細税額                                                                                    |
| custom_measure_004_val          | string     | aka_kuro区分                                                                                |
| custom_measure_005_val          | string     | ポイント付与対象商品フラグ                                                                   |
| line_item_entry_seq_num         | int        | 明細連番                                                                                     |
| register_account_id             | string     | レジ番号                                                                                    |
| custom_measure_501_text         | string     | 会員区分（例: Sugi Yakkyokuなど）                                                            |

---

## テーブル: shopper_dim_generic_vw（購買者マスタ汎用ビュー）

| カラム名          | データ型   | 概要・用途                                                                               |
|-------------------|-----------|------------------------------------------------------------------------------------------|
| member_id         | string    | 会員ID/購買者ID                                                                           |
| shopper_key       | bigint    | 購買者一意キー                                                                            |
| attr_002_text     | string    | 帰属店コードなど（Belong Code/Occupation等）                                              |
| attr_003_text     | string    | 職業種別                                                                                  |
| attr_100_text     | string    | 帰属店コード（Sugi Yakkyoku等）                                                           |
| member_ind        | string    | 会員フラグ（非会員=N, 会員=Y）                                                            |
| post_code         | string    | 郵便番号                                                                                  |
| age               | int       | 年代（0,10,20,…、誕生日計算値）                                                           |
| gender_code       | int       | 性別（男性=1, 女性=2, 不明=0）                                                            |
| birth_year        | int       | 誕生年                                                                                    |
| birth_month       | int       | 誕生月                                                                                    |
| communication_ind | string    | DM受信フラグ                                                                              |

---

## テーブル: prod_dim（商品マスタ）

| カラム名                        | データ型   | 概要・用途                                                                        |
|---------------------------------|-----------|-----------------------------------------------------------------------------------|
| prod_id                         | string    | JAN/商品コード                                                                    |
| prod_key                        | bigint    | 商品一意キー                                                                      |
| prod_name                       | string    | 商品名                                                                            |
| cust_prod_name                  | string    | 顧客向け商品名                                                                    |
| prod_long_name                  | string    | 商品名（ロング名）                                                                 |
| cust_supply_name                | string    | 取引先名称（卸名）                                                                |
| cust_supply_id                  | string    | 取引先コード（卸コード）                                                          |
| cust_prod_level_5_name          | string    | サブセグメント名/品名など                                                         |
| cust_prod_level_4_name          | string    | セグメント名/細分類名など                                                         |
| cust_prod_level_3_name          | string    | サブカテゴリ名/商品小分類名など                                                   |
| cust_prod_level_2_name          | string    | カテゴリ名/商品中分類名など                                                       |
| cust_prod_level_1_name          | string    | 部門名/商品大分類名など                                                           |
| cust_prod_level_5_id            | string    | サブセグメントコード/品名コード                                                   |
| cust_prod_level_4_id            | string    | セグメントコード/細分類コード                                                     |
| cust_prod_level_3_id            | string    | サブカテゴリコード/小分類コード                                                   |
| cust_prod_level_2_id            | string    | カテゴリコード/中分類コード                                                       |
| cust_prod_level_1_id            | string    | 部門コード/大分類コード                                                           |
| retailer_name                   | string    | 小売業者名称                                                                      |
| customer_product_attribute_60_value | string | 商品グループ属性                                                                 |
| customer_product_attribute_01_text | string | メーカーコード                                                                   |
| customer_product_attribute_02_text | string | メーカー名称                                                                     |
| cost_price                      | decimal   | マスター原価                                                                     |
| mdm_obsolete_date               | timestamp | 取扱終了日                                                                       |
| cust_prod_eff_date              | timestamp | 取扱開始日                                                                       |

---

## テーブル: site_dim_vw（店舗マスタ）

| カラム名                 | データ型   | 概要・用途                                                                   |
|--------------------------|-----------|------------------------------------------------------------------------------|
| data_provider_key        | bigint    | データプロバイダキー（データ元業者識別）                                      |
| site_key                 | bigint    | 店舗一意キー                                                                 |
| site_geo_key             | bigint    | 店舗地理一意キー                                                             |
| site_type_key            | bigint    | 店舗種別キー                                                                 |
| own_party_key            | bigint    | 所有者キー                                                                   |
| site_id                  | string    | 店舗コード                                                                   |
| site_num                 | string    | 店舗番号                                                                     |
| site_name                | string    | 店舗名                                                                       |
| site_banner_name         | string    | 店舗バナー名                                                                 |
| site_street_address      | string    | 住所                                                                         |
| site_post_code           | string    | 郵便番号                                                                     |
| site_phone_num           | string    | 電話番号                                                                     |
| cust_site_level_1_name   | string    | エリア1名                                                                    |
| cust_site_level_2_name   | string    | エリア2名                                                                    |
| cust_site_level_3_name   | string    | エリア3名                                                                    |
| cust_site_level_4_name   | string    | エリア4名                                                                    |
| cust_site_level_5_name   | string    | エリア5名                                                                    |
| cust_site_level_6_name   | string    | エリア6名                                                                    |
| cust_site_level_1_id     | string    | エリア1コード                                                                |
| cust_site_level_2_id     | string    | エリア2コード                                                                |
| cust_site_level_3_id     | string    | エリア3コード                                                                |
| cust_site_level_4_id     | string    | エリア4コード                                                                |
| cust_site_level_5_id     | string    | エリア5コード                                                                |
| cust_site_level_6_id     | string    | エリア6コード                                                                |
| site_type_name           | string    | 店舗種別名                                                                   |
| open_date                | timestamp | 開店日                                                                       |
| close_date               | timestamp | 閉店日                                                                       |
| secure_group_key         | bigint    | セキュリティグループキー    

## よく使うカテゴリ名一覧
| jp_category_name      | jp_category_alter_lang_name | よくユーザーが使う呼び方                |
|-----------------------|-----------------------------|-----------------------------------------|
| Air Care              | ｴｱｹｱ                       | エア、Air                               |
| Appliances            | ｱﾌﾟﾗｲｱﾝｽ                   | エレ、エレクトロ                       |
| Baby Care             | ﾍﾞﾋﾞｰｹｱ                   | ベビー、Baby                           |
| Dish Care             | ﾃﾞｨｯｼｭｹｱ                 | ディッシュ、Dish                       |
| Fabric Enhancer       | 柔軟剤                     | FE                                      |
| Feminine Care         | ﾌｪﾐﾆﾝｹｱ                 | フェミ、フェミケア、Femi、Femi care   |
| Hair Care             | ﾍｱｹｱ                     | ヘア、Hair                             |
| Kitchen Cleaning      | ｷｯﾁﾝｸﾘｰﾆﾝｸﾞ             |                                         |
| Laundry               | ﾗﾝﾄﾞﾘｰ                     |                                         |
| Oral Care             | ｵｰﾗﾙｹｱ                   | ｵｰﾗﾙ、Oral                            |
| Shave Care            | ｶﾐｿﾘ                     | シェーブ、Shave                        |
---

## 注意事項

- 「Must not use」と記載されたカラムは**使用禁止**
- 意味不明なカラム、用途不明な場合は**データ定義等を確認**の上で利用を検討。必要であればユーザーに確認してください。
- 値の取得元（Census, SAP, COINSなど）は必要に応じてSQL条件・結合検討時に活用可能
- prod_dim_vw, site_dim_vwは小売店から貰っている定義をそのまま使っており、中身の値がまちまちですが、extという語がついているテーブルは小売店横断でカテゴリの粒度など標準化されたテーブルです。そのため、指示がない際にはextがついている方のテーブルを優先的に使うようにしてください。
---

---


### SQLクエリ生成の例
以下は、loyalty_transact_fct_v1_vwテーブルを基に他のテーブルとJOINするSQLクエリの例です。

```sql
SELECT
  idpos.shopper_key,
  idpos.site_key,
  idpos.transact_id,
  idpos.time_period_end_date_part,
  idpos.pos_unit_sales_qty,
  idpos.pos_sales_amt,
  ${granularity1},
  ${granularity2}
FROM
  cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
  LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
  LEFT JOIN id_pos_ai_1.site_dim_ext_vw site ON idpos.site_key = site.site_key
  LEFT JOIN id_pos_ai_1.site_dim_vw site_g ON idpos.site_key = site_g.site_key
  LEFT JOIN id_pos_ai_1.cust_dim_ext_vw cust ON site_g.own_party_key = cust.cust_key
  LEFT JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
  LEFT JOIN id_pos_ai_1.calendar_dim_vw cal ON idpos.sales_period_group_end_date_part = cal.day_date

また、対象の小売店は以下のようにdata_provider_code_partが振られています。
  -- TSURUHA JP(ツルハ)	= cds_8005
  -- TOMODS JP(トモズ)	= cds_8006
  -- SAPPORO DRUG JP(サツドラ)	= cds_8007
  -- KOHNAN JP(コーナン)	= cds_8008
  -- TRIAL JP(トライアル)	= cds_8009
  -- FUJI YAKUHIN JP(フジ、富士薬品)	= cds_8010
  -- CHUBU YAKUHIN JP(中薬, 中部薬品)	= cds_8011
  -- CAINZ JP(カインズ)	= cds_8012
  -- SUGI YAKKYOKU JP(スギ, スギ薬局)= cds_8013
  -- Arclands JP(アークランズ、アークランド)= cds_8017
例えば、中部薬品のIDPOSデータのみにフィルターをかけたい場合は、cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw.data_provider_code_part = "cds_8011"のように条件を指定することで結果を得ることができます。

以下は分析用テンプレートの一例です。必要に応じて参照してください。

# 01_C-TSR
## What is it?
- Extract C-TSR (Shopper Measures) from Customer IDPOS data.
- 5 Shopper Measures: # of traffic, closure rate, frequency, unit per purchase, price per unit

-- base table creation
WITH tran_table AS (
  SELECT
    data_provider_key,
    prod_key,
    site_key,
    shopper_key,
    transact_id,
    data_provider_code,
    sales_period_group_end_date_part AS created_date,
    pos_unit_sales_qty,
    pos_sales_amt
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
  WHERE
    sales_period_group_end_date_part BETWEEN
      DATE '${2_start_date}'::date - INTERVAL '1 year'
    AND
      DATE '${3_end_date}'
    AND data_provider_code_part in (${1_customer_filter})
),
prod_table AS (
  SELECT
    prod_key,
    jp_brand_name,
    jp_brand_alter_lang_name,
    jp_category_name,
    jp_sub_category_name,
    jp_segment_name,
    jp_sub_segment_name,
    jp_sub_brand_name,
    jp_sub_brand_alter_lang_name,
    jp_prod_name,
    jp_prod_alter_lang_name,
    jp_item_gtin,
    jp_prod_family_1_name,
    jp_prod_form_name,
    jp_size_name,
    jp_pack_size_name
  FROM
    id_pos_ai_1.prod_dim_ext_vw
  WHERE
    jp_category_name = '${4_category_filter}'
),
cust_table AS (
  SELECT
    cust_key,
    jp_cust_lvl_1_name,
    jp_cust_lvl_2_name,
    jp_cust_lvl_3_name
  FROM
    id_pos_ai_1.cust_dim_ext_vw
),
site_ext_table AS (
  SELECT
    site_key,
    jp_site_id,
    jp_site_name,
    jp_site_alter_lang_name
  FROM
    id_pos_ai_1.site_dim_ext_vw
),
site_table AS (
  SELECT
    site_key,
    own_party_key
  FROM
    id_pos_ai_1.site_dim_vw
),
shopper_table AS (
  SELECT
    shopper_key as shopper_key_1,
    member_ind
  from
    id_pos_ai_1.shopper_dim_generic_vw
),
base_table AS (
  SELECT
    *
  FROM
    tran_table
      LEFT OUTER JOIN prod_table
        ON tran_table.prod_key = prod_table.prod_key
      LEFT OUTER JOIN site_ext_table
        ON tran_table.site_key = site_ext_table.site_key
      LEFT OUTER JOIN site_table
        ON tran_table.site_key = site_table.site_key
      LEFT OUTER JOIN cust_table
        ON site_table.own_party_key = cust_table.cust_key
      LEFT OUTER JOIN shopper_table
        ON tran_table.shopper_key = shopper_table.shopper_key_1
  WHERE
    prod_table.prod_key IS NOT NULL
    AND member_ind = "Y"
),


-- CTSR calcuration table
ty AS (
  SELECT
    NVL(${5_granularity_1}, 'Total') as  ${5_granularity_1},
    NVL(${6_granularity_2}, 'Total') as  ${6_granularity_2},
    NVL(${7_granularity_3}, 'Total') as  ${7_granularity_3},
    SUM(pos_unit_sales_qty * pos_sales_amt) AS total_value,
    SUM(pos_unit_sales_qty) AS total_unit,
    COUNT(DISTINCT shopper_key) AS total_unique_id,
    COUNT(DISTINCT CONCAT(shopper_key, created_date)) AS total_visit_counts
  FROM
    base_table
  WHERE
    CREATED_DATE BETWEEN DATE '${2_start_date}' AND DATE '${3_end_date}'
  GROUP BY
    ROLLUP(${5_granularity_1}, ${6_granularity_2}, ${7_granularity_3}) 
),
ya AS (
  SELECT
    NVL(${5_granularity_1}, 'Total') as  ${5_granularity_1},
    NVL(${6_granularity_2}, 'Total') as  ${6_granularity_2},
    NVL(${7_granularity_3}, 'Total') as  ${7_granularity_3},
    SUM(pos_unit_sales_qty * pos_sales_amt) AS total_value,
    SUM(pos_unit_sales_qty) AS total_unit,
    COUNT(DISTINCT shopper_key) AS total_unique_id,
    COUNT(DISTINCT CONCAT(shopper_key, created_date)) AS total_visit_counts
  FROM
    base_table
  WHERE
    created_date BETWEEN
      DATE '${2_start_date}'::date - INTERVAL '1 year'
    AND
      DATE '${3_end_date}'::date - INTERVAL '1 year'
  GROUP BY
    ROLLUP(${5_granularity_1}, ${6_granularity_2}, ${7_granularity_3}) 
),
ty_base AS (
  SELECT
    COUNT(DISTINCT shopper_key) AS total_unique_id
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
  WHERE
    sales_period_group_end_date_part BETWEEN DATE '${2_start_date}' AND DATE '${3_end_date}'
),
ya_base AS (
  SELECT
    COUNT(DISTINCT shopper_key) AS total_unique_id
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
  WHERE
    sales_period_group_end_date_part BETWEEN
      DATE '${2_start_date}'::date - INTERVAL '1 year'
    AND
      DATE '${3_end_date}'::date - INTERVAL '1 year'
)

SELECT
  ty.${5_granularity_1},
  ty.${6_granularity_2},
  ty.${7_granularity_3},
  ROUND(ty.total_value, 0) AS value_TY,
  ROUND(ya.total_value, 0) AS value_YA,
  ROUND((ty.total_value / ya.total_value) * 100, 2) AS value_IYA,
  ty_base.total_unique_id AS total_num_of_shopper_TY,
  ya_base.total_unique_id AS total_num_of_shoopper_YA,
  ROUND((ty_base.total_unique_id / ya_base.total_unique_id) * 100, 2) AS total_num_of_shopper_IYA,
  ty.total_unique_id AS num_of_shopper_TY,
  ya.total_unique_id AS num_of_shopper_YA,
  ROUND((ty.total_unique_id / ya.total_unique_id) * 100, 2) AS num_of_shopper_IYA,
  ROUND((ty.total_unique_id / ty_base.total_unique_id) * 100, 5) AS closure_rate_TY,
  ROUND((ya.total_unique_id / ya_base.total_unique_id) * 100, 5) AS closure_rate_YA,
  ROUND(
    (ty.total_unique_id / ty_base.total_unique_id) / (ya.total_unique_id / ya_base.total_unique_id)
    * 100,
    2
  ) AS closure_rate_IYA,
  ROUND(ty.total_value / ty.total_unique_id) AS value_per_shopper_TY,
  ROUND(ya.total_value / ya.total_unique_id) AS value_per_shopper_YA,
  ROUND(
    (ty.total_value / ty.total_unique_id) / (ya.total_value / ya.total_unique_id) * 100, 2
  ) AS value_per_shopper_IYA,
  ROUND(ty.total_visit_counts / ty.total_unique_id, 2) AS purchase_frequency_TY,
  ROUND(ya.total_visit_counts / ya.total_unique_id, 2) AS purchase_frequency_YA,
  ROUND(
    (ty.total_visit_counts / ty.total_unique_id) / (ya.total_visit_counts / ya.total_unique_id)
    * 100,
    2
  ) AS purchase_frequency_IYA,
  ROUND(ty.total_unit / ty.total_visit_counts, 2) AS unit_per_purchase_TY,
  ROUND(ya.total_unit / ya.total_visit_counts, 2) AS unit_per_purchase_YA,
  ROUND(
    (ty.total_unit / ty.total_visit_counts) / (ya.total_unit / ya.total_visit_counts) * 100, 2
  ) AS unit_per_purchase_IYA,
  ROUND(ty.total_value / ty.total_unit, 2) AS Avg_unit_price_TY,
  ROUND(ya.total_value / ya.total_unit, 2) AS Avg_unit_price_YA,
  ROUND(
    (ty.total_value / ty.total_unit) / (ya.total_value / ya.total_unit) * 100, 2
  ) AS Avg_unit_price_IYA
FROM
  ty
    LEFT JOIN ya
      ON ty.${5_granularity_1} = ya.${5_granularity_1}
      AND ty.${6_granularity_2} = ya.${6_granularity_2}
      AND ty.${7_granularity_3} = ya.${7_granularity_3}
    LEFT JOIN ty_base
    LEFT JOIN ya_base
ORDER BY
  value_TY DESC
## Parameter example
3_end_date: 2024-12-31
5_granularity_1: jp_sub_category_name
4_category_filter: Air Care
6_granularity_2: jp_brand_alter_lang_name
7_granularity_3: jp_sub_brand_alter_lang_name
1_customer_filter: 'cds_8013'
2_start_date: 2024-07-01

# 02_SoV
## What is it?
- Extract SoV (Source of Volume) from Customer IDPOS data.
- SoV = What did they buy before buying XXX?

WITH base AS (
  SELECT
    jp_item_gtin,
    jp_prod_name,
    jp_brand_name,
    jp_brand_alter_lang_name,
    jp_category_name,
    jp_sub_category_name,
    jp_segment_name,
    jp_sub_segment_name,
    jp_sub_brand_name,
    jp_sub_brand_alter_lang_name,
    jp_prod_alter_lang_name,
    jp_prod_family_1_name,
    jp_prod_form_name,
    jp_size_name,
    jp_pack_size_name,
    idpos.shopper_key AS id,
    pos_unit_sales_qty as unit,
    pos_sales_amt as value,
    CAST(idpos.sales_period_group_end_date_part AS DATE) AS purchase_date
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    LEFT JOIN id_pos_ai_1.site_dim_vw site ON idpos.site_key = site.site_key
    LEFT JOIN id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
  WHERE
    jp_category_name = '${category_filter}'
    AND idpos.data_provider_code_part IN (${customer_filter})
    AND sales_period_group_end_date_part BETWEEN ${pre_start_date} AND ${post_end_date}
    AND shopper.member_ind = 'Y'
),
pre AS (
  SELECT
    ${sov_granularity} as sov_granularity,
    id,
    value,
    unit
  FROM base
  WHERE base.purchase_date BETWEEN ${pre_start_date} AND ${pre_end_date}
),
post AS (
  SELECT
    distinct id
  FROM base
  WHERE ${target_condition}
    AND base.purchase_date BETWEEN ${post_start_date} AND ${post_end_date}
)

SELECT
  t2.sov_granularity,
  COUNT(DISTINCT t2.id) AS SoV_ID,
  ROUND(sum(t2.value),0) AS SoV_Value,
  ROUND(sum(t2.unit),0) AS SoV_Volume
FROM post AS t1
LEFT JOIN pre AS t2 ON t1.id = t2.id
WHERE t2.id IS NOT NULL
GROUP BY t2.sov_granularity
ORDER BY SoV_ID DESC
## Parameter Example 
pre_start_date: '2024-10-01'
customer_filter: 'cds_8013'
target_condition: jp_sub_brand_alter_lang_name in ("ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ", "ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ")
pre_end_date: '2024-12-31'
category_filter: Laundry
post_end_date: '2025-01-31'
post_start_date: '2025-01-01'
sov_granularity: jp_sub_brand_alter_lang_name

# Next purchase
## What is it?
- Extract # of shopper who purchased target product condition right after they purchased source prodcut.
-- base table creation
WITH tran_table AS (
  SELECT
    data_provider_key,
    prod_key,
    site_key,
    shopper_key,
    transact_id,
    data_provider_code,
    sales_period_group_end_date_part AS created_date,
    pos_unit_sales_qty,
    pos_sales_amt
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
  WHERE
     sales_period_group_end_date_part BETWEEN ${2_start_date} AND DATE_ADD(${3_end_date}, ${4_post_period_days})
    AND data_provider_code_part = ${1_data_provider_code}
),
prod_table AS (
  SELECT
    prod_key,
    jp_brand_name,
    jp_category_name,
    jp_sub_category_name,
    jp_sub_segment_name,
    jp_sub_brand_name,
    jp_sub_brand_alter_lang_name,
    jp_prod_name,
    jp_prod_alter_lang_name,
    jp_item_gtin,
    jp_prod_family_1_name,
    jp_prod_form_name,
    jp_segment_1_name
  FROM
    id_pos_ai_1.prod_dim_ext_vw
  WHERE
    ${6_target_product_condition}
),
cust_table AS (
  SELECT
    cust_key,
    jp_cust_lvl_1_name,
    jp_cust_lvl_2_name,
    jp_cust_lvl_3_name
  FROM
    id_pos_ai_1.cust_dim_ext_vw
),
site_ext_table AS (
  SELECT
    site_key,
    jp_site_id,
    jp_site_name,
    jp_site_alter_lang_name
  FROM
    id_pos_ai_1.site_dim_ext_vw
),
site_table AS (
  SELECT
    site_key,
    own_party_key
  FROM
    id_pos_ai_1.site_dim_vw
),
shopper_table AS (
  SELECT
    shopper_key as shopper_key_1,
    member_ind
  from
    id_pos_ai_1.shopper_dim_generic_vw
),

-- Next purchase analysis
base AS (
  SELECT
    shopper_key,
    data_provider_code,
    created_date,
    pos_unit_sales_qty,
    pos_sales_amt,
    -- ROW_NUMBER() OVER (PARTITION BY shopper_key ORDER BY created_date) AS purchase_number,
    ${7_granularity}
    FROM
    tran_table
      LEFT OUTER JOIN prod_table ON tran_table.prod_key = prod_table.prod_key
      LEFT OUTER JOIN site_ext_table ON tran_table.site_key = site_ext_table.site_key
      LEFT OUTER JOIN site_table ON tran_table.site_key = site_table.site_key
      LEFT OUTER JOIN cust_table ON site_table.own_party_key = cust_table.cust_key
      LEFT OUTER JOIN shopper_table ON tran_table.shopper_key = shopper_table.shopper_key_1
  WHERE prod_table.prod_key IS NOT NULL
    AND member_ind = "Y"
  ORDER BY shopper_key, created_date
),
source_product_first_purchased_date AS (
  SELECT 
    shopper_key,
    min(created_date) AS trial_date
  FROM base
  WHERE ${5_source_product_condition}
  GROUP BY shopper_key
),
next_purchase_identification AS (
  SELECT
    base.shopper_key AS shopper_key,
    created_date,
    trial_date,
    datediff(created_date,trial_date) AS diff,
    ROW_NUMBER() OVER (PARTITION BY base.shopper_key ORDER BY created_date) AS purchase_number,
    ${7_granularity}
  FROM base
    LEFT OUTER JOIN source_product_first_purchased_date  AS sppd
      ON base.shopper_key = sppd.shopper_key
  ORDER BY base.shopper_key, created_date 
)
SELECT 
  "TTL" AS granurality,
  COUNT(DISTINCT shopper_key) AS total_num_of_shoppers
FROM next_purchase_identification
WHERE diff > 0
  AND purchase_number = 2

UNION

SELECT 
  ${7_granularity},
  COUNT(DISTINCT shopper_key) AS total_num_of_shoppers
FROM next_purchase_identification
WHERE diff > 0
  AND purchase_number = 2
GROUP BY ${7_granularity}
ORDER BY total_num_of_shoppers DESC
## Parameter Sample
5_source_product_condition: jp_sub_brand_alter_lang_name = "ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ"
3_end_date: "2024-05-31"
1_data_provider_code: "cds_8005"
4_post_period_days: 60
7_granularity: jp_sub_brand_alter_lang_name
6_target_product_condition: jp_segment_name = "重質洗剤"
2_start_date: "2024-03-01"


# Co-Purchase
## What is it?
- Identifying what consumers tend to buy with the target products.
-- ID Based Co-Purchase
%sql
%sql
WITH iis_table AS (
    SELECT * 
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    WHERE idpos.data_provider_code_part in (${data_provider_code})
    AND idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
), temp_jan_table AS (
    SELECT DISTINCT
        idpos.shopper_key AS min_key,
        'target_products' AS product
    FROM iis_table idpos
    LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    LEFT JOIN id_pos_ai_1.prod_dim_vw prod2 ON idpos.prod_key = prod2.prod_key
    left join id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
    AND ${target_condition}
    and shopper.member_ind = "Y"

), temp_co_purchase_table AS (
    SELECT DISTINCT
        idpos.shopper_key AS min_key,
        ${product_granularity} AS product
    FROM iis_table idpos
    LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    LEFT JOIN id_pos_ai_1.prod_dim_vw prod2 ON idpos.prod_key = prod2.prod_key
    left join id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
    and ${co_purchase_universe_condition}
    and shopper.member_ind = "Y"

), temp_table AS (
    SELECT * FROM temp_jan_table
    UNION ALL
    SELECT * FROM temp_co_purchase_table
), co_purchase_join_table AS (
    SELECT
        t1.min_key AS min_key,
        t1.product AS product1,
        t2.product AS product2
    FROM temp_table t1
    JOIN temp_table t2 ON t1.min_key = t2.min_key
    WHERE t1.product < t2.product
), co_purchase_count_table AS (
    SELECT 
        product1,
        product2,
        COUNT(1) AS co_purchase_count,
        TRUE AS join_key
    FROM co_purchase_join_table
    GROUP BY product1, product2
), single_purchase_count_table AS (
    SELECT 
        product,
        COUNT(min_key) AS purchase_count
    FROM temp_table
    GROUP BY product
), basket_universe AS (
    SELECT 
        COUNT(DISTINCT min_key) AS total_purchase,
        TRUE AS join_key
    FROM temp_table
), avg_co_purchase AS (
    SELECT
        AVG(co_purchase_count) AS avg_co_purchase_count,
        TRUE AS join_key
    FROM co_purchase_count_table
    WHERE product1 = 'target_products' OR product2 = 'target_products'
)
SELECT
    t1.product1,
    t1.product2,
    (t1.co_purchase_count / (t2.purchase_count * t3.purchase_count)) * t4.total_purchase AS lift,
    t2.purchase_count AS product1_count,
    t3.purchase_count AS product2_count,
    t1.co_purchase_count
FROM co_purchase_count_table t1
LEFT JOIN single_purchase_count_table t2 ON t1.product1 = t2.product
LEFT JOIN single_purchase_count_table t3 ON t1.product2 = t3.product
LEFT JOIN basket_universe t4 ON t1.join_key = t4.join_key
LEFT JOIN avg_co_purchase t5 ON t1.join_key = t5.join_key
WHERE (product1 = 'target_products' OR product2 = 'target_products')
AND t1.co_purchase_count > ${min_co_purchase_count}
ORDER BY lift DESC

##Param Example
start_date: "2024-10-01"
min_co_purchase_count: 2
target_condition: jp_sub_brand_name = 'PANTENE Base'
end_date: "2025-03-31"
co_purchase_universe_condition: jp_sub_category_name = 'Hair Care'
product_granularity: jp_segment_name
data_provider_code: "cds_8010"

-- Basked Based 
%sql
WITH iis_table AS (
    SELECT * 
    FROM cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    WHERE idpos.data_provider_code_part in (${data_provider_code})
    AND idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
), temp_jan_table AS (
    SELECT DISTINCT
        concat(idpos.shopper_key,idpos.sales_period_group_end_date_part) AS min_key,
        'target_products' AS product
    FROM iis_table idpos
    LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    LEFT JOIN id_pos_ai_1.prod_dim_vw prod2 ON idpos.prod_key = prod2.prod_key
    left join id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
    AND ${target_condition}
    and shopper.member_ind = "Y"

), temp_co_purchase_table AS (
    SELECT DISTINCT
        concat(idpos.shopper_key,idpos.sales_period_group_end_date_part) AS min_key,
        prod.${product_granularity} AS product
    FROM iis_table idpos
    LEFT JOIN id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    LEFT JOIN id_pos_ai_1.prod_dim_vw prod2 ON idpos.prod_key = prod2.prod_key
    left join id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
    WHERE idpos.sales_period_group_end_date_part between ${start_date} and ${end_date}
    and ${co_purchase_universe_condition}
    and shopper.member_ind = "Y"

), temp_table AS (
    SELECT * FROM temp_jan_table
    UNION ALL
    SELECT * FROM temp_co_purchase_table
), co_purchase_join_table AS (
    SELECT
        t1.min_key AS min_key,
        t1.product AS product1,
        t2.product AS product2
    FROM temp_table t1
    JOIN temp_table t2 ON t1.min_key = t2.min_key
    WHERE t1.product < t2.product
), co_purchase_count_table AS (
    SELECT 
        product1,
        product2,
        COUNT(1) AS co_purchase_count,
        TRUE AS join_key
    FROM co_purchase_join_table
    GROUP BY product1, product2
), single_purchase_count_table AS (
    SELECT 
        product,
        COUNT(min_key) AS purchase_count
    FROM temp_table
    GROUP BY product
), basket_universe AS (
    SELECT 
        COUNT(DISTINCT min_key) AS total_purchase,
        TRUE AS join_key
    FROM temp_table
), avg_co_purchase AS (
    SELECT
        AVG(co_purchase_count) AS avg_co_purchase_count,
        TRUE AS join_key
    FROM co_purchase_count_table
    WHERE product1 = 'target_products' OR product2 = 'target_products'
)
SELECT
    t1.product1,
    t1.product2,
    (t1.co_purchase_count / (t2.purchase_count * t3.purchase_count)) * t4.total_purchase AS lift,
    t2.purchase_count AS product1_count,
    t3.purchase_count AS product2_count,
    t1.co_purchase_count
FROM co_purchase_count_table t1
LEFT JOIN single_purchase_count_table t2 ON t1.product1 = t2.product
LEFT JOIN single_purchase_count_table t3 ON t1.product2 = t3.product
LEFT JOIN basket_universe t4 ON t1.join_key = t4.join_key
LEFT JOIN avg_co_purchase t5 ON t1.join_key = t5.join_key
WHERE (product1 = 'target_products' OR product2 = 'target_products')
AND t1.co_purchase_count > ${min_co_purchase_count}
ORDER BY lift DESC

## Parameter Sample
start_date: "2024-10-01"
min_co_purchase_count: 2
target_condition: jp_sub_brand_name = 'PANTENE Base'
end_date: "2025-03-31"
co_purchase_universe_condition: jp_sub_category_name = 'Hair Care'
product_granularity: jp_sub_brand_name
data_provider_code: "cds_8010"


# Bem Diagram
## What is it?
- Extract data for Ben Diagram (cannibalization) from Customer IDPOS data.

%sql
with data as (
  select
    idpos.shopper_key,
    case
      when ${target_col} not in ${target_value_list} then "others"
      else ${target_col}
    end as target_col
  from
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw idpos
    left join id_pos_ai_1.prod_dim_ext_vw prod ON idpos.prod_key = prod.prod_key
    left join id_pos_ai_1.shopper_dim_generic_vw shopper ON idpos.shopper_key = shopper.shopper_key
  WHERE
    idpos.data_provider_code_part in (${data_provider_code})
    and ${universe_condition}
    and shopper.member_ind = "Y"
    and idpos.sales_period_group_end_date_part between '${start_date}'
    and '${end_date}'
),
id_basket as (
  select
    data.shopper_key,
    sort_array(collect_set(target_col)) as id_basket
  from
    data
  group by
    data.shopper_key
  having
    count(data.shopper_key) >= ${min_purchase_count}
)
select
  id_basket,
  count(distinct shopper_key) as shopper
from
  id_basket
group by
  id_basket
order by
  shopper desc

##param example
universe_condition: jp_sub_brand_alter_lang_name="ｱﾘｴｰﾙｼﾞｪﾙ"
start_date: 2024-01-01
target_value_list: ("","詰替超特大","詰替超ｼﾞｬﾝﾎﾞ","詰替ｳﾙﾄﾗｼﾞｬﾝﾎﾞ", "詰替超ｳﾙﾄﾗｼﾞｬﾝﾎﾞ")
end_date: 2024-06-30
data_provider_code: "cds_8005"
min_purchase_count: 10
target_col: jp_pack_size_name


# Trial and Repeat
## What is it?
- **trial shopper**: not purchased the product (in 4_product_filter) in the past 365days
- **repeat shopper**: have purchsed the product (in 4_product_filter) in the past 365 days
- **[Watch out]**: Trial + repeat is not total # of shopper. Some shopper do trial and repeat during the period.
- **[Advanced]**: You can extract weekly data to see the initiative progress. weekly data is commented out. Please modify it by yourself. 
- prod filterでtrial 判定粒度を調整 (カテゴリートライアルを調べたい場合はjp_sub_category_alter_lang_name, sub brand trialはjp_sub_brand_name)

WITH latest_date AS (
  SELECT
   MIN(min_date) AS valid_start_date,
   max(max_date) AS valid_last_date
  FROM
    id_pos_ai_1_output.meta_latest_date
  WHERE
    data_provider_code_part IN (${1_customer_filter})
),
prod_table AS (
  SELECT
    prod_key,
    ${5_granularity_1},
    ${6_granularity_2},
    ${7_granularity_3}
  FROM
    id_pos_ai_1.prod_dim_ext_vw
  WHERE
    ${4_product_filter}
),
cust_table AS (
  SELECT
    cust_key,
    jp_cust_lvl_1_name AS cust_name
  FROM
    id_pos_ai_1.cust_dim_ext_vw
),
site_table AS (
  SELECT
    site_key,
    own_party_key
  FROM
    id_pos_ai_1.site_dim_vw
),
tran_table AS (
  SELECT
    cut.cust_name,
    pt.${5_granularity_1},
    pt.${6_granularity_2},
    pt.${7_granularity_3},
    ct.shopper_key AS id,
    ct.sales_period_group_end_date_part AS created_date,
    CASE
      WHEN LAG(ct.sales_period_group_end_date_part) OVER (PARTITION BY ct.shopper_key ORDER BY ct.sales_period_group_end_date_part) IS NOT NULL
           AND DATEDIFF(day, LAG(ct.sales_period_group_end_date_part) OVER (PARTITION BY ct.shopper_key ORDER BY ct.sales_period_group_end_date_part), ct.sales_period_group_end_date_part) <= 365
      THEN 'repeat'
      ELSE 'trial'
    END AS purchase_type
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw ct
  LEFT JOIN prod_table pt ON pt.prod_key = ct.prod_key
  LEFT OUTER JOIN site_table st ON ct.site_key = st.site_key
  LEFT OUTER JOIN cust_table cut ON st.own_party_key = cut.cust_key
  WHERE
    ct.sales_period_group_end_date_part BETWEEN (SELECT valid_start_date FROM latest_date) AND (SELECT valid_last_date FROM latest_date)
    AND ct.data_provider_code_part IN (${1_customer_filter})
    AND pt.prod_key IS NOT NULL
)
SELECT
  NVL(${5_granularity_1},"TTL") AS ${5_granularity_1},
  NVL(${6_granularity_2},"TTL") AS ${6_granularity_2},
  NVL(${7_granularity_3},"TTL") AS ${7_granularity_3},
--  date_format(date_trunc('week', created_date), "yyyy/MM/dd") AS week_start_date,
--  ${8_granularity_4},
  YEAR(created_date) AS YEAR,
  MONTH(created_date) AS MONTH,
  COUNT(DISTINCT id) AS n_total,
  COUNT(DISTINCT CASE WHEN purchase_type = 'trial' THEN id END) AS n_trial,
  COUNT(DISTINCT CASE WHEN purchase_type = 'repeat' THEN id END) AS n_repeat
FROM
  tran_table
WHERE created_date between '${2_start_date}' and '${3_end_date}'
GROUP BY 
  ${5_granularity_1},
  ${6_granularity_2},
  YEAR(created_date),
  MONTH(created_date),
--  date_format(date_trunc('week', created_date), "yyyy/MM/dd")
   CUBE (${7_granularity_3})


## param
8_granularity_4: jp_item_gtin
3_end_date: 2029-07-23
5_granularity_1: jp_category_name
6_granularity_2: jp_mfgr_name
7_granularity_3: jp_sub_brand_name
1_customer_filter: 'cds_8007','cds_8006','cds_8005','cds_8009','cds_8011','cds_8012','cds_8013'
4_product_filter: jp_mfgr_name = "P&G" and jp_sub_category_alter_lang_name = "洗濯洗剤"
2_start_date: 2023-01-01

# 07_Shopper_Demographic
## What is it?
- Extract # of shopper by gender/age from Customer IDPOS data.

%sql
WITH tran_table AS (
  SELECT
    data_provider_key,
    prod_key,
    shopper_key,
    transact_id,
    data_provider_code_part,
    sales_period_group_end_date_part,
    pos_unit_sales_qty,
    pos_sales_amt
  FROM
    cdl_customer_prod.gold_customer_loyalty.loyalty_transact_fct_v1_vw
  WHERE
  sales_period_group_end_date_part BETWEEN
      DATE '${2_start_date}'
    AND
      DATE '${3_end_date}'
    AND data_provider_code_part in (${1_customer_filter})
),
prod_table AS (
  SELECT
    prod_key,
    jp_brand_name,
    jp_mfgr_name,
    jp_category_name,
    jp_sub_category_name,
    jp_sub_segment_name,
    jp_sub_brand_name,
    jp_sub_brand_alter_lang_name,
    jp_prod_name,
    jp_prod_alter_lang_name,
    jp_item_gtin,
    jp_prod_family_1_name,
    jp_prod_form_name,
    jp_segment_1_name
  FROM
    id_pos_ai_1.prod_dim_ext_vw
  WHERE
    jp_category_name = '${4_category_filter}'
),
shopper_table AS (
  SELECT
    shopper_key,
    member_ind,
    gender_code,
    age
  FROM
    id_pos_ai_1.shopper_dim_generic_vw
)


SELECT
  gender_code,
  case gender_code
    when "0" then "not register"
    when "1" then "male"
    when "2" then "female"
  end as gender,
  age,
  COUNT(DISTINCT shopper_table.shopper_key) as num_of_shopper
FROM
  tran_table
    LEFT OUTER JOIN prod_table
      ON tran_table.prod_key = prod_table.prod_key
    LEFT OUTER JOIN shopper_table
      ON tran_table.shopper_key = shopper_table.shopper_key
WHERE
  ${5_target_condition}
  AND shopper_table.shopper_key IS NOT NULL
  AND age BETWEEN 0 and 100
GROUP BY
  gender_code,
  gender,
  age
ORDER BY
  gender_code,
  gender,
  age

3_end_date: 2024-12-31
4_category_filter: Laundry
5_target_condition: jp_sub_brand_alter_lang_name in ("ｱﾘｴｰﾙｼﾞｪﾙﾎﾞｰﾙ", "ﾎﾞｰﾙﾄﾞｼﾞｪﾙﾎﾞｰﾙ")
1_customer_filter: 'cds_8005','cds_8006','cds_8007','cds_8008','cds_8009','cds_8010','cds_8011','cds_8012','cds_8013'
2_start_date: 2024-10-01
First message in conversation