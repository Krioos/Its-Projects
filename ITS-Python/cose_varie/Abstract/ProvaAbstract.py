from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, nome, cognome, cf, età)-> None:
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.età = età
    
    @abstractmethod
    def __str__(self)-> str:
        pass


class Student(Person):
    def __init__(self, nome, cognome, cf)-> None:
        super().__init__(nome, cognome, cf)
    
    def __str__(self)-> str:
        return f"Nome: {self.nome}\nCognome: {self.cognome}\ncf: {self.cf}"



class Lecturer(Person):
    def __init__():
        pass

class Group():
    def __init__(self, name, n_studenti ):
        self.name = name
        self.n_studenti = n_studenti
        self.students = list()
        self.lecturers =  list()

    

person1 = Student("Prova", "Provini", "djnwfnfwo")

print(person1)