from abc import ABC, abstractmethod

class Mamifero(ABC):
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self): return self._nome
    
    @nome.setter
    def nome(self, valor): self._nome = valor

    @abstractmethod
    def fazer_som(self): ...

class Cachorro(Mamifero):
    def __init__(self, nome, patas):
        super().__init__(nome)
        self._patas = patas

    @property
    def patas(self): return self._patas

    @patas.setter
    def patas(self,valor) : self._patas = valor

    def fazer_som(self):
        print("Au Au Auuuu...")

class SerHumano(Mamifero):

    def __init__(self, nome, profissao):
        super().__init__(nome)
        self._profissao = profissao

    @property
    def profissao(self): return self._profissao

    @profissao.setter
    def profissao(self, valor) : self._profissao = valor

    def fazer_som(self):
        print("Ola! Bom dia")


rex = Cachorro("Rex", 4)
joao = SerHumano("Joao" , "Estudante")


print(vars(joao))
print(vars(rex))

rex.fazer_som()
joao.fazer_som()

rex.nome = "Thor"
rex.patas = 3

joao.nome = "Pedro"
joao.profissao = "Estagiario"

print(vars(joao))
print(vars(rex))