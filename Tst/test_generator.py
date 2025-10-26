import os
import unittest
from Src.Logics.factory_entities import factory_entities
from Src.Core.response_format import response_formats

from Src.Models.group_model import group_model
from Src.Models.range_model import range_model
from Src.Models.storage_model import storage_model
from Src.Models.company_model import company_model
from Src.Models.receipt_item_model import receipt_item_model
from Src.Models.receipt_model import receipt_model
from Src.Models.nomenclature_model import nomenclature_model


class TestFileGeneration(unittest.TestCase):
    OUTPUT_DIR = "Responses"

    def setUp(self):
        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)
        self.factory = factory_entities()

    def save_to_file(self, filename, content):
        with open(os.path.join(self.OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)

    def create_group(self):
        return group_model.create("test")

    def create_range(self):
        base_range = range_model.create("base", 1)
        return range_model.create("range_test", 10, base_range)

    def create_storage(self):
        return storage_model.create("storage_test")

    def create_company(self):
        return company_model.create("Company XYZ")

    def create_receipt_item(self):
        return receipt_item_model.create("ItemName", 5, 12.34)

    def create_receipt(self):
        return receipt_model.create("Receipt001", "1 hour", 100)

    def create_nomenclature(self):
        base_range = range_model.create("base", 1)
        group = group_model.create("group1")
        return nomenclature_model.create("code123", group, base_range)

    CREATE_FUNCS = {
        "groups": create_group,
        "ranges": create_range,
        "storages": create_storage,
        "companies": create_company,
        "receipt_items": create_receipt_item,
        "receipts": create_receipt,
        "nomenclatures": create_nomenclature,
    }


    def test_generate_and_save_files(self):
        for model_name, create_func in self.CREATE_FUNCS.items():
            data = [create_func(self)]
            for fmt in [response_formats.csv(), response_formats.json(), response_formats.md(), response_formats.xml()]:
                content = self.factory.create_default(fmt, data)
                filename = f"{model_name}.{fmt}"
                self.save_to_file(filename, content)
                print(f"Generated file: {filename}")


if __name__ == "__main__":
    unittest.main()
