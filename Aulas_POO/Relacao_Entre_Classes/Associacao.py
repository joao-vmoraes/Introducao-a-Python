class Atirador:
    def __init__(self, nome, arma = None):
        self.nome = nome
        self._arma = arma

    @property
    def arma(self):
        return vars(self._arma)

    @arma.setter
    def arma(self, arma):
        print('arma atualizada')
        self._arma = arma

class ArmaDeCombate:
    def __init__(self, nome, municoes):
        self.nome = nome
        self._municoes = municoes

    @property
    def municoes(self):
        return self._municoes
    
    @municoes.setter
    def municoes(self, valor):
        if valor is None or valor <= 0:
            raise ValueError('Numero invalido')
        self._municoes = valor


p1 = ArmaDeCombate('Pistola', 22)
a1 = Atirador('Caloudo', p1)
print(a1.arma)
