from math import fabs

def contar(inicio, fim, passo):
    if passo == 0:
        print("Erro: A contagem não é possível com passo zero.")
        return

    if inicio > fim and passo > 0:
        passo *= -1
    elif inicio < fim and passo < 0:
        passo *= -1

    print("---")
    print(f"Contagem de {inicio} até {fim} com intervalo de {int(fabs(passo))}:")
    
    if inicio > fim:
        for i in range(inicio, fim - 1, passo):
            print(f"{i}", end=" ")
    elif inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f"{i}", end=" ")
    else:
        print(inicio)
    
    print("\n---")


print("~" * 20)
print("INICIO DA CONTAGEM")
print("~" * 20)

inicio = int(input("Digite o início da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o intervalo: "))
contar(inicio, fim, passo)
