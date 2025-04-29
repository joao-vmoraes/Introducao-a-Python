#escolhendo os termos e contadores
a1 = int(input('Escolha o primeiro termo: '))
razao = int(input('Escolha a razao: '))
termo = a1
count = 1

#primeira progressao
while count <= 10:
    print(termo , end=' -> ')
    termo += razao
    count += 1

#perguntando a quantidade de termos adicionais
quantidade = int(input('Quer adicionar mais quantos termos? ')) 

while quantidade > 0:

    for i in range(quantidade): 
        print(termo, end=' -> ')
        termo += razao
        count += 1
    
    quantidade = int(input('Quer adicionar mais quantos termos? '))
