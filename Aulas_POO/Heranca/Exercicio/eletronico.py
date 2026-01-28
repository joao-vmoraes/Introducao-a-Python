from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    @property
    def nome(self):
        return self._nome
    
    @property
    def ligado(self):
        return self._ligado
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @ligado.setter
    def ligado(self, valor):
        self._ligado = valor

    def ligar(self):
        if not self.ligado:
            self.ligado = True

    def desligar(self):
        if self.ligado:
            self.ligado = False

class Celular(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self.ligado:
            msg = f"{self.nome} ja esta ligado."
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self.ligado:
            msg = f"{self.nome} esta desligado."
            self.log_success(msg)
