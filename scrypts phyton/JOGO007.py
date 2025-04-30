import random
contador = 0
defesa_jogador = 0
defesa_pc = 0
balas_jogador = 0
balas_pc = 0
atirar_jogador = 0
atirar_pc = 0

while True:
    if contador == 0:
        print('==' * 20)
        print(f"\033[1;33m{'JOGO DO 007' :^40}\033[m")
        contador += 1

    if balas_jogador == 0: #se o jogador estiver sem munição
        print('==' * 20)
        print('DECIDA A SUA AÇÃO: ')
        print('\033[1;32m[1]\033[m DEFENDER')
        print('\033[1;33m[2]\033[m RECARREGAR')
        print(f'Você tem {balas_jogador} muniçoes')
        print(f'Muniçoes do adversário: {balas_pc}')
        decisao_jogador = int(input('Escolha: '))
        print(decisao_jogador)
            

        if decisao_jogador == 1:#se o jogador estiver sem munição e defende
            defesa_jogador = 1
            
        elif decisao_jogador == 2:#se o jogador esta sem mun. e recarrega
            balas_jogador += 1
            defesa_jogador = 0
            
        
    elif balas_jogador >= 1:
            print('=' * 40)
            print('DECIDA A SUA AÇÃO:')
            print('\033[1;32m[1]\033[m DEFENDER')
            print('\033[1;33m[2]\033[m RECARREGAR')
            print('\033[1;31m[3]\033[m ATIRAR')
            print(f'Você tem {balas_jogador} Munições.')
            print(f'Muniçoes do adversario: {balas_pc}')
            decisao_jogador = int(input('ESCOLHA: '))
        
        
            if decisao_jogador == 1:
                defesa_jogador = 1
                
            elif decisao_jogador == 2:
                balas_jogador += 1
                defesa_jogador = 0
                
            elif decisao_jogador == 3:
                atirar_jogador = 1
                balas_jogador -= 1
                defesa_jogador = 0

    if contador == 1:
        balas_pc += 1

    elif balas_pc == 0: #se o computador esta sem munição pergunta
        decisao_pc = random.choices([1, 2] , weights=[ 65 , 35 ])[0]
        
        if decisao_pc == 1: # computador defende
            defesa_pc = 1
        else:
            balas_pc += 1 # computador recarrega
            defesa_pc = 0
                
        
    elif balas_pc >= 1:
        decisao_pc = random.choices([1 , 2 , 3] , weights=[ 20, 20, 60])[0]
        if decisao_pc == 1:
            defesa_pc = 1
            
        elif decisao_pc == 2:
            balas_pc += 1
            defesa_pc = 0
            
        elif decisao_pc == 3:
            atirar_pc = 1
            balas_pc -= 1
            defesa_pc = 0
            
    contador += 1

    if atirar_jogador == 1 and atirar_pc == 0 and defesa_pc == 0:
        print('Voce Atirou e eu nao defendi! Voce venceu!')
        break
    
    elif atirar_pc == 1 and defesa_jogador == 0 and atirar_jogador == 0:
        print('Eu atirei e voce nao defendeu! Eu venci!')
        break
    
    elif atirar_jogador == 1 and defesa_pc == 1:
        print('Voce atirou e eu defendi!')
        atirar_jogador = 0
    
    elif atirar_pc == 1 and defesa_jogador == 1:
        print('Eu atirei e voce defendeu!')
        atirar_pc = 0
    
    elif atirar_jogador == 1 and atirar_pc == 1:
        print('Nós dois atiramos no mesmo tempo! Empate.')
        atirar_jogador = 0
        atirar_pc = 0