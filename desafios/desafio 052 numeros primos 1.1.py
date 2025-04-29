count = 0 #contador de vezes que o numero foi dividido

numero = int(input('Digite um número: ')) #perguntando um número

for i in range(1 , numero + 1):#indo de 1 ate o número
    if numero % i == 0:     #se o resto da divisao do numero por i for igual a zero é poruqe ele foi diidido por i.
        print('\033[1;32m' ,i, '\033[m' ,end=' ' )# cor verde, imprimindo o numero, voltando ao normal, e juntando as linhas
        count += 1
    else:
        print( i ,end=' ')

#se o contador for maior que 2 é por que o numero foi dividido por 1, por ele mesmo e mais numeros,ou seja, nao é primo!
if count == 2:
    print(f'o número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')