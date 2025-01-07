from user import User
class UserRepository:
    def __init__(self):
        self.list_of_users = []

    def add(self, user:User):
        self.list_of_users.append(user)

    def view_users(self):
        return str(self.list_of_users)


