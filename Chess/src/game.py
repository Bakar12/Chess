from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def play(self):
        while not self.is_game_over():
            self.board.display()
            from_pos = input('Enter from position: ')
            to_pos = input('Enter to position: ')
            if self.is_valid_move(from_pos, to_pos):
                self.board.move_piece(from_pos, to_pos)
                self.switch_turn()

    def is_valid_move(self, from_pos, to_pos):
        # Validate move based on the game rules
        pass

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def is_game_over(self):
        # Check if the game is over
        pass
