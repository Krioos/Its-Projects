class Resturant():
    def __init__(self):
        self.name: str  = self.getname()
        self.cuisine: str = self.getcuisine()
        self.number_served = self.set_number_served()
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
    def set_number_served(self, number_served = 0):
        try:
            number_served = int(input("Set number of customer served: "))
            print(number_served)
        except Exception:
            print("Error invalid number")
        print(f"{number_served} served!!")
        return number_served

    def increment_number(self):
        self.number_served += self.set_number_served()
        print(f"{self.number_served} clients served in total today!!")


    def describe_resturant(self) -> None:
        print(f"{self.name}, {self.cuisine} cuisine")
    
    def open_resturant(self) -> None:
        print(f"{self.name} is now open!")



resturant_list = [Resturant() for _ in range (3)]


resturant_list[0].increment_number()