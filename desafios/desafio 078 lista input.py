lista = []
for e in range(5):
    n = int(input(f'Digite o {e}°  valor: '))
    lista.append(n)
print(f'O maior valor foi: {max(lista)} e ele esta na posição de múmero: { lista.index(max(lista)) + 1}° ')
print(f'O menor valor foi: {min(lista)} e ele esta na posição de número: {lista.index(min(lista)) + 1}° ')