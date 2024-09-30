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
    def factorial(self, a):
        if a < 0:
            raise ValueError("El número debe ser no negativo")
        elif a == 0 or a == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, a + 1):
                resultado *= i
            return resultado
