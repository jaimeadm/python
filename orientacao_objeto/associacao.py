# Associação é a relação entre objetos. 
# Um objeto tem um atributo que referencia outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Fulano')
caneta = FerramentaDeEscrever('Caneta')
escritor.ferramenta = caneta    # associação

print(caneta.escrever())
print(escritor.ferramenta.escrever())