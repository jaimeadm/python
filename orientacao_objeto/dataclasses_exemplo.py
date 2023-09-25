# dataclasses fornecem decoradores e funções para criar métodos
# como: __init__(), __repr__(), __eq__()
# syntax sugar de classes normais

# from dataclasses import dataclass, asdict, astuple
# from dataclasses import dataclass
from dataclasses import dataclass, field


# @dataclass(repr=True)
# @dataclass(init=False)
@dataclass
class Pessoa:
    nome: str = field(default='Fulano', repr=False)
    sobrenome: str = 'Ciclano'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':

    # p1 = Pessoa('Fulano', 'da Silva')
    # p2 = Pessoa('Ciclano', 'das Couves')
    # print(p1)
    # print(p1 == p2)
    # print(p2.nome_completo)

    # p3 = Pessoa('Beltrano', 'Felício')
    # # p3.nome_completo = 'Maria Oliveira Costa'
    # print(p3.nome_completo)
    # p1 = Pessoa('Fulano', 'Ciclano')
    # print(asdict(p1))
    # print(asdict(p1).items())
    # print(astuple(p1)[0])
    p1 = Pessoa()
    print(p1)
