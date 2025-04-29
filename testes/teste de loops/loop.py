from random import randint
aleatorio = randint(1,5)
palpite = int(input('Vamos brincar! tente adivinha em qual número eu pensei de 1 ate 5: '))
while aleatorio != palpite:
    if palpite > 5:
        palpite = int(input('Para de graça! tente acertar:'))

    elif palpite < 6:
        palpite = int(input('Errado! tente novamente: '))
print('Parabens, você acertou! Foi um prazer jogar com voce!')