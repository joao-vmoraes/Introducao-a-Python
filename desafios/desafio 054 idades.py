maiores = 0
menores = 0
ano = 2025

#adicionar elementos a pessoas
for idades in range(4):
    idades = int(input('Digite o ano de nascimento de uma pessoa: '))
    if ano - idades < 18:
        menores += 1
    else: 
        maiores += 1
print(f'O resultado final ficou: {menores} pessoa(s) menores de idade e {maiores} pessoa(s) maiores de idade ')
