count = 0 #number of attempts
from random import randint #importing random libery

#making the computer randomize a number
numero = randint(1,10)

#asking a intire number to the player
palpite = int(input('Tente acertar no número que eu pensei de 1 até 10: '))
count += 1

#making the variable palpite be only a natural number > -1 and < 10
while (palpite < 0) or (palpite > 10):
    palpite = int(input('ERRO: Numero inválido. Digite uma tentativa válida: '))

#while the guess is different from the number, continue asking
while palpite != numero:

    while (palpite < 0) or (palpite > 10):
        palpite = int(input('ERRO: Número inválido, tente novamente: '))

    palpite = int(input('Número errado, tente novamente: '))
    count += 1

#printing the number of attempts and the win word
print(f'Parabens! Eu pensei no número {numero}. Você ganhou Com um total de {count} tentativas')