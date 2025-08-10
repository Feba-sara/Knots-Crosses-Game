class KnotsAndCrosses:
    def __init__(self):
        # Initialize a 3x3 board with empty spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X starts

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        b = self.board
        # Check rows and columns
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != ' ':
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != ' ':
                return b[0][i]
        # Check diagonals
        if b[0][0] == b[1][1] == b[2][2] != ' ':
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != ' ':
            return b[0][2]
        return None

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        print("Welcome to Knots and Crosses!")
        while True:
            self.print_board()
            try:
                move = input(f"Player {self.current_player}, enter your move as row,col (0-based): ")
                row, col = map(int, move.split(','))
            except Exception:
                print("Invalid input. Please enter row and column as 'row,col'.")
                continue

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid position. Try again.")
                continue

            if not self.make_move(row, col):
                print("Cell already taken! Try another move.")
                continue

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = KnotsAndCrosses()
    game.play()