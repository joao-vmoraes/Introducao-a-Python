r1 = int(input('Qual o tamanho da primeira reta? '))
r2 = int(input('Qual o tamanho da segunda reta? '))
r3 = int(input('Qual o tamanho da terceira reta? '))
retas = [r1, r2, r3]

if max(retas) == r1:
    if (r1 > r2 + r3):
        print('Esse triangulo nao existe')
    else:
        print('Esse triangulo existe')    
if max(retas) == r2:
    if (r2 > r1 + r3):
        print('Esse triangulo nao existe')
    else:
        print('Esse triangulo existe')    
if max(retas) == r3:
    if (r3 > r1 + r2):
        print('esse triangulo nao existe')
    else:
        print('Esse triangulo existe') 
print('Foi um prazer ajudar!')  


#FORMA MAIS SIMPLES POSSIVEL:
print('-------------------------------')
if (r1>= r2 + r3) or (r2 > r1 + r3) or (r3 > r1 +r2):
    print('Esse triangulo nao existe')
else:
    print('esse triangulo existe')
