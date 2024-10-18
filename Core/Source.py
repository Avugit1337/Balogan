from typing import List, Union

from Core.Misc import BaloganType, BaloganObj
from Core.Report import Report
from Core.Scenario import Scenario


class Source(BaloganObj):
    def __init__(self, name: str, children: List[Union[Scenario, Report]] = None):
        super().__init__(BaloganType.SOURCE)
        self.name = name
        self.children = children if children else []

    def as_dict(self) -> dict:
        return {'t': self.balogan_type,
                'n': self.name,
                'c': self.children}

    @staticmethod
    def from_dict(report_dict: dict) -> 'Source':
        ret = Source(name=report_dict['n'])
        for child in report_dict['c']:
            ret.append_child((Scenario if child['t'] == BaloganType.SCENARIO.value else Report).from_dict(child))
        return ret

    def append_child(self, child: Union[Scenario, Report]):
        self.children.append(child)

    def append_children(self, children: List[Union[Scenario, Report]]):
        self.children.extend(children)
