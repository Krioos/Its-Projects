def calcola_tempo_semaforo(nord_sud, est_ovest, soglia):
    '''Calcola la percentuale di tempo assegnata a ciascuna direzione del semaforo.'''
    if nord_sud > soglia and est_ovest > soglia:
        time_ns, time_eo = 50, 50
    elif nord_sud > soglia:
        time_ns, time_eo = 60, 40
    elif est_ovest > soglia:
        time_ns, time_eo = 40, 60
    else:
        totale = nord_sud + est_ovest
        if totale == 0:
            time_ns, time_eo = 50, 50
        else:
            time_ns = (nord_sud / totale) * 100
            time_eo = 100 - time_ns
    
    return time_ns, time_eo

def main():
    '''Gestisce l'input dell'utente e mostra i risultati.'''
    try:
        nord_sud = int(input("Inserire il numero di veicoli dalla direzione Nord-Sud: "))
        est_ovest = int(input("Inserire il numero di veicoli dalla direzione Est-Ovest: "))
        soglia = int(input("Inserire il valore soglia: "))

        if nord_sud < 0 or est_ovest < 0 or soglia < 0:
            print("Errore: i valori devono essere numeri positivi.")
            return
        
        time_ns, time_eo = calcola_tempo_semaforo(nord_sud, est_ovest, soglia)

        print(f"Il tempo assegnato alla direzione Nord-Sud è {time_ns:.2f}%")
        print(f"Il tempo assegnato alla direzione Est-Ovest è {time_eo:.2f}%")

    except ValueError:
        print("Errore: inserire solo numeri interi validi.")

if __name__ == "__main__":
    main()
