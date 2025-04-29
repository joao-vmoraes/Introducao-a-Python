#permutar uma lista de alunos
import random
alunos = ['joao', 'pedro', 'henrique', 'clara']
random.shuffle(alunos)
sorteados = ','.join(alunos)
print('A nova lista é : \033[32;1m',sorteados , '\033[m')