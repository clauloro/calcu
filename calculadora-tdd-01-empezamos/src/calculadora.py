import math
class Calculadora:
    def sumar(self,a,b):
        return a + b
    def restar(self,a,b):
        return a-b
    def multiplicar(self,a,b):
        return a*b
    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir entre 0"
        return a / b
    def factorial(numero):
        fact = 1
        for i in range(1, numero + 1):
            fact *= i
        return fact