import json
PATH = "Lezione_15/Esercizi/Esercizio3/json3.json"
dictionary = {}
with open(PATH, mode = "r")as file:
    dictionary = json.load(file)

dictionary["UQFHUQFOIEFHIQ9343FEQF"] = {
    "nome": "Anna",
    "cognome": "Karenina",
    "age": 22
}

with open(PATH, mode = "w")as file:
    json.dump(dictionary, file, indent=4)
