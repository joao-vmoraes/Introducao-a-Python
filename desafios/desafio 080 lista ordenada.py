#digitar 5 valores
lista = []
contador = 1
for _ in range(5):
    n = int(input('Digite um valor: '))

    if contador == 1:
        lista.append(n)
        contador += 1

    else:
        for elemento in lista:
            if n < elemento:
                lista.insert([elemento], n)

print(lista)