#salarios inferiores a 1250 aumentarao em 15%, e superiores em 10%
s = int(input('qual é o seu salario? R$'))


if s <= 1250:
    print('Seu novo salário sera R$', int(s * 1.15))
else:
    print('Seu novo salário sera R$', int(s * 1.10 ))