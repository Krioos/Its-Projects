class Media:
    """
    Attributi della classe Media:
    self.title: str
    self.year: int
    """
    def __init__(self, title:str, year:int):
        self.set_title(title)
        self.set_year(year)

    def set_title(self, title: str)-> None:
        if title:
            self.title = title
        else:
            print("Errore")

    def set_year(self, year: int)-> None:
        if year > 1000:
            self.year = year
        else:
            print("Errore")

    def get_title(self)-> str :
        return self.title
    
    def get_year(self)-> int:
        return self.year

    def __str__(self)-> str:
        return f"Titolo: {self.title}, Anno: {self.year}"