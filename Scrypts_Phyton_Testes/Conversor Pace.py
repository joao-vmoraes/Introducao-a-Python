continuar = 1

while continuar == 1:
    print("========== Conversor de Velocidade/Distancia ==========")
    print("[1] Calcular Km/H baseado em Pace")
    print("[2] Calcular Pace baseado em Km/H")
    print("[3] Sair")
    opcao = int(input(">>> "))

    if opcao == 1:
        print("-----------------------------------")
        print("-- Calcular Km/H baseado em Pace --")
        print("Digite o seu Pace: ")
        pace = float(input(">>> "))
        velocidade = 60 / pace
        print(f"-- Velocidade = {velocidade:.2f} Km/H --")

    elif opcao == 2:
        print("-----------------------------------")
        print("-- Calcular Pace baseado em Km/H --")
        print("Digite a sua velocidade: ")
        velocidade = float(input(">>> "))
        pace = 60 / velocidade
        print(f"-- Pace = {pace:.2f} Min/Km --")

    elif opcao == 3:
        break