from random import randint
class D6():
    def __init__(self, sides:int = 6) -> None:
        self.sides = sides

    def rolldice(self) -> None:
        print(f"Rolled {randint(1,self.sides)}")
    def dice_type(self):
        print(f"This a {self.sides} sided dice")

class D10():
    def __init__(self, sides:int = 10) -> None:
        self.sides = sides

    def rolldice(self) -> None:
        print(f"Rolled {randint(1,self.sides)}")
    def dice_type(self):
        print(f"This a {self.sides} sided dice")

class D20():
    def __init__(self, sides:int = 20) -> None:
        self.sides = sides

    def rolldice(self) -> None:
        rolled = randint (1, self.sides)
        if rolled == 20:
            print(f"Rolled {rolled} a critical hit!!")
        elif rolled == 1:
            print(f"Rolled {rolled} a critical miss!!")
        else:
            print(f"Rolled {randint(1,self.sides)}")
    def dice_type(self):
        print(f"This a {self.sides} sided dice")
dices:list[object] = [D6(), D10(), D20()] 
for i in dices:
    i.dice_type()
    for _ in range(10):
        i.rolldice()
