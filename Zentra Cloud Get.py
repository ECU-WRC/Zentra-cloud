import requests
import pandas as pd

def get_zentra_data(api_token):
    url = "https://zentracloud.com/api/v4/get_readings/"

    headers = {
        'Authorization': f'{api_token}',
    }

    params = {
        'device_sn': 'z6-07292',
        'start_date': '2020-07-01 00:00',
        'end_date': '2023-07-31 23:59',
        'start_mrid': '3500',
        'end_mrid': '3800',
        'output_format': 'json',
        'page_num': '2',
        'per_page': '1000',
        'device_depth': 'true',
        'sort_by': 'descending',
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data)
        print(df)
    else:
        print(f"Error: {response.status_code}, {response.text}")

api_token = 'Token bb01d080aa3dbac21cc70b87cf01fc386a442121'
get_zentra_data(api_token)
