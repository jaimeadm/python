import contas
import pessoas


class Banco:
    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None,):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    cliente1 = pessoas.Cliente('Fulano', 22)
    conta1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente1.conta = conta1

    cliente2 = pessoas.Cliente('Ciclano', 53)
    conta2 = contas.ContaPoupanca(333, 551, 100)
    cliente2.conta = conta2

    banco = Banco()
    banco.clientes.extend([cliente1, cliente2])
    banco.contas.extend([conta1, conta2])
    banco.agencias.extend([111, 222])

    if banco.autenticar(cliente1, conta1):
        conta1.depositar(10)
        cliente1.conta.depositar(20)
        print(cliente1.conta)
