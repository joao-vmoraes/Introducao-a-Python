#monte um programa que leia um número inteiro e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('digite um número para eu dar o seu dobro, triplo e raiz quadrada:'))
d = int(n1 * 2)
t = int(n1 * 3)
r = n1 ** 0.5
print('o dobro de \033[32;1m{}\033[m é {} \no triplo de \033[32;1m{}\033[m é {}\n a raiz quadrada de \033[32;1m{}\033[m é {}'.format(n1,d,n1,t,n1,r) )