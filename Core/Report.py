import atexit
import time
from typing import List

from Core.Element import Element, ElementType
from Core.Misc import BaloganStatus, BaloganType, SaveAs, BaloganObj, dict_to_dictobj_list


class Report(BaloganObj):
    def __init__(self, name: str = "", start_epoch: int = 0, uid: str = None, description: str = None,
                 properties: dict = None, parameters: dict = None, elements: List[Element] = None,
                 save_on_exit: bool = False, save_as: SaveAs = SaveAs.JS, verbose: bool = True):
        super().__init__(BaloganType.REPORT)
        self.name = name
        self.start_epoch: int = start_epoch if start_epoch > 0 else int(time.time())
        self.uid: str = uid if uid else f'{name}_{str(self.start_epoch)}'
        self.description = description
        self.properties = properties
        self.parameters = parameters
        self.elements: List[Element] = elements if elements else []
        if save_on_exit:
            atexit.register(self.save_to_file, save_as=save_as, file_abs=f'Templates/Report{save_as.value}')
        self.verbose = verbose

    @staticmethod
    def from_dict(report_dict: dict) -> 'Report':
        return Report(name=report_dict['n'], start_epoch=report_dict['S'], uid=report_dict['u'],
                      description=report_dict['D'], properties=report_dict['p'], parameters=report_dict['P'],
                      elements=dict_to_dictobj_list(report_dict['E'], Element))

    def as_dict(self) -> dict:
        return {'t': self.balogan_type,
                'n': self.name,
                'S': self.start_epoch,
                'u': self.uid,
                'D': self.description,
                'p': self.properties,
                'P': self.parameters,
                'E': self.elements}

    def print_elements(self):
        for elem in self.elements:
            print(elem.verbose_str())

    def append(self, elem: Element):
        if self.verbose:
            print(elem.verbose_str())
        self.elements.append(elem)

    def log(self, msg: str = "", status: BaloganStatus = BaloganStatus.INFO, epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.from_status(status), data=msg))

    def log_multi(self, msgs: List[str], status: BaloganStatus = BaloganStatus.INFO, epoch: int = 0) -> None:
        e_epoch = epoch if epoch > 0 else int(time.time())
        e_type = ElementType.from_status(status)
        for msg in msgs:
            self.append(Element(epoch=e_epoch, element_type=e_type, data=msg))

    def info(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, data=msg))

    def bold(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.BOLD, data=msg))

    def success(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.SUCCESS, data=msg))

    def warn(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.WARNING, data=msg))

    def fail(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.FAILURE, data=msg))

    def err(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.ERROR, data=msg))

    def l_start(self, msg: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.LEVEL_START, data=msg))

    def l_stop(self, epoch: int = 0):
        self.append(Element(epoch=epoch, element_type=ElementType.LEVEL_STOP))

    def link(self, addr: str = "", replace: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.LINK, data=f'{addr}__{replace}'))

    def img(self, addr: str = "", alt: str = "", epoch: int = 0):
        self.append(Element(epoch=epoch, element_type=ElementType.IMG, data=f'{addr}__{alt}'))

    def html(self, html_code: str = "", epoch: int = 0) -> None:
        self.append(Element(epoch=epoch, element_type=ElementType.HTML, data=html_code))
