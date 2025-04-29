lista = []

while True:
    numero = int(input('Digite um número: '))

    if numero not in lista:
        lista.append(numero)
    else:
        print('ERRO: Valor ja foi registrado!')
    escolha = int(input('Quer continuar? [1 = sim / 2 = não]: '))

    if escolha != 1:
        break

print(f'Sua lista ficou assim: {sorted(lista)}')