class Calculadora:

    def soma (self, a, b):
        return a + b
    def sub (self, a, b):
        return a - b
    def multi (self, a, b):
        return a * b
    def divi (self, a, b):
        return a / b

calculadora = Calculadora()

print("A soma é: ", calculadora.soma(10,2))
print("A sub é: ", calculadora.sub(5,3))
print("A multi é: ", calculadora.multi(7,8))
print("A divisão é: ", calculadora.divi(9,3))
