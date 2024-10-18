from typing import List

from Core.Misc import BaloganObj, BaloganType, dict_to_dictobj_list
from Core.Source import Source


class Execution(BaloganObj):
    def __init__(self, name: str, sources: List[Source] = None):
        super().__init__(BaloganType.EXECUTION)
        self.name = name
        self.sources: List[Source] = sources if sources else []

    def as_dict(self) -> dict:
        return {'t': self.balogan_type,
                'n': self.name,
                's': self.sources}

    @staticmethod
    def from_dict(report_dict: dict) -> 'Execution':
        return Execution(name=report_dict['n'], sources=dict_to_dictobj_list(report_dict['s'], Source))

    def append_source(self, source: Source):
        self.sources.append(source)
