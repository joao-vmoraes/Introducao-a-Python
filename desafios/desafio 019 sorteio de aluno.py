#sorteio de 4 alunos
import random
aluno1 = input('Diga o nome de um aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1 , aluno2, aluno3, aluno4]
print('o aluno escolhido foi: \033[31;1m{}\033[m'.format(random.choice(lista)))