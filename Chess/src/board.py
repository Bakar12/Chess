import tkinter as tk

from PIL import Image, ImageTk

from Chess.src.pieces import Pawn


class Board:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Board")
        self.board = self.create_board()
        self.pieces = self.create_pieces()
        self.white_pawn_image = ImageTk.PhotoImage(Image.open("white_pawn.png"))
        self.black_pawn_image = ImageTk.PhotoImage(Image.open("black_pawn.png"))

    def create_pieces(self):
        # Create a 8x8 2D list with initial pieces setup
        pieces = [[None for _ in range(8)] for _ in range(8)]

        # Place white pawns on the second row
        for i in range(8):
            pieces[1][i] = Pawn('white', (1, i))

        # Place black pawns on the seventh row
        for i in range(8):
            pieces[6][i] = Pawn('black', (6, i))

        return pieces

    def create_board(self):
        # Create a 8x8 board with initial pieces setup
        board = tk.Canvas(self.window, width=400, height=400)
        board.pack()

        color = "white"
        for i in range(8):
            for j in range(8):
                x1 = j * 50
                y1 = i * 50
                x2 = x1 + 50
                y2 = y1 + 50
                if color == "white":
                    color = "black"
                else:
                    color = "white"
                board.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.pieces[i][j]
                if isinstance(piece, Pawn):
                    image = self.white_pawn_image if piece.color == 'white' else self.black_pawn_image
                    board.create_image(x1, y1, anchor='nw', image=image)
            if color == "white":
                color = "black"
            else:
                color = "white"

        return board

    def display(self):
        self.window.mainloop()

    def move_piece(self, from_pos, to_pos):
        # Code to move a piece
        pass
