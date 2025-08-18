import random
jogo_unico = []
jogos = []
posicao = 1

while True:
    print("=== GERADOR MEGA SENA ===")
    print("[1] Gerar Jogo ")
    print("[2] Ver Jogo")
    print("[3] Sair")
    escolha = str(input(">>> "))

    if escolha == "1":
        print(f"Gerando o jogo de posição {posicao}° ...")
        posicao += 1
        jogo_unico = random.sample(range(1,61) , 6)
        jogos.append(sorted(jogo_unico[:]))
        jogo_unico.clear()

    elif escolha == "2":
        jogo_selecionado = int(input("Digite a posição do jogo que voce quer ver >>> "))

        try:
            print(f"=== JOGO DE POSICAO  {jogo_selecionado}° :   {jogos[jogo_selecionado - 1]}")
        except:
            print("ERRO: O jogo selecionado ainda nao existe")

    else:
        print("Ate logo!")
        break