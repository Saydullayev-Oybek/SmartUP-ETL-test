import sys
sys.path.append("..")

import requests
import pandas as pd
from config import get_header

def get_data(url, key):
    response = requests.get(url, headers=get_header())

    if response.status_code != 200:
        return "Xato"

    records = response.json()

    if not records:
        return pd.DataFrame()

    return pd.json_normalize(records[key])
