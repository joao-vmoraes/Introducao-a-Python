n1 = int(input('escolha um numero:'))
n2 = int(input('escolha outro número:'))
s = n1 + n2
normal = '\033[m'
azul = '\033[34m'
print('a soma entre {0}{1}{4} e {0}{2}{4} é {5}{3}{4}'.format(azul,n1, n2, s,normal,('\033[1;34m')))