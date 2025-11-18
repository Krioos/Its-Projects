import pandas as pd

## Esercizio 1: Carica il CSV in un DataFrame
## Task: Leggi i dati del file CSV fornito in un Pandas DataFrame e visualizza le prime 3 righe  
## Soluzione:
print("***ESERCIZIO 1***")
path = "Data/test/dati/some_music_albums.csv"
df: pd.DataFrame = pd.read_csv(path)
print(df.head(3))
print("*****************"+"\n")     
 
### Esercizio 2: Mostra informazioni di base sul DataFrame 
### Task: Mostra il numero di righe, colonne e tipi di dati per ogni colonna 
### Soluzione:
print("***ESERCIZIO 2***")
df.info()
print("*****************"+"\n")
 
### Esercizio 3: Filtra gli album per genere
### Task: Crea un nuovo DataFrame contenente solo gli album con "rock" nella colonna 'Genre'
### Soluzione:
print("***ESERCIZIO 3***")
rock_df: pd.DataFrame = df[df["Genre"].str.contains("rock", case=False, na=False)]
print(rock_df)
print("*****************"+"\n")

## Esercizio 4: Trova gli album pubblicati dopo il 1980
## Task: Filtra gli album pubblicati dopo il 1980 e visualizza solo le colonne 'Artist', 'Album' e 'Released'
## Soluzione:
print("***ESERCIZIO 4***")
after_1980: pd.DataFrame = df[df["Released"] > 1980][["Artist", "Album", "Released"]]
print(after_1980)
print("*****************"+"\n")

### Esercizio 5: Calcola la media delle valutazioni
### Task: Calcola la media della colonna 'Rating' per tutti gli album
### Soluzione:
print("***ESERCIZIO 5***")
avg: float = df["Rating"].astype("float").mean()
print(f"Average Rating: {avg}")
print("*****************"+"\n")

### Esercizio 6: Trova l'album più lungo e il più breve
### Task: Identifica l'album con la durata massima e minima nella colonna 'Length' e visualizza i suoi dettagli
### Soluzione:
print("***ESERCIZIO 6***")
def time_conversion(time:str)-> int:
    return int(time.split(":")[0]) * 3600 + int(time.split(":")[1]) * 60 + int(time.split(":")[2])
df["Length_seconds"] = df["Length"].apply(time_conversion)
length_max = df["Length_seconds"].idxmax()
lenght_min = df["Length_seconds"].idxmin()
longhest = df.loc[length_max]
shortest = df.loc[lenght_min]
print(f"Longhest: {longhest}")
print(f"Shortest: {shortest}")
print("*****************"+"\n")
 
### NON FARE
### Esercizio 7: Elenco generi unici
### Task: Estrai e stampa tutti i generi unici nel dataset (dividendo i generi combinati come "pop, rock")
### Soluzione:
print("***ESERCIZIO 7***")
genres = (
    df["Genre"]
    .dropna()                    # rimuove eventuali NaN
    .str.split(",")              # crea liste ["pop", " rock"]
    .explode()                   # trasforma le liste in righe singole
    .str.strip()                 # rimuove spazi extra
    .unique()                    # prende valori unici
)

print("Generi unici trovati:")
for g in sorted(genres):
    print("-", g)
print("*****************"+"\n")

### Esercizio 8: Confronta le vendite con vendite dichiarate
### Task: Aggiungi una nuova colonna 'Sales_Difference' che mostri la differenza tra 'Claimed Sales' e 'Music Recording Sales'
### Soluzione:
print("***ESERCIZIO 8***")

df["Sales_Difference"] = (
    df["Claimed Sales (millions)"] 
    - df["Music Recording Sales (millions)"]
)

print(df[["Artist", "Album", "Sales_Difference"]])
print("*****************"+"\n")
  
### Esercizio 9: Trova gli album colonna sonora
### Task: Elenca tutti gli album contrassegnati come 'Soundtrack' (dove la colonna è "Y")
### Soluzione:
print("***ESERCIZIO 9***")

soundtracks = df[df["Soundtrack"] == "Y"]

print(soundtracks)
print("*****************"+"\n")

### Esercizio 10: Salva i dati filtrati in un file CSV
### Task: Salva tutti gli album con una valutazione (Rating) ≥ 9 in un nuovo file CSV
### Soluzione:
print("***ESERCIZIO 10***")

# Filtra tutti gli album con Rating ≥ 9
top_rated = df[df["Rating"].astype(float) >= 9]

# Salva in un nuovo file CSV
top_rated.to_csv("Data/test/dati/top_rated_albums.csv", index=False)

print("File salvato come: top_rated_albums.csv")

print("******************"+"\n")

### NON FARE  
### Esercizio 11: Conta gli album per genere
### Task:Conta quanti album appartengono a ogni genere unico (dividendo generi combinati come "pop, rock")
### Soluzione:  
print("***ESERCIZIO 11***")

print("******************"+"\n")

### Esercizio 12: Trova l'album con la maggior differenza tra vendite e vendite dichiarate
### Task: Identifica l'album con la maggiore differenza tra 'Claimed Sales' e 'Music Recording Sales' e visualizza i suoi dettagli
### Soluzione:  
print("***ESERCIZIO 12***")

# Se la colonna non esiste, ricreala
df["Sales_Difference"] = (
    df["Claimed Sales (millions)"] 
    - df["Music Recording Sales (millions)"]
)

# Trova l'indice dell'album con la differenza maggiore
idx_max_diff = df["Sales_Difference"].idxmax()

# Estrai tutti i dettagli dell'album
max_diff_album = df.loc[idx_max_diff]

print("Album con la maggior differenza tra vendite dichiarate e registrate:")
print(max_diff_album)

print("******************"+"\n")
  
### Esercizio 13: Filtra gli album per generi multipli
### Task: Crea un nuovo DataFrame contenente gli album che includono entrambi "rock" e "pop" nella colonna 'Genre'
### Soluzione:**  
print("***ESERCIZIO 13***")

multi_genre = df[
    df["Genre"].str.contains("rock", case=False, na=False)
    & df["Genre"].str.contains("pop", case=False, na=False)
]

print(multi_genre)
print("******************"+"\n")

### NON FARE    
### Esercizio 14: Calcola la durata media per genere
### Task: Calcola la media della durata (in minuti) degli album per ogni genere (dividendo generi combinati)
### Soluzione:  
print("***ESERCIZIO 14***")

print("******************"+"\n")

### Esercizio 15: Trova l'album più venduto che non è una colonna sonora
### Task: Identifica l'album con le maggiori 'Music Recording Sales' che non è una colonna sonora
### Soluzione:  
print("***ESERCIZIO 15***")

print("******************"+"\n")
