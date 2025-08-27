import modulos as md
import os

opcoes_menu_principal = ["Abrir Treino" , "Adicionar Treino" , "Excluir Treino" , "Sair do Sistema"]


opcao = md.menu_principal(opcoes_menu_principal)

while True:
    if opcao == 1:
        continue#abrir treino
    elif opcao == 2:
        continue#adicionar treino
    elif opcao == 3:
        continue#excluir treino
    elif opcao == 4:
        break#sair do sistema

