import json

CAMINHO = 'Aulas_POO\Salvando_Classes_JSON/aula127.json'


class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joao' , 23)
p2 = Pessoa('Carlos' , 20)
p3 = Pessoa('Pedro' , 33)
db = [vars(p1), vars(p2) , vars(p3)]

with open(CAMINHO, 'w') as arquivo:
    json.dump(db, arquivo, ensure_ascii = False, indent = 2)