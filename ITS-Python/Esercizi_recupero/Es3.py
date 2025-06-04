def my_dict(dizionario:dict)-> dict:
    result = {}
    for k,v in dizionario.items():
        if v < 50:
            result[k] = round(v *1.1, 2)
    return result


dizionario = {
    "Pesce": 33.5,
    "Carne": 44.99,
    "Pallone": 10.99,
    "Tv": 200
}

nuovo_diz = my_dict(dizionario)
print(nuovo_diz)