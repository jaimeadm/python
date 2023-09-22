class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

gol = Carro('Gol')
print(gol.nome)
gol.acelerar()







