from dataclasses import dataclass
from typing import List

from .JoySoundSearchQueryField import (
    Filter,
    Format,
    Sort,
    Order,
    ApiVer,
)


@dataclass
class JoySoundSearchQuery:
    filters: List[Filter]
    format: Format = 'all'
    sort: Sort = 'popular'
    order: Order = 'desc'
    start: int = 1
    count: int = 20
    apiVer: ApiVer = '1.0'
