class Persona():
    def __init__(self, first_name:str, last_name:str)-> None:
        if self.setName(first_name):
            self.__first_name = self.setName(first_name)
        else:
            self.__first_name = None
        
        if self.setLastName(last_name):
            self.__last_name = self.setLastName(last_name)
        else:
            self.__last_name = None

        if self.__first_name == None or self.__last_name == None:
            self.__age = None
        else:
            self.__age = 0

    def setName(self,value:str)-> str | bool:
        if isinstance(value,str):
            return value
        else:
            print(f"Errore {value} non è una stringa")
            return False
    
    def setLastName(self, value:str)-> bool:
        if isinstance(value, str):
            return value
        else:
            print(f"Errore {value} non è una stringa")
            return False
    
    def setAge(self, value:int)-> None:
        if isinstance(value, int):
            self.__age = value
        else:
            print(f"{value} non è un numero intero")

    def getFirstName(self)-> str:
        return self.__first_name

    def getLastName(self)-> str:
        return self.__last_name

    def getAge(self)-> int | None:
        return self.__age           

    def greet(self)-> None:
        print(f"Sono {self.getFirstName()} {self.getLastName()}! Ho {self.getAge()} anni")
