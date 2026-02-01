class Multiplicar:
    def __init__(self, func):
        self.func = func
        print("INIT")

    def __call__(self, *args, **kwds):
        print(args, kwds)
        return self.func(*args, **kwds)

@Multiplicar
def soma(x , y):
    return x + y

dois = soma(2 , 2)
print(dois)