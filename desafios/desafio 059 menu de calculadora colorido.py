continuar = 1 #CRIANDO UMA VARIAVEL PARA CONTINUAÇÃO DO PROGRAMA

from time import sleep

#asking the numbers
print('\033[1;36m-=\033[m' * 20)
for n in range(1,3):
    if n == 1:
        n1 = int(input(f'Digite o \033[1;31m{n}°\033[m numero: '))#armazenando n1
    else:
        n2 = int(input(f'digite o \033[1;31m{n}°\033[m numero: '))#armazenando n2

while continuar == 1: #CRIANDO UM MENU INFINITO ATE TER UM BREAK
    print('-=' * 20)
    print('\033[1;36mMENU\033[m')
    print('-=' * 20)
    print('\033[1;31m[1]\033[m Somar')
    print('\033[1;32m[2]\033[m Multiplicar')
    print('\033[1;33m[3]\033[m Dividir')
    print('\033[1;34m[4]\033[m Maior')
    print('\033[1;35m[5]\033[m Outros números')
    print('\033[1;36m[6]\033[m Sair')
    print('')
    escolha = int(input('Escolha: '))

    if escolha == 1: #ADIÇÃO
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        sleep(2)

    if escolha == 2: #MULTIPLICAÇÃO
        print(f'A multiplicação entre {n1} e {n2} é : {n1 * n2}')
        sleep(2)

    if escolha == 3: #DIVISAO
        print(f'O valor da divisão entre {n1} e {n2} é: {n1 / n2}') 
        sleep(2)

    if escolha == 4: #O MAIOR NUMERO
        if n1 > n2:
            print(f'O maior número é {n1}.')
        elif n1 == n2:
            print(f'os numeros são iguais!')
        else:
            print(f'o maior número é {n2}')
        sleep(2)

    if escolha == 5: #escolhendo novos numero
        #asking the numbers
        print('-=' * 20)
        for n in range(1,3):
            if n == 1:
                n1 = int(input(f'Digite o {n}° numero: '))#armazenando n1
            else:
                n2 = int(input(f'digite o {n}° numero: '))#armazenando n2


    if escolha == 6:
        print('Foi um prazer! Qualquer coisa me chame novamente.')
        continuar = 0