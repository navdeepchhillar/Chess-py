# Define base Piece class and all specific pieces

class Piece:
    def __init__(self, color):
        self.color = color  # 'white' or 'black'
        self.symbol = '?'

    def __str__(self):
        return self.symbol

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'white' else 'p'

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'white' else 'r'

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'white' else 'n'

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'white' else 'b'

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'white' else 'q'

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'white' else 'k'

# Board class with piece setup and display

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Black pieces (top)
        self.grid[0] = [
            Rook('black'), Knight('black'), Bishop('black'), Queen('black'),
            King('black'), Bishop('black'), Knight('black'), Rook('black')
        ]
        self.grid[1] = [Pawn('black') for _ in range(8)]

        # Empty squares
        for row in range(2, 6):
            self.grid[row] = [None for _ in range(8)]

        # White pieces (bottom)
        self.grid[6] = [Pawn('white') for _ in range(8)]
        self.grid[7] = [
            Rook('white'), Knight('white'), Bishop('white'), Queen('white'),
            King('white'), Bishop('white'), Knight('white'), Rook('white')
        ]

    def display(self):
        print("    a  b  c  d  e  f  g  h")
        print("  +" + "---+" * 8)
        for row in range(8):
            row_str = f"{8 - row} |"
            for col in range(8):
                piece = self.grid[row][col]
                row_str += f" {str(piece) if piece else '.'} |"
            print(row_str + f" {8 - row}")
            print("  +" + "---+" * 8)
        print("    a  b  c  d  e  f  g  h\n")

# Game class to run the board

class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        print("Welcome to Manual Python Chess!")
        self.board.display()

if __name__ == "__main__":
    game = Game()
    game.start()
