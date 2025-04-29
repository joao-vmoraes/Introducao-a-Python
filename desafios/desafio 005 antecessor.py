#faça um programa que leia um numero inteiro e diga o seu antecessor e o seu sucessor
n1 = int(input('Digite um número que eu direi o sucessor e o antecessor:'))
su = int(n1 + 1)
an = int(n1 - 1)
print('o antecessor de \033[34;1m{}\033[m é \033[31;1m{}\033[m \no sucessor de \033[34;1m{}\033[m é \033[32;1m{}\033[m'.format(n1, an, n1, su))