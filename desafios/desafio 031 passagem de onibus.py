#viagens de ate 200km sera pago 0,50 por KM e viagens de 200+KM sera pago 40 por KM

km = float(int(input('Qual a distancia que sera percorrida na sua viagem: ')))

if km <= 200:
    print('o valor da passagem ficou R$', km * 0.5)

else:
    print('O valor da passagem ficou R$', km * 0.4)
print('Pague e venha conosco nessa jornada incrivel!')
