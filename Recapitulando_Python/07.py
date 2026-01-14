numero = int(input('Digite um número de 0 até 999: ')) 

while (numero > 999) or (numero < 0):
    numero = int(input('Digite um número válido: ')) 

numero = str(numero + 1000)

print(f'Unidade = {numero[3]}') 
print(f'Dezena = {numero[2]}') 
print(f'Centena = {numero[1]}') 