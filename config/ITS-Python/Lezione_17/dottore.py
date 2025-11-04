from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name:str, last_name:str, specialization:str, parcel: float)-> None:
        super().__init__(first_name, last_name)
        if self.setSpecialization(specialization):
            self.__specialization = self.setSpecialization(specialization)
        else:
            self.__specialization = None
        
        if self.setParcel(parcel):
            self.__parcel = self.setParcel(parcel)
        else:
            self.__parcel = None

    def setSpecialization(self, value: str)-> str | bool:
        if isinstance(value, str):
            return value
        else:
            print(f"Errore {value} non è una stringa")
            return False
    
    def setParcel(self, value: float)-> float | None:
        if isinstance(value, float):
            return value
        else:
            print(f"Errore {value} non è un float")
            return False

    def getSpecialization(self)-> str | None:
        return self.__specialization
    
    def getParcel(self)-> float | None:
        return self.__parcel

    def isAValidDoctor(self)-> bool:
        if self.getAge() > 30:
            print(f"Il Dottore {self.getFirstName()} {self.getLastName()} è valido")
            return True
        else:
            return False
    
    def doctorGreet(self)-> None:
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")
