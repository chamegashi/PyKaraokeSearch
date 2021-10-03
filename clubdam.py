import json
import requests

api_url = 'https://www.clubdam.com/dkwebsys/search-api/SearchVariousByKeywordApi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Content-Type': 'application/json',
}

payload = {
    'authKey': '2/Qb9R@8s*',
    'compId': '1',
    'contentsCode': None,
    'dispCount': '100',
    'keyword': 'Starlight',
    'modelTypeCode': '1',
    'pageNo': '1',
    'serialNo': 'AT00001',
    'serviceCode': None,
    'sort': '2', # 1: 50音順, 2: 人気順
}

res = requests.post(api_url, headers=headers, data=json.dumps(payload))

data = res.json()
status = data.get('result', {}).get('statusCode')

print(res.status_code)
print(status)
print(data)
