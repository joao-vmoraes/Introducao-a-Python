import modulos as md
import os

treinos = ["Costas" , "Peito" , "Perna"]
opcoes_menu_principal = ["Abrir Treino" , "Adicionar Treino" , "Excluir Treino" , "Sair do Sistema"]



while True:
    opcao = md.menu_principal(opcoes_menu_principal)

    if opcao == 1:
        md.listar_treinos(treinos)
        continue#abrir treino

    elif opcao == 2:
        md.adicionar_treino(treinos)
        continue#adicionar treino

    elif opcao == 3:
        teino_selecionado = md.excluir_treino()
        
        continue#excluir treino

    elif opcao == 4:
        print("")
        
        break#sair do sistema


