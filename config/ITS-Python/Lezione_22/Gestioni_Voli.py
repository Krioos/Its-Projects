from abc import ABC, abstractmethod
import sys
class Volo(ABC):
    def __init__(self, codice_volo: str, max_posti: int) -> None:
        self.setCodice_volo(codice_volo)
        self.setMax_posti(max_posti)
        self.__prenotazioni = 0

    def getCodice_volo(self) -> str:
        return self.__codice_volo

    def setCodice_volo(self, value: str) -> None:
        self.__codice_volo = value

    def getMax_posti(self) -> int:
        return self.__max_posti

    def setMax_posti(self, value: int) -> None:
        self.__max_posti = value

    @abstractmethod
    def prenota_posto(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def posti_disponibili(self) -> None:
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice_volo: str, max_posti: int, costo_biglietto:float) -> None:
        super().__init__(codice_volo, max_posti)
        self.setCosto_biglietto(costo_biglietto)
        self.__posti_economica: int = round(self.getMax_posti() * 70 / 100)
        self.__posti_business: int = round(self.getMax_posti() * 20 / 100)
        self.__posti_prima: int = self.getMax_posti() - (self.__posti_economica + self.__posti_business)
        self.__prenotazioni = 0
        self.__prenotazioni_economica: int = 0
        self.__prenotazioni_business: int = 0
        self.__prenotazioni_prima: int = 0

    def setCosto_biglietto(self, value)-> None:
        self.__costo_biglietto = value
    
    def getCosto_biglietto(self)-> float:
        return self.__costo_biglietto
    
    def getPrenotazioniEconomica(self) -> int:
        return self.__prenotazioni_economica

    def getPrenotazioniBusiness(self) -> int:
        return self.__prenotazioni_business

    def getPrenotazioniPrima(self) -> int:
        return self.__prenotazioni_prima

    def posti_disponibili(self) -> dict[str, int]:
        return {
            "posti disponibili": self.getMax_posti() - self.__prenotazioni,
            "economica": self.__posti_economica - self.__prenotazioni_economica,
            "business": self.__posti_business - self.__prenotazioni_business,
            "prima": self.__posti_prima - self.__prenotazioni_prima
        }

    def prenota_posto(self, posti: int, classe_servizio: str):
        classi: list[str] = ["economica", "business", "prima"]
        dict_posti: dict[str, int] = self.posti_disponibili()

        if classe_servizio not in classi:
            print("Errore: classe richiesta non valida")
        elif posti > dict_posti["posti disponibili"]:
            print("Volo al completo")
        else:
            if classe_servizio == "economica":
                if posti <= dict_posti["economica"]:
                    self.__prenotazioni_economica += posti
                    self.__prenotazioni += posti
                    print(f"Prenotati {posti} posti in classe economica")
                else:
                    print(f"Solo {dict_posti['economica']} posti restanti in economica")
            elif classe_servizio == "business":
                if posti <= dict_posti["business"]:
                    self.__prenotazioni_business += posti
                    self.__prenotazioni += posti
                    print(f"Prenotati {posti} posti in classe business")
                else:
                    print(f"Solo {dict_posti['business']} posti restanti in business")
            elif classe_servizio == "prima":
                if posti <= dict_posti["prima"]:
                    self.__prenotazioni_prima += posti
                    self.__prenotazioni += posti
                    print(f"Prenotati {posti} posti in prima classe")
                else:
                    print(f"Solo {dict_posti['prima']} posti restanti in prima classe")

class VoloCharter(Volo):
    def __init__(self, codice_volo: str, max_posti: int, costo_volo: float) -> None:
        super().__init__(codice_volo, max_posti)
        self.setCosto_volo(costo_volo)
        self.__prenotazioni = 0

    def getCosto_volo(self) -> float:
        return self.__costo_volo

    def setCosto_volo(self, value) -> None:
        self.__costo_volo = value

    def posti_disponibili(self):
        return self.getMax_posti() - self.__prenotazioni

    def prenota_posto(self):
        if self.posti_disponibili() == self.getMax_posti():
            self.__prenotazioni += self.getMax_posti()
            print(f"Il volo {self.getCodice_volo()} prenotato, costo {self.getCosto_volo()}")
        else:
            print(f"Il volo {self.getCodice_volo()} è al completo")

class CompagniaAerea():
    def __init__(self, nome: str) -> None:
        self.setNome(nome)
        self.__prezzo: float = 0.00
        self.__flotta: list[VoloCommerciale] = []

    def getNome(self) -> str:
        return self.__nome

    def setNome(self, value) -> None:
        self.__nome = value

    def getPrezzo(self) -> float:
        return self.__prezzo

    def getFlotta(self) -> list[VoloCommerciale]:
        return self.__flotta

    def aggiungi_volo(self, volo: VoloCommerciale) -> None:
        self.__flotta.append(volo)

    def rimuovi_volo(self, volo: VoloCommerciale) -> None:
        try:
            self.__flotta.remove(volo)
        except ValueError:
            print("Errore: volo non presente")

    def mostra_flotta(self) -> None:
        print(f"Ecco tutti i voli della compagnia aerea {self.getNome()}")
        for elem in self.getFlotta():
            print(f"Volo commerciale {elem.getCodice_volo()}")

    def guadagno(self):
        profit: float = 0
        for volo in self.getFlotta():
            profit += (
                volo.getPrenotazioniEconomica() +
                volo.getPrenotazioniBusiness() * 2 +
                volo.getPrenotazioniPrima() * 3
            ) * volo.getCosto_biglietto()
        return round(profit, 2)
with open ("Lezione_22/report.txt", "w") as file:
    sys.stdout = file
    print("File di report di Gestione Voli")
    print()
    print()
    volo1 = VoloCommerciale("COM123", 100, 50.75)
    print(volo1.posti_disponibili())
    volo1.prenota_posto(70, "economica")
    print(volo1.posti_disponibili())
    volo1.prenota_posto(20, "business")
    print(volo1.posti_disponibili())
    volo1.prenota_posto(70, "prima classe")  # Errore
    print(volo1.posti_disponibili())
    volo1.prenota_posto(10, "prima")
    print(volo1.posti_disponibili())
    volo1.prenota_posto(10, "prima")
    print(volo1.posti_disponibili())

    volo2 = VoloCharter("CHA456", 200, 20000)
    volo2.prenota_posto()
    volo2.prenota_posto()

    volo3 = VoloCommerciale("COM456", 200, 50.75)
    volo3.prenota_posto(100, "economica")  # Errore (classe non riconosciuta)
    volo3.prenota_posto(100, "economica")  # Valido

    compagnia = CompagniaAerea("ITA")
    compagnia.aggiungi_volo(volo1)
    compagnia.aggiungi_volo(volo3)
    compagnia.mostra_flotta()
    print(f"La compagnia {compagnia.getNome()} ha guadagnato {compagnia.guadagno()}")
