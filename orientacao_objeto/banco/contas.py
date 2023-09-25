import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depósito: (R$ {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'Saldo Atual: (R$ {self.saldo:.2f}) | {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque: (R$ {valor})')
            return self.saldo

        self.detalhes(f'Não foi possível sacar | Saque Negado (R$ {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Saque: (R$ {valor})')
            return self.saldo

        print(f'Não foi possível sacar | Limite: (R$ {-self.limite:.2f})')
        self.detalhes(f'Saque Negado (R$ {valor})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    conta_poupanca1 = ContaPoupanca(111, 222)
    conta_poupanca1.sacar(10)
    conta_poupanca1.depositar(55)
    conta_poupanca1.sacar(23)

    print('-' * 50)

    conta_corrente1 = ContaCorrente(111, 222, 0, 50)
    conta_corrente1.sacar(20)
    conta_corrente1.depositar(30)
    conta_corrente1.sacar(15)
    conta_corrente1.sacar(80)
