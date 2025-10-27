import unittest
from datetime import datetime
from Src.Convertors.basic_convertor import basic_convertor
from Src.Convertors.datetime_convertor import datetime_convertor
from Src.Convertors.reference_convertor import reference_convertor
from Src.Logics.convert_factory import convert_factory

'''Используем для тестирования собственные классы, чтобы тесты не ломались при изменении моделей системы'''
class Dummy:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class DummyDate:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class DummyReference:
    def __init__(self, num, text, dt, nested=None):
        self.num = num
        self.text = text
        self.dt = dt
        self.nested = nested
class BasicConvertorTests(unittest.TestCase):

    def test_basic_types_conversion(self):
        converter = basic_convertor()
        obj = Dummy(a=10, b=3.14, c="test")
        expected = {'a': 10, 'b': 3.14, 'c': "test"}

        result = converter.Convert(obj)
        self.assertEqual(result, expected)


class DateTimeConvertorTest(unittest.TestCase):
    def test_datetime_conversion(self):
        converter = datetime_convertor()
        start = datetime(2023, 10, 26, 11, 30, 0)
        end = datetime(2023, 10, 26, 12, 30, 0)
        obj = DummyDate(start, end)
        result = converter.Convert(obj)

        self.assertEqual(result['start'], start.isoformat())
        self.assertEqual(result['end'], end.isoformat())

class ReferenceConvertorTests(unittest.TestCase):

    def test_convert_simple_fields(self):
        converter = reference_convertor()
        obj = DummyReference(1, "abc", datetime(2025, 10, 26))
        result = converter.Convert(obj)

        self.assertEqual(result['num'], 1)
        self.assertEqual(result['text'], "abc")
        self.assertEqual(result['dt'], "2025-10-26T00:00:00")

    def test_convert_with_nested_reference(self):
        converter = reference_convertor()
        nested_obj = DummyReference(2, "nested", datetime(2024, 5, 10))
        obj = DummyReference(1, "parent", datetime(2025, 10, 26), nested=nested_obj)
        result = converter.Convert(obj)

        self.assertIn('nested', result)
        self.assertEqual(result['nested']['num'], 2)
        self.assertEqual(result['nested']['text'], "nested")
        self.assertEqual(result['nested']['dt'], "2024-05-10T00:00:00")

    def test_convert_with_none_field(self):
        converter = reference_convertor()
        obj = DummyReference(1, "abc", datetime(2025, 10, 26), nested=None)
        result = converter.Convert(obj)
        self.assertIn('nested', result)
        self.assertIsNone(result['nested'])

class ConvertFactoryTests(unittest.TestCase):

    def test_basic_convert(self):
        factory = convert_factory()
        res = factory.convert(42)
        self.assertEqual(res, {"value": 42})

        res = factory.convert("test string")
        self.assertEqual(res, {"value": "test string"})

        res = factory.convert(3.14)
        self.assertEqual(res, {"value": 3.14})

    def test_datetime_convert(self):
        factory = convert_factory()
        dt = datetime(2025, 10, 26, 15, 30)
        res = factory.convert(dt)
        self.assertEqual(res, {"value": dt.isoformat()})

    def test_reference_convert(self):
        factory = convert_factory()
        class DummyRef:
            pass
        dummy = DummyRef()
        res = factory.convert(dummy)
        self.assertEqual(res, {})



if __name__ == "__main__":
    unittest.main()
