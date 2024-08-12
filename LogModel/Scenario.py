import json

from LogModel.Misc import ReportType, ReportStatus, obj_list_to_dict_list


class Scenario:
    def __init__(self, name: str, properties: dict = None, parameters: dict = None):
        self.name = name
        self.properties = properties
        self.parameters = parameters
        self.status = ReportStatus.SUCCESS
        self.children = []  # Scenarios & Reports

    def append_child(self, child):
        self.children.append(child)

    def append_children(self, children):
        self.children.extend(children)

    def __str__(self):
        return json.dumps({
            't': ReportType.SCENARIO.value,
            'n': self.name,
            's': self.status,
            'p': self.properties,
            'P': self.parameters,
            'c': obj_list_to_dict_list(self.children)
        })
