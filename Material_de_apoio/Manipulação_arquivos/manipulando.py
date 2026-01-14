with open("testes/Manipulação_arquivos/Contatos.txt", "w", encoding="utf-8") as arq:

    arq.write("Cláudia - 9898\n") # `w` Cria e escreve o que esta escrito, se ja existir, sobrescreve apagando o que ja tinha antes.

with open("testes/Manipulação_arquivos/Contatos.txt", "a", encoding="utf-8") as arq: 

    arq.write('Pedro - 7162\n') # 'a' usando o metodo write para acrescentar coisas no arquivo sem sobrescrever o que ja tinha antes

with open("testes/Manipulação_arquivos/Contatos.txt", "r", encoding="utf-8") as arq:
    
    contatos = arq.read() #Copia o arquivo no formato original
    arq.seek(0) # Volta o ponteiro para o início, permitindo ler a partir do comeco do arquivo.
    contatos_linhas = arq.readlines() #tranforma cada linha em um item de uma lista

    print(contatos)
    print('=-=-=-')
    print(contatos_linhas)