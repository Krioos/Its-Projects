from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codice_volo:str, max_posti:int)-> None:
        self.setCodice_volo(codice_volo)
        self.setMax_posti(max_posti)
        self.__prenotazioni = 0
    
    def getCodice_volo(self)-> str:
        return self.__codice_volo
    
    def setCodice_volo(self, value:str)-> None:
        self.__codice_volo = value

    def getMax_posti(self)-> int:
        return self.__max_posti
    
    def setMax_posti(self, value:int)-> None:
        self.__max_posti = value

    @abstractmethod
    def prenota_posto(self)->None:
        pass

    @abstractmethod
    def posti_disponibili(self)-> None:
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice_volo:str, max_posti:int)-> None:
        super().__init__(codice_volo, max_posti)
        self.__posti_economica:int = round(self.getMax_posti() * 70 / 100)
        self.__posti_buisness: int = round(self.getMax_posti() *20 / 100)
        self.__prenotazioni = 0
        self.__posti_prima:int = self.getMax_posti() -(self.__posti_economica + self.__posti_buisness)
        self.__prenotazioni_economica:int = 0
        self.__prenotazioni_buisness:int = 0
        self.__prenotazioni_prima: int = 0

    def posti_disponibili(self)-> dict[str, int]:
        return {"posti disponibili": self.getMax_posti() - self.__prenotazioni,
                "classe economica": self.__posti_economica - self.__prenotazioni_economica,
                "classe buisness": self.__posti_buisness - self.__prenotazioni_buisness,
                "prima classe": self.__posti_prima - self.__prenotazioni_prima}
    
    def prenota_posto(self, posti:int, classe_servizio:str):
        classi:list[str] = ["economica", "buisness", "prima"]
        dict_posti: dict[str, int] = self.posti_disponibili()
        if classe_servizio not in classi:
            print("Errore classe richiesta non valida")
        else:
            if posti <= dict_posti["posti disponibili"]:
                if classe_servizio == "economica":
                    if posti <= dict_posti["classe economica"]:
                        self.__prenotazioni_economica += posti
                        self.__prenotazioni += posti
                        print(f"Prenotati {posti} alla classe economica")
                    else:
                        print(f"Solo {dict_posti['classe economica']} posti\
                              restanti")
                elif classe_servizio == "buisness":
                    if posti <= dict_posti["classe buisness"]:
                        self.__prenotazioni_buisness += posti
                        self.__prenotazioni += posti
                        print(f"Prenotati {posti} alla classe buisness")
                    else:
                        print(f"Solo {dict_posti['classe buisness']} posti\
                              restanti")
                else:
                    if posti <= dict_posti["prima classe"]:
                        self.__prenotazioni_prima += posti
                        self.__prenotazioni
                        print(f"Prenotati {posti} prima classe")
                    else:
                        print(f"Solo {dict_posti['prima classe']} posti\
                              restanti")
            else:
                print("Volo al completo")
            
class VoloCharter(Volo):
    def __init__(self, codice_volo:str, max_posti: int, costo_volo:float)-> None:
        super().__init__(codice_volo, max_posti)
        self.setCosto_volo(costo_volo)
        self.__prenotazioni = 0

    def getCosto_volo(self)-> float:
        return self.__costo_volo
    
    def setCosto_volo(self, value)-> None:
        self.__costo_volo = value
    
    def posti_disponibili(self):
        return self.getMax_posti() - self.__prenotazioni
    
    def prenota_posto(self):
        if self.posti_disponibili() == self.getMax_posti():
            self.__prenotazioni += self.getMax_posti()
            print(f"Il volo {self.getCodice_volo()} prenotato, costo {self.getCosto_volo()}")

class CompagniaAerea():
    def __init__(self, nome:str)-> None:
        self.setNome(nome)
        self.__prezzo:float = 0.00
        self.__flotta:list[VoloCommerciale] = []
    
    def getNome(self)-> str:
        return self.__nome

    def setNome(self, value)-> None:
        self.__nome = value
    
    def getPrezzo(self)-> float:
        return self.__prezzo
    
    def getFlotta(self)-> list[VoloCommerciale]:
        return self.__flotta
    
    def aggiungi_volo(self, volo: VoloCommerciale)-> None:
        self.__flotta.append(volo)

    def rimuovi_volo(self, volo: VoloCommerciale)-> None:
        try:
            self.__flotta.remove(volo)
        except ValueError:
            print("Errore volo non presente")
    
    def mostra_flotta(self)-> list[VoloCommerciale]:
        print(f"Ecco tutti i voli dellla compagnia aerea {self.getNome}")
        for elem in self.getFlotta:
            print(f"volo commerciale {elem.getCodice_volo}")
    
    def guadagno(self):
        profit: float = 0
        for volo in self.getFlotta:
            profit += volo.__prenotazioni_economica + volo.__prenotazioni_buisness *2 + volo.__prenotazioni_prima * 3
        return round(profit, 2)
        

volo1 = VoloCommerciale("COM123", 100)
print(volo1.posti_disponibili())
volo1.prenota_posto()
