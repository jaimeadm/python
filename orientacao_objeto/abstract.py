# 4 pilares da programação orientada a objetos
# abstração, herança, encapsulamento, polimorfismo

# Classes abstratas são usadas como definição de novas classes.
# Elas força outras classes a criarem métodos concretos.
# @abstractmethods são métodos sem corpo.
# Classes e Métodos abstratos não podem ser instânciados diretamente.

from abc import ABC, ABCMeta, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name        

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Foo...')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

    

foo = Foo('Bar')
print(foo.name)