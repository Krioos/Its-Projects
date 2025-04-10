coordinate:tuple = (float(input("Inserire la coordinata x: ")), float(input("Inserire la coordinata y: ")))

match coordinate:
    case (0,0):
        print("Il punto è nell'origine")
    case (_, 0):
        print("Il punto è sull'asse X")
    case(0, _):
        print("Il punto è sull'asse Y")
    case _ if coordinate[0] > 0 and coordinate[1] > 0:
        print("Il punto si trova nel primo quadrante")
    case _ if coordinate[0] < 0 and coordinate[1] > 0:
        print("Il punto si trova nel secondo quadrante")
    case _ if coordinate[0] < 0 and coordinate[1] < 0:
        print("Il punto si trova nel terzo quadrante")
    case _ if coordinate[0] > 0 and coordinate[1] < 0:
        print("Il punto si trova nel quarto quadrante")
    case _:
        print("Punto non classificabile")