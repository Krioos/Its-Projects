from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patient:list[Paziente], doctor: Dottore)-> None:
        if not doctor.isAValidDoctor():
            print("Errore il dottore non è valido")
            self.__patient = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
        else:
            self.__patient = patient
            self.__doctor = doctor
            self.getFatture()
            self.__salary:float = 0.00

    def getSalary(self)-> str:
        value = self.__doctor.getParcel() * len(self.__patient)
        self.__salary = value
        return f"Il Dottore ha guadagnato{value}"
    
    def getFatture(self)-> int:
        result = len(self.__patient)
        self.__fatture = result
        print(f"Il Dottore ha {result} fatture")
        return result
    
    def addPatient(self, new_patient:Paziente)-> None:
        self.__patient.append(new_patient)
        print(f"Al dottore {self.__doctor.getLastName()} è stato aggiunto il paziente {new_patient.getId()}")
        self.getSalary()
        self.getFatture()
    
    def removePatient(self, id_code: str) -> None:
        try:
            patient_to_remove = next(p for p in self.__patient if p.getId() == id_code)
            self.__patient.remove(patient_to_remove)
            print(f"Paziente {id_code} rimosso dal dottore {self.__doctor.getLastName()}")
            self.getSalary()
            self.getFatture()
        except StopIteration:
            print(f"Nessun paziente con id {id_code} trovato.")

            