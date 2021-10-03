from dataclasses import dataclass
import requests
from typing import Dict, Any

from .ClubDamSearchQuery import ClubDamSearchQuery


@dataclass
class ClubDamSearchErrorData:
    response: requests.Response
    request_query: Dict[str, Any]
    request_payload: ClubDamSearchQuery
