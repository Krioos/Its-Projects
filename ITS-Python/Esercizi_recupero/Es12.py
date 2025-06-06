def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    """
    Calcola la somma degli elementi sulla diagonale principale di una matrice quadrata o rettangolare.
    """
    m = len(matrix)
    n = len(matrix[0])
    limit = min(m, n)
    result = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                result += matrix[i][j]
        if i == limit:
            break
    return result

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    """
    Calcola la somma degli elementi sulla diagonale secondaria di una matrice quadrata o rettangolare.
    """
    m = len(matrix)
    n = len(matrix[0])
    result = 0
    limit = min(m, n)
    for i in range(m):
        for j in range(n):
            if j == n - i - 1:
                result += matrix[i][j]
        if i == limit:
            break
    return result
# Esempio di utilizzo
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(sum_primary_diagonal(mat1)) # restituisce 1 + 5 + 9 = 15
print(sum_secondary_diagonal(mat1)) # restituisce 3 + 5 + 7 = 15

mat2 = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

print(sum_primary_diagonal(mat2)) # restituisce 1 + 6 + 11 = 18
print(sum_secondary_diagonal(mat2)) # restituisce 4 + 6 + 9 = 19