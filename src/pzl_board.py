import numpy as np
import re
from tools import *
from pzl_tools import *
from pzl_solvability import *

class PuzzleBoard:

    def __init__(self):
        self.dim = -1
        self.pzl = 0
        self.slt = 0
        self.lck = 0
        self.nb_move = 0

    def parsePuzzle(self, data:str):
        lines = data.split('\n')
        x = []
        for line in lines:
            line_nb = re.search('^([\d\t ]+).*', line)
            if line_nb == None:
                continue
            for nb in re.findall('(\d+)', line_nb.group(1)):
                if self.dim == -1:
                    self.dim = int(nb)
                else:
                    x.append(int(nb))
        return x

    def checkValues(self, values:list):
        if len(values) != self.dim * self.dim:
            return False
        xcheck = np.arange(self.dim * self.dim)
        for x_val in xcheck:
            x_match = False
            for x in values:
                if x_val == x:
                    x_match = True
            if x_match == False:
                return False
        return True

    def generateSolution(self):
        values = np.arange(self.dim * self.dim)
        values = values[1:]

        solution = np.full((self.dim + 2, self.dim + 2), 0, dtype=int)
        solution[:, 0] = -1
        solution[:, -1] = -1
        solution[0, :] = -1
        solution[-1, :] = -1
        self.lck = np.copy(solution)

        x = 1
        y = 1
        dir = "→"
        for val in values:
            solution[x, y] = val
            dir = get_direction(solution, (x, y), dir)
            if dir == "→":
                y += 1
            elif dir == "↓":
                x += 1
            elif dir == "←":
                y -= 1
            elif dir == "↑":
                x -= 1
        self.slt = solution

    def generatePuzzle(self, values=None, dim=3):
        if values == None:
            self.dim = dim
            self.generateSolution()
            values = np.arange(self.dim * self.dim)
            np.random.shuffle(values)
            while not Solvability(self.dim, values, self.slt).solvable:
                np.random.shuffle(values)
        elif not self.checkValues(values):
            print('[Error puzzle file values]')
            sys.exit(2)
        self.generateSolution()
        if not Solvability(self.dim, values, self.slt).solvable:
            print('[Error puzzle not solvable]')
            sys.exit(2)

        values = np.asarray(values)
        board = np.ndarray((self.dim, self.dim), buffer=values, dtype=int)
        board = np.c_[np.full(self.dim, -1, dtype=int), board, np.full(self.dim, -1, dtype=int)]
        board = np.r_[[np.full(self.dim + 2, -1, dtype=int)], board, [np.full(self.dim + 2, -1, dtype=int)]]
        self.pzl = board

        return board


# boards = PuzzleBoard()
#
# if len(sys.argv) > 1:
#     file = readFile(sys.argv[1])
#     values = boards.parsePuzzle(file)
#     boards.generatePuzzle(values)
# else:
#     boards.dim = 3
#     boards.generatePuzzle()
#
# print(boards.pzl)