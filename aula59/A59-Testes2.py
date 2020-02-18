# Teste parte 2

class Calc:
    def __init__(self, numero1, numero2):
        # variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        self.__resultado = self.__n1 + self.__n2

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2

    def multiplicacao(self):
        self.__resultado = self.__n1 * self.__n2

    def divisão(self):
        self.__resultado = self.__n1 / self.__n2

c = Calc(10,20)
assert isinstance(c, Calc)

assert c.soma() == None
assert c.get_resultado() == 30

assert c.subtracao() == None
assert c.get_resultado() == -10

assert c.multiplicacao() == None
assert c.get_resultado() == 200

assert c.divisão() == None
assert c.get_resultado() == 0.5

assert c.get_n1() == 10

assert c.get_n2() == 20

assert c.set_n1(5) == None
assert c.get_n1() == 5

assert c.set_n2(6) == None
assert c.get_n2() == 6
