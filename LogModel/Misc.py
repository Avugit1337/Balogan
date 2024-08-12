import json
from enum import IntEnum, Enum
from typing import List, Any


class ReportType(IntEnum):
    SOURCE = 0
    SCENARIO = 1
    REPORT = 2


class ReportStatus(IntEnum):
    SUCCESS = 0
    WARNING = 1
    FAILURE = 2
    ERROR = 3


class SaveAs(Enum):
    JSON = '.json'
    JS = '.js'


def obj_list_to_dict_list(list_to_concat: List[Any]) -> List[dict]:
    ret: List[dict] = []
    if list_to_concat and len(list_to_concat) > 0:
        for obj in list_to_concat:
            ret.append(json.loads(str(obj)))
    return ret
