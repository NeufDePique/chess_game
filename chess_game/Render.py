import tkinter

class Render(tkinter.Canvas):
    def __init__(self, win, side = 528):
        super().__init__(win, width = side, height = side)
        self.side = side
        self.unit = side // 8
        self.draw_board(win.board)
        self.pack()

    def case_top_left(self, case):
        i, j = case
        return (i - 1) * self.unit, (j - 1) * self.unit

    def case_bottom_right(self, case):
        i, j = case
        return i * self.unit, j * self.unit

    def pos_to_units(self, pos):
        return pos[0] // self.unit + 1, pos[1] // self.unit + 1

    def draw_checker_pattern(self):
        """draws a checker patterned board"""
        for i in range(8):
            for j in range(8):
                self.create_rectangle(i * self.unit, j * self.unit, (i + 1) * self.unit, (j + 1) * self.unit,
                                      fill = ("white" if (i % 2 == j % 2) else "blue"))
                
    def draw_piece(self, piece):
        """draws any piece on the board"""
        x_left, y_top = self.case_top_left(piece.pos)
        x_right, y_bottom = self.case_bottom_right(piece.pos)
        if piece.activated:
            self.create_rectangle(x_left, y_top, x_right, y_bottom, fill = "red")
        self.create_image(x_left + self.unit / 2, y_top + self.unit / 2, image = piece.image)

    def draw_pieces(self, pieces):
        for piece in pieces:
            self.draw_piece(piece)

    def draw_move_set(self, move_set):
        for case in move_set:
            x_left, y_top = self.case_top_left(case)
            x_right, y_bottom = self.case_bottom_right(case)
            self.create_rectangle(x_left, y_top, x_right, y_bottom, fill = "red")

    def draw_board(self, board, move_set = []):
        self.delete("all")
        self.draw_checker_pattern()
        self.draw_move_set(move_set)
        self.draw_pieces(board.pieces)

    def inform_of_lameness(self, loser):
        self.delete("all")
        self.create_text(self.side / 2, self.side / 2, text = loser.name + " a perdu.")
