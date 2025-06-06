def binary_search(lista:list, x:int) -> bool:
    """
    Funzione che implementa la ricerca binaria in una lista ordinata.
    Restituisce True se l'elemento x è presente, altrimenti False.
    """
    try:
        x = int(x)
    except ValueError:
        raise ValueError("L'elemento da cercare deve essere un intero.")
    median_element: int = lista[len(lista) // 2]
    if x == median_element:
        return True
    elif x < median_element:
        for i in range (0, len(lista) // 2):
            if lista[i] == x:
                return True
    else:
        for i in range ((len(lista) //2) + 1, len(lista)):
            if lista[i] == x:
                return True
    return False
            


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lista, 5))  # True
print(binary_search(lista, 10)) # False
print(binary_search(lista, 1))  # True
print(binary_search(lista, 9))  # True