#perguntando a massa e altura da pessoa
massa = float(input('Qual a sua massa em KG?: '))
altura = float(input('Qual a sua altura em metros?: '))

#massa e altura nao podem ser negativas
while altura < 0 or massa < 0:
    print('Altura ou Massa inválida, digite novamente.')
    massa = float(input('Qual a sua massa em KG?: '))
    altura = float(input('Qual a sua altura em metros?: '))

#formula do imc:
imc = massa / altura * 2

#imc:
# menor que 18,5 = magreza
#entre 18,5 e 24,9 = normal
#entre 25 e 29,9 = sobrepeso
#entre 30 e 39,9 = obesidade
#igual ou maior que 40 = obesidade grave

if imc < 18.5:
    print('IMC : Magreza')
elif 18.5 <= imc <= 24.9:
    print('IMC : Normal')
elif 25 <= imc <= 29.9:
    print('IMC : Sobrepeso')
elif 30 <= imc <= 40:
    print('IMC : Obesidade')
else:
    print('IMC : Obesidade Grave')

