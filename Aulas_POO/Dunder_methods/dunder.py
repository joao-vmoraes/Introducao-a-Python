from __future__ import annotations

class Ponto:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __repr__(self): # é mais para comunicar os outros desenvolvedores sobre o objeto
        class_name = type(self).__name__ # self.__class__.__name__ mesma coisa
        return f'{class_name}(x={self.x!r},y={self.y!r})' #usando o !r para chamar a funcao repr daquele atributo, para caso seja um objeto.
    
    def __str__(self): # é o metodo principal quando chamar o print(objeto)
        return f'({self.x} , {self.y})'
    
    def __add__(self, other: Ponto) -> Ponto: # adicionar
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other: Ponto) -> bool: # maior que
        p1 = self.x + self.y
        p2 = other.x + other.y
        return p1 > p2

p1 = Ponto(1,2)
p2 = Ponto(4,5)
p3 = p1 + p2

print(p1)
print(f'{p2!r}') # repr
print(p3)


print(p1 > p3)