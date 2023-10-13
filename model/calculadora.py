import math
import re


class Calculadora:
    args = []
    __expression = None

    def __init__(self):
        self.operations_one_number = ["sqrt", "+/-", "1/x"]
        self.operations_two_number = ["+", "-", "*", "/", "^"]
        self.operation = {
            "+": self.somar,
            "-": self.diminuir,
            "*": self.multiplicar,
            "/": self.dividir,
            "^": self.potencia,
            "sqrt": self.raiz_quadrada,
            "+/-": self.inverter_sinal,
            "1/x": self.inverter_base
        }

    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression):
        self.__expression = expression

    def resetCalculadora(self):
        self.args = []

    def calcular(self, expression): # 0
        self.expression = expression
        functions = ["^", "sqrt", "+/-", "1/x"]
        operadores = ["*", "/", "+", "-"]
        for operador in operadores: # 2
            if operador in self.expression:
                pattern = f"[0-9]+\.?[0-9]*\{operador}[0-9]+\.?[0-9]*"
                operandos = re.findall(pattern, self.expression) # 1
                if len(operandos) > 0:
                    operandos_operador = operandos[0].split(operador)
                    self.args.append(float(operandos_operador[0])) # 3
                    self.args.append(float(operandos_operador[1])) # 3
                    if self.validar_operation(operador):
                        result = self.operation[operador]() # 4
                        self.resetCalculadora()
                        self.expression = self.expression.replace(operandos[0], str(result)) # 5
                        self.calcular(self.expression)
                    else:
                        raise ValueError("Operação ou número de argumentos inválidos!")
        return self.expression

    def validar_operation(self, operation):
        if (operation in self.operations_two_number and len(self.args) == 2) or (
                operation in self.operations_one_number and len(self.args) == 1):
            return True
        else:
            return False

    def somar(self):
        return self.args[0] + self.args[1]

    def diminuir(self):
        return self.args[0] - self.args[1]

    def multiplicar(self):
        return self.args[0] * self.args[1]

    def dividir(self):
        try:
            resultado = self.args[0] / self.args[1]
        except ZeroDivisionError:
            return "Erro: divisão por zero!"
        else:
            return resultado

    def potencia(self):
        return self.args[0] ** self.args[1]

    def raiz_quadrada(self):
        return math.sqrt(self.args[0])

    def inverter_sinal(self):
        return -self.args[0]

    def inverter_base(self, a):
        return 1 / self.args[0]
