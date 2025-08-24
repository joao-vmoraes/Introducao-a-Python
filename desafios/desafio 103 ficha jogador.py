def listar(gols = 0 , nome="<desconhecido>" ):
    return print(f"O jogador {nome} fez um total de {gols} gols no campeonato.")

    
nome = input("Digite o nome do jogador: ")
gols = input("Digite a quantidade de gols do jogador: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


if nome.strip() == "":
    listar(gols)
else:
    listar(gols, nome)