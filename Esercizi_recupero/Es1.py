def converter(lista:list[tuple])-> dict:
    result = {}
    for elem in lista:
        k,v  = elem
        if k in result:
            result[k] += v
        else:
            result[k] = v

    return result


lista = lista = [
    ("k1", 10),
    ("k2", 25),
    ("k1", 10),  # duplicato di k1
    ("k4", 40)
]
dizionario = converter(lista)
print(dizionario)
