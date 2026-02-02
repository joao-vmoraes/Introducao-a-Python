import enum

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2

def mover(direcao:Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError("A direcao solicitada nao existe")
    print(f"Movendo para {direcao.name}")

mover(Direcoes.ESQUERDA)
print(Direcoes.ESQUERDA.name)
