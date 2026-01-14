#montando uma calculadora de uma função do segundo grau que mostra o delta e as raizes da equação
#ax² + bx + c

a = float(input('Me diga qual o número que corresponde o A da função de segundo grau: '))
b = float(input('Agora o que corresponde o B da função do segundo grau:' ))
c = float(input('Agora o que corresponde o C da função do segundo grau: '))
d = b**2-4*a*c
x1 = (-b + d**0.5)/2 * a
x2 = (-b - d**0.5)/2 * a

if d < 0:
    print('Essa equação nao possui raizes reais')
elif d == 0:
    print('Essa equação só possui uma raiz: x=',x1)
else:
    print('Essa equação possui duas raizes: x={:.2f} e x={:.2f}'.format(x1, x2))    
