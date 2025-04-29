#de real para dollar
print('\033[33m-=\033[m' * 30)
r = float(input('Me diga a quantidade de R$ que voce tem que eu converto para Dollar:'))
print('\033[33m-=\033[m' * 10)
d = r / 6.7
print('com \033[32;1mR${}\033[m você possui\033[32;1m${:.2f}\033[m'.format(r, d))
print('\033[33m-=\033[m' * 30)

