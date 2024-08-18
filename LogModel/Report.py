import atexit
import json
import time
from enum import IntEnum
from typing import List

from LogModel.Misc import ReportStatus, ReportType, obj_list_to_dict_list, SaveAs


class ReportElementType(IntEnum):
    REGULAR = 0
    SUCCESS = 1
    BOLD = 2
    LINK = 3
    IMG = 4
    WARNING = 5
    FAILURE = 6
    ERROR = 7
    LEVEL_START = 8
    LEVEL_STOP = 9
    HTML = 10


class ReportElement:
    def __init__(self, element_type: ReportElementType = ReportElementType.REGULAR,
                 status: ReportStatus = ReportStatus.INFO, data: str = None):
        self.epoch: int = int(time.time())
        self.element_type = element_type
        self.status = status
        self.data = data

    def __str__(self):
        ret = {
            't': self.element_type.value,
            'e': self.epoch,
            's': self.status.value
        }
        if self.data:
            ret['d'] = self.data
        return json.dumps(ret)


class Report:
    uid_idx = 0

    def __init__(self, name: str = "", description: str = None,
                 properties: dict = None, parameters: dict = None):
        self.name: str = name
        self.description = description
        self.properties = properties
        self.parameters = parameters
        self.elements: List[ReportElement] = []
        self.start_epoch: int = int(time.time())
        self.uid: str = str(Report.uid_idx) + "_" + str(self.start_epoch)
        atexit.register(self.save_to_file, save_as=SaveAs.JS, file_abs='Templates/Report.js')
        Report.uid_idx += 1

    def __str__(self):
        return json.dumps({
            't': ReportType.REPORT.value,
            'n': self.name,
            'u': self.uid,
            'S': self.start_epoch,
            'D': self.description,
            'p': self.properties,
            'P': self.parameters,
            'E': obj_list_to_dict_list(self.elements)
        })

    def save_to_file(self, save_as: SaveAs = SaveAs.JSON, file_abs: str = None) -> None:
        if not file_abs or not isinstance(file_abs, str) or file_abs.strip() == "":
            file_abs = f'Report_{self.uid}{save_as.value}'
        print(f'Saving report to "{file_abs}"')
        try:
            with open(file_abs, 'w') as file:
                file.write(str(self) if save_as == SaveAs.JSON else f'var report={str(self)}')
        except Exception as e:
            print(f'Failed saving to "{file_abs}": {str(e)}')

    def log(self, msg: str = "", status: ReportStatus = ReportStatus.INFO) -> None:
        self.elements.append(ReportElement(data=msg, status=status))

    def info(self, msg: str = "") -> None:
        self.elements.append(ReportElement(data=msg))

    def bold(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.BOLD, data=msg))

    def success(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.SUCCESS,
                                           status=ReportStatus.SUCCESS, data=msg))

    def warn(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.WARNING,
                                           status=ReportStatus.WARNING, data=msg))

    def fail(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.FAILURE,
                                           status=ReportStatus.FAILURE, data=msg))

    def err(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.ERROR,
                                           status=ReportStatus.ERROR, data=msg))

    def l_start(self, msg: str = "", status: ReportStatus = ReportStatus.INFO) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.LEVEL_START, status=status, data=msg))

    def l_stop(self):
        self.elements.append(ReportElement(element_type=ReportElementType.LEVEL_STOP))

    def link(self, replacement: str = "", link_addr: str = "", status: ReportStatus = ReportStatus.INFO) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.LINK, status=status,
                                           data=f'{replacement}__{link_addr}'))

    def img(self, img_path: str = "", alt: str = "Image", status: ReportStatus = ReportStatus.INFO):
        self.elements.append(ReportElement(element_type=ReportElementType.IMG, status=status,
                                           data=f'{img_path}__{alt}'))

    def html(self, html_code: str = "", status: ReportStatus = ReportStatus.INFO) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.HTML, status=status, data=html_code))
