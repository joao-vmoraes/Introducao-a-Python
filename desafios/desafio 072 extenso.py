tupla = ('zero' , 'um' , 'dois', 'Tres' ,'quatro' ,
        'cinco' ,'seis' ,'sete' ,'oito' ,'nove' ,'dez'
)
numero = int(input('Digite um número de 0 até 10: '))

while True:
    while numero < 0 or numero > 10:
        numero = int(input('Digite um número de 0 até 10: '))
    print(f'Você digitou o número: {tupla[numero].title()}')

    continuar = int(input('Voce quer continuar? [1 = Sim / 2 = Não]'))

    if continuar != 1:
        break