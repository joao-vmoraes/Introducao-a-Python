nome = input('Qual é o seu nome? ')
splitado = nome.split()
n1 = splitado[0]
n2 = splitado[len (splitado) - 1]
print('Prazer {}!'.format(nome))
print('Seu primeiro nome é {}'.format(n1))
print('E seu ultimo nome é ', n2)
