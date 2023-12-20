import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=0.001)

    def test_area_simple(self):
        res = area(12)
        self.assertAlmostEqual(res, 452.38934, delta=0.001)

    def test_area_big(self):
        with self.assertRaises(ValueError) as context:
            result = area(-15)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=0.001)

    def test_perimeter_simple(self):
        res = perimeter(15)
        self.assertAlmostEqual(res, 94.24778, delta=0.001)

    def test_perimeter_big(self):
        with self.assertRaises(ValueError) as context:
            result = area(-9)
