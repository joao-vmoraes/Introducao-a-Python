# de metros para centimetros
n1 = float(input('unidade de metro que deseja converter:'))
c = float(n1 * 100)
m = float(c * 10)
print('\033[31;1m{}\033[m metros é igual a \033[1;31m{:.2f}\033[m centimetros ou \033[1;31m{:.2f}\033[m milimetros'.format(n1, c, m))