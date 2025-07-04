from FormaGenerica import FormaGeometrica

class Rettangolo(FormaGeometrica):
    def __init__ (self):
        super().__init__()
        self.setShape("Rettangolo")

    def draw(self)-> None:
        print(f"\n{self.getShape()}\n")
        base = int(input("Inserire la base del rettangolo: "))
        altezza = int(input("Inserire l'altezza del rettangolo: "))
        for i in range(altezza):
            for j in range(base):
                if i == 0 or i == altezza -1:
                    print("*", end="")
                else:
                    if j== 0 or j == base -1:
                        print("*", end="")
                    else:
                        print(" ", end="")
            print()