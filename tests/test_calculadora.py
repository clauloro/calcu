import unittest 
from src.calculadora import Calculadora 

class Testcalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
    def test_myfactorial(self):
        self.assertEqual(self.calculadora.factorial(3), 6)
    def test_factorial_zero(self):
        self.assertEqual(self.calculadora.factorial(0), 1)

    def test_factorial_negative(self):
        self.assertEqual(self.calculadora.factorial(-5), "No se puede calcular el factorial de un número negativo")

    
