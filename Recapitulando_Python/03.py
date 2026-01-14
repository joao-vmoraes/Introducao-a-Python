import math
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundio número: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
exp = math.pow(n1 , n2)
raiz1 =  math.sqrt(n1)
raiz2 = math.sqrt(n2)
print(f'a soma é {soma :.2f}, asubtração é {sub:.2f}, a multiplicação é {mult:.2f}, a exponenciação é {exp:.2f}, a raiz de {n1:.2f} é {raiz1:.2f} e a raiz de {n2:.2f} é {raiz2:.2f}')