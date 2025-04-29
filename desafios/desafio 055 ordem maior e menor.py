#criando uma listados pesos:

#METODO 1

pesos = []
for i in range(1,8):
    peso = float(input(f'Qual o valor da {i} pessoa?'))
    pesos += [peso]
print(f'O maior número é {max(pesos)} e o menor é {min(pesos)}.')

#METODO 2

maior = 0
menor = 0

for i in range(1,8):
    peso = float(input(f'Qual o peso da pessoa {i}?'))

    if i == 1:          #a primeira pessoa ela sera o maior e o menor peso
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

#printando
print(f'o maior número é {maior} e o menor é {menor}')