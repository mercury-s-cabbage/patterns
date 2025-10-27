from Src.Core.abstract_response import abstract_response
from Src.Logics.response_csv import response_csv
from Src.Logics.response_md import response_md
from Src.Logics.response_xml import response_xml
from Src.Logics.response_json import response_json
from Src.Core.validator import operation_exception


class factory_entities:
    def __init__(self, default_format: str = "csv"):
        # Сопоставление форматов и классов ответов
        self.__match = {
            "csv": response_csv,
            "json": response_json,
            "md": response_md,
            "xml": response_xml,
        }
        self.__default_format = default_format

    # Метод получения экземпляра класса по формату
    def create(self, format: str) -> abstract_response:
        if format not in self.__match:
            raise operation_exception(f"Формат не верный: {format}")
        # Возвращаем новый экземпляр соответствующего класса
        return self.__match[format]()

    # Метод для создания ответа по умолчанию с использованием текущей настройки
    def create_default(self, data) -> abstract_response:
        return self.create(self.__default_format)

    # Свойство для получения/установки текущего формата
    @property
    def default_format(self) -> str:
        return self.__default_format

    @default_format.setter
    def default_format(self, value: str):
        if value not in self.__match:
            raise operation_exception(f"Формат не верный: {value}")
        self.__default_format = value

