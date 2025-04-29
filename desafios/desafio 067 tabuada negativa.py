#parar a tabuada quando o número for negativo
numero = 1

while True:
    numero = int(input('Digite um número : '))

    if numero >= 0:  #if number >= 0 the program will continue
        for i in range(1,11):
            print(f'{numero :>} X {i :>2} = {numero * i :>3}')
    
    else:
        break

print('Até logo!')