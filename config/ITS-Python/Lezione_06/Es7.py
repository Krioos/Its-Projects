class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        return f"User: {self.first_name} {self.last_name}, Username: {self.username}, Email: {self.email}"

    def greet_user(self):
        return f"Hello, {self.first_name}!"

class Privileges():
    def __init__(self, privileges = None):
        if privileges is None:
            privileges:list = []
        self.privileges = privileges


    def show_privileges(self):
         if not self.privileges:
             print ("No privileges for this user")
         else:
            return "Privileges: " + ", ".join(self.privileges)

class Admin():
    def __init__(self, user, privileges):
        self.user = user
        self.privileges = privileges
    def describe_admin(self):
        return  self.user.describe_user()+ "\n" + self.privileges.show_privileges()



#gettter oer stampare i valori
#print(f"{user1.get_name()}\n{user1.get_lastname()}\n{user1.get_username()}\n{user1.get_email()}")

