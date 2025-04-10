def iscrivi_studenti(corso, posti_occupati):
    """Iscrive uno studente al corso se ci sono posti disponibili."""
    if posti_occupati < 100:
        posti_occupati += 1
        print(f"Iscrizione avvenuta con successo. Posti occupati: {posti_occupati}")
    else:
        print("Non ci sono più posti disponibili per questo corso.")
    return posti_occupati

def annulla_iscrizione(corso, posti_occupati):
    """Annulla un'iscrizione se ci sono studenti iscritti."""
    if posti_occupati > 0:
        posti_occupati -= 1
        print(f"Iscrizione annullata. Posti occupati: {posti_occupati}")
    else:
        print("Nessuna iscrizione da annullare.")
    return posti_occupati

def visualizza_stato(corso, posti_occupati):
    """Mostra il numero di posti liberi e occupati nel corso."""
    posti_liberi = 100 - posti_occupati
    print(f"Corso: {corso}\nPosti occupati: {posti_occupati}\nPosti liberi: {posti_liberi}")

def main():
    """Gestisce il menu interattivo."""
    corso = input("Inserisci il nome del corso: ").strip()
    posti_occupati = 0
    
    while True:
        print("\nOpzioni disponibili:")
        print("1. Iscrivi uno studente ('iscrivi')")
        print("2. Annulla un'iscrizione ('annulla')")
        print("3. Visualizza lo stato ('visualizza')")
        print("4. Elimina il corso e inserisci un nuovo corso ('elimina')")
        print("5. Esci ('esci')")
        
        scelta = input("Scegli un'opzione: ").strip().lower()

        match scelta:
            case "iscrivi":
                posti_occupati = iscrivi_studenti(corso, posti_occupati)
            case "annulla":
                posti_occupati = annulla_iscrizione(corso, posti_occupati)
            case "visualizza":
                visualizza_stato(corso, posti_occupati)
            case "elimina":
                corso = input("Inserisci il nuovo nome del corso: ").strip()
                posti_occupati = 0 
                print(f"Il corso è stato cambiato in '{corso}' con 100 posti disponibili.")
            case "esci":
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()
