# O Carrinho de Compras TEM UM OU MAIS produtos

class Carrinho:
    def __init__(self):
        self.produtos = []

    def total(self):
        return sum([p.preco for p in self.produtos])

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)
    
    def inserir_produtos(self, *produtos):
        self.produtos += produtos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1,p2 = Produto('Livro', 30) , Produto('bolsa' , 200)
carrinho.inserir_produtos(p1,p2)
carrinho.listar_produtos()
print(carrinho.total())