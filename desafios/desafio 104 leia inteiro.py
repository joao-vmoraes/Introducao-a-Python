def leiaint(algo):

    while not algo.isnumeric():
        algo = input("Digite um numero valido: ")
    return int(algo)


numero = leiaint("a")
print(f"O numero {numero} é inteiro")
