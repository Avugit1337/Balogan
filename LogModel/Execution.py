import json
from typing import List

from LogModel.Misc import obj_list_to_dict_list
from LogModel.Source import Source


class Execution:
    def __init__(self):
        self.sources: List[Source] = []

    def append_source(self, source: Source):
        self.sources.append(source)

    def __str__(self):
        return json.dumps({'s': obj_list_to_dict_list(self.sources)})
