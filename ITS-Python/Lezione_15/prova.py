# prova di apertura file di testo 
'''
file = open("example.txt")
print(file) 

'''
import json 
#prova di lettura di file json esistente
'''
PATH:str  = "Lezione_15/config.json"
mode:str = "r"

with open(PATH, mode = mode) as file:
    config: dict = json.load(file)

    print(config)

    nome_applicazione:str  = config["app_name"]
    print(nome_applicazione)

    host = config["server"]["host"]
    port = config["server"]["port"]

    print(f"host: {host}\nport: {port}")
'''
# prova di scrittura di file json
'''
PATH:str =  "Lezione_15/prova_scrittura.json"
mode:str = "w"

with open(PATH, mode = mode) as file:
    config:dict = {
        "nome": "2048",
        "versione": "1.1.42",
        "OS": "Android 16.1.0"
    }
    json.dump(config, file, indent = 4)
'''
# prova modifica file

PATH:str  = "Lezione_15/config.json"
mode:str = "r"
config = {}

with open(PATH, mode = mode) as file:
    config: dict = json.load(file)

config["server"]["host"] = "prova_modificata"
config["server"]["port"] = 5000

with open(PATH, mode = "w") as file:
    json.dump(config, file, indent = 4)
