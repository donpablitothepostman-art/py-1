class game:
    def __init__(self):
        self.is_game = True
        self.turn = "O"
        self.board = [" "] * 9

    def game_over(self, winner: str):
        print("game over!")
        self.print_board()
        print(f"the winner is {winner}")

    def print_board(self):
        for row in range(0, 9, 3):
            print(f"{self.board[row]}|{self.board[row+1]}|{self.board[row+2]}")

    def play_turn(self):
        print("It is now " + ("Naught" if self.turn == "O" else "Cross") + "'s turn.")
        self.print_board()
        while True:
            try:
                go = int(input("[1-9]> ").strip())
            except ValueError:
                self.print_board()
                print("Invalid input.")
                continue
            if 1 <= go <= 9 and self.board[go-1] == " ":
                break
            self.print_board()
            print("Invalid input.")
        self.board[go-1] = self.turn

    def check_board(self, board):
        # rows
        for row in range(0, 9, 3):
            if board[row] == board[row+1] == board[row+2] != " ":
                self.is_game = False
        # columns
        for col in range(3):
            if board[col] == board[col+3] == board[col+6] != " ":
                self.is_game = False
        # diagonals
        if board[0] == board[4] == board[8] != " ":
            self.is_game = False
        if board[2] == board[4] == board[6] != " ":
            self.is_game = False

    def check_draw(self, board):
        return " " not in board

    def main(self):
        while self.is_game:
            self.play_turn()
            self.check_board(self.board)
            if not self.is_game:
                self.game_over("Naught" if self.turn == "O" else "Cross")
                self.print_board()
                break
            if self.check_draw(self.board):
                self.game_over("Nobody")
                break
            # change turn
            self.turn = "X" if self.turn == "O" else "O"


if __name__ == "__main__":
    newgame = game()
    newgame.main()
