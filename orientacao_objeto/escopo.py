class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comer(*args, **kwargs)

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('carne'))