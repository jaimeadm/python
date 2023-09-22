class Caneta:
    def __init__(self, cor):
        #self.cor_tinta = cor
        self._cor = cor         # private, protected
        self._cor_tampa = None

    @property
    def cor(self):
        print('GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('SETTER', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        print('GETTER - COR TAMPA')
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('SETTER - COR TAMPA')
        self._cor_tampa = valor

# Inicio
caneta = Caneta('Azul')

caneta.cor = 'Vermelha'
print(caneta.cor)

print('-' * 50)

caneta.cor_tampa = 'Preta'
print(caneta.cor_tampa)