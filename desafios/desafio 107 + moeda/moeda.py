def dobrar(n):
    return 2 * n

def metade(n):
    return n / 2

def aumento(n, t):
    return n * (1 + t / 100)

def desconto(n , t):
    return n * (1 - t / 100)

def titulo(msg):
    print("=-" * 15)
    print(f"  {msg}")
    print("=-" * 15)

def resumo(v , a , d):
    titulo(f"{"Resumo Valor":^26}")
    print(f"O dobro de R${v} é R${dobrar(v):.2f}")
    print(f"A metade de R${v} é R${metade(v):.2f}")
    print(f"Um desconto de {d}% em R${v} é R${desconto(v , d):.2f}")
    print(f"Um aumento de {a}% em R${v} é R${aumento(v , a):.2f}")
    print("=-" * 15)