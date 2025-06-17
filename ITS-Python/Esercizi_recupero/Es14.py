def merge_intervals(lista:list[list[int]]) -> list | list[list[int]]:
    """
    Restituisce una lista di intervalli uniti. Unisce gli intervalli che si sovrappongono.
    """
    if not lista:
        return []
    out_list: list[list[int]] = []
    i = 0
    while i in range(len(lista)):
        if i == len(lista) - 1:
            out_list.append(lista[i])
            break
        next: list[int] = lista[i+1]
        if lista[i][1] >= next[0]:
            out_list.append([lista[i][0], next[1]])
            i += 2
        else:
            out_list.append(lista[i])
            i += 1
    return out_list

lista =  [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(lista))  # Output: [[1, 6], [8, 10], [15, 18]]
lsita = [[1, 4], [4, 5]]
print(merge_intervals(lsita))  # Output: [[1, 5]]