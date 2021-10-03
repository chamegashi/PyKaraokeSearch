from dataclasses import dataclass
from typing import Literal, Union


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
