alunos = []

def Cadastro():
    print("-- Cadastro de Aluno --")
    nome = input(("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome , nota1, nota2 , media])

def Media_alunos():
    contador = 1
    print("-- Alunos --")
    for aluno in alunos:
        print(f"Codigo: {contador} - Nome: {aluno[0]:20}  - Media: {aluno[3]}")
        contador += 1

def Notas_aluno():
    print("-- Nota do Aluno --")
    print("Digite o codigo do aluno")
    codigo = int(input(">>> "))
    contador = 1
    achado = 0
    for aluno in alunos:
        if codigo == contador:
            print(f"Notas de :{aluno[0]}  -- 1 Nota: {aluno[1]}  -- 2 Nota: {aluno[2]}  -- Media : {aluno[3]}")
            achado = 1
            break
        contador += 1
    if achado == 0:
        print(f"O Aluno de Codigo {codigo} nao existe")

while True:
    print("=======================")
    print("Gerenciamento de Notas")
    print("[1] Cadastrar aluno")
    print("[2] Ver media dos alunos")
    print("[3] Ver notas do aluno")
    print("[4] Sair")

    escolha = input(">>> ")
    try:
        escolha = int(escolha)
    except:
        escolha = 0

    if escolha == 1:
        Cadastro()
    elif escolha == 2:
        Media_alunos()
    elif escolha == 3:
        Notas_aluno()
    elif escolha == 4:
        break
    else:
        print("Opcao Invalida")

print("Programa Encerrado! Ate logo. ")