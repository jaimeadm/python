# method - self, método de instância
# @classmethod - cls, método da classe
# @staticmethod - metódio estático sem self e cls
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod # função que não tem acesso a classe
    def log_conn(msg):
        return f'Log: {msg}'
        

conexao = Connection()
conexao.set_user('admin')
conexao.set_password('senha123')
print(conexao.host, conexao.user, conexao.password)

conn = Connection.create_auth('root', 'pass123')

print(Connection.log_conn('Estou conectando...'))