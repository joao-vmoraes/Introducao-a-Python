#ask the name and the price for each undefined products
counter = 0
preço_mais_barato = 0
nome_mais_barato = 0
total = 0
mais_de_1000 = 0

while True:
    print('==' * 20)
    print(f'{'Mercadinho De Hobber' :^40}' )
    print('==' * 20)
    nome = str(input('Digite  nome do produto: '))
    preço = float(input('DIgite o preço do produto: R$'))
    counter += 1

    if counter == 1 or preço < preço_mais_barato :
        preço_mais_barato = preço
        nome_mais_barato = nome
    
    if preço > 999:
        mais_de_1000 += 1
    
    total += preço
    
    continuar = int(input('Deseja continuar: [1 = Sim  /  2 = Não] : '))
    if continuar == 2:
        break

print('----------------------------')
print(f'O total deu : R${total :.2f}')
print(f'Existem {mais_de_1000} produtos mais de R$1000,00')
print(f'E o produto mais barato foi : {nome_mais_barato} , que custa R${preço_mais_barato :.2f}')
print('--------------- FIM DO PROGRAMA -----------------')