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
          "      [2] linear heuristic function\n"
          "      [3] foo heuristic function\n"
          "\n"
          "    AStar algorithme :\n"
          "      [4] faster\n"
          "$>")

    save = numpy.copy(boards.pzl)

    if user == '1':
        ida = IDAStar(manhattan_distance)
        result = ida.solve(boards.pzl, boards.slt)
        print(result)
        for node in result[3]:
            print(node)
    elif user == '2':
        ida = IDAStar(linear_conflict)
        result = ida.solve(boards.pzl, boards.slt)
        print(result)
        for node in result[3]:
            print(node)
    elif user == '3':
        print("Foooo")
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

