soma = 0 #definindo a soma inicial

for N in range(6):
    N = int(input('Escolha um número: '))#perguntando um número 6 vezes
    
    if N % 2 == 0:#se o numero for par
        soma += N# o novo valor da soma sera o antigo valor + N

print(soma)