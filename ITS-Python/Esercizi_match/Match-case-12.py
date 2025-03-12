print("Inserire un giorno ed un mese entrambi in formato numerico")
data:tuple = (int(input("Inserire il giorno: ")), int(input("Inserire il mese: ")))

festivity:dict = {
    (1, 1): "Capodanno",
    (14, 2): "San Valentino",
    (2, 6): "Festa della Repubblica",
    (15, 8): "Ferragosto",
    (31, 10): "Halloween",
    (25, 12): "Natale"
}

match data:
    case _ if data in festivity.keys():
        print(f"Il {data[0]}/{data[1]} è {festivity[data]}")
    case _:
        print("Nessuna festività in questa data")
