# se a velocidade do carro passar de 60KM/h o cara vai pagar R$40,00 por cada km a mais

#perguntar pra pessoa a velocidade do carro
velocidade = float(int(input('Qual foi a velocidade que apareceu no radar: ')))

if velocidade > 60:
    print('O valor da multa foi de R$', (velocidade - 60) * 40)
else:
    print('Não há multa nesta velocidade, obrigado pelo atendimento')  
print('retorne sempre!')      