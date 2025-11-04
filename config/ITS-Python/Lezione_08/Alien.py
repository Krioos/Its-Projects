class Alien():

    def __init__(self, galaxy: str)-> None:
        self.galaxy = self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str)-> str:
        if galaxy:
            return galaxy
        else:
            print("Galaxy can't be empty")
    
    def getGalaxy(self)-> str:
        return self.galaxy
    
    def speak(slef)-> None:
        print(f"\nWW91IGhhdmUgY2FuY2VyCg==\n")
    
    def __str__(self)-> str:
        return (f"\nAlien form galaxy {self.getGalaxy()}")

