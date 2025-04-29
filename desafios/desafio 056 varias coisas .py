nomes_masculinos = []
sexo_masculino = []
sexo_feminino = []
nomes_femininos = []
idades_masculinas = []
idades_femininas = []
idades = []
menores_de_20 = 0

for i in range(1,5):
    print(f'{i}ª pessoa')
    print('-=-=-===-=-==-=')

    sexo = input(f' sexo da {i} pessoa. [F/M]: ').lower().strip() #loop para sexos invalidos
    while sexo != 'f' and sexo != 'm':
        sexo = input('ERRO: Sexo inválido! Tente novamente: ')

    nome = input(f' nome da {i} pessoa: ') #adicionando os nomes em uma lista
    idade = int(input(f' idade da {i} pessoa: ')) #adicionando as idades na lista de idades

    if sexo == 'm': #se o nome for masculino ele ira para os dados masculinos
        nomes_masculinos += [nome]
        sexo_masculino += [sexo]
        idades_masculinas += [idade]
        idades += [idade]

    elif sexo == 'f': #se o nome for feminino ele ira para os dados femininos
        nomes_femininos += [nome]
        sexo_feminino += [sexo]
        idades_femininas += [idade]
        idades += [idade]
        if idade < 20:
            menores_de_20 += 1

media = (idades[0] + idades[1] + idades[2] + idades[3] ) / 4
print(f'a média das idades foi : {media}')

print(f'o homem com a maior idade é {nomes_masculinos[len(max(str(idades_masculinas)))]} . ')

print(f'existem {menores_de_20} mulheres menores de 20 anos.')