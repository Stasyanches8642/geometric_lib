import unittest

def area(a, b):
    return a * b 

def perimeter(a, b):
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_simple(self):
        res = area(8, 5)
        self.assertEqual(res, 40)

    def test_area_big(self):
        res = area(-3, -7)
        self.assertEqual(res, "Error")

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_simple(self):
        res = perimeter(7, 13)
        self.assertEqual(res, 40)

    def test_perimeter_big(self):
        res = perimeter(-8, 4)
        self.assertEqual(res, "Error")
