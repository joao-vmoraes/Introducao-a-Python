class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome , f"esta chamando {self.phone} ")

c1 = CallMe('23123123131')
c1('Luiz Otavio')