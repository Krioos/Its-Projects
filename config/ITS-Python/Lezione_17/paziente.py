from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name:str, last_name:str, id: str)-> None:
        super().__init__(first_name, last_name)
        self.setId(id)

    def setId(self, value:str)-> None:
        self.__id = value
    
    def getId(self)-> str:
        return self.__id

    def patientinfo(self):
        print(f"Paziente {self.getFirstName()} {self.getLastName()}\nID: {self.getId()}")


    
