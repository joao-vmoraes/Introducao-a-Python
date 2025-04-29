#programa que le um nome e manda o mesmo nome com as letras maiucuals, o nome com todas minusculas,quantas letras ao todo sem esaços, e auqntas letras tem o primeiro nome
nome = input('Digite o seu nome: ')
nomemaiusculo = nome.upper()
nomeminusculo = nome.lower()
caracteres = len(''.join(nome.split()))
primeiro = nome.split()
primeironome = len(primeiro[0])
print('''seu nome maiúsculo é: {}
        seu nome minusculo é: {}
        seu nome possui: {} letras
        seu primeiro nome possui: {} letras'''.format(nomemaiusculo, nomeminusculo, caracteres, primeironome))


