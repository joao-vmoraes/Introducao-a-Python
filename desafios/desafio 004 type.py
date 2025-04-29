#crie um aplicativo que mostre seu tipo primitivo e todas as informações
a = input('digite algo:')
t = type(a)
n = a.isnumeric()
l = a.isalpha()
nl = a.isalnum ()
print('\033[35;1m{}\033[m é do tipo:{}, é um número:{}, é uma letra:{}, é alfanumérico:{}'.format(a , t, n, l, nl))
