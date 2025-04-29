#programa que com os catetos mostre a hipotenusa
from math import hypot
b = float(input('Digite um cateto: '))
c = float(input('Digite o outro cateto: '))
a  = hypot(b,c)
print('O valor da hipotenusa é \033[34;1m{:.2f}\033[m.'.format(a))
