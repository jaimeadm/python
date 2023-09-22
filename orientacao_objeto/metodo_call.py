class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Chamando: ', self.phone)
        return 'valor'

call1 = CallMe('1192911029')
retorno = call1('Fulano')
print(retorno)