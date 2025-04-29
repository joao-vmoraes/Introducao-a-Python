n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha mais um: '))
if n1 > n2:
    print('O maior número é {} e o menor é {}.'.format(n1 , n2))
elif n2 > n1:
    print('O maior número é {} e o menor é {}.'.format(n2 , n1))
else:
    print('Os números são iguais!')