def summer_69(lista:list[int])-> int:
    somma: int = 0
    flag: bool = False
    for i in lista:
        if flag:
            if i == 9:
                flag = False
        else:
            if i == 6:
                flag = True
            else:
                somma += i
    return somma

l1 = [1,3,5]
l2 = [4,5,6,7,8,9]
l3 = [2,1,6,9,11]

#check
assert summer_69(l1) == 9, "Test fallito per l1"
assert summer_69(l2) == 9, "Test fallito per l2"
assert summer_69(l3) == 14, "Test fallito per l3"
print("Tutti i test sono stati superati con successo!")

#versione con while
def summer_69_while(lista:list[int])-> int:
    somma: int = 0
    i: int = 0
    flag: bool = False
    while i < len(lista):
        if flag:
            if lista[i] == 9:
                flag = False
        else:
            if lista[i] == 6:
                flag = True
            else:
                somma += lista[i]
        i += 1
    return somma