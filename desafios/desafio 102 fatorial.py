

def fatorial(num, show=True):
    if show:
        print("== PROCEDIMENTO DO CALCULO DE FATORIAL ==")
        fat = 1
        for i in range(num , 0 , -1):
            if i == 1:
                print(f"{i} = {fat}")
            else:
                print(f"{i} x ", end="")
            fat *= i
    
    else:
        print("-- fatorial --")
        fat = 1
        for i in range(num , 0 , -1):
            fat *= i
        print(f"O fatorial de {num} = {fat}")
    return fat


fatorial(5)
fatorial(8, show=False)