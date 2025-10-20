from Src.Core.abstract_response import abstract_response
from Src.Core.common import common


class response_csv(abstract_response):

    def create(self, fmt: str, dataset: list):
        output = super().create(fmt, dataset)

        if not dataset:
            return output

        first_item = dataset[0]
        cols = common.get_fields(first_item)

        # Формируем заголовок CSV
        output += ";".join(cols) + "\n"

        # Добавляем строки данных
        for record in dataset:
            row = [str(getattr(record, col, '')) for col in cols]
            output += ";".join(row) + "\n"

        return output
