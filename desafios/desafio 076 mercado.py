produtos = ('Caderno' , 35, 'Caneta', 2, 'Bola de futebol', 20, 'Mouse', 25, 'Guitarra', 1200)
print('==' * 20)
print(F'{'LISTAGEM DE PREÇOS' :^40}')
print('==' * 20)
contador = 1

for _ in produtos[::2]:
    print(f'{ _ :.<35} R$ {produtos[contador] :>8,.2f}')
    contador += 2