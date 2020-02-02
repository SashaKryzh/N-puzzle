import random
import numpy as np
import sys
import re
from tools import read_file

class puzzle_board:

    def __init__(self):
        self.dim = -1

    def parse_puzzle(self, data:str):
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

    def check_values(self, values:list):
        if len(values) != self.dim * self.dim:
            return -1
        xcheck = np.arange(self.dim * self.dim)
        for x_val in xcheck:
            x_match = False
            for x in values:
                if x_val == x:
                    x_match = True
            if x_match == False:
                return -1

    def define_dim(self):
        size = input("Enter puzzle size or 0 for random : ")
        if not re.match('^[03-9]$|^[0-9]{2,4}$', size):
            print("Incorrect value! Exit.")
            sys.exit(2)
        if (size == '0'):
            size = random.randint(3, 100)
        self.dim = int(size)

    def generate_puzzle(self, values=None):
        if values == None:
            values = np.arange(self.dim * self.dim)
            np.random.shuffle(values)
        elif self.check_values(values) == -1:
            print('[Error puzzle file values]')
            sys.exit(2)

        values = np.asarray(values)
        board = np.ndarray((self.dim, self.dim), buffer=values, dtype=int)
        return board


pzl = puzzle_board()

if len(sys.argv) > 1:
    file = read_file(sys.argv[1])
    values = pzl.parse_puzzle(file)
    board = pzl.generate_puzzle(values)
else:
    pzl.define_dim()
    board = pzl.generate_puzzle()

print(board)
