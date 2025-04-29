#cadastro de varias pessoas
maiores_de_idade = 0
homens = 0
mulheres_20anos = 0


while True:
    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo [ M = Masculino / F = Feminino:] ')).strip().upper()[0]
    idade = int(input('digite a idade dessa pessoa: '))

    if idade >= 18:
        maiores_de_idade += 1
    
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade <= 20:
        mulheres_20anos += 1

    escolha = 2
    while escolha != 0 and escolha != 1:
        escolha = int(input('Deseja continuar? [1 = Sim  / 0 = Não ] : '))

    if escolha != 1:
        break

print(f'No total tiveram :\n{homens} Homens.')
print(f'{maiores_de_idade} Pessoas maiores de idade.')
print(f'{mulheres_20anos} mulheres com menos de 20 anos.')