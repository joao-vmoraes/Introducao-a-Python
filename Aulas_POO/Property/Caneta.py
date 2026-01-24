class Caneta:
    def __init__(self, cor):
        self.cor = cor

    @property # Funciona como se fosse um getter para um atributo da classe.
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        print("ESTOU NO SETTER", cor)
        self._cor = cor


c1 = Caneta("Azul")
c1.cor = 'Vermelho'
print(c1.cor)#A chamada é feita como se fosse um atributo!!!!
