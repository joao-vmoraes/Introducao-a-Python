from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, usuario):
        self.usuario = usuario

    @abstractmethod
    def enviar(self, msg):
        pass

class NotificacaoEmail(Notificacao):
    def __init__(self, usuario, email):
        super().__init__(usuario)
        self.email = email

    def enviar(self, msg):
        print(f"Enviando Por Email para {self.usuario} do email ({self.email}) : {msg}")

class NotificacaoSms(Notificacao):
    def __init__(self, usuario, numero):
        super().__init__(usuario)
        self.numero = numero

    def enviar(self, msg):
        print(f"Enviando por Sms para {self.usuario} do numero ({self.numero}) : {msg}")

def enviar_alertas(lista_notificacoes, msg):
    for notif in lista_notificacoes:
        notif.enviar(msg)

em1 = NotificacaoEmail('Paulo', "Pauloricardo@gmail.com")
em2 = NotificacaoEmail('Joao' , "JoaoPedro2312@gmail.com")
em3 = NotificacaoEmail('Miguel', "Miguelescaravana@hotmail.com")

sm1 = NotificacaoSms('Ana', '82 980762514')
sm2 = NotificacaoSms('Maria', '51 98362534')
sm3 = NotificacaoSms('Duda', '71 8 97532400')

lista = [em1,em2,em3,sm1,sm2,sm3]

enviar_alertas(lista, 'Bom dia! Seu pedido esta sendo enviado!')