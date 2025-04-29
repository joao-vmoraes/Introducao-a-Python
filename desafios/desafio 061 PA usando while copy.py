a1 = float(input('Escolha o primeio termo : '))
razao = float(input('Escolha a razão: '))
an = a1
final = 1
sequencia = [a1]


#começando a adicionar os itens
while (an != a1 + 9 * razao):
    an = a1 + final * razao
    final += 1
    sequencia += [an]
print(sequencia)