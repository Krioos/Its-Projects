def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    dict = {}
    for elem in tuples:
        k,v = elem
        if k in dict:
            dict[k].append(v)
        else:
            dict[k] = [v]
    
    return dict


print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))