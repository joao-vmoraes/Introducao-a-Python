while True:
    #asking the quantity
    print('=' * 40)
    print(f'{'CAIXA ELETRONICO' :^40}')
    print('=' * 40)

    quantidade = int(input('Digite a quantidade a ser sacada: '))

    cedulas_de_50 = quantidade // 50
    cedulas_de_20 = (quantidade - cedulas_de_50 * 50) // 20
    cedulas_de_10 = ((quantidade - cedulas_de_50 * 50) - cedulas_de_20 * 20) // 10
    cedulas_de_1 = ((quantidade - cedulas_de_50 * 50) - cedulas_de_20 * 20) % 10


    print(f'Total de {cedulas_de_50} Cédulas de R$50')
    print(f'Total de {cedulas_de_20} Cédulas de R$20')
    print(f'Total de {cedulas_de_10} Cédulas de R$10')
    print(f'Total de {cedulas_de_1} Moedas de R$1')

    escolha = int(input('Deseja continuar? [1 = Sim / 2 = Não] : '))

    if escolha == 2:
        break

print('--------- FIM DO PROGRAMA ----------')