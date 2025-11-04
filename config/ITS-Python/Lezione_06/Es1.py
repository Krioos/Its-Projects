class Resturant():
    def __init__(self):
        self.name: str  = self.getname()
        self.cuisine: str = self.getcuisine()
        self.describe_resturant()
        self.open_resturant()


    def getname(slef) -> str:
        while True:
            name: str = input("Insert resturant name: ")
            if name:
                return name
            else:
                print("Error resturant name can't be empty ")

    
    def getcuisine(self) -> str:
        while True:
            cuisine: str = input("Insert the resturant cuisine: ")
            if cuisine:
                return cuisine
            else:
                print ("Error cuisine type can't be empty")
    
    def describe_resturant(self) -> None:
        print(f"{self.name}, {self.cuisine} cuisine")
    
    def open_resturant(self) -> None:
        print(f"{self.name} is now open!")



resturant_list = [Resturant() for _ in range (3)]
