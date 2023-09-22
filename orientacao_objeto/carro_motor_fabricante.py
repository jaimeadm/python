class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None

    def inserir_motor(self, motor):
        self._motor = motor

    def mostrar_carro(self):
        print(f'{self.nome} tem motor: {self._motor.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []

    def inserir_carro(self, *carros):
        for carro in carros:
            self._carros.append(carro)

    def mostrar_carros(self):
        print(f'Motor: {self.nome}')
        for chave, carro in enumerate(self._carros):
            print(f'{chave} - {carro.nome}')

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._carros = []

    def inserir_carro(self, *carros):
        for carro in carros:
            self._carros.append(carro)

    def mostrar_carros(self):
        print(f'Fabricante: {self.nome}')
        for chave, carro in enumerate(self._carros):
            print(f'{chave} - {carro.nome}')

motor = Motor('16v')
fabricante = Fabricante('Fiat')

carro1, carro2 = Carro('Uno'), Carro('Argo')

motor.inserir_carro(carro1, carro2)
motor.mostrar_carros()

fabricante.inserir_carro(carro1, carro2)
fabricante.mostrar_carros()