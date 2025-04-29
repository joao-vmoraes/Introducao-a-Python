#frase palindroma
frase = str(input('me fale uma algo: ')).strip().upper()

#juntar as palavras
frase_junta =  ''.join(frase.split())

#o inverso:
inverso = ''

#invertendo as letras
for letras in range(len(frase_junta) -1 , -1 , -1):
    inverso += frase_junta[letras]

print(f'O inverso da palavra {frase_junta} é {inverso}')

if frase_junta == inverso:
    print('\033[32;1mÉ palindromo!\033[m')
else:
    print('não é palindromo!')

#UMA OUTRA FORMA SEM UTILIZAR O FOR É:
inverso = frase[::-1]

