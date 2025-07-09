import unittest
from unittest import TestCase
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
        result =calc.add(10,20)
        self.assertEqual(result,30)
    def test_sub(self):
        result = calc.sub(20,30)
        self.assertEqual(result,-10)
    def test_mul(self):
            result = calc.mul(10, 30)
            self.assertEqual(result, 300)
    def test_div(self):
        result = calc.div(20,2)
        self.assertEqual(result,10)

