class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password
        
    @classmethod # metodo de classe, que nao tera self, e sim uma classe
    def create_with_auth(cls, password, user):
        connection = cls()
        connection.password = password
        connection.user = user
        return connection

c1 = Connection()
print(c1.user)
