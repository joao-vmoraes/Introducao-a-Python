numeros = []
impares = list()
pares = list()

while True:
    numero = int(input("Digite um numero: "))
    if numero % 2 == 1:
        impares.append(numero)
    else:
        pares.append(numero)
    
    continuar = input("Deseja continuar com a listagem? [S/N] >>>")
    if continuar not in "Ss":
        numeros.append(pares[:])
        numeros.append(impares[:])
        break
print(numeros)
print(f"Os numeros pares foram {sorted(numeros[0])}")
print(f"Os numeros impares foram {sorted(numeros[1])}")