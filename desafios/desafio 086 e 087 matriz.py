linha1 = [0, 0,0]
linha2 = [0, 0,0]
linha3 = [0, 0,0]
matriz = []
pares = []
soma_terceira_coluna = 0 
soma_pares = 0
contador = 1
maior_numero = 0

while True:
    print("==" * 20)
    print(linha1)
    print(linha2)
    print(linha3)

    numero = int(input("Digite o numero >>> ")) 
    linha = int(input("Digite a linha >>> "))
    while (linha < 1 or linha > 3):
        linha = int(input("Digite a linha >>> "))
    coluna = int(input("Digite a coluna >>> "))
    while (coluna < 1 or coluna > 3):
        coluna = int(input("Digite a coluna >>> "))
    
    if linha == 1:
            linha1[coluna - 1] = numero
    elif linha == 2:
            linha2[coluna - 1] = numero
    elif linha == 3:
            linha3[coluna - 1] = numero
    else:
        print("linha invalida.")

    escolha = input("Deseja continuar? [S/N] >>>")
    if escolha not in "Ss":
        break

matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])

for lista in matriz:
    try:
        soma_terceira_coluna += lista[2] 
    except:
        continue

for linha in matriz:
    for c in linha:
        if c % 2 == 0:
            pares.append(c)
            soma_pares += c

maior_numero = max(linha2)

print("=-=-=-=-=-=-=-=-=-=")
print("A Matriz ficou assim: ")
print(linha1)
print(linha2)
print(linha3)
print("=-=-=-=-=-=-=-=-=-=-=")

print(f"A soma de todos os numeros pares e: {soma_pares}")
print(f"O maior valor da segunda linha e: {maior_numero}")
print(f"A soma dos valores da terceira coluna e: {soma_terceira_coluna}")