palavras = ("gato", "montanha", "estrela", "código", "aventura", "lua", "oceano", "dragão")

for palavra in palavras:
    print(f'\n{palavra + ' Tem de vogais: ' :->35} ' , end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra , end='')