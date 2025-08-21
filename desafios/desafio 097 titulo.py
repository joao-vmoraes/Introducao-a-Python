def escreva(msg):
    print("~" * len(msg))
    print(f"{msg:^3}")
    print("~" * len(msg))


mensagem = input("Escreva algo: ")
escreva(mensagem)