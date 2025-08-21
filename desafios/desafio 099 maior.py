def maior(*num):
    for i in num:
        if i == num[0]:
            maior = i
        elif i > maior:
            maior = i

    print("~" * 10)
    print(f"Foram passados {len(num)} numeros")
    print(f"os numeros foram: {num}")
    print(f"e o maior valor foi {maior}")

maior(2,4,6,7)
maior(4,6,1,3,99,100,2,34,54)