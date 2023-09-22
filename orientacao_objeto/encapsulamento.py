# Encapsulamento (modificadores de acesso: public, protected, private)
# 4 pilares da programação orientada a objetos
# abstração, herança, encapsulamento, polimorfismo

class Pessoa:

    def __init__(self):
        self.public = 'Público - usar em qualquer lugar'
        self._protected = 'Protegido - usar somente na classe e sub-classes'
        self.__private = 'Privado - usar somente na classe'

    def metodo_public(self):
        print(self._protected)
        self._metodo_protected()

        print(self.__private)
        self.__metodo_private()

        print(self.public)
        return 'metodo_public'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    

p1 = Pessoa()
print(p1.metodo_public())

print('-' * 50)

# Exemplo 2
class Connection:
    def __init__(self, host, user, password):
        self.host = host            # public
        self._user = user           # protected
        self.__password = password  # private

    def __get_password_private(self):
        return self.__password

    def _get_user_protected(self):
        return self._user

    def get_host_public(self):
        print(self.__get_password_private())
        print(self._get_user_protected())
        return self.host

conn = Connection('localhost', 'admin', 'pass123')
print(conn.get_host_public())