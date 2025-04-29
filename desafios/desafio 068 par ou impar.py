#programa to play odd or even
from random import randint


while True:
    choice = randint(1, 10)
    
    print('-' * 20)
    jogador = int(input('Digite um número: '))
    print('-' * 20)
    
    resultado = choice + jogador

    if resultado % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    resposta = input('PAR OU IMPAR? [P/I] : ').strip().upper()[0]

    print(f'Eu escolhi o número {choice}, o resultado deu {jogador + choice} !')
    
    if resposta == resultado:
        print('Voce Venceu!! Pode ir embora!')
        break
    else:
        print('HAHAHHA VOCÊ PERDEU!!! TENTE NOVAMENTE!')