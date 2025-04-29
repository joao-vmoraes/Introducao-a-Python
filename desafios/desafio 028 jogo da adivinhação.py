#o computador vai pensar em um numero e voce vai tentar adivinhar o numero escolhido
from random import randint

#randomizar um número
n = int(randint(0 , 5))
traços = '-=-' * 20

#perguntar pro jogador
print(traços)
a = int(input('Pensei em um número! Adivinhe:  '))
print(traços)

if a == n:
    print('Não acredito! Você acertou!!! Eu pensei no número', n)

else:
    print('Não foi dessa vez, é realmente muito dificil me vencer! Eu pensei no número', n)        