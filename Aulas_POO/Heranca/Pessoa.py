class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar_nome_classe(self):
        print(self.__class__.__name__, self.nome, self.idade)


class Professor(Pessoa): # Professor esta herdando de Pessoa
    ...

p1 = Professor("joao", 12)
p1.falar_nome_classe()