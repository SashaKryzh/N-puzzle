import random
import numpy as np
import sys
import re
from tools import *
from pzl_tools import *
import math

class PuzzleBoard:

    def __init__(self):
        self.dim = -1
        self.pzl = 0
        self.slt = 0
        self.lck = 0

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

    def checkSolvable(self, values:list):
        idx0 = values.index(0)
        dim = self.dim
        parite = math.ceil((dim - 1) + (dim - 1) - ((idx0 / dim) + (idx0 % dim)))
        tmp_val = values.copy()
        nb_permutation = 0
        if tmp_val[-1] != 0:
            tmp_val[idx0] = tmp_val[-1]
            tmp_val[-1] = 0
            nb_permutation += 1
        i = len(tmp_val) - 1
        while i > 0:
            if tmp_val[i - 1] < i:
                n = i - 1
                while n >= 0:
                    if tmp_val[n] == i:
                        tmp = tmp_val[n]
                        tmp_val[n] = tmp_val[i - 1]
                        tmp_val[i - 1] = tmp
                        nb_permutation += 1
                    n -= 1
            i -= 1
        print(f"nb permutation {nb_permutation} et parite {parite}")
        if parite % 2 == nb_permutation % 2:
            print("Not solvable")
            return False
        else:
            return True

    def defineDim(self):
        size = input("Enter puzzle size or 0 for random : ")
        if not re.match('^[03-9]$|^[0-9]{2,4}$', size):
            print("Incorrect value! Exit.")
            sys.exit(2)
        if (size == '0'):
            size = random.randint(3, 100)
        self.dim = int(size)

    def generatePuzzle(self, values=None):
        if values == None:
            values = np.arange(self.dim * self.dim)
            solvable = False
            while not solvable:
                np.random.shuffle(values)
                solvable = self.checkSolvable(values)
        elif not self.checkValues(values) or not self.checkSolvable(values):
            print('[Error puzzle file values]')
            sys.exit(2)

        values = np.asarray(values)
        board = np.ndarray((self.dim, self.dim), buffer=values, dtype=int)
        board = np.c_[np.full(self.dim, -1, dtype=int), board, np.full(self.dim, -1, dtype=int)]
        board = np.r_[[np.full(self.dim + 2, -1, dtype=int)], board, [np.full(self.dim + 2, -1, dtype=int)]]
        self.pzl = board
        return board

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
        return solution


# boards = PuzzleBoard()
#
# if len(sys.argv) > 1:
#     file = readFile(sys.argv[1])
#     values = boards.parsePuzzle(file)
#     boards.generatePuzzle(values)
# else:
#     boards.defineDim()
#     boards.generatePuzzle()
#
# boards.generateSolution()
#
# print(boards.pzl)
# print(boards.slt)