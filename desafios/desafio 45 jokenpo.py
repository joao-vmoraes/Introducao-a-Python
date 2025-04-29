#desafio de pedra papel e tesoura
import random
from time import sleep
lista = ['Pedra', 'Papel' , 'Tesoura']
pc = random.choice(lista) #palpite do pc
escolha = 1 #variavel se decide se vai jogar de novo ou encerrar o programa
placar_jogador = 0
placar_pc = 0

while escolha == 1: #enquanto a escolha de jogar for 1 o jogo sempre vai continuar rodando
    #mostrando na tela as opções
    print('Vamos jogar Pedra, Papel e Tesoura! Tente me vencer!')
    print('[1] para Pedra')
    print('[2] para Papel')
    print('[3] para Tesoura')
    jogador = int(input('Escolha: '))
    print('=-=-=-=-=-=-=-=-=-=-==-==-=-=-=-=-=-=-')
    #condição para apenas ser jogados os numeros 1,2 e 3
    while jogador != 1 and jogador !=2 and jogador !=3:
        jogador = int(input('ops, opção errada! Digite outro número: '))

    #transformando os números em strings
    if jogador == 1:
        jogador = 'Pedra'

    elif jogador == 2:
        jogador = 'Papel'

    elif jogador == 3:
        jogador = 'Tesoura'

    #mostrando os palpites
    print('Eu escolhi: {}.'.format(pc))
    print('Você escolheu : {}'.format(jogador))

    #Probabilidades de jogos
    if jogador == pc:
        print('empate')
    elif jogador == 'Tesoura' and pc == 'Pedra' or \
    jogador == 'Pedra' and pc == 'Papel' or \
    jogador == 'Papel' and pc == 'Tesoura':
        print('Você perdeu!')
        placar_pc += 1
    else:
        print('Você ganhou!')
        placar_jogador += 1
    
    sleep(2)

    #placar
    print('=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=--=-=')
    print('O placar esta: {} x {}'.format(placar_jogador, placar_pc))
    print('Você deseja jogar novamente?')
    
    #perguntando se vai jogar dnv
    print('[1] SIM')
    print('[2] Nao')
    print('')
    escolha = int(input(''))

if escolha == 2: #finalizando o jogo
    print('Foi um prazer jogar com você! Volte mais tarde.')