class Classe:

    @staticmethod
    def funcao_na_classe(*args, **kwargs):
        print('Olá', args, kwargs)

c1 = Classe()
c1.funcao_na_classe(1, 2, 3)
Classe.funcao_na_classe(nomeado=11)