class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self.arquivo = None
        print("Init")

    def __enter__(self):
        print("Abrindo arquivo")
        self.arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self.arquivo

    def __exit__(self, class_exception, exception_, taceback_):
        print("Fechando arquivo")
        self.arquivo.close()


with MyOpen('Aulas_POO\Context_manager\open.txt' , 'w' ) as arquivo:
    arquivo.write("Linha1\n")
    arquivo.write("Linha1\n")
    print("With", arquivo)