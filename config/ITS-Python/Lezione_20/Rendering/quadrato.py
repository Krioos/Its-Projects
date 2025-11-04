'''
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

'''

def dedup_stable(nums: list[int]) -> list[int]:
    result:list[int] = [elem for elem in nums if elem not in result]
    return result


print(dedup_stable([1,2,4,5,5,6,7,8,8,9]))


def chunk(lst: list[int], size: int) -> list[list[int]]:
    count:int = 0
    result:list[int] = []
    chunck: list[int] = []
    for i in range (len(lst)) :
        if count < size and i != len(lst) -1:
            chunck.append(lst[i])
        else:
            result.append(chunck)
            chunck = []
    return result
            
