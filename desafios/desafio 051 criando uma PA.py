#perguntando o primeiro termo e a razao:
print('-=' * 20)
a1 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite o valor da razao: '))
progressao = [] # deixando a progressao vazia

#desenvolver a progressao:
for n in range (a1, a1 + 10 * razao, razao):
    progressao += [n]
print(f'A sua PA ficou assim: {progressao}')