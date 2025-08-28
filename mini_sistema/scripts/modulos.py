from time import sleep
import os
import datetime
import json

opcoes_treino = ["Cadastrar Treino" , "Excluir Treino" , "Analisar Treino"]

treino = { #formato em que os treinos serão guardados .jason
    "nome":"Peito" ,
    "data" : "dia/mes/ano" ,
    "Exercicios" : [
        {
            "nome" : "supino" ,
            "series" : 0 ,
            "repeticoes" : [0] ,
            "carga" : [0]
        }
    ]
}

def linha(tam=40): #para a simples criação d e uma linha
    print("\033[35m=\033[m" * tam)

def sair_programa(): # quando o usuario quiser sair do programa
    cabecalho("Até mais!")
    sleep(2)

def cabecalho(frase):   #usado para criar cabeçalhos com alguma frase, com 40 caracteres de alinhamento
    linha()
    print(f"\033[34m{frase:^40}\033[m")
    linha()

def menu_principal(opcoes_menu): # usado para mostrar as opções no menu e receber a resposta do usuario
    c = 1
    cabecalho("Menu de Gerenciamento de Treinos")
    for i in opcoes_menu:
        print(f"\033[36m{c}\033[m - {i}")
        c += 1
    linha()
    while True:
        try:
            resposta = int(input("Digite a opção >>> "))
            return resposta
        except:
            print("ERRO: Tipo de dado enviado não válido.")
            sleep(2)

def listar_treinos(): #listar os treinos que o usuario ja cadastrou
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
                linha()
                resposta = int(input("Digite a opção >>> "))
                return resposta
            except:
                print("ERRO: Tipo de dado enviado não válido.")
                sleep(2)
                break

    except:
        print("Voce ainda nao cadastrou nenhum treino.")
        sleep(2)


def selecionar_treino(numero_do_treino_selecionado): #usado para mostrar as opcoes do que fazer quando o usuario selecionar algum treino
    caminho = 'mini_sistema/treinos/treinos.txt'
    c = 1

    with open(caminho , "r" , encoding='utf-8') as arq:
        treinos = arq.readlines()

        try:
            if numero_do_treino_selecionado <= 0 or numero_do_treino_selecionado > len(treinos):
                raise IndexError
                
            cabecalho(f"Treino de {treinos[numero_do_treino_selecionado - 1]}")
            for i in opcoes_treino:
                print(f"\033[31m{c}\033[m - {i}")
                c += 1
            linha()
            resposta = int(input("Digite a sua opção >>> "))
            return resposta
        
        except ( IndexError , ValueError):
            print("ERRO: o numero selecionado não é compativel com nenhum treino.")
            sleep(2)


def criar_treino(): #usado para o usuario cadastrar um treino
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
    linha()
    cabecalho("Adicionado com sucesso!")
    sleep(2)


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
    cabecalho("Treino atualizado.")
    sleep(2)