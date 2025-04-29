a1 = 0
a2 = 1
a3 = a1 + a2
count = 0

quant = int(input('Quantos termos você quer ? '))

if quant <= 1:
    print(a1)

else:
    while count != quant:
        print(a1 , end='  ')
        a1 = a2
        a2 = a3
        a3 = a2 + a1
        count += 1
print('FIM')