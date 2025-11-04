class User():
    def __init__(self):
        self.first_name = self.get_first_name()
        self.last_name =  self.get_last_name()
        self.describe_user()
        self.greet_user()

    def get_first_name(self)-> str:
        first_name: str = input("Insert your first name: ").title()
        while True:
            if first_name:
                return first_name
            else:
                print("Error first name can't be empty")

    def get_last_name(self)-> str:
        last_name: str = input("Insert your last name: ").title()
        while True:
            if last_name:
                return last_name
            else:
                print("Error last name can't be empty")

    def describe_user(self)-> None:
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self)-> None:
        print(f"Hi {self.first_name} {self.last_name} nice to meet you!")

users = [User() for _ in range (2)]