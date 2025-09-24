from forma import Forma

class Quadrato(Forma):
    def __init__(self, lato:float)-> None:
        self.__nome = "Quadrato"
    

    def setLato(self, value:float)-> None:
        if isinstance(value, float):
            self.__lato = value
        else:
            print("Errore")
    
    def getLato(self)-> float | None:
        try:
            return self.__lato
        
        except Exception:
            return None
        
    
    def getArea(self)-> float:
        return self.getLato() **2
    
    def getRemder
