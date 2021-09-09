class User:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        print(f"Name: {self.name}   email:  {self.email}")




oneUser = User(name="Juan", email="juan@gmail.com", age=50)

oneUser.greeting()



