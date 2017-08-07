import tkinter
from Pieces import *
from Board import Board
from Piece import Piece
from Player import Player
from Police import Police
from Render import Render

class Chess(tkinter.Tk):
    def __init__(self, first_player, second_player):
        super().__init__()
        self.title = "Chess game"
        self.in_play = True
        self.board = Board()
        self.render = Render(self)
        self.render.bind("<Button-1>", self.click)
        self.white = self.current_player = Player(first_player, "white")
        self.black = Player(second_player, "black")
        self.police = Police(self.board)
        tkinter.Label(self, text = self.white.name, fg = "gray").pack(side = "left")
        tkinter.Label(self,text = self.black.name, fg = "black").pack(side = "right")
        self.mainloop()

    def next_turn(self):
        """changes the current player to the other one"""
        if (self.current_player == self.white):
            self.current_player = self.black
        else:
            self.current_player = self.white
        if self.police.checkmated(self.board.get_king(self.current_player.color)):
            self.in_play = False
            self.render.inform_of_lameness(self.current_player)
    
    def click(self, e):
        """everything that happens when a case is clicked"""
        if self.in_play:
            case_clicked = self.render.pos_to_units((e.x, e.y))
            move_set = []
            if self.board.get_activated_piece() != None:
                if case_clicked in self.police.strip_illegal_moves(self.board.get_activated_piece()):
                    if self.board.piece_on_case(case_clicked) != None:
                        self.current_player.score += self.board.piece_on_case(case_clicked).value
                        self.board.disappear(self.board.piece_on_case(case_clicked))
                    self.board.get_activated_piece().move(case_clicked)
                    self.next_turn()
                self.board.get_activated_piece().deactivate()
            else:
                if self.board.piece_on_case(case_clicked) != None and self.board.piece_on_case(case_clicked).color == self.current_player.color:
                    self.board.piece_on_case(case_clicked).activate()
                    move_set = self.police.strip_illegal_moves(self.board.get_activated_piece())
            self.render.draw_board(self.board, move_set)



if __name__ == "__main__":
    chess = Chess("Dipper", "Ford")
