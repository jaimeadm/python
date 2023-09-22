"""Este é um módulo de exemplo

Este módulo contém class e exemplos de documentação de métodos.
Métodos disponíveis são soma e multiplica.
"""

variavel_1 = 1

class Foo:
    """Class de Exemplo

    Esta class contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.
    """

    def soma(x: int | float, y: int | float) -> int | float:
        """Soma x e y

        Este módulo contém funções e exemplos de documentação de métodos.
        Exemplo do método.
        
        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float

        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def multiplica(
            x: int | float,
            y: int | float,
            z: int | float | None = None
    ) -> int | float:
        """Multiplica x, y e/ou z
        
        Multiplica x e y. Se z for enviado, multiplica x, y, z.
        """
        if z is None:
            return x * y
        return x * y * z
    
    def bar(self) -> int:
        """ O que este método faz

        Levanta uma exceção        
        : raise NotImplementedError('Exemplo')
        """
        raise NotImplementedError('Exemplo')

variavel_2 = 2
variavel_3 = 5