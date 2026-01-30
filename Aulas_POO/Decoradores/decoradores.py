def adiciona_repr(cls):
    def criar_repr(self):
        class_name = type(self).__name__
        class_dict = self.__dict__
        return f'{class_name}({class_dict})'
    cls.__repr__ = criar_repr
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time("Brasil")
portugal = Time("portugal")

terra = Planeta('Terra')
jupiter = Planeta('jupiter')

print(jupiter)
print(terra)
print(brasil)
print(portugal)