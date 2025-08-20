jogador = dict()
gols = []
soma = 0

jogador["nome"] = input("Digite o nome do jogador: ")
jogador["partidas"] = int(input("Digite a quantidade de partidas jogadas: "))

for i in range(jogador["partidas"]):
    gols_partida = int(input(f"Quantidade de gols na {i + 1} partida: "))
    soma += gols_partida
    gols.append(gols_partida)

jogador["gols"] = gols[:]
jogador["tot_gols"] = soma

print("=-" * 20)
for k in range(jogador["partidas"]):
    print(f" => {jogador["nome"]} fez {jogador["gols"][k]} gols na {k + 1}° partida")

aproveitamento = soma / jogador["partidas"]

print(f"tendo assim um total de {soma} gols em {jogador["partidas"]} partidas, tendo um aproveitamento de {aproveitamento} gols por partida")