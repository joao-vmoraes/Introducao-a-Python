numero = float(input('Digite um número [999 para parar] : '))
soma = contador = 0
while True:
    if numero == 999:
        break
    else:
        soma += numero
        contador += 1
        numero = float(input('Digite um número [999 para parar] : '))
print(f'Voce digitou {contador} números e a soma foi : {soma}')