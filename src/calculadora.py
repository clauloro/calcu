class Calculadora():
    def __init__(self):
        self.valor = 0
    def sumar(self,a,b):
        self.valor = a + b
        return self.valor
    def restar(self,a,b):
        self.valor = a - b
        return self.valor
    def multiplicar(self,a,b):
        self.valor = a * b
        return self.valor
    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir entre 0"
        self.valor = a / b
        return self.valor
    def factorial(self, numero):
        self.valor = 1
        if numero < 0:
            return "No se puede calcular el factorial de un número negativo"
        for i in range(1, numero + 1):
            self.valor *= i
        return self.valor