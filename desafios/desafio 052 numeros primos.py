#perguntando um número
numero = int(input('Digite um número: '))

while numero < 2: #loop ate digitar um numero maior que 1
    print('ERRO: opção inválida.')
    numero = int(input('Digite novamente: '))

primo = True#começando dizendo que o numero é primo

for n in range(2, numero ) : #dividir por todos os numeros
    if numero % n == 0:#se o resto da divisao for 0 por algum numero ele nao é primo
        primo = False
        break

if primo == False:
    print('o número não é primo')
else:
    print('O número é primo')