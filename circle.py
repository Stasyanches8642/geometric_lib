import math
import unittest

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_simple(self):
        res = area(12)
        self.assertEqual(res, 452.38934)

    def test_area_big(self):
        res = area(-15)
        self.assertEqual(res, "Error")

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_simple(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24778)

    def test_perimeter_big(self):
        res = perimeter(-9)
        self.assertEqual(res, "Error")
