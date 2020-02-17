import numpy as np

class Cell:
    def __init__(self, boards, number, target):
        self.nb = number
        self.cp = np.where(boards.pzl == number)
        self.trgt = target
        self.nxt_move = []
        self.last_move = [0]
        self.tmp_board = 0
        self.tmp_nb_move = 0
        self.tmp_direction = 0