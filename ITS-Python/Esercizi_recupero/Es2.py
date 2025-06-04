from random import randint
def dizionario_diviso(lista:list)-> dict:
    dizionario = {"positivi": [], "negativi": []}
    for elem in lista:
        if elem >= 0:
            dizionario["positivi"].append(elem)
        else:
            dizionario["negativi"].append(elem)
    return dizionario


lista = [randint(-30, 30) for _ in range(8)]
dizionario = dizionario_diviso(lista)
print(dizionario)