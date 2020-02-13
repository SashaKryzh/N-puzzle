import argparse
import sys
from pzl_move import move_puzzle
from pzl_board import PuzzleBoard
from tools import readFile

import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', default=False,
                        help="Puzzle file to solve")
    parser.add_argument("-h1", "--Manhattan", action='count', default=True,
                        help="Will use heuristic function 1")
    parser.add_argument("-h2", "--heuristic2", action='count', default=False,
                        help="Will use heuristic function 2")
    parser.add_argument("-h3", "--heuristic3", action='count', default=False,
                        help="Will use heuristic function 3")

    args = parser.parse_args()
    boards = PuzzleBoard()

    if args.file:
        file = readFile(args.file)
        values = boards.parsePuzzle(file)
        boards.generatePuzzle(values)
    else:
        boards.generatePuzzle(dim=4)

    if (args.heuristic1 and (args.heuristic2 or args.heuristic3) or
        args.heuristic2 and (args.heuristic1 or args.heuristic3) or
        args.heuristic3 and (args.heuristic1 or args.heuristic2)):
        print("Can't use 2 different heuristic function")
        sys.exit(1)

    save = numpy.copy(boards.pzl)
    if args.heuristic1:
        move_puzzle(boards)
    print(save)
    print(boards.pzl)
    print(boards.nb_move)







