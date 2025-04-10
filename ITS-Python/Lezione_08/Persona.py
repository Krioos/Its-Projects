class Person():
    def __init__(self, name: str, surname:str , age: int):
        name = self.setName(name)
        self.surname = surname
        self.age = age
    
    def setName(self, name):
        if name:
            return name
        else:
            print("Name can't be empty")

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return (f"{self.name} {self.surname}, {self.age}")