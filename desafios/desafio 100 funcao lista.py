import random
numeros = list(range(0,50))
sorteados = []

def sorteia(list):
    sorteados = random.sample(numeros, 5)
    print(f"A lista sorteada da outra lista foi {sorteados}")
    return sorteados

def soma_par(list):
    soma= 0
    for i in list:
        if i % 2 == 0:
            soma += i
    print(f"A soma de todos os pares contidos em {list} é : {soma}")



soma_par(sorteia(numeros))

