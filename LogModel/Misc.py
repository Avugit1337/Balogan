import json
from enum import IntEnum, Enum
from typing import List, Any


class ReportType(IntEnum):
    SOURCE = 0
    SCENARIO = 1
    REPORT = 2


class ReportStatus(IntEnum):
    INFO = 0
    SUCCESS = 1
    WARNING = 2
    FAILURE = 3
    ERROR = 4


class SaveAs(Enum):
    JSON = '.json'
    JS = '.js'


def obj_list_to_dict_list(list_to_concat: List[Any]) -> List[dict]:
    ret: List[dict] = []
    if list_to_concat and len(list_to_concat) > 0:
        for obj in list_to_concat:
            ret.append(json.loads(str(obj)))
    return ret
