class Sala:

    def __init__(self):
        self._alunos = []

    def adicionar_aluno(self, *alunos):
        self._alunos += alunos

    def remover_alunos(self, *alunos):
        for aluno in alunos:
            if aluno in self.alunos:
                self._alunos.remove(aluno)
    
    @property
    def alunos(self):
        return self._alunos

class Aluno: 

    def __init__(self, nome, idade): 
        self.nome = f"{nome}" 
        self.idade = idade 

a1 = Aluno('Pedro', 12)
a2 = Aluno('Carlos', 13)
a3 = Aluno('José', 14)

t1 = Sala()
t1.adicionar_aluno(a1,a2,a3)
t1.remover_alunos(a3)
print(t1.alunos)
