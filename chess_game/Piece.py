import tkinter

class Piece :
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.image = tkinter.PhotoImage(file = self.color + "_" + self.image_name)
        self.activated = False

    def move(self, new_pos):
        if new_pos in self.move_set():
            self.pos = new_pos
            self.activated = True

    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False

    def move_set(self):
        return []

