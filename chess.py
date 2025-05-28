class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, board, start, end):
        # Override in child classes
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, board, start, end):
        # Implement pawn movement logic
        return True  # placeholder

# Repeat for Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        # Place pieces here
        return board

    def print_board(self):
        for row in self.grid:
            print(" ".join([piece.symbol if piece else "." for piece in row]))

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'

    def play(self):
        while True:
            self.board.print_board()
            move = input(f"{self.turn}'s move (e.g., e2 e4): ")
            # Handle move, validate, and switch turns
