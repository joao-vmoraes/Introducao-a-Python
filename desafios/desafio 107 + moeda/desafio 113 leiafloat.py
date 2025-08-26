def leiaint():

    while True:
        try:
            algo = int(input("Digite um numero inteiro: "))
            return algo
        except:
            print("Houve um erro de tipo de dado.")


def leiafloat():
    while True:
        try:
            algo = float(input("Digite um numero: "))
            return algo
        except:
            print("Houve um erro de tipo de dado.")



numero1 = leiaint()
numero2 = leiafloat()
print(f"O numero {numero1} é inteiro e {numero2} é float")
