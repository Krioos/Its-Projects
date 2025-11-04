n:int = int(input("Inserire il voto: "))

match n:
    case n if n == 10:
        print("Eccellente")
    case n if n >= 8 and n <= 9:
        print("Molto buono")
    case n if n >=6 and n <=7:
        print("Sufficiente")
    case n if n >= 4 and n <= 5:
        print("Insufficiente")
    case n if n >= 1 and n <= 3:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")