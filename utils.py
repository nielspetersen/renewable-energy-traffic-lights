
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import math
import energy_info_api 
import requests

def getCurrentTimestampInMilliseconds(dt):
    # rounded up to next 15 minute unit
    delta = timedelta(minutes=15)
    rounded_dt = datetime.min + math.ceil((dt - datetime.min) / delta) * delta
    return  int(rounded_dt.timestamp())


# default country de for Germany
def requestCurrentREShare(dt, country='de', postal_code=None):
    url = energy_info_api.REN_SHARE_ENDPOINT + country + (f'&postal_code={postal_code}' if postal_code else '')
    print(url)
    re_share_response = requests.get(url).json()
    
    # Identify index with equal timestamp
    share_index = re_share_response['unix_seconds'].index(dt)
    print(share_index)
    re_share_value = re_share_response['share'][share_index]
    return re_share_value
    