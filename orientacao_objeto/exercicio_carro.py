class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# Exemplo 1
uno = Carro('Uno')
fiat =  Fabricante('Fiat')
motor_16v = Motor('16v')

uno.fabricante = fiat
uno.motor = motor_16v

print(uno.nome, uno.fabricante.nome, uno.motor.nome)

# Exemplo 2
argo = Carro('Argo')

argo.fabricante = fiat
argo.motor = motor_16v

print(argo.nome, argo.fabricante.nome, argo.motor.nome)