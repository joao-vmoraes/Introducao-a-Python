soma = 0 #acumulador
count = 0 #contador

for N in range(3 , 500, 6): #escolhendo os numeros
    soma += N#somando o antigo valor da soma com o novo numero N
    count += 1

print(soma)