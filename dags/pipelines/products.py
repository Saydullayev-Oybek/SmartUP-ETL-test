from client import get_data
import pandas as pd
from config import ENDPOINTS
from load import loader

# ETL, full_load

## EXTRACT
print('Productsni yuklash boshlandi...')
products_df = get_data(ENDPOINTS['inventory'], 'inventory')

## TRANSFORM
# product table
df = products_df[products_df['state'] == 'A'][[
    'product_id',
    'name',
    'box_type_code', 
    'weight_netto', 
    'weight_brutto', 
    'litr', 
    'box_quant', 
    'order_no',
    'barcodes'
]]

df.drop_duplicates(inplace=True)
df['product_id'].dropna(inplace=True)

int_columns = ['product_id', 'weight_netto', 'weight_brutto', 'litr', 'box_quant', 'order_no']

for col in int_columns:
    df[col] = pd.to_numeric(df[col])

## LOAD
print("Product jadvalini databasega yuklash boshlandi....")

loader(df, 'products')

print("Yuklash tugadi....")


# TODO: product_group

# TODO: product_sector_code

# TODO: product_inventory_kinds