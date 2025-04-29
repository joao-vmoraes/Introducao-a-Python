lista = []
lista_impar = []
lista_par = []

#perguntando o numero
while True:
    print('=' * 20)
    numero = int(input('Digite um número: \033[32m'))
    print('\033[m=' * 20)

    if numero in lista:
        print('\033[1;31mERRO:\033[m O numero ja esta na lista! Digite outro')
        print('=' * 20)
    elif numero % 2 == 0:
        lista_par.append(numero)
        lista.append(numero)
    else:
        lista_impar.append(numero)
        lista.append(numero)

    continuar = int(input('Quer continuar? [1 = Sim / 2 = Não]: '))
    if continuar != 1:
        break

print('=' * 20)
print(f'Os numeros que voce digitou foram: {sorted(lista)}')
print(f'Os numeros pares foram: {sorted(lista_par)}')
print(f'Os numero impares que voce digiou foram: {sorted(lista_impar)}')