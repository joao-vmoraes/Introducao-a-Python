class Aluno: # declaração da classe

    def __init__(self): #metodo construtor
        self.nome = "joao" # atributo de instancia
        self.idade = 0 # atributo de instancia

    # Métodos

    def aniversario(self):
        self.idade += 1
        print(f"Agora voce tem {self.idade} anos!")

    def boasVindas(self):
        print(f"Ola {self.nome} ! Seja bem vindo!!!")

# Main

a = Aluno()
a.aniversario()
a.boasVindas()
a.aniversario()