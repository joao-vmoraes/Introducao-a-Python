class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

c1 = Connection()
print(c1.user)
c1.set_user('adm')
print(c1.user)