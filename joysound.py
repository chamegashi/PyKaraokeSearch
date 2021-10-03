import requests
from dataclasses import dataclass
from typing import Literal, Union, List, Dict, Any, get_args


Format = Literal['all', 'group']
"""
    all: 検索結果
    group: 不明。うたスキ動画タブのページでも送られる
"""

Kind = Literal[
    'compound',
    'song',
    'artist',
    'tieup',

    'selArrange',
    'selService'
]
"""
    タブ: kind1, word1, match1

    compound: すべて
    song: 曲
    artist: 歌手
    tieup: 番組

    うたスキ動画は別API
    GET https://www.joysound.com/api/1.0/utasukiMovie/movies


    対応コンテンツ: kind2, word2, match2, kind3, word3, match3, ...
        「すべて」の場合は送信されない
        1つ選択すると、kind2、word2、match2が追加される
        2つ目を選択すると、kind3、word3、match3のように連番で追加される
        match#は常にexact

    selArrange: wordにWordSelArrangeを指定
    selService: wordにWordSelServiceを指定
"""

WordSelArrange = Literal['1,7', '2,8', '3,9', '22']
"""
    1,7: 本人映像
    2,8: アニメカラオケ
    3,9: LIVEカラオケ
    22: ギタナビ
"""

WordSelService = Literal['001000000', '100000000']
"""
    001000000: お店で歌える曲
    100000000: 家庭用カラオケ
"""

Match = Literal['partial', 'front', 'exact']
"""
    partial: 部分一致
    front: 前方一致
    exact: 完全一致
"""

Sort = Literal['popular', 'name']
"""
    ソートキー

    popular: 人気順
    name: 曲名の降順/曲名の昇順
"""

Order = Literal['desc', 'asc']
"""
    ソート順

    desc: 降順. sort=popularのとき固定値
    asc: 昇順
"""

ApiVer = Literal['1.0']
"""
    APIバージョン

    1.0: 固定値
"""

@dataclass
class Filter:
    kind: Kind
    word: Union[str, WordSelArrange, WordSelService]
    match: Match

@dataclass
class JoySoundSearchQuery:
    """
        aaa
    """
    filters: List[Filter]
    format: Format = 'all'
    sort: Sort = 'popular'
    order: Order = 'desc'
    start: int = 1
    count: int = 20
    apiVer: ApiVer = '1.0'

@dataclass
class JoySoundSearchErrorData:
    response: requests.Response
    request_query: Dict[str, Any]
    request_payload: JoySoundSearchQuery


def search(query: JoySoundSearchQuery):
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


if __name__ == '__main__':
    import json
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('songname', type=str)
    parser.add_argument('-m', '--match', type=str, default='partial', choices=get_args(Match))
    parser.add_argument('-o', '--output_path', type=str)
    args = parser.parse_args()

    songname = args.songname
    match = args.match
    output_path = args.output_path

    result = search(JoySoundSearchQuery(
        filters=[
            Filter(
                kind='song',
                word=songname,
                match=match,
            ),
        ],
    ))

    with open(output_path if output_path else 0, 'w') as fp:
        json.dump(result, fp, ensure_ascii=False)
