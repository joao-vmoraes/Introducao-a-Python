import modulos as md
import os
from time import sleep

opcoes_menu_principal = ["Abrir Treinos" , "Adicionar Treino" , "Excluir Treino" , "Sair do Sistema"] # opções que apareceram no menu principal
md.existencia_arq() #verificando se existe o arquivo treino.txt, se nao houver ele cria

while True:
    with open('mini_sistema/treinos/treinos.txt' , "r" , encoding='utf-8') as arq:
        treinos = arq.readlines()

    opcao = md.menu_principal(opcoes_menu_principal)

    if opcao == 1: #Cadastrar dia de treino
            
        treino_selecionado = md.listar_treinos()
        if treino_selecionado == -1: # caso nao tenha nenhum treino registrado ainda
            continue
        resposta = md.selecionar_treino(treino_selecionado)

        if resposta == 1:
            dicionario_treino = md.Cadastrar_treino_do_dia(treinos[treino_selecionado - 1].strip())
            if dicionario_treino != -1: # quando o usuario não cancelar a criação de um treino
                md.criar_arquivo_treino(dicionario_treino) 

        elif resposta == 2:
            continue # Excluir dia de Treino

        elif resposta == 3:
            continue # Analisar Treinos

        elif resposta == 4:
            md.cabecalho("Saindo ...")
            sleep(1)
            continue
        

    elif opcao == 2:
        md.criar_treino()
        continue#adicionar categoria de treino

    elif opcao == 3:
        teino_selecionado = md.excluir_treino()
        continue#excluir categoria de treino

    elif opcao == 4:
        md.sair_programa()
        break#sair do sistema

    else:
        print("\033[31m Digite uma opção valida.\033[m")
        sleep(2)
