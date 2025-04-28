from abc import ABC, abstractmethod
class FormaGeometrica(ABC): #ABC è una classe base astratta

    @abstractmethod #decorator serve ad indicare che il metodo è astratto
    def draw(slef)-> None:
        pass

    def setShape(self, shape)-> str:
        if shape:
            self.shape = shape
        else:
            print("Errore! shape non può essere vuoto")

    def getShape(self)-> str:
        return self.shape
    
    