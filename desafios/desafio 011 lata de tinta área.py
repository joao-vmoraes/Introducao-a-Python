#crie um programa que calcula a area de uma parede e quantos baldes de tinta sao necessarios para pintar essa parede sabendo que uma lata de tinta de 3,6 L consegue pintar aproximadamente 12m²
from math import ceil
#perguntar para o cliente a largura e comprimento da parede
l = float(input('Qual a \033[34mlargura\033[m da sua parede em \033[34mMetros\033[m?'))
c = float(input('qual o \033[34mcomprimento\033[m da sua parede em \033[34mMetros\033[m?'))
a = l * c
t = a / 12
li = t * 3.6
print('-=-' * 15)
print('{:.1f} \033[31mlatas de tintas\033[m de 3,6 Litros, ou \033[31m{:.2f}\033[m Litros de tinta'.format(ceil(t), li))