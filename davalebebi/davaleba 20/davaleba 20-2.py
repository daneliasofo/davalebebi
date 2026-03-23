class User:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"User: {self.name}")


class Admin(User):
    def info(self):
        print(f"Admin: {self.name}")


u = User("2341")
a = Admin("sofo")

u.info()
a.info()