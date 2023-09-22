# Para criar exception é preciso herdar uma exceção da linguagem (Exception)

class MeuError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('Mensagem de erro.', 'Erro novamente', 'Arrume já')
    exception_.add_note('Nota 1')
    raise exception_
    
try:    
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Lançar novamente!')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Outra Nota')
    raise exception_ from error
