p = float(input('Qual o preço do produto?'))
n = 95/100 * p
print('o novo valor com 5% de desconto sera \033[32;1mR${:.2f}\033[m'.format(n))