import psycopg2
import random
from datetime import date, timedelta
try:
    conn = psycopg2.connect(
        host = "localhost",
        database = "accademia",
        user = "postgres",
        password = "postgres"
    )

    print("Connessione riuscita")

    cur = conn.cursor()

    # Dati base
    nomi = ["Luca", "Maria", "Giulia", "Paolo", "Chiara", "Marco", "Anna", "Luigi", "Elisa", "Davide"]
    cognomi = ["Rossi", "Bianchi", "Verdi", "Neri", "Russo", "Gallo", "Ferrari", "Esposito", "Colombo", "Romano"]
    posizioni = ["Ricercatore", "Professore Associato", "Professore Ordinario"]
    lavori_progetto = ["Ricerca e Sviluppo", "Dimostrazione", "Management", "Altro"]
    lavori_non_proj = ["Didattica", "Ricerca", "Missione", "Incontro Dipartimentale", "Incontro Accademico", "Altro"]
    assenze = ["Chiusura Universitaria", "Maternita", "Malattia"]

    def rand_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # Inserisci persone
    for i in range(1, 21):
        cur.execute("""
            INSERT INTO Persona (id, nome, cognome, posizione, stipendio)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            i,
            random.choice(nomi),
            random.choice(cognomi),
            random.choice(posizioni),
            round(random.uniform(25000, 80000), 2)
        ))

    # Inserisci progetti
    for i in range(1, 6):
        inizio = rand_date(date(2022, 1, 1), date(2022, 12, 31))
        fine = inizio + timedelta(days=random.randint(180, 360))
        cur.execute("""
            INSERT INTO Progetto (id, nome, inizio, fine, budget)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            i,
            f"Progetto {i}",
            inizio,
            fine,
            round(random.uniform(100000, 500000), 2)
        ))

    # Inserisci WP (Work Package)
    wp_id = 1
    for progetto_id in range(1, 6):
        for j in range(1, 4):  # 3 WP per progetto
            inizio = rand_date(date(2022, 1, 1), date(2022, 12, 31))
            fine = inizio + timedelta(days=random.randint(60, 180))
            cur.execute("""
                INSERT INTO WP (progetto, id, nome, inizio, fine)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                progetto_id,
                j,
                f"WP{j}_Proj{progetto_id}",
                inizio,
                fine
            ))

    # Inserisci AttivitaProgetto
    for i in range(1, 51):
        persona_id = random.randint(1, 20)
        progetto_id = random.randint(1, 5)
        wp_id = random.randint(1, 3)
        giorno = rand_date(date(2023, 1, 1), date(2023, 12, 31))
        cur.execute("""
            INSERT INTO AttivitaProgetto (id, persona, progetto, wp, giorno, tipo, oreDurata)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            i,
            persona_id,
            progetto_id,
            wp_id,
            giorno,
            random.choice(lavori_progetto),
            random.randint(1, 8)
        ))

    # Inserisci AttivitaNonProgettuale
    for i in range(1, 41):
        persona_id = random.randint(1, 20)
        giorno = rand_date(date(2023, 1, 1), date(2023, 12, 31))
        cur.execute("""
            INSERT INTO AttivitaNonProgettuale (id, persona, tipo, giorno, oreDurata)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            i,
            persona_id,
            random.choice(lavori_non_proj),
            giorno,
            random.randint(1, 8)
        ))

    # Inserisci Assenze
    assenze_set = set()
    i = 1
    while len(assenze_set) < 20:
        persona_id = random.randint(1, 20)
        giorno = rand_date(date(2023, 1, 1), date(2023, 12, 31))
        if (persona_id, giorno) not in assenze_set:
            assenze_set.add((persona_id, giorno))
            cur.execute("""
                INSERT INTO Assenza (id, persona, tipo, giorno)
                VALUES (%s, %s, %s, %s)
            """, (
                i,
                persona_id,
                random.choice(assenze),
                giorno
            ))
            i += 1

    # Conferma e chiudi
    conn.commit()
    cur.close()
    conn.close()
    print("Dati inseriti con successo")
except Exception as e:
    print("Errore nella connessione:", e)