from time import sleep
import os
import datetime

def linha(tam=40):
    print("\033[35m=\033[m" * tam)

def sair_programa():
    cabecalho("Até mais!")
    sleep(2)

def cabecalho(frase):
    #usado para criar cabeçalhos com alguma frase, com 40 caracteres de alinhamento
    linha()
    print(f"\033[34m{frase:^40}\033[m")
    linha()

def menu_principal(list):
    c = 1
    cabecalho("Menu de Gerenciamento de Treinos")
    for i in list:
        print(f"{c} - {i}")
        c += 1
    linha()
    while True:
        try:
            resposta = int(input("Digite a opção >>> "))
            return resposta
        except:
            print("ERRO: Tipo de dado enviado não válido.")
            sleep(2)

def listar_treinos(list):
    cabecalho("Lista de Treinos")
    caminho = 'mini_sistema/treinos/treinos.txt'
    c = 1

    try:
        with open(caminho , "r" , encoding='utf-8') as arquivo:

            treinos = arquivo.readlines()
            for treino in treinos:
                print(f"\033[31m{c}\033[m - {treino.strip()}") #usando o metodo strip para nao imrimir uma linha vazia por causa do \n
                c += 1
                
        while True:
            try:
                resposta = int(input("Digite a opção >>> "))
                sleep(1)
                return resposta
            except:
                print("ERRO: Tipo de dado enviado não válido.")
                sleep(2)
                break

    except:
        print("Voce ainda nao cadastrou nenhum treino.")
        sleep(2)



def escolher_treino():
    while True:
        try:
            resposta = int(input("Digite a opção >>> "))
            sleep(1)
            return resposta
        except:
            print("ERRO: Tipo de dado enviado não válido.")
            sleep(2)
            break

def adicionar_treino(lista):
    caminho = 'mini_sistema/treinos/treinos.txt'
    nome = input('Digite o nome do treino (Deixe vazio e Aperte ENTER para cancelar) : ')
    if nome == "":
        sleep(1)
        return

    #verificando se existe algum treino ja cadastrado, se nao houver ele cria, se tiver ele adiciona
    if os.path.isfile(caminho):
        with open(caminho , "a" , encoding='utf-8') as arquivo:
            arquivo.write(f"{nome}\n")

    else:
        with open(caminho , "w" , encoding='utf-8') as arquivo:
            arquivo.write(f"{nome}\n")


def excluir_treino(): 
    novo_treino = []
    caminho = 'mini_sistema/treinos/treinos.txt'
    escolha = input("Digite o nome EXATO do treino que voce deseja excluir >>> ")
    
    with open(caminho , "r" , encoding='utf-8') as arq:
        for lin in arq:
            if escolha != lin.strip():
                novo_treino.append(lin)
        
    with open(caminho , "w" , encoding='utf-8') as arq:
        arq.writelines(novo_treino)
        sleep(2)

    linha()
    print("Treino atualizado.")