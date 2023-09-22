class MinhaString(str):
    def upper(self):
        print('Método Upper Interno')
        result = super().upper()
        print('Método pós Upper')
        return result

string = MinhaString('Fulano')
print(string.upper())

print('-' * 50)

class A:
    atributo_a = 'AAA'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A', '- Classe:', self.__class__.__name__)

class B(A):
    atributo_b = 'BBB'

    def __init__(self, atributo, outro_atributo):
        super().__init__(atributo)
        self.outro_atributo = outro_atributo

    def metodo(self):
        print('B', '- Classe:', self.__class__.__name__)

class C(B):
    atributo_c = 'CCC'

    def __init__(self, *args, **kwargs):
        print('Argumentos...')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super(C, self).metodo()
        super(B, self).metodo()
        print('C', '- Classe:', self.__class__.__name__)


print(C.mro())
print(B.mro())
print(A.mro())
print()

c = C('Atributo', 'Outro-Atributo')
print(c.atributo, c.outro_atributo)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()