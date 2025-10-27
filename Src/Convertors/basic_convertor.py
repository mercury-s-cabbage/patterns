from Src.Core.abstract_covertor import abstract_covertor
class basic_convertor(abstract_covertor):
    def Convert(self, obj) -> dict:
        result = {}

        # Перебираем все публичные атрибуты объекта
        for attr in dir(obj):
            if attr.startswith('_'):
                continue
            value = getattr(obj, attr)
            # Проверяем, что тип простые: числовой или строковый
            if isinstance(value, (int, float, str)):
                result[attr] = value
        return result
