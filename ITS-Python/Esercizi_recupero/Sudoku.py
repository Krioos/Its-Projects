def is_valid(board:list[list[int]], row: int, col: int, num: int) -> bool:
    # Controlla se num è nella riga
    if num in board[row]:
        return False

    # Controlla se num è nella colonna
    if num in [board[i][col] for i in range(9)]:
        return False

    # Controlla se num è nel quadrato 3x3
    start_row: int = row - row % 3
    start_col: int = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(board:list[list[int]])-> tuple | None:
    # Trova la prossima cella vuota (indicata con 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board:list[list[int]])-> bool:
    empty: tuple[int] = find_empty(board)
    if not empty:
        return True  # Risoluzione

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False  # Nessuna soluzione trovata

# Esempio di utilizzo
sudoku_board: list[list[int]] = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("Nessuna soluzione trovata.")