class Aluno: # declaração da classe
    escola = 'Escola Menino Jesus' # Como se fosse um atributo estático em Java. Todos da classe compartilharam 

    def __init__(self, nome, idade): #metodo construtor
        self.nome = f"{nome}" # atributo de instancia
        self.idade = idade # atributo de instancia


    # Métodos

    def aniversario(self):
        self.idade += 1
        print(f"Agora voce tem {self.idade} anos!")

    def boasVindas(self):
        print(f"Ola {self.nome} ! Seja bem vindo a {self.escola}!!!")

# Main

a1 = Aluno("Luiz", 20)
a2 = Aluno("Pedro", 10)

a1.boasVindas()
a2.boasVindas()

a1.aniversario()
a2.aniversario()