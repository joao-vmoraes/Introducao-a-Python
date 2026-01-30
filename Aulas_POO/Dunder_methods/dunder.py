# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
from __future__ import annotations

class Ponto:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def soma_interna(self) -> int:
        return self.x + self.y

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
        p1 = self.soma_interna()
        p2 = other.soma_interna()
        return p1 > p2
    
    def __ge__(self, other: Ponto) -> bool: #maior ou igual
        p1 = self.soma_interna()
        p2 = other.soma_interna()
        return p1 >= p2
    
    def __eq__(self, other: Ponto) -> bool: # igual
        x = self.x == other.x
        y = self.y == other.y
        return (x and y)
    

p1 = Ponto(1,2)
p2 = Ponto(4,5)
p3 = p1 + p2

print(p1)
print(f'{p2!r}') # repr
print(p3)


print(p1 > p3)
print(p3 >= p1)
print(p3 == p3)