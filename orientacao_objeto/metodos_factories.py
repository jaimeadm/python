class Pessoa:
    ano = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Olá')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Sem Nome', idade)

p1 = Pessoa('Fulano', 19)
p2 = Pessoa.criar_com_50_anos('Ciclano')
p3 = Pessoa.criar_anonimo(30)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)
print(Pessoa.ano)
Pessoa.metodo_de_classe()