class User():
    def __init__(self):
        self.first_name = self.get_first_name()
        self.last_name =  self.get_last_name()
        self.login_attempts = 0

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
    
    def increment_login_attempt(self) -> None:
        self.login_attempts += 1
        print(f"New login attempts detected, {self.login_attempts} login attempts now")

    def reset_attempts(self):
        self.login_attempts = 0
        print(f"Attempts resetted, {self.login_attempts} login attempts now")

users = [User() for _ in range (2)]

for _ in range (3):
    users[0].increment_login_attempt()
users[0].reset_attempts()