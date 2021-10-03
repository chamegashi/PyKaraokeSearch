import json
import requests
from typing import Dict, Any

from .ClubDamSearchQuery import ClubDamSearchQuery
from .ClubDamSearchErrorData import ClubDamSearchErrorData


def search_clubdam(query: ClubDamSearchQuery, timeout: float = None) -> Dict[str, Any]:
    # https://www.clubdam.com/karaokesearch/
    api_url = 'https://www.clubdam.com/dkwebsys/search-api/SearchVariousByKeywordApi'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Content-Type': 'application/json',
    }

    payload = {
        'authKey': query.authKey,
        'compId': query.compId,
        'contentsCode': query.contentsCode,
        'dispCount': str(query.dispCount),
        'keyword': query.keyword,
        'modelTypeCode': query.modelTypeCode,
        'pageNo': str(query.pageNo),
        'serialNo': query.serialNo,
        'serviceCode': query.serviceCode,
        'sort': query.sort,
    }

    res = requests.post(api_url, headers=headers, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), timeout=timeout)
    if res.status_code != 200:
        raise Exception(ClubDamSearchErrorData(
            response=res,
            request_query=query,
            request_payload=payload,
        ))

    data = res.json()
    status = data.get('result', {}).get('statusCode')
    if status != '0000':
        raise Exception(ClubDamSearchErrorData(
            response=res,
            request_query=query,
            request_payload=payload,
        ))

    return data
