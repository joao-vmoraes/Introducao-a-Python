class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua , numero):
        self.enderecos.append(Endereco(rua, numero)) # A classe endereco so é intanciada dentro da classe Cliente.Dai, quand o cliente parar de existir o endereço tambem vai!

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua ,  numero):
        self.rua = rua
        self.numero = numero

c1 = Cliente('Pedro')
c1.inserir_endereco("Rua do Peixe", 12)
c1.inserir_endereco("Rua do Leão", 341)
print(c1.listar_enderecos())