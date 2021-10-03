from dataclasses import dataclass

from .ClubDamSearchQueryField import Sort


@dataclass
class ClubDamSearchQuery:
    keyword: str
    dispCount: int = 100
    pageNo: int = 1
    sort: Sort = '2'

    authKey: str = '2/Qb9R@8s*'
    compId: str = '1'
    contentsCode: str = None
    modelTypeCode: str = '1'
    serialNo: str = 'AT00001'
    serviceCode: str = None
