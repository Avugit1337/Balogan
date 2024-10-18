from typing import List, Union

from Core.Misc import BaloganType, BaloganObj
from Core.Report import Report


class Scenario(BaloganObj):
    def __init__(self, name: str, properties: dict = None, parameters: dict = None,
                 children: List[Union['Scenario', Report]] = None):
        super().__init__(BaloganType.SCENARIO)
        self.name = name
        self.properties = properties
        self.parameters = parameters
        self.children: List[Union['Scenario', Report]] = children if children else []

    def as_dict(self) -> dict:
        return {'t': self.balogan_type,
                'n': self.name,
                'p': self.properties,
                'P': self.parameters,
                'c': self.children}

    @staticmethod
    def from_dict(report_dict: dict) -> 'Scenario':
        ret = Scenario(name=report_dict['n'], properties=report_dict['p'], parameters=report_dict['P'])
        for child in report_dict['c']:
            ret.append_child((Scenario if child['t'] == BaloganType.SCENARIO.value else Report).from_dict(child))
        return ret

    def append_child(self, child: Union['Scenario', Report]):
        self.children.append(child)

    def append_children(self, children: List[Union['Scenario', Report]]):
        self.children.extend(children)
