import unittest
import pytest 
from src import calculadora 

class Testcalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = calculadora()
    def test_myfactorial(self):
        self.assertEqual(self.calculadora.factorial(3), 6)

    def test_factorial_zero(self):
        self.assertEqual(self.calculadora.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.calculadora.factorial(-1)

    
