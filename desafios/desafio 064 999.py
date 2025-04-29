#perguntando o numero
soma = 0
count = 0
numero = float(input('Digite um número: '))

while numero != 999:
    soma += numero
    count+= 1
    numero = float(input('Digite mais um numero: '))
print(f' A soma dos seus números foi {soma} e voce teve um total de {count} tentativas.')