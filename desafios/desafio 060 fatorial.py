#aplicativo de fatorial usando o while


#perguntando o numero do fatorial
print('-=' * 20)
numero_escolhido = int(input('Escolha um número para o fátorial: '))
print('-=' * 20)

resultado = numero_escolhido
numero = int(numero_escolhido - 1) #escolhendo o primeiro numero a multiplicar o numero escolhido

#enquanto que o inicio for != 0 continuar multiplicando por n e diminuindo em 1
while numero != 0:
    resultado = resultado * numero
    numero -= 1

print(f'O fatorial de {numero_escolhido} é : {resultado}')