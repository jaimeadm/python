# new - cria e retorna a class na metaclasse
# call - cria e retona a instância
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLESS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 123
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        return cls
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        return instancia

class Pessoa(metaclass=Meta):

    def __new__(cls, *args, **kwargs):
        print('NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('INIT')
        self.nome = nome

    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Fulano')
p1.falar()