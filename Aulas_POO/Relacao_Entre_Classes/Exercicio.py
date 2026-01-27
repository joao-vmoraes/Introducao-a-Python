class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self.fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor


class Motor:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self, *carros):
        for carro in carros:
            carro.fabricante = self.nome
            self.carros.append(carro)

    def listar_carros(self):
        print(f"-=-= {self.nome.upper()} -=-=")
        for carro in self.carros:
            print(carro.nome , carro.motor.nome)

m1 = Motor("Bx00")
c1 = Carro("Onix")
c1.motor = m1

c2 = Carro("Cobalt LTZ")
c2.motor = m1

c3 = Carro("Camaro")
m2 = Motor("Motorsp 99f")
c3.motor = m2

f1 = Fabricante("Chevrolet")
f1.inserir_carro(c1,c2,c3)

f1.listar_carros()