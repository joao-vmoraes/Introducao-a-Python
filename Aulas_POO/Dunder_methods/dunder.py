class Ponto:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __repr__(self): # é mais para comunicar os outros desenvolvedores sobre o objeto
        class_name = type(self).__name__ # self.__class__.__name__ mesma coisa
        return f'{class_name}(x={self.x!r},y={self.y!r})' #usando o !r para chamar a funcao repr daquele atributo, para caso seja um objeto.
    
    def __str__(self): # é o metodo principal quando chamar o print(objeto)
        return f'({self.x} , {self.y})'

p1 = Ponto(1,2)
p2 = Ponto(4,5)

print(p1)
print(repr(p2))