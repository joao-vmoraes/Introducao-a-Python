pessoa = list()
grupo = list()
pesadas = list()
leves = list()
count = 0


while True:
    pessoa.append(str(input("Digite o nome: ")))
    pessoa.append(int(input("Digite a idade: ")))
    grupo.append(pessoa[:])
    count += 1

    if pessoa[1] <= 70:
        pesadas.append(pessoa[0])
    elif pessoa[1] >= 100:
        leves.append(pessoa[0])
    
    pessoa.clear()
    continuar = input("Deseja continuar com a listagem? [S/N] >>>")
    if continuar not in "Ss":
        break

print(f"a quantidade de pessoas listadas foi de {count}")
print(f"As pessoas mais leves foram: {leves}")
print(f"As pessoas mais pesadas foram {pesadas}")
