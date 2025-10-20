from Src.Core.abstract_response import abstract_response
from Src.Core.common import common


class response_md(abstract_response):

    def create(self, fmt: str, dataset: list):
        markdown = ""
        if not dataset:
            return markdown

        first_item = dataset[0]
        columns = common.get_fields(first_item)

        header = "| " + " | ".join(columns) + " |\n"
        separator = "| " + " | ".join(["---"] * len(columns)) + " |\n"
        markdown += header + separator

        for row in dataset:
            values = [str(getattr(row, col, "")) for col in columns]
            markdown += "| " + " | ".join(values) + " |\n"

        return markdown
