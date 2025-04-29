#programa que pede dias alugados + km rodados = total a pagar
d = int(input('quntos dias o carro foi alugado? '))
km = int(input('quantos kms o carro rodou? '))
vt = (d * 60) + (km * 0.15)
print('o valor total a ser pago pelos \033[4;34m{}\033[m dias rodados e \033[4;34m{}km\033[m rodados é \033[32;1mR${:.2f}\033[m .'.format(d, km ,vt))