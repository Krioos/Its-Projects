import json

PATH =  "Lezione_15/Esercizi/Esercizio2/json2.json"
dict = {
    "fiscale1": "NTLLSS00E15H501Y",
    "fiscale2": "AFNJEQBOE1JOBOFB",
    "fiscale3": "IFOQBEFPBÈORÈBNSK"
}
with open(PATH, mode = "w", encoding="utf-8")as file:
    json.dump(dict, file, indent= 4)
