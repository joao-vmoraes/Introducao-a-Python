from time import sleep
import os
import datetime

def linha(tam=40):
    print("=" * tam)

def cabecalho(frase):
    #usado para criar cabeçalhos com alguma frase, com 40 caracteres de alinhamento
    linha()
    print(f"{frase:^40}")
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

    c = 1
    for i in list:
        print(f"{c} - {i}") #funcao para nao sair na impressao o tipo do arquivo
        c += 1

def escolher_treino():
    while True:
        try:
            resposta = int(input("Digite a opção >>> "))
            return resposta
        except:
            print("ERRO: Tipo de dado enviado não válido.")
            sleep(2)