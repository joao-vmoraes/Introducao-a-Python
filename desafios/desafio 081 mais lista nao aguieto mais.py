lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    continuar = int(input('Quer continuar? [1 = sim / 2 = nao ] :  '))
    if continuar != 1:
        break



print(f'Você digitou {len(lista)} números.')
print(f'A lista em ordem decrescente ficou: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O 5 apareceu na posição {sorted(lista, reverse=True).index(5) + 1}°')
else:
    print('O valor 5 não apareceu!')
