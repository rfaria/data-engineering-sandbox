# https://housestockwatcher.com/api

from requests import request
import json
from pandas.io.json import json_normalize

response=request(url='https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json', method='get')
raw = response.json()
raw[0:1]
# data = json.loads(raw)
# json_normalize(data['results'])
