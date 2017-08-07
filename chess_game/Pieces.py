import tkinter
from Piece import Piece

class Bishop(Piece):
    image_name = "bishop.png"
    STARTING_POSITIONS = {"white" : [(3, 8), (6, 8)],
                          "black" : [(3, 1), (6, 1)]}
    value = 3

class Queen(Piece):
    image_name = "queen.png"
    STARTING_POSITIONS = {"white" : [(4, 8)],
                          "black" : [(4, 1)]}
    value = 9

class Knight(Piece):
    image_name = "knight.png"
    STARTING_POSITIONS = {"white" : [(2, 8), (7, 8)],
                          "black" : [(2, 1), (7, 1)]}
    value = 3

class King(Piece):
    image_name = "king.png"
    STARTING_POSITIONS = {"white" : [(5, 8)],
                          "black" : [(5, 1)]}
    value = 0

class Rook(Piece):
    image_name = "rook.png"
    STARTING_POSITIONS = {"white" : [(1, 8), (8, 8)],
                          "black" : [(1, 1), (8, 1)]}
    value = 5

    def move_set(self):
        move_set = []
        for i in range(1, 8):
            move_set.append((i, self.pos.y))
            move_set.append((self.pos.x, i))
        return move_set

class Pawn(Piece):
    image_name = "pawn.png"
    STARTING_POSITIONS = {"white" : [(i, 7) for i in range(9)],
                          "black" : [(i, 2) for i in range(9)]}
    value = 1

    def move_set(self):
        moves = [(self.pos[0], self.pos[1] + (1 if self.color == "black" else -1))]
        if (self.pos in [case for case in self.STARTING_POSITIONS[self.color]]):
            moves.append((self.pos[0], self.pos[1] + (2 if self.color == "black" else -2)))
        moves.append((self.pos[0] - 1, self.pos[1] + (1 if self.color == "black" else -1)))
        moves.append((self.pos[0] + 1, self.pos[1] + (1 if self.color == "black" else -1)))
        return moves


if __name__ == "__main__":
    root = tkinter.Tk()
    pawn = Pawn("e4", "black")
    print(pawn.image)


listed = [Bishop, Queen, Knight, King, Rook, Pawn]

