import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_int(self):
        price = 12345
        self.assertEqual(format_price(price), '12 345.00')

    def test_float(self):
        price = 12345.0000
        self.assertEqual(format_price(price), '12 345.00')

    def test_float_round(self):
        price = 12345.98
        self.assertEqual(format_price(price), '12 345.98')

    def test_float_with_comma(self):
        price = '12345,0000'
        self.assertIsNone(format_price(price))

    def test_string(self):
        price = '12345'
        self.assertEqual(format_price(price), '12 345.00')

    def test_nondidgit_string(self):
        price = '12345sdf'
        self.assertIsNone(format_price(price))

    def test_empty_string(self):
        price = ''
        self.assertIsNone(format_price(price))

    def test_None(self):
        price = None
        self.assertIsNone(format_price(price))

    def test_zero(self):
        price = 0
        self.assertEqual(format_price(price), '0.00')

    def test_negative_int(self):
        price = -100000
        self.assertEqual(format_price(price), '-100 000.00')

    def test_negative_float(self):
        price = -100000.00
        self.assertEqual(format_price(price), '-100 000.00')

    def test_boolean(self):
        price = True
        self.assertIsNone(format_price(price))

    def test_list(self):
        price = [1, 2, 3]
        self.assertIsNone(format_price(price))


if __name__ == '__main__':
    unittest.main()
