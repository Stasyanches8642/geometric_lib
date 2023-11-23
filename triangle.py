import unittest

def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_simple(self):
        res = area(2, 6)
        self.assertEqual(res, 6)

    def test_area_big(self):
        res = area(-5, 7.3)
        self.assertEqual(res, "Error")

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_simple(self):
        res = perimeter(4, 9, 12)
        self.assertEqual(res, 25)

    def test_perimeter_big(self):
        res = perimeter(-3, -8, 5)
        self.assertEqual(res, "Error")
