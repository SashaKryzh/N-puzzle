import argparse
import sys
from pzl_board import PuzzleBoard
from pzl_move import Astar
from IDAStar import IDAStar, manhattan_distance
from tools import readFile

import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', default=False,
                        help="Puzzle file to solve")
    parser.add_argument("-h1", "--Astar", action='count', default=False,
                        help="Will use heuristic function 1")
    parser.add_argument("-h2", "--IDAStar", action='count', default=False,
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
        boards.generatePuzzle(dim=3)

    if (args.Astar and (args.IDAStar or args.heuristic3) or
        args.IDAStar and (args.Astar or args.heuristic3) or
        args.heuristic3 and (args.Astar or args.IDAStar)):
        print("Can't use 2 different heuristic function")
        sys.exit(1)

    save = numpy.copy(boards.pzl)

    if args.Astar:
        boards.addBorder()
        Astar(boards)
        boards.pzl = boards.delBorder(boards.pzl)
    if args.IDAStar:
        ida = IDAStar(manhattan_distance)
        result = ida.solve(boards.pzl, boards.slt)
        print(result)

    print(save)
    print(boards.pzl)
    print(boards.nb_move)
