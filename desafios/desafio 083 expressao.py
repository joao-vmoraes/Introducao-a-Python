expressao = input('Digite a sua expressao:\033[32m')
print('\033[m-' * 30)
parenteses_abertos = expressao.count('(')
parenteses_fechados = expressao.count(')')

if parenteses_abertos != parenteses_fechados:
    print(f'A expressão nao existe!')
else:
    print('A expressão existe!')