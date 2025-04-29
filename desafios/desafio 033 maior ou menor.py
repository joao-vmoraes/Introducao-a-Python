#programa que leia 3 numeros e diga qual o menor e qual o maior
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha o segundo número: '))
n3 = int(input('Escolha o terceiro numero: '))
if (n1 > n2 > n3):
    print('{} é o maior número e o menor é {}'.format(n1, n3))
elif (n1 > n3 > n2):
    print('{} é o maior número e o menor é {}'.format(n1, n2))
elif (n2 > n3 > n1):
    print('{} é o maior número e o menor é {}'.format(n2 , n1))
elif (n2 > n1 > n3):
    print('{} é o maior número e {} é o menor'.format(n2, n3)) 
elif (n3 > n2 > n1):
    print('{} é o maior número e {} é o menor'.format(n3, n1))
else:
    print('{} é o maior número e {} é o menor'.format(n3 , n2))   
print('Foi um prazer fazer essa análise!')                    