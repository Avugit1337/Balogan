import json

from LogModel.Misc import ReportStatus, ReportType, obj_list_to_dict_list


class Source:
    def __init__(self, name: str):
        self.name = name
        self.status = ReportStatus.SUCCESS
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def __str__(self):
        return json.dumps({
            't': ReportType.SOURCE.value,
            'n': self.name,
            's': self.status.value,
            'c': obj_list_to_dict_list(self.children)
        })
