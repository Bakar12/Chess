import tkinter as tk

class Board:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Board")
        self.board = self.create_board()

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