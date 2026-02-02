from abc import ABC, abstractmethod

class Habilidade(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def executar(self):
        pass

class HabilidadeDeFogo(Habilidade):
    def __init__(self, nome):
        super().__init__(nome)

    def executar(self):
        print("Usando ataque de fogo! 15 de Dano.")

class Cura(Habilidade):
    def __init__(self, nome):
        super().__init__(nome)

    def executar(self):
        print("Usando magia de Cura! + 10 de Vida")

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.habilidades = []

    def aprender_habilidade(self, hab : Habilidade):
        self.habilidades.append(hab)

    def executar_todas_habilidades(self):
        for habilidade in self.habilidades:
            habilidade.executar()

joao = Personagem("Joao O Heroi")
joao.aprender_habilidade(HabilidadeDeFogo("Bola de fogo"))
joao.aprender_habilidade(Cura("Cura Fraca"))
joao.executar_todas_habilidades()

