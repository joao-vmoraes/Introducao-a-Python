frase = str(input('Fale uma frase: ')).strip().lower()
totala = frase.count('a')
primeira = int(frase.find('a')) + 1
ultima = int(frase.rfind('a')) + 1
print('Na sua frase existem: {} letras A\nA primeira apareceu na posição: {}\nA ultima apareceu na posiçao: {}'.format(totala, primeira, ultima))