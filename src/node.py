class Node:

    def __init__(self, board, g, h):
        self.board = board
        self.g = g
        self.h = h

    @property
    def f(self):
        return self.g + self.h
