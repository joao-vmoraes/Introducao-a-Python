#triangulo existe ou nao e qual o tipo: isosceles, equilateo ou escaleno

#perguntando as retas
retas = (input('me diga o valor de 3 retas: '))
lista = (retas.split())

#querendo apenas 3 elementos
while len(lista) != 3:
    retas = input('Quantidade errada! me diga o valor de 3 retas: ')
    lista = (retas.split())

#denominando cada elemento da lista para uma variavel
r1 = int(lista[0])
r2 = int(lista[1])
r3 = int(lista[2])

#condição de existencia
if (r1 > r2 + r3) or (r2 > r1 + r3) or (r3 > r1 + r2):
    print('Esse triangulo não existe.')
#tipo do triangulo
elif r1 == r2 == r3:
    print('Esse triangulo existe e é equilátero.')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Esse triangulo existe e é isoceles. ')
else:
    print('Esse triangulo existe e é escaleno.')



