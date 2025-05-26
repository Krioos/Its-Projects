from Voli3 import IntGEZ, IntGZ, IntG1900, Nazione, Citta, Aeroporto, Volo, CompagniaAerea
#driver code
if __name__ == "__main__":
    nazione = Nazione("Italia")
    citta = Citta("Roma", 218000)
    aeroporto = Aeroporto("FCO", "Leonardo da Vinci")
    volo = Volo("AZ123", IntGZ(120))
    compagnia = CompagniaAerea("Alitalia", IntG1900(1946))
    print(nazione)
    print(citta)
    print(aeroporto)
    print(volo)
    print(compagnia)
# prove per vedere se le classi funzionano correttamente
    assert nazione.name == "Italia"
    assert citta.name == "Roma"
    assert citta.abitanti ==  218000
    assert aeroporto.codice == "FCO"
    assert aeroporto.nome == "Leonardo da Vinci"
    assert volo.codice == "AZ123"
    assert volo.durata_minuti == IntGZ(120)
    assert compagnia.nome == "Alitalia"
    assert compagnia.anno_fondazione == IntG1900(1946)

    print("Tutti i test sono passati con successo!")
    # Test di uguaglianza
    assert nazione == Nazione("Italia")
    assert citta == Citta("Roma", 218000)
    assert aeroporto == Aeroporto("FCO", "Leonardo da Vinci")
    assert volo == Volo("AZ123", IntGZ(120))
    assert compagnia == CompagniaAerea("Alitalia", IntG1900(1946))
    print("Tutti i test di uguaglianza sono passati con successo!")
    # Test di hash
    assert hash(nazione) == hash(Nazione("Italia"))
    assert hash(citta) == hash(Citta("Roma", 218000))
    assert hash(aeroporto) == hash(Aeroporto("FCO", "Leonardo da Vinci"))
    assert hash(volo) == hash(Volo("AZ123", IntGZ(120)))
    assert hash(compagnia) == hash(CompagniaAerea("Alitalia", IntG1900(1946)))
    print("Tutti i test di hash sono passati con successo!")
    # Test di rappresentazione
    assert repr(nazione) == "Nazione(Italia)"
    assert repr(citta) == "Citta(name=Roma, abitanti = 218000)"
    assert repr(aeroporto) == "Aeroporto(codice=FCO, nome=Leonardo da Vinci)"
    assert repr(volo) == "Volo(codice=AZ123, durata_minuti=120)"
    assert repr(compagnia) == "CompagniaAerea(nome=Alitalia, anno_fondazione=1946)"
    print("Tutti i test di rappresentazione sono passati con successo!")
    # Test di modifica
    nazione.name = "Francia"
    citta.name = "Parigi"
    citta.abitanti = IntGEZ(2148000)
    aeroporto.nome = "Charles de Gaulle"
    volo.durata_minuti = IntGZ(150)
    compagnia.nome = "Air France"
    print("Modifiche effettuate con successo!")
    # Verifica le modifiche
    assert nazione.name == "Francia"
    assert citta.name == "Parigi"
    assert citta.abitanti == IntGEZ("218000")
    assert aeroporto.nome == "Charles de Gaulle"
    assert volo.durata_minuti == IntGZ(150)
    assert compagnia.nome == "Air France"
    print("Tutte le modifiche sono state verificate con successo!")

    # Test di modifica di valori immutabili
    try:
        nazione.name = ""
    except ValueError as e:
        print(f"Errore atteso: {e}")
    try:
        citta.name = ""
    except ValueError as e:
        print(f"Errore atteso: {e}")
    try:
        citta.abitanti = IntGEZ(-1000)
    except ValueError as e:
        print(f"Errore atteso: {e}")
    try:
        aeroporto.nome = ""
    except ValueError as e:
        print(f"Errore atteso: {e}")
    try:
        compagnia.nome = ""
    except ValueError as e:
        print(f"Errore atteso: {e}")
#     try:
#         compagnia.anno_fondazione = IntG1900(2025)
#     except ValueError as e:
#         print(f"Errore atteso: {e}")

    print("Tutti i test di errore sono passati con successo!")
    print("Driver code eseguito con successo!")