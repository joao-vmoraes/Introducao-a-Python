import modulos as md
import os


opcoes_menu_principal = ["Abrir Treino" , "Adicionar Treino" , "Excluir Treino" , "Sair do Sistema"]



while True:
    opcao = md.menu_principal(opcoes_menu_principal)

    if opcao == 1:
        resposta = md.listar_treinos()
        md.selecionar_treino(resposta)
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


