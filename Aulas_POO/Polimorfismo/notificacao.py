from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool : ...

class NotificacaoSms(Notificacao):
    def enviar(self):
        print("Sms: enviando -", self.msg)
        return True

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f"Email: enviando -", self.msg )
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificacao enviada")
    else:
        print("Notificacao nao enviada")

notificar(NotificacaoEmail("Testando email"))
notificar(NotificacaoSms("Testando email"))
