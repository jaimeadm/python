import hashlib

class Connection:
    def __init__(self, host, user):
        self.host = host
        self.user = user
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


conn = Connection(host='localhost', user='admin')
print('Host:', conn.host, 'User:', conn.user)

conn.password = hashlib.md5('pass123'.encode())
print('Password:', conn.password.hexdigest())

        