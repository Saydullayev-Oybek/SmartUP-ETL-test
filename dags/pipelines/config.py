import json
import base64

ENDPOINTS = {
    'inventory': 'https://smartup.online/b/anor/mxsx/mr/inventory$export',
    'legal_person': 'https://smartup.online/b/anor/mxsx/mr/legal_person$export',
    'natural_person': 'https://smartup.online/b/anor/mxsx/mr/natural_person$export'
}

# db_url
db_url = f"postgresql://oybek:0121@host.docker.internal:5432/smartup"

# 
with open('auth.json', 'r') as file:
    data = json.load(file)

PROJECT_CODE = data['PROJECT_CODE']
FILIAL_ID = data['FILIAL_ID']
username = data['username']
password = data['password']

def get_header():
    token = base64.b64encode(
        f"{username}:{password}".encode()
    ).decode()

    header = {
        "Authorization": f"Basic {token}",
        "project_code":  PROJECT_CODE,
        "filial_id":     FILIAL_ID,
    }

    return header
