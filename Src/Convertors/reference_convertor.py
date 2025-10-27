from Src.Core.abstract_covertor import abstract_covertor
from Src.Core.validator import argument_exception
from Src.Convertors.basic_convertor import basic_convertor
from Src.Convertors.datetime_convertor import datetime_convertor
from datetime import datetime

class reference_convertor(abstract_covertor):

    def __init__(self):
        self.basic = basic_convertor()
        self.datetime = datetime_convertor()

    def Convert(self, obj) -> dict:
        if obj is None:
            return None

        if isinstance(obj, datetime):
            return {'value': obj.isoformat()}

        if isinstance(obj, (str, int, float)):
            return {'value': obj}

        # Получаем словари из базовых конверторов
        try:
            simple_fields = self.basic.Convert(obj)
        except argument_exception:
            simple_fields = {}

        try:
            date_fields = self.datetime.Convert(obj)
        except argument_exception:
            date_fields = {}

        nested_fields = {}
        if not isinstance(obj, (int, str, float, datetime)):

            # Обрабатываем вложенные объекты рекурсивно

            for attr in dir(obj):
                if attr.startswith('_') or attr in simple_fields or attr in date_fields:
                    continue
                value = getattr(obj, attr)
                if callable(value):  # исключаем функции и методы
                    continue
                if value is None:
                    nested_fields[attr] = None
                else:
                    try:
                        nested_fields[attr] = self.Convert(value)
                    except Exception as e:
                        raise argument_exception(f"Невозможно конвертировать поле '{attr}': {e}")

        # Объединяем все словари
        result = {}
        result.update(simple_fields)
        result.update(date_fields)
        result.update(nested_fields)

        return result
