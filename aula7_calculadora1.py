class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma (self):
        return self.a + self.b
    def sub (self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def divi(self):
        return self.a / self.b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.a,"e", calculadora.b)
    print("A soma é: ", calculadora.soma())
    print("A sub é: ", calculadora.sub())
    print("A multi é: ", calculadora.multi())
    print("A divisão é: ", calculadora.divi())



