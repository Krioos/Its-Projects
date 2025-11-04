import json
PATH =  "Lezione_15/Esercizi/Esercizio1/json_1.json"

with open(PATH, mode = "r")as file:
    dictionary = json.load(file)
    print(dictionary["nome"])