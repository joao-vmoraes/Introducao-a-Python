class A:
    def quem_sou(self):
        print("Sou A")

class B(A):
    def quem_sou(self):
        print("Sou B")

class C(A):
    def quem_sou(self):
        print("Sou C")

class D(B, C):
    ...

d = D()
d.quem_sou()
print(D.mro())