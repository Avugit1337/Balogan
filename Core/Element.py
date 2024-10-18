import time
from enum import IntEnum

from Core.Misc import BaloganObj, BaloganType, BaloganStatus


class ElementType(IntEnum):
    NA = 0
    INFO = 1
    BOLD = 2
    LINK = 3
    IMG = 4
    SUCCESS = 5
    WARNING = 6
    FAILURE = 7
    ERROR = 8
    LEVEL_START = 9
    LEVEL_STOP = 10
    HTML = 11

    def __str__(self):
        return {
            ElementType.NA: 'N/A',
            ElementType.INFO: 'INFO',
            ElementType.BOLD: 'BOLD',
            ElementType.LINK: 'LINK',
            ElementType.IMG: 'IMG',
            ElementType.SUCCESS: 'SUCCESS',
            ElementType.WARNING: 'WARNING',
            ElementType.FAILURE: 'FAILURE',
            ElementType.ERROR: 'ERROR',
            ElementType.LEVEL_START: 'LEVEL +',
            ElementType.LEVEL_STOP: 'LEVEL -',
            ElementType.HTML: 'HTML'
        }.get(self, 'N/A')

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_status(status: BaloganStatus) -> 'ElementType':
        return {
            BaloganStatus.NA: ElementType.NA,
            BaloganStatus.INFO: ElementType.INFO,
            BaloganStatus.SUCCESS: ElementType.SUCCESS,
            BaloganStatus.WARNING: ElementType.WARNING,
            BaloganStatus.FAILURE: ElementType.FAILURE,
            BaloganStatus.ERROR: ElementType.ERROR
        }.get(status, ElementType.NA)


class Element(BaloganObj):
    def __init__(self, epoch: int = 0, element_type: ElementType = ElementType.INFO, data: str = None):
        super().__init__(BaloganType.ELEMENT)
        self.epoch: int = epoch if epoch > 0 else int(time.time())
        self.element_type = element_type
        self.data = data

    def as_dict(self) -> dict:
        ret = {'t': self.element_type,
               'e': self.epoch}
        if self.data:
            ret['d'] = self.data
        return ret

    @staticmethod
    def from_dict(loaded_dict: dict) -> 'Element':
        return Element(element_type=loaded_dict['t'], epoch=loaded_dict['e'], data=loaded_dict.get('d', None))

    def verbose_str(self) -> str:
        time_str = time.strftime('%H:%M:%S', time.localtime(self.epoch))
        return f'[{time_str} | ' + {
            ElementType.NA: f'N/A    ]: {self.data}',
            ElementType.INFO: f'INFO   ]: {self.data}',
            ElementType.BOLD: f'BOLD   ]: >> {self.data} <<',
            ElementType.LINK: f'LINK   ]: {self.data}',
            ElementType.IMG: f'IMG    ]: {self.data}',
            ElementType.SUCCESS: f'SUCCESS]: >> {self.data} <<',
            ElementType.WARNING: f'WARNING]: >> {self.data} <<',
            ElementType.FAILURE: f'FAILURE]: >> {self.data} <<',
            ElementType.ERROR: f'ERROR  ]: >> {self.data} <<',
            ElementType.LEVEL_START: f'LEVEL +]: {self.data}\n=====================================',
            ElementType.LEVEL_STOP: 'LEVEL -]: ==========================\n',
            ElementType.HTML: f'HTML   ]: {self.data}',
        }.get(self.element_type, f'ISSUE: Unknown element type: {str(self.element_type)}')
