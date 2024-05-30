class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def is_valid_move(self, from_pos, to_pos):
        return False


class Pawn(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Pawns can only move forward one square, but capture diagonally
        if self.color == 'white':
            return to_pos == (from_pos[0] - 1, from_pos[1]) or \
                to_pos in [(from_pos[0] - 1, from_pos[1] - 1), (from_pos[0] - 1, from_pos[1] + 1)]
        else:
            return to_pos == (from_pos[0] + 1, from_pos[1]) or \
                to_pos in [(from_pos[0] + 1, from_pos[1] - 1), (from_pos[0] + 1, from_pos[1] + 1)]


class Rook(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Rooks can move any number of squares along a row or column
        return from_pos[0] == to_pos[0] or from_pos[1] == to_pos[1]


class Knight(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Knights can move to any square that is two squares horizontally and one square vertically away,
        # or two squares vertically and one square horizontally away
        return to_pos in [(from_pos[0] + 2, from_pos[1] + 1), (from_pos[0] + 2, from_pos[1] - 1),
                          (from_pos[0] - 2, from_pos[1] + 1), (from_pos[0] - 2, from_pos[1] - 1),
                          (from_pos[0] + 1, from_pos[1] + 2), (from_pos[0] + 1, from_pos[1] - 2),
                          (from_pos[0] - 1, from_pos[1] + 2), (from_pos[0] - 1, from_pos[1] - 2)]


class Bishop(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Bishops can move any number of squares diagonally
        return abs(from_pos[0] - to_pos[0]) == abs(from_pos[1] - to_pos[1])


class Queen(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Queens can move any number of squares along a row, column, or diagonal
        return Rook(self.color, from_pos).is_valid_move(from_pos, to_pos) or \
            Bishop(self.color, from_pos).is_valid_move(from_pos, to_pos)


class King(Piece):
    def is_valid_move(self, from_pos, to_pos):
        # Kings can move one square in any direction
        return abs(from_pos[0] - to_pos[0]) <= 1 and abs(from_pos[1] - to_pos[1]) <= 1
