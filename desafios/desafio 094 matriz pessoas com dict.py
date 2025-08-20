pessoa = {}
continuar = "S"
grupo = []
soma_idades = 0
mulheres = []
idades_maiores_que_media = []


while True:
    if continuar == "S":
        pessoa["nome"] = input("Digite o nome da pessoa: ")
        pessoa["sexo"] = input(f"Digite o sexo de {pessoa["nome"]}: ").upper().strip()[0]
        pessoa["idade"] = int(input(f"Digite a idade de {pessoa["nome"]}: "))
        grupo.append(pessoa.copy())

        if pessoa["sexo"] == "F":
            mulheres.append(pessoa["nome"])

        continuar = input("Deseja adicionar mais alguem? [S/N] >>> ").upper().strip()[0]
    
    elif continuar == "N":
        break

for pessoa in grupo:
    soma_idades += pessoa["idade"] 

media = soma_idades / len(grupo)

for pessoa in grupo:
    if pessoa["idade"] >= media:
        idades_maiores_que_media.append(pessoa["nome"])


print("=-" * 10)
print(f"total de pessoas cadastradas: {len(grupo)}")
print(f"A media de todas idades é igual a {media}")
print(f"A lista com todas a mulheres é {mulheres}")
print(f"A lista com as pessoas com a idade maiores que a media de idades é {idades_maiores_que_media}")
print("=-" * 10)