from Src.Core.abstract_response import abstract_response
from Src.Core.common import common
import json


class response_json(abstract_response):

    def create(self, fmt: str, dataset: list):
        _ = super().create(fmt, dataset)
        if not dataset:
            return "[]"

        result_list = []

        for entry in dataset:
            cols = common.get_fields(entry)
            obj = {col: str(getattr(entry, col, "")) for col in cols}
            result_list.append(obj)

        return json.dumps(result_list, ensure_ascii=False, indent=2)
