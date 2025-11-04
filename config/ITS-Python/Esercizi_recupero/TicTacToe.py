class TicTacToe():
    def __init__(self)-> None:
        self.board = [" " for _ in range(9)]
        self.human = "X"
        self.pc = "O"

    def __repr__(self) -> str:
        rows = []
        for i in range(3):
            row = " | ".join(self.board[i*3:(i+1)*3])
            rows.append(row)
        return "\n-----------\n".join(rows)

    def player1choice(self)-> None:
        while True:
            selection = int(input("Inserire una scelta tra 0 ed 8: "))
            if 0 <= selection <= 8 and self.board[selection] == " ":
                self.board[selection] = "X"
                break
            else:
                print("Scelta non valida")
                continue

    def player2choice(self)-> None:
        while True:
            selection = int(input("Inserire una scelta tra 0 ed 8: "))
            if 0 <= selection <= 8 and self.board[selection] == " ":
                self.board[selection] = "0"
                break
            else:
                print("Scelta non valida")
                continue

    def win(self)-> bool:
        

if __name__ == "__main__":
    print("Benvenuto al gioco di Tris")
    board = TicTacToe()
    turn = 1
    print(board)
    while True:
        if turn % 2 == 0:
            board.player2choice()
        else:
            board.player1choice()
        turn += 1
        print(board)
