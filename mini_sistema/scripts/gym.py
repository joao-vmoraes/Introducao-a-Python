import modulos as md
import os
from time import sleep

with open('mini_sistema/treinos/treinos.txt' , "r" , encoding='utf-8') as arq:
    treinos = arq.readlines()

opcoes_menu_principal = ["Abrir Treino" , "Adicionar Treino" , "Excluir Treino" , "Sair do Sistema"]



while True:
    opcao = md.menu_principal(opcoes_menu_principal)

    if opcao == 1:
        treino_selecionado = md.listar_treinos()
        resposta = md.selecionar_treino(treino_selecionado)

        if resposta == 1:
            dicionario_treino = md.Cadastrar_treino_do_dia(treinos[treino_selecionado - 1].strip())
            md.criar_arquivo_treino(dicionario_treino)
            continue #Cadastrar dia de treino

        elif resposta == 2:
            continue # Excluir Treino

        elif resposta == 3:
            continue # Analisar Treino 

        elif resposta == 4:
            md.cabecalho("Saindo ...")
            sleep(1)
            break
        continue#abrir treino

    elif opcao == 2:
        md.criar_treino()
        continue#adicionar treino

    elif opcao == 3:
        teino_selecionado = md.excluir_treino()
        continue#excluir treino

    elif opcao == 4:
        md.sair_programa()
        break#sair do sistema


