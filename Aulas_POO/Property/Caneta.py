class Caneta:
    def __init__(self, cor):
        self.cor = cor # Chama o setter

    @property # Funciona como se fosse um getter para um atributo da classe.
    def cor(self):
        return f'Estou no getter {self._cor}'

    @cor.setter # Setter
    def cor(self, cor):
        print("ESTOU NO SETTER", cor)
        self._cor = cor


c1 = Caneta("Azul")
c1.cor = 'Vermelho'
print(c1.cor)#A chamada é feita como se fosse um atributo!!!!
