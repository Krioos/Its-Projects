from Media import Media

class Movie(Media):
    def __init__ (self, title:str, year:int, time:int)-> None:
        super().__init__(title, year)
        self.set_time(time)

    def set_time(self,time):
        if time:
            self.time = time
        else:
            print("Errore")

    def get_time(self)-> int:
        return self.time
    
    def __str__(self):
        return f"{super().__str__()}, Durata: {self.time}"
        


film1  = Movie("GG", 2013, 34)
print(film1)