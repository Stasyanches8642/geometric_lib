import unittest


def area(a):
    return a * a


def perimeter(a):
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_simple(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_big(self):
        with self.assertRaises(ValueError) as context:
            result = area(-20)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_simple(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_perimeter_big(self):
        with self.assertRaises(ValueError) as context:
            result = area(-11)
