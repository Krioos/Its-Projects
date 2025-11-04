def sorting(lista:list)-> None:
    for i in range (len(lista)):
        for j in range (i + 1 , len(lista)):
            if lista[i] > lista[j]:
                lista[j], lista[i] = lista[i], lista[j]
                print (lista)



lista = [2, 5, 1, 4, 3, 6]
sorting(lista)

print(lista)