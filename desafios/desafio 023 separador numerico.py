#crie um programa que separe as unidades dezenas centenas e milhar de um numero
numero = str(10000 + int(input('Escolha um número de 0 a 9999: ')))
milhar = numero[1]
centena = numero[2]
dezena = numero[3]
unidade = numero[4]
print('o número {} possui como:\nAlgarismo da Milhar: \033[32m{}\033[m\n Algarismo da centena: \033[32m{}\033[m\nAlgarismo da Dezena: \033[32m{}\033[m\nAlgarismo da Unidade: \033[32m{}\033[m'.format(numero, milhar, centena, dezena, unidade))

