from Pieces import *
from Piece import Piece
from Board import Board

class Police(object):
    def __init__(self, board):
        self.board = board
    
    def strip_illegal_moves_by_pos(self, piece):
        """returns the list of positions the piece can physically travel to"""
        legal_moves = []
        if isinstance(piece, Pawn):
            for x, y in piece.move_set():
                if not((x != piece.pos[0] and (self.board.piece_on_case((x, y)) == None or self.board.piece_on_case((x, y)).color == piece.color)) or (x == piece.pos[0] and self.board.case_taken((x, y)))):
                    legal_moves.append((x, y))
        return legal_moves

    def strip_illegal_moves(self, piece):
        """returns the list of positions the piece can legally travel to"""
        legal_moves_by_pos = self.strip_illegal_moves_by_pos(piece)
        legal_moves = []

        old_pos = piece.pos
        for x, y in legal_moves_by_pos:
            piece.pos = x, y
            if not(self.king_in_check(self.board.get_king(piece.color))):
                legal_moves.append((x, y))
                print(legal_moves)
        piece.pos = old_pos
        return legal_moves

    def king_in_check(self, king):
        """checks if the king is in check"""
        for piece in self.board.pieces:
            if piece.color != king.color and king.pos in self.strip_illegal_moves_by_pos(piece):
                return True
        return False

    def checkmated(self, king):
        for piece in self.board.pieces:
            if piece.color == king.color:
                for move in self.strip_illegal_moves(piece):
                    if not(self.king_in_check(king)):
                        return False
        return True
