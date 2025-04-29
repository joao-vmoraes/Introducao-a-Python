#perguntando o preço
preço = float(input('\033[1;31mDigite o preço do produto:\033[32m R$\033[m '))
print('\033[34;1m-=-\033[m' * 20)
parcela = 2

#modulo sleep
from time import sleep


#Perguntando o metodo de pagamento
print('\033[1;34mEscolha o metodo de pagamento:\033[m')
print('\033[1;31m[1]\033[m. para a vista no dinheiro(sem juros)')
print('\033[1;32m[2]\033[m. para a vista no debito(sem juros)')
print('\033[1;33m[3]\033[m. para parcelado no credito em 2x(sem juros)')
print('\033[1;35m[4]\033[m. para parcelado no credito em 3x ou até 12x (20% juros) ')
metodo = 0

while (metodo != 0) or metodo !=1 or metodo !=2 or metodo != 3 or metodo !=4: #perguntando o metodo e limitando as opções
    metodo = int(input('Qual metodo: '))

    if metodo == 1:  #opção no dinheiro
        print('o metodo escolhido foi \033[33;1mdinheiro\033[m a vista e valor total ficou: \033[32mR${:.2f}\033[m'.format(preço))
        break

    elif metodo == 2: #opção debito
        print('o metódo escolhido foi \033[33mdebito\033[m a vista e o valor ficou: \033[33mR${:.2f}\033[m'.format(preço))
        break

    elif metodo == 3: #opção credito 2x
        print('o metodo de pagamento foi \033[33mcrédito\033[m em 2x e o valor ficou: \033[33mR${:.2f}\033[m'.format(preço / 2))
        break

    elif metodo == 4: #opção credito 3x +
        parcela = int(input('o metodo escolhido foi \033[33mcrédito\033[m. escolha as parcelas:'))
        
        while (parcela < 3) or (parcela > 12): #eunquanto que a parcela nao for permitida vai ser sempre perguntada
            parcela = int(input('Quantidade errada, escolha outra parcela: '))
        
        print('O metodo escolhido foi \033[33mcrédito\033[m em \033[34m{}x parcelas\033[m, e o valor parcelado foi : \033[33mR${:.2f}\033[m '.format(parcela, preço * 1.2 / parcela))
        break
print('-=-' * 20)
print('\033[33;1mconfirmando pagamento...\033[m')
sleep(4)
print('Muito obrigado pela preferencia!')
