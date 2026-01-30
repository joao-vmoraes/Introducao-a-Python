from __future__ import annotations
from math import sqrt

class Vetor:
    def __init__(self, x: int , y: int ):
        self._x = x
        self._y = y

    @property
    def x(self) -> int: return self._x
    
    @property
    def y(self) -> int: return self._y

    @x.setter
    def x(self, valor) : self._x = valor

    @y.setter
    def y(self, valor): self._y = valor

    def __str__(self):
        return f'({self.x} , {self.y})'
    
    def tamanho_vetor(self):
        a_ = (self.x)**2 + (self.y)**2
        tamanho = sqrt(a_)
        return tamanho

    def __add__(self, other: Vetor):
        x = self.x + other.x
        y = self.y + other.y
        return Vetor(x,y)
    
v1 = Vetor(3,4)
v2 = Vetor(3,3)
print(v1 + v2)
print(v1.tamanho_vetor())