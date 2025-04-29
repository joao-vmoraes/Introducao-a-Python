#perguntar as notas n1 e n2
n1 = float(input('Qual foi a sua nota na prova 1: '))
n2 = float(input('Qual foi a nota na prova 2: '))

#calculando a media
m = (n1 + n2) / 2

#mostrando na tela
if m >= 7:
    print('Sua média foi {:.2f} .Você foi aprovado!'.format(m))
elif (5.5 <= m < 7):
    print('Sua média foi {:.2f} .Voce ficou de recuperação!'.format(m))
else:
    print('Sua média foi {:.2f} .Você foi reprovado!'.format(m))