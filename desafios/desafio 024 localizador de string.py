#programa que verifica se uma cidade começa com a palavra SANTO
cidade = input('Escolha o nome da cidade e eu direi se começa com SANTO ou nao: ')
split = cidade.upper().split()
print('SANTO' in split[0] )
