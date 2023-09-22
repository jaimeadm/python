# Associação - usa
# Agregação - tem
# Composição - é dono de
# Herança - é um

class Pessoa:

    cpf = '123'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    cpf = '999'
    def falar_nome_classe(self):
        print('Classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

c1 = Cliente('Fulano', 'da Silva')
c1.falar_nome_classe()
print(c1.cpf)
#help(Cliente)