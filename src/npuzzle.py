import argparse
import sys
from pzl_board import PuzzleBoard
from pzl_move import Astar
from IDAStar import *
from tools import readFile

import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', default=False,
                        help="Puzzle file to solve")
    # parser.add_argument('--greedy', '-g', default=False,
    #                     help="Greedy search")
    # parser.add_argument('--uniform', '-u', default=False,
    #                     help="Uniform cost")

    args = parser.parse_args()
    boards = PuzzleBoard()

    if args.file:
        file = readFile(args.file)
        values = boards.parsePuzzle(file)
        boards.generatePuzzle(values)
    else:
        boards.generatePuzzle(dim=3)

    print(f"\nPUZZLE BOARD GENERATED :\n{boards.pzl}\n")
    user = input("Select algorithme to solve above puzzle.\n"
          "    IDAStar algorithm :\n"
          "      [1] manhattan heuristic function\n"
          "      [2] linear conflict heuristic function\n"
          "      [3] misplaced heuristic function\n"
          "\n"
          "    AStar algorithme :\n"
          "      [4] faster\n"
          "$>")

    save = numpy.copy(boards.pzl)

    if user == '1' or user == '2' or user == '3':
        heuristic = manhattan_distance if user == '1' else linear_conflict if user == '2' else misplaced
        ida = IDAStar(heuristic)
        result = ida.solve(boards.pzl, boards.slt)
        ida.show_result()

    elif user == '4':
        boards.addBorder()
        Astar(boards)
        boards.pzl = boards.delBorder(boards.pzl)
        print(save)
        print(boards.pzl)
        print(boards.nb_move)

    else:
        print("Wrong input. Exit.")
        sys.exit(1)

