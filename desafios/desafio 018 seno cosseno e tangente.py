#programa que recebe o valor de ummangulo e devolve o valor do seu seno cosseno e tangente em radiano e em grau

#digite o angulo
import math
angulo = float(input('Digite o angulo em graus: '))
radiano = math.radians(angulo)
print('o valor do seno de {}° é \033[32m{:.2f}\033[m\nO cosseno é \033[32m{:.2f}\033[m\nA tangente é \033[32m{:.2f}\033[m \nE seu valor em radiano é\033[32m{:.2f}\033[m'.format(angulo, math.sin(radiano), math.cos(radiano), math.tan(radiano), radiano))


