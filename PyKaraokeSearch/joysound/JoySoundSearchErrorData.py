from dataclasses import dataclass
import requests
from typing import Dict, Any

from .JoySoundSearchQuery import JoySoundSearchQuery


@dataclass
class JoySoundSearchErrorData:
    response: requests.Response
    request_query: Dict[str, Any]
    request_payload: JoySoundSearchQuery
