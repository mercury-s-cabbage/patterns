from Src.Core.abstract_response import abstract_response
from Src.Core.common import common


class response_xml(abstract_response):

    def create(self, fmt: str, dataset: list):
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n<data>\n'

        for item in dataset:
            xml_str += "  <item>\n"
            cols = common.get_fields(item)
            for col in cols:
                val = str(getattr(item, col, ""))
                xml_str += f"    <{col}>{val}</{col}>\n"
            xml_str += "  </item>\n"

        xml_str += "</data>\n"
        return xml_str