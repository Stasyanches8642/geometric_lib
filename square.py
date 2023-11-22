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
        res = area(2500)
        self.assertEqual(res, 6250000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_simple(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_perimeter_big(self):
        res = perimeter(1000)
        self.assertEqual(res, 4000)
