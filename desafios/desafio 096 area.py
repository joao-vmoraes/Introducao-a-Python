def area(l,c):
    a = l * c
    print(f"A area de um terreno {l:.2f} x {c:.2f} é de {a:.2f} m2")

l = int(input("digite a largura do terreno >>> "))
c = int(input("Digite o comprimento do terreno >>> "))
area(l , c)