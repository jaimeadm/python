class Pai:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        print('Pai falando...')

class Filho(Pai):
    def __init__(self, nome, sobrenome, idade):
        super().__init__(nome, sobrenome)
        self.idade = idade

    def falar(self):
        super(Filho, self).falar()
        print('Filho falando...')


filho1 = Filho('Fulano', 'da Silva', 21)
print(filho1.nome, filho1.sobrenome, filho1.idade)

filho1.falar()
