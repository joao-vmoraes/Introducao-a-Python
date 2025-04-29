#perguntando o sexo da pessoa
print('-=' * 20)
sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = input('ERRO: sexo inválido. Digite novamente: ').strip().upper()
