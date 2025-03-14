def ingresso():
    global posti_liberi
    if posti_liberi > 0:
        posti_liberi -= 1
        print(f"Posto prenotato, posti restanti {posti_liberi}")
    else:
        print("Mi dispiace, non ci sono più posti liberi.")

def uscita():
    global posti_liberi
    if posti_liberi < posti:
        posti_liberi += 1
        print(f"Posto liberato, posti restanti {posti_liberi}")
    else:
        print("Mi dispiace, tutti i posti sono già liberi.")

def stato():
    print(f"Al momento nel parcheggio ci sono {posti_liberi} posti liberi e {posti - posti_liberi} posti occupati.")

def main():
    while True:
        opzione = input("Cosa si vuole fare?\nOpzioni disponibili:\nIngresso\nUscita\nStato\nEsci\n: ").lower().strip()
        
        match opzione:
            case "ingresso":
                ingresso()
            case "uscita":
                uscita()
            case "stato":
                stato()
            case "esci":
                print("Uscita dal programma.")
                break
            case _:
                print("Comando non valido, riprova.")

if __name__ == '__main__':
    posti = int(input("Quanti posti ha il parcheggio?: "))
    posti_liberi = posti
    main()
