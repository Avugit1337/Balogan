import gzip
import json
import time
from abc import abstractmethod, ABC
from enum import IntEnum, Enum
from typing import List, Type, TypeVar


class BaloganType(IntEnum):
    NA = 0
    EXECUTION = 1
    SOURCE = 2
    SCENARIO = 3
    REPORT = 4
    ELEMENT = 5

    def __str__(self):
        return {
            BaloganType.NA: 'NONE',
            BaloganType.EXECUTION: 'EXECUTION',
            BaloganType.SOURCE: 'SOURCE',
            BaloganType.SCENARIO: 'SCENARIO',
            BaloganType.REPORT: 'REPORT',
            BaloganType.ELEMENT: 'ELEMENT'
        }.get(self, 'N/A')

    def __repr__(self):
        return self.__str__()


class BaloganStatus(IntEnum):
    NA = 0
    INFO = 1
    SUCCESS = 2
    WARNING = 3
    FAILURE = 4
    ERROR = 5

    def __str__(self):
        return {
            BaloganStatus.NA: 'N/A',
            BaloganStatus.INFO: 'INFO',
            BaloganStatus.SUCCESS: 'SUCCESS',
            BaloganStatus.WARNING: 'WARNING',
            BaloganStatus.FAILURE: 'FAILURE',
            BaloganStatus.ERROR: 'ERROR'
        }.get(self, 'N/A')

    def __repr__(self):
        return self.__str__()


class SaveAs(Enum):
    JSON = '.json'
    JS = '.js'
    JSON_GZ = '.json.gz'
    JS_GZ = '.js.gz'


class BaloganObj(ABC):
    def __init__(self, balogan_type: BaloganType):
        self.balogan_type = balogan_type

    @abstractmethod
    def as_dict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_dict(loaded_dict: dict) -> 'BaloganObj':
        pass

    def __str__(self) -> str:
        return json.dumps(self.as_dict(), default=lambda o: o.as_dict())

    def __repr__(self):
        return self.__str__()

    def save_to_file(self, save_as: SaveAs = SaveAs.JSON, file_abs: str = None) -> bool:
        if not file_abs:
            file_abs = f'{str(self.balogan_type)}_{str(int(time.time()))}{save_as.value}'
        type_lower = str(self.balogan_type).lower()
        print(f'Saving {type_lower} to "{file_abs}"')
        to_write = str(self) if save_as.value.startswith('.json') else f'var {type_lower}={str(self)};'
        try:
            if save_as.value.endswith('.gz'):
                with gzip.open(file_abs, 'wb') as f:
                    f.write(to_write.encode())
            else:
                with open(file_abs, 'w') as file:
                    file.write(to_write)
        except Exception as e:
            print(f'ERROR: Failed saving to "{file_abs}": {str(e)}')
            return False
        return True


T = TypeVar('T', bound=BaloganObj)


def load_from_file(file_abs: str, clazz: Type[T]) -> T:
    print(f'Loading {str(clazz.__name__).lower()} from "{file_abs}"')
    with gzip.open(file_abs) if file_abs.endswith('.gz') else open(file_abs) as file:
        return clazz.from_dict(json.loads(file.read()))


def dict_to_dictobj_list(dict_list: List[dict], clazz: Type[T]) -> List[T]:
    ret: List[clazz] = []
    for report_dict in dict_list:
        ret.append(clazz.from_dict(report_dict))
    return ret
