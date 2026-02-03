from collections import namedtuple

Carta = namedtuple("Carta", ['valor', 'naipe'])
as_espadas = Carta('A', 'Espadas')

print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)
print(as_espadas._asdict)