#programa de media de um aluno
n1 = float(input('qual foi a nota da sua primeira prova:'))
n2 = float(input('qual foi a nota da sua segunda prova:'))
n3 = float(input('qual foi a nota da sua terceira prova:'))
m = (n1 + n2 + n3)/3
print('sua média foi \033[7m{:.2f}\033[m.'.format(m))