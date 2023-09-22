class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    

p1 = Pessoa('Alan', 35)
print(p1.get_ano_nascimento())
print(Pessoa.ano_atual)

dados = {'nome': 'Fulano', 'idade': 22}
p2 = Pessoa(**dados)
print(p2.__dict__)
print(vars(p2))