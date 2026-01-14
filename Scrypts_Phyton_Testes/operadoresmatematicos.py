#temos no python alguns operadodes matematicos que seguem a mesma regra de procedencia da mtematica base.
#para somar use +, para subtrair use -, para multiplicar use *, para dividir use /, para potência use **, para divisão inteira use //, para divissao de resto use %
n1 = int(input('escolha um número:'))
n2 = int(input('escolha mais um:'))
add = n1 + n2
sub = n1 - n2
mu = n1 * n2
div = n1 / n2
pot = n1 ** n2
divin = n1 // n2
rest = n1 % n2
print('a soma entre {} e {} da {}'.format(n1,n2,add))
print('a subtração entre {} e {} da {}'.format(n1,n2,sub))
print('a multiplicação entre {} e {} da {}'.format(n1,n2,mu))
print('a divisão entre {} e {} da {:.3f}'.format(n1,n2,div))
print('{} elevado a {} da {}'.format(n1,n2,pot))
print('a divisão inteira entre {} e {} da {}'.format(n1,n2,divin))
print('o resto da divisão entre {} e {} da {}'.format(n1,n2,rest))
input('aperte enter para sair')
