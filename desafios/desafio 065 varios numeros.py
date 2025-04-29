escolha = 1 #constante de continuiudade do programa
soma = 0
c = 0
menor = 0
maior = 0

while escolha == 1:
    numero = float(input('Digite um número: '))
    soma += numero
    c += 1 

    print('voce deseja adicionar mais números? ')
    print('[1] Sim')
    print('[2] Não')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        escolha = 1
    
    if c == 1:
        menor = numero
        maior = numero
    if numero < menor :
        menor = numero
    if numero > maior:
        maior = numero

print(f'Você escolheu {c} números ')
print(f'O maior foi: {maior} . e o menor foi: {menor}.')
print(f'E a média foi {soma / c}')

