import random
nome = input('Digite seu nome: ')
lista = nome.split()
a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]
e = lista[4]
f = lista[5]
new = [a,b ,c ,d, e, f]
aleatorio = random.shuffle(new)
print(aleatorio)

