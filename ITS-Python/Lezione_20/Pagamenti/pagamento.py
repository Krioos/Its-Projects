from abc import ABC, abstractmethod
class Pagamento(ABC):

    @abstractmethod
    def __init__(self, importo:float = 0.00)-> None:
        self.setImporto(importo)

    def setImporto(self, value:float)-> None:
        if isinstance(value, float):
            self.__importo = value
        else:
            print("Errore il valore non è corretto")


    def getImporto(self)-> float | None:
        try:
            return self.__importo
        except Exception:
            return None
        
    def dettagliPagamento(self)-> str:
        return f"L'importo del pagamento: {self.getImporto()}€"