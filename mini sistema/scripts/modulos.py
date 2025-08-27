from time import sleep
import os

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

def listar_treinos():
    caminho_do_script = os.path.abspath(__file__) #pega o caminho completo do arquivo
    caminho_da_pasta_do_script = os.path.dirname(caminho_do_script) #pega o caminho da pasta onde o script esta
    caminho_da_pasta_acima = os.path.dirname(caminho_da_pasta_do_script) # pega o caminho da pasta que contem a pasta do script
    pasta_treinos = os.path.join(caminho_da_pasta_acima, "treinos") #recebe o caminho da pasta 'treinos'

    lista_treinos = os.listdir(pasta_treinos) #adiciona todos os arquivos em uma lista

    cabecalho("Lista de Treinos")

    c = 1
    for i in lista_treinos:
        print(f"{c} - {os.path.splitext(i)[0]}") #funcao para nao sair na impressao o tipo do arquivo
        c += 1

