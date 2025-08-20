jogador = dict()
gols = []
soma_gols = 0
jogadores = []
contador = -1
buscar = 1

while True: 
    contador += 1
    jogador["nome"] = input("Digite o nome do jogador: ")
    jogador["partidas"] = int(input("Digite a quantidade de partidas jogadas: "))

    for i in range(jogador["partidas"]):
        gols_partida = int(input(f"Quantidade de gols na {i + 1} partida: "))
        soma_gols += gols_partida
        gols.append(gols_partida)

    jogador["gols"] = gols[:]
    jogador["tot_gols"] = soma_gols
    jogador["aproveitamento"] = soma_gols / jogador["partidas"]
    jogador["cod"] = contador

    jogadores.append(jogador.copy())
    soma_gols = 0
    gols.clear()

    continuar = int(input("Deseja adicionar mais alguem? [1 - sim / 0 - nao]"))
    if continuar == 0:
        break

print(f"Cod   Nome               partidas     gols")
print(f"=-" * 20)
for jogador in jogadores:
    print(f"{jogador["cod"]}     {jogador["nome"]:20} {jogador["partidas"]}            {jogador["tot_gols"]}")

while buscar != 999:
    print("-=" * 20)
    buscar = int(input("Qual jogador voce quer ter uma visao detalhada, digite o codigo dele [999 para sair] >>>"))
    if buscar == 999:
        break

    for i in range(jogadores[buscar]["partidas"]):
        print(f"Na {i + 1}° partida o jogador {jogadores[buscar]["nome"]} fez {jogadores[buscar]["gols"][i]} gols")

print("Até logo! Programa encerrado.")


