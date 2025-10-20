import unittest
from Src.Models.group_model import group_model
from Src.Logics.response_csv import response_csv
from Src.Logics.response_json import response_json
from Src.Logics.response_xml import response_xml
from Src.Logics.response_md import response_md
from Src.Core.common import common
from Src.Logics.factory_entities import factory_entities
from Src.Core.response_format import response_formats
from Src.Core.validator import validator
from Src.Core.abstract_response import abstract_response


class test_logics(unittest.TestCase):

    # Проверка, что CSV-ответ не None
    def test_csv_create_not_empty(self):
        resp = response_csv()
        data = [group_model.create("test")]
        result = resp.create("csv", data)
        self.assertIsNotNone(result)

    # Проверка, что JSON-ответ не None
    def test_json_create_not_empty(self):
        resp = response_json()
        data = [group_model.create("test")]
        result = resp.create("json", data)
        self.assertIsNotNone(result)

    # Проверка, что Markdown-ответ не None
    def test_md_create_not_empty(self):
        resp = response_md()
        data = [group_model.create("test")]
        result = resp.create("md", data)
        self.assertIsNotNone(result)

    # Проверка, что XML-ответ не None
    def test_xml_create_not_empty(self):
        resp = response_xml()
        data = [group_model.create("test")]
        result = resp.create("xml", data)
        self.assertIsNotNone(result)

    # Проверяем, что фабрика создаёт корректный объект логики
    def test_factory_produces_response_instance(self):
        factory = factory_entities()
        data = [group_model.create("test")]
        logic_cls = factory.create(response_formats.csv())
        self.assertIsNotNone(logic_cls)
        instance = logic_cls()
        validator.validate(instance, abstract_response)
        output = instance.create(response_formats.csv(), data)
        self.assertGreater(len(output), 0)

    # Проверка корректного состава данных в CSV
    def test_csv_contains_all_fields_and_values(self):
        resp = response_csv()
        data = [group_model.create("test")]
        fields = common.get_fields(data[0])
        output = resp.create("csv", data)

        for field in fields:
            self.assertIn(field, output)
        for obj in data:
            for field in fields:
                val = str(getattr(obj, field, ""))
                self.assertIn(val, output)

    # Проверка корректного состава данных в JSON
    def test_json_contains_all_fields_and_values(self):
        resp = response_json()
        data = [group_model.create("test")]
        fields = common.get_fields(data[0])
        output = resp.create("json", data)

        for field in fields:
            self.assertIn(field, output)
        for obj in data:
            for field in fields:
                val = str(getattr(obj, field, ""))
                self.assertIn(val, output)

    # Проверка корректного состава данных в XML
    def test_xml_contains_all_fields_and_values(self):
        resp = response_xml()
        data = [group_model.create("test")]
        fields = common.get_fields(data[0])
        output = resp.create("xml", data)

        for field in fields:
            self.assertIn(f"<{field}>", output)
        for obj in data:
            for field in fields:
                val = str(getattr(obj, field, ""))
                self.assertIn(val, output)

    # Проверка корректного состава данных в Markdown
    def test_md_contains_all_fields_and_values(self):
        resp = response_md()
        data = [group_model.create("test")]
        fields = common.get_fields(data[0])
        output = resp.create("md", data)

        for field in fields:
            self.assertIn(field, output)
        for obj in data:
            for field in fields:
                val = str(getattr(obj, field, ""))
                self.assertIn(val, output)

    # Дополнительная проверка: структура заголовков CSV корректна
    def test_csv_header_structure(self):
        resp = response_csv()
        data = [group_model.create("test")]
        fields = common.get_fields(data[0])
        output = resp.create("csv", data)
        header_line = output.split("\n")[0]
        for field in fields:
            self.assertIn(field, header_line)

    # Дополнительно можете добавить похожие проверки структуры markdown, xml, json


if __name__ == "__main__":
    unittest.main()
