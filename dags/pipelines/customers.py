from client import get_data
import pandas as pd
from load import loader
from config import ENDPOINTS

## legal_person
# EXTRACT

legal_entity_df = get_data(ENDPOINTS['legal_person'], 'legal_person')

# TRANSFORM
# customers
legal_df = legal_entity_df.loc[
    legal_entity_df['state'] == 'A',
    ['person_id', 'name', 'main_phone', 'telegram', 'address']
]

legal_df.drop_duplicates(inplace=True)

legal_df['type'] = 'legal_entity'

# customer_groups
rows = []
for _, row  in legal_entity_df[['person_id', 'groups']].iterrows():
    # print(row)
    for group in row['groups']:
        rows.append({
            'person_id': row['person_id'],
            'group_id': group.get('group_id'),
            'group_code': group.get('group_code'),
            'type_id': group.get('type_id'),
            'type_code': group.get('type_code')
        })
legal_entity_groups_df = pd.json_normalize(rows)


## natural_person
# EXTRACT
natular_person_df = get_data(ENDPOINTS['natural_person'], 'natural_person')

# TRANSFORM

rows = []
for _, row  in natular_person_df[['person_id', 'groups']].iterrows():
    # print(row)
    for group in row['groups']:
        rows.append({
            'person_id': row['person_id'],
            'group_id': group.get('group_id'),
            'group_code': group.get('group_code'),
            'type_id': group.get('type_id'),
            'type_code': group.get('type_code')
        })
natular_person_groups_df = pd.json_normalize(rows)


natular_person_df['full_name'] = natular_person_df['first_name'] + ' ' + natular_person_df['last_name']
# natular_person_df.drop_duplicates(inplace=True)

natular_person_df = natular_person_df.loc[
    natular_person_df['state'] == 'A',
    ['person_id', 'full_name', 'main_phone', 'telegram', 'address']
]

natular_person_df['type'] = 'natural_person'

customers_df = pd.concat([legal_df, natular_person_df])
customer_groups_df = pd.concat([legal_entity_groups_df, natular_person_groups_df])

# LOAD
loader(customers_df, 'customers')
loader(customer_groups_df, "customer_groups")
