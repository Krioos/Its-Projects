utente: dict = {"nome": input("Inserisci il tuo nome: ").lower().strip(),
                "età": int(input("Inserisci la tua età: ").lower().strip()),
                "ruolo": input("Inserisci il tuo ruolo: ").lower().strip()
                }


match utente:
    case utente if utente["ruolo"] == "admin":
        print(f"Salve {utente['nome']}. Accesso completo a tutte le funzionalità.")
    case utente if utente['ruolo'] == "moderatore":
        print(f"Salve {utente['nome']}. Può gestire i contenuti ma non modificare le impostazioni.")
    case utente if utente['ruolo'] == "utente" and utente["età"] >= 18:
        print(f"Salve {utente['nome']}. Accesso standard a tutti i servizi.")
    case utente if utente['ruolo'] == "utente" and utente["età"] < 18:
        print(f"Salve {utente['nome']}. Accesso limitato! Alcune funzionalità sono bloccate.")
    case _:
        print(f"Errore {utente['ruolo']} non riconosciuto come ruolo")


match (utente["ruolo"], utente["età"]):
    case ("admin", _):
        print(f"Salve {utente['nome']}. Accesso completo a tutte le funzionalità.")
    case ("moderatore", _):
        print(f"Salve {utente['nome']}. Può gestire i contenuti ma non modificare le impostazioni.")
    case("utente", age) if age >= 18:
        print(f"Salve {utente['nome']}. Accesso standard a tutti i servizi.")
    case("utente", age) if age < 18:
        print(f"Salve {utente['nome']}. Accesso limitato! Alcune funzionalità sono bloccate.")
    case _:
        print(f"Errore {utente['ruolo']} non riconosciuto come ruolo")