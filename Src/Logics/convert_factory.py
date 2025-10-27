from datetime import datetime

from Src.Convertors.basic_convertor import basic_convertor
from Src.Convertors.datetime_convertor import datetime_convertor
from Src.Convertors.reference_convertor import reference_convertor

class convert_factory:

    def __init__(self):
        self.basic_converter = basic_convertor()
        self.datetime_converter = datetime_convertor()
        self.reference_converter = reference_convertor()

    def convert(self, obj) -> dict:
        return self.reference_converter.Convert(obj)
