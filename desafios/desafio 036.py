#emprestimo bancario,o programa vai perguntar o valor da casa, o salario do comprador e quantos meses ele vai pagar,o valor mensal nao pode passar de 30%, e que o valor total do emprestimo é 20% a mais que o valor da casa.
import math

#perguntas para o comprador

casa = float(input('Qual o valor do emprestimo que voce quer? R$'))
salario = float(input('Agora digite o seu salário: R$'))
emprestimo_total = casa * 1.2
valor_max = salario * 0.3
meses_min = math.ceil(emprestimo_total / valor_max)

meses = int(input('De acordo com seu salário e o valor todal do emprestimo, a quntidade mínima de meses que você pode escolher é de {} meses. Escolha a quantidade de meses que você quer parcelar: '.format(meses_min)))

valor_mensal = emprestimo_total / meses

while meses < meses_min:   
    if meses < meses_min:
        print('Você nao pode fazer um emprestimo com essa quantidade de meses, por favor escolha um minimo de {} meses'.format(meses_min))
        meses = int(input('Escolha a quantidade de meses: '))
print('Está tudo certo! O valor mensal ficou de R${:.2f} ,levando em vista os 20% de juros no emprestimo!'.format(valor_mensal))
