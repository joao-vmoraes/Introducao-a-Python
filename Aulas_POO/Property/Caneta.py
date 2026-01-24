class Caneta:
    def __init__(self, cor):
        self._cor_tinta = cor

    @property # Funciona como se fosse um getter para um atributo da classe.
    def cor(self):
        return self._cor_tinta

    @cor.setter
    def cor(self, cor):
        print("ESTOU NO SETTER ", cor)
        self._cor = cor


c1 = Caneta("Azul")

c1.cor = 'Vermelho'
c1.cor = 'Amarelo'

print(c1.cor)
print(c1.cor)
print(c1.cor)
print(c1.cor)
print(c1.cor_vidro) #A chamada é feita como se fosse um atributo!!!!
print(c1.cor_vidro)