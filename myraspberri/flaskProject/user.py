class User:
    def __init__(self):
        self.name = None
        self.password = None


    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password


user = User()

print(user.name)