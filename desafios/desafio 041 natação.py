#pereguntando a idade
idade = int(input('Qual a sua idade: '))
a = 'Voce é da categoria: '
while idade < 0:
    idade = int(input('Qual a sua idade: '))

if idade < 9:
    print(a,'mirim')
elif idade < 14:
    print(a,'mirim')
elif idade < 19:
    print(a, 'junior')
elif idade == 20:
    print(a, 'senior')
else:
    print(a, 'mestre')
    
