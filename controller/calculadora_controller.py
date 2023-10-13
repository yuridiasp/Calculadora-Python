from model.calculadora import *
from view.calculadora_view import *


class Controller:

    def __init__(self):
        self.__calculadora = Calculadora()
        self.__interface = Interface(self)

    def calcular(self, expression):
        try:
            resultado = self.__calculadora.calcular(expression)
        except Exception as e:
            print(e)
            return e
        else:
            return resultado

