def baricentro(v:list[int])-> int | None:
    for i in range(len(v)):
        if i == len(v) - 1:
            if sum(v) == 0:
                return i
            else:
                return None
        elif sum(v[:i+1]) == sum(v[i+1:]):
            return i
    return None

def baricentroOttimizzato(v:list[int])-> int | None:
    somma = sum(v)
    sum_second = 0
    for i in range(len(v)):
        sum_second += v[i]
        if sum_second == somma - sum_second:
            return i
    return None

def printResult(v:list[int])-> None:
    result = baricentro(v)
    if result:
        print(f"Esiste il baricentro del vettore v={v} ed è indice i={result}!")
    else:
        print(f"Il baricentro del vettore v={v} non esiste!")

def printResultOttimizzata(v:list[int])-> None:
    result = baricentroOttimizzato(v)
    if result:
        print(f"Esiste il baricentro del vettore v={v} ed è indice i={result}!")
    else:
        print(f"Il baricentro del vettore v={v} non esiste!")



v1 = [1, 2, 3, 2, 5, 2, 1]

v2 = [2, 0, -1, 4, 6, 3, -1]

printResult(v1)
printResult(v2)
printResultOttimizzata(v1)
printResultOttimizzata(v2)
