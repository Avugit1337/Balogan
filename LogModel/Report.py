import json
import time
from enum import IntEnum
from typing import List

from LogModel.Misc import ReportStatus, ReportType, obj_list_to_dict_list, SaveAs


class ReportElementType(IntEnum):
    REGULAR = 0
    BOLD = 1
    LINK = 2
    IMG = 3
    WARNING = 4
    FAILURE = 5
    ERROR = 6
    LEVEL_START = 7
    LEVEL_STOP = 8
    HTML = 9


class ReportElement:
    def __init__(self, element_type: ReportElementType = ReportElementType.REGULAR,
                 status: ReportStatus = ReportStatus.SUCCESS, data: str = None):
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
        self.status: ReportStatus = ReportStatus.SUCCESS
        self.elements: List[ReportElement] = []
        self.start_epoch: int = int(time.time())
        self.uid: str = str(Report.uid_idx) + "_" + str(self.start_epoch)
        Report.uid_idx += 1

    def __str__(self):
        return json.dumps({
            't': ReportType.REPORT.value,
            'n': self.name,
            'u': self.uid,
            'S': self.start_epoch,
            's': self.status.value,
            'D': self.description,
            'p': self.properties,
            'P': self.parameters,
            'E': obj_list_to_dict_list(self.elements),
            'e': self.start_epoch if not self.elements else self.elements[-1].epoch
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

    def info(self, msg: str = "") -> None:
        self.elements.append(ReportElement(data=msg))

    def bold(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.BOLD, data=msg))

    def warn(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.WARNING,
                                           status=ReportStatus.WARNING, data=msg))

    def fail(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.FAILURE,
                                           status=ReportStatus.FAILURE, data=msg))

    def err(self, msg: str = "") -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.ERROR,
                                           status=ReportStatus.ERROR, data=msg))

    def l_start(self, msg: str = "", status: ReportStatus = ReportStatus.SUCCESS) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.LEVEL_START, status=status, data=msg))

    def l_stop(self):
        self.elements.append(ReportElement(element_type=ReportElementType.LEVEL_STOP))

    def link(self, replacement: str = "", link_addr: str = "", status: ReportStatus = ReportStatus.SUCCESS) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.LINK, status=status,
                                           data=f'{replacement}__{link_addr}'))

    def img(self, img_path: str = "", alt: str = "Image", status: ReportStatus = ReportStatus.SUCCESS):
        self.elements.append(ReportElement(element_type=ReportElementType.IMG, status=status,
                                           data=f'{img_path}__{alt}'))

    def html(self, html_code: str = "", status: ReportStatus = ReportStatus.SUCCESS) -> None:
        self.elements.append(ReportElement(element_type=ReportElementType.HTML, status=status, data=html_code))
