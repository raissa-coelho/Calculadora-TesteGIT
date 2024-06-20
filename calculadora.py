class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b
        
    def multiplicar(self, a, b):
        return a*b

    def dividir(self, a, b):
        if b != 0:
            result = a/b
        return result