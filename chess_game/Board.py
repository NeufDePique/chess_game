import tkinter
import inspect
import Pieces
from Piece import Piece

class Board(object):
    "the chessboard (principal class)"
    def __init__(self):
        """super().__init__(win, width = width, height = height)
        self.width = width
        self.height = height"""
        self.clear()

    """def draw_board(self):
        "draws a checker patterned board"
        self.delete("all")
        for i in range(8):
            for j in range(8):
                self.create_rectangle(i * self.unit, j * self.unit, (i + 1) * self.unit, (j + 1) * self.unit,
                                      fill = ("white" if (i % 2 == j % 2) else "blue"))"""

    """def draw_piece(self, piece):
        "draws any piece on the board"
        self.create_image((piece.pos[0] - 1) * self.unit + self.unit / 2, (piece.pos[1] - 1) * self.unit + self.unit / 2, image = piece.image)"""

    """def draw_all(self, move_set = []):
        "draws all pieces set into the list pieces"
        self.draw_board()
        self.draw_move_set(move_set)
        self.draw_all_pieces()"""

    """def draw_all_pieces(self):
        for i in self.pieces:
            if i.activated :
                x, y = i.pos
                self.create_rectangle((x - 1) * self.unit, (y - 1) * self.unit, x * self.unit, y * self.unit, fill = "red")
            self.draw_piece(i)"""

    """def draw_move_set(self, move_set):
        for x, y in move_set:
            self.create_rectangle((x - 1) * self.unit, (y - 1) * self.unit, x * self.unit, y * self.unit, fill = "red")"""

    def clear(self):
        "sets the board back to its original position"
        self.pieces = []
        for piece in Pieces.listed:
            for color, positions in piece.STARTING_POSITIONS.items():
                for i in positions:
                    self.pieces.append(piece(i, color))
    
        #self.draw_all()

    def case_taken(self, case):
        for piece in self.pieces:
            if piece.pos == case:
                return True
        return False

    def piece_on_case(self, case):
        """ returns the piece on the parameter case (return None if the case is empty)"""
        for piece in self.pieces:
            if piece.pos == case:
                return piece
        return None

    """def select_unit(self, e):
        "selects the unit the click is on and shows its moveset if applicable"
        case_clicked = self.pos_to_units((e.x, e.y))
        
        self.draw_board()
        for piece in self.pieces:
            if piece.activated and case_clicked in piece.move_set():
                piece.move(case_clicked)
            piece.activated = False
        if self.case_taken(case_clicked):
            self.create_rectangle(e.x - e.x % self.unit, e.y - e.y % self.unit, e.x - e.x % self.unit + self.unit, e.y - e.y % self.unit + self.unit, fill = "red")
            self.piece_on_case(case_clicked).activated = True
            for column, line in self.piece_on_case(case_clicked).move_set():
                self.create_rectangle((column - 1) * self.unit, (line - 1) * self.unit, (column - 1) * self.unit + self.unit, (line - 1) * self.unit + self.unit, fill = "red")
        self.draw_all_pieces()
    """

    def disappear(self, piece):
        """makes piece disappear permanently from the board"""
        self.pieces.remove(piece)

    def get_activated_piece(self):
        """return the piece in pieces whose state is activated"""
        for i in self.pieces:
            if i.activated:
                return i
        return None

    def get_king(self, color):
        """returns the king of the parameter color (piece with a value of 0)"""
        for i in self.pieces:
            if i.value == 0 and color == i.color:
                return i
        return None

if __name__ == "__main__":
    win = tkinter.Tk()
    board = Board(win)
