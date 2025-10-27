from Src.Core.abstract_response import abstract_response
from Src.Core.common import common
import json
from Src.Convertors.reference_convertor import reference_convertor


class response_json(abstract_response):


    def create(self, format:str, dataset: list):
        conv = reference_convertor()
        _ = super().create("json", dataset)
        if not dataset:
            return "[]"

        result_list = []

        for entry in dataset:
            # cols = common.get_fields(entry)
            # obj = {col: str(getattr(entry, col, "")) for col in cols}
            result_list.append(conv.Convert(entry))

        return json.dumps(result_list, ensure_ascii=False, indent=2)