class Media():
    valutazioni: dict[int, str] = {
            1: "Terribile",
            2: "Brutto",
            3: "Normale",
            4: "Bello",
            5: "Grandioso"
        }
    def __init__(self, title: str)-> None:
        self.__title = title
        self.__reviews: list[int] = []

    @property
    def title(self)-> str:
        return self.__title
    
    @title.setter
    def title(self, value: str)-> None:
        if isinstance(value, str):
            self.__title = value
        else:
            print("Valore non corretto impostazione default")
            self.__title = "Titolo generico"
    
    @property
    def reviews(self)-> list[int]:
        return self.__reviews
    
    def aggiungiValutazione(self, voto: int)-> None:
        if 1 <= voto <= 5:
            self.__reviews.append(voto)
        else:
            print(f"Il voto {voto} non è un formato corretto")
    
    def getMedia(self)-> float:
        if self.reviews:
            return round(sum(self.reviews) / len(self.reviews), 2)
        else:
            return 0.00

    def getRate(self)-> str:
        return Media.valutazioni[round(self.getMedia())]

    def ratePercentage(self, voto: int)-> str:
        if self.reviews:
            return f"{self.reviews.count(voto) / len(self.reviews) * 100}%"
        else:
            return f"0%"

    def recensione(self)-> None:
        print(f"Titolo del Film: {self.title}")
        print(f"voto Medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")
        for k,v in Media.valutazioni.items():
            print(f"{v}: {self.ratePercentage(k)}")

class Film(Media):
    def __init__(self, title:str)-> None:
        super().__init__(title)


def main():
    # Creazione dei film
    film1 = Film("Il Ritorno del Codice")
    film2 = Film("Python: Odissea Digitale")

    # Aggiunta delle recensioni al primo film
    recensioni_film1 = [5, 4, 5, 4, 3, 5, 4, 5, 5, 4]
    for voto in recensioni_film1:
        film1.aggiungiValutazione(voto)

    # Aggiunta delle recensioni al secondo film
    recensioni_film2 = [2, 3, 3, 2, 4, 1, 2, 3, 2, 3]
    for voto in recensioni_film2:
        film2.aggiungiValutazione(voto)

    # Stampa delle recensioni
    film1.recensione()
    print("\n" + "="*40 + "\n")
    film2.recensione()

main()