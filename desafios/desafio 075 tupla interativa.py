n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um: '))
n3 = int(input('Digite mais um: '))
n4 = int(input('Digite mais um: '))
contador = 1

tupla = (n1, n2 , n3, n4)

print(f'Você digitou os núimeros: {tupla}')

print(f'A quantidade de 9 é de : {tupla.count(9)}')

if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3) + 1 }')

for n in tupla:
    if contador == 1:
        print('OS números pares foram: ', end='')
        contador += 1

    if n % 2 == 0:
        print(n, end=', ')