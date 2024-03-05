class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adcionar(num1, num2)

        elif op == '-':
            return self.__subtrair(num1, num2)

        else:
            print('Operação Invalida!')

    def __adcionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2

calculadora = Calculadora()
resultado = calculadora.calcular('+', 3, 2)
print(resultado)
