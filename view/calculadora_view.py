from tkinter import *


class Interface:
    __expression = "0"
    __visor = None
    __teclado = None
    __clear = False

    def __init__(self, controller):
        self.controller = controller

        root = Tk()

        titulo = self.Titulo(self, root)
        titulo.frame.pack()

        self.__visor = self.Visor(self, root)
        self.__visor.frame.pack()

        self.__teclado = self.Teclado(self, root)
        self.__teclado.frame.pack()

        root.mainloop()

    @property
    def clear(self):
        return self.__clear

    @clear.setter
    def clear(self, booleano):
        self.__clear = booleano

    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, param):
        self.__expression = param

    def set_expression(self, param, delete=False):
        if self.expression == "0" or delete:
            self.expression = param
        else:
            self.expression += param

    def AtualizarVisor(self):
        self.__visor.set_text(self.expression)

    def InserirDigito(self, tecla):
        array = ["*", "/", "+", "-", "^", "sqrt", "+/-", "1/x", "."]
        if tecla == '.' and self.expression == "0":
            self.expression = "0."
        elif tecla in array and self.expression[len(self.expression)-1] in array:
            self.expression[len(self.expression)-1] = tecla[0]
        else:
            self.set_expression(tecla)
            self.AtualizarVisor()

    def Calcular(self):
        expression_math = self.expression + " = "
        self.expression = self.controller.calcular(self.expression)
        self.__visor.set_text(expression_math + str(self.expression))
        self.clear = True

    def Deletar(self):
        if len(self.expression) > 1 and not self.clear:
            self.set_expression(self.expression[:-1], True)
        else:
            self.expression = "0"
            self.clear = False
        self.AtualizarVisor()

    def Limpar(self):
        self.expression = "0"
        self.clear = False
        self.AtualizarVisor()

    class Titulo:
        def __init__(self, interface, root_one):
            self.interface = interface
            self.frame = Frame(root_one)
            self.label = Label(text="Calculadora Python")
            self.label.pack()

    class Visor:
        def __init__(self, interface, root_one):
            self.interface = interface
            self.frame = Frame(root_one)
            self.label = Label(self.frame, width=45, height=5, bg="Black", fg="White")
            self.set_text(self.interface.expression)
            self.label.pack()

        def set_text(self, expression):
            self.label.config(text=expression)

    class Teclado:
        def __init__(self, interface, root_one):
            self.interface = interface
            coord_x = 10
            coord_y = 5
            self.frame = Frame(root_one)

            self.zero = Button(self.frame, text="0", width=coord_x, height=coord_y,
                               command=lambda: self.interface.InserirDigito("0"))
            self.one = Button(self.frame, text="1", width=coord_x, height=coord_y,
                              command=lambda: self.interface.InserirDigito("1"))
            self.two = Button(self.frame, text="2", width=coord_x, height=coord_y,
                              command=lambda: self.interface.InserirDigito("2"))
            self.three = Button(self.frame, text="3", width=coord_x, height=coord_y,
                                command=lambda: self.interface.InserirDigito("3"))
            self.four = Button(self.frame, text="4", width=coord_x, height=coord_y,
                               command=lambda: self.interface.InserirDigito("4"))
            self.five = Button(self.frame, text="5", width=coord_x, height=coord_y,
                               command=lambda: self.interface.InserirDigito("5"))
            self.six = Button(self.frame, text="6", width=coord_x, height=coord_y,
                              command=lambda: self.interface.InserirDigito("6"))
            self.seven = Button(self.frame, text="7", width=coord_x, height=coord_y,
                                command=lambda: self.interface.InserirDigito("7"))
            self.eit = Button(self.frame, text="8", width=coord_x, height=coord_y,
                              command=lambda: self.interface.InserirDigito("8"))
            self.nine = Button(self.frame, text="9", width=coord_x, height=coord_y,
                               command=lambda: self.interface.InserirDigito("9"))

            self.igual = Button(self.frame, text="=", width=coord_x, height=coord_y, command=self.interface.Calcular)
            self.virgula = Button(self.frame, text=",", width=coord_x, height=coord_y,
                                  command=lambda: self.interface.InserirDigito("."))
            self.delete = Button(self.frame, text="Del", width=22, command=self.interface.Deletar)
            self.limpar = Button(self.frame, text="C", width=22, command=self.interface.Limpar)

            self.somar = Button(self.frame, text="+", width=coord_x, height=coord_y,
                                command=lambda: self.interface.InserirDigito("+"))
            self.diminuir = Button(self.frame, text="-", width=coord_x, height=coord_y,
                                   command=lambda: self.interface.InserirDigito("-"))
            self.multiplicar = Button(self.frame, text="*", width=coord_x, height=coord_y,
                                      command=lambda: self.interface.InserirDigito("*"))
            self.dividir = Button(self.frame, text="/", width=coord_x, height=coord_y,
                                  command=lambda: self.interface.InserirDigito("/"))
            self.potencia = Button(self.frame, text="^", width=coord_x, height=coord_y)
            self.raiz_quadrada = Button(self.frame, text="r(x)", width=coord_x, height=coord_y)
            self.inverter_sinal = Button(self.frame, text="+/-", width=coord_x, height=coord_y)
            self.inverter_base = Button(self.frame, text="1/x", width=coord_x, height=coord_y)

            self.zero.grid(row=5, column=1)
            self.one.grid(row=4, column=0)
            self.two.grid(row=4, column=1)
            self.three.grid(row=4, column=2)
            self.four.grid(row=3, column=0)
            self.five.grid(row=3, column=1)
            self.six.grid(row=3, column=2)
            self.seven.grid(row=2, column=0)
            self.eit.grid(row=2, column=1)
            self.nine.grid(row=2, column=2)
            self.igual.grid(row=5, column=3)
            self.virgula.grid(row=5, column=2)
            self.limpar.grid(row=0, column=0, columnspan=2)
            self.delete.grid(row=0, column=2, columnspan=2)
            self.somar.grid(row=4, column=3)
            self.diminuir.grid(row=3, column=3)
            self.multiplicar.grid(row=2, column=3)
            self.dividir.grid(row=1, column=3)
            self.potencia.grid(row=1, column=0)
            self.raiz_quadrada.grid(row=1, column=1)
            self.inverter_sinal.grid(row=5, column=0)
            self.inverter_base.grid(row=1, column=2)
