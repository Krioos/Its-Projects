class Person():
    def __init__(self, name: str, lastname:str , age: int)-> None:
        self.name = self.setName(name)
        self.lastname = self.setLastname(lastname)
        self.age = self.setAge(age)
    
    def setName(self, name)-> str:
        if name:
            return name
        else:
            print("Name can't be empty")
    
    def setLastname(self, lastname)-> str:
        if lastname:
            return lastname
        else:
            print("Lastname can't be empty")
    
    def setAge(self, age)-> int:  
        if age >= 0:
            return age
        else:
            print("Age can't be negative")
        return 0
    

    def get_name(self)-> str:
        return self.name
    
    def get_lastName(self)-> str:
        return self.lastname
    
    def get_age(self)-> int:
        return self.age
    
    def __repr__(self)-> str:
        return (f"\nNome: {self.get_name()},\nLast name: {self.get_lastName()},\nAge: {self.get_age()}")
    

    def speak(self)-> None:
        print(f"\nHi my name is {self.get_name()}!\n")