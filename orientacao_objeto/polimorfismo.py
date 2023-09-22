# 4 pilares da programação orientada a objetos
# abstração, herança, encapsulamento, polimorfismo

# Polimorfismo permite que classes derivadas de uma 
# mesma superclasse tenham métodos iguais, mas compartamentos diferentes

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Enviando e-mail:', self.mensagem)
        return True
    
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('Enviando sms:', self.mensagem)
        return False

# Polimorfismo
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada.')

notificar_email = NotificacaoEmail('teste por e-mail')
notificar(notificar_email)

notificar_sms = NotificacaoSMS('teste por sms')
notificar(notificar_sms)