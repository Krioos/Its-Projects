from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def __init__(self)-> None:
        pass

    @abstractmethod
    def getArea(self)-> None:
        pass

    @abstractmethod
    def render(self)-> None:
        pass