import requests
from typing import Dict, Any

from .JoySoundSearchQuery import JoySoundSearchQuery
from .JoySoundSearchErrorData import JoySoundSearchErrorData


def search_joysound(query: JoySoundSearchQuery) -> Dict[str, Any]:
    kindCnt = len(query.filters)

    payload = {
        'format': query.format,
        'kindCnt': kindCnt,
        'start': query.start,
        'count': query.count,
        'sort': query.sort,
        'order': query.order,
        'apiVer': query.apiVer
    }

    for index, filter in enumerate(query.filters):
        payload[f'kind{index+1}'] = filter.kind
        payload[f'word{index+1}'] = filter.word
        payload[f'match{index+1}'] = filter.match

    # https://www.joysound.com/web/search/song
    api_url = 'https://mspxy.joysound.com/Common/ContentsList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'x-jsp-app-name': '0000800'
    }

    res = requests.post(api_url, headers=headers, data=payload)
    if res.status_code != 200:
        raise Exception(JoySoundSearchErrorData(
            response=res,
            request_query=query,
            request_payload=payload,
        ))

    return res.json()
