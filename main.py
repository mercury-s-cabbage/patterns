import connexion
from flask import request, jsonify, Response
from Src.Core.response_format import response_formats
from Src.Logics.factory_entities import factory_entities

# Импорт моделей, добавить при необходимости
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.range_model import range_model
from Src.Models.company_model import company_model
from Src.Models.storage_model import storage_model
from Src.Models.receipt_model import receipt_model
from Src.Models.receipt_item_model import receipt_item_model

app = connexion.FlaskApp(__name__)

# Сопоставление типа данных и модели
def create_group():
    return group_model.create("test")

def create_range():
    base_range = range_model.create("base", 1)
    return range_model.create("range_test", 10, base_range)

def create_storage():
    return storage_model.create("storage_test")

def create_company():
    return company_model.create("Company XYZ")

def create_receipt_item():
    return receipt_item_model.create("ItemName", 5, 12.34)

def create_receipt():
    return receipt_model.create("Receipt001", "1 hour", 100)

def create_nomenclature():
    base_range = range_model.create("base", 1)
    group = group_model.create("group1")
    return nomenclature_model.create("code123", group, base_range)

MODEL_MAPPING = {
    "groups": create_group,
    "ranges": create_range,
    "storages": create_storage,
    "companies": create_company,
    "receipt_items": create_receipt_item,
    "receipts": create_receipt,
    "nomenclatures": create_nomenclature,
}

@app.route("/api/data", methods=['GET'])
def generate_data():
    fmt = request.args.get("format", "json").lower()
    type_ = request.args.get("type")

    if fmt not in {"csv", "json", "md", "xml"}:
        return jsonify({"error": "Unsupported format"}), 400
    if type_ not in MODEL_MAPPING:
        return jsonify({"error": "Unsupported or missing type parameter"}), 400

    create_func = MODEL_MAPPING[type_]

    try:
        data = [create_func()]
    except Exception as ex:
        return jsonify({"error": f"Error creating data: {str(ex)}"}), 500

    factory = factory_entities()

    try:
        result = factory.create_default(fmt, data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return Response(result, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
