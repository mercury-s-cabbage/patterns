from datetime import datetime
from Src.Core.abstract_covertor import abstract_covertor

class datetime_convertor(abstract_covertor):

    def Convert(self, obj) -> dict:
        result = {}


        for attr in dir(obj):
            if attr.startswith('_'):
                continue
            value = getattr(obj, attr)

            if isinstance(value, datetime):
                result[attr] = value.isoformat()

        return result
