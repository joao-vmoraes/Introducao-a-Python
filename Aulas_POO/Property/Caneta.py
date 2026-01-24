class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property # Funciona como se fosse um getter para um atributo da classe.
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_vidro(self):
        return "AHHAHAHAHAHAHAHAH"

c1 = Caneta("Azul")

print(c1.cor)
print(c1.cor)
print(c1.cor)
print(c1.cor)
print(c1.cor_vidro) #A chamada é feita como se fosse um atributo!!!!
print(c1.cor_vidro)