import argparse
from pzl_board import PuzzleBoard
from pzl_move import Astar
from IDAStar import *
from tools import readFile

import numpy


def select_algorithm(is_file=False):
    if is_file:
        print('Given board :')
    else:
        print('Generated board :')
    print(boards.pzl)
    print()

    user = input("Select algorithm to solve above puzzle :\n"
                 "    IDAStar algorithm :\n"
                 "      [1] manhattan heuristic\n"
                 "      [2] linear conflict heuristic\n"
                 "      [3] misplaced heuristic\n"
                 "\n"
                 "    AStar algorithm :\n"
                 "      [4] manhattan heuristic\n"
                 "$>")

    additional = "0"
    if user >= "1" and user <= "3":
        additional = input("Select additional parameters :\n"
                           "    [0] nothing\n"
                           "    [1] greedy search\n")

    return user, additional


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default=False,
                        help="file with a puzzle")
    parser.add_argument('-g', '--generate', action='count', default=False,
                        help="generate puzzle board")
    args = parser.parse_args()

    boards = PuzzleBoard()
    if not (args.file or args.generate):
        parser.print_help()
        exit(1)
    elif args.file:
        file = readFile(args.file)
        values = boards.parsePuzzle(file)
        boards.generatePuzzle(values)
    else:
        boards.generatePuzzle(dim=3)

    user, additional = select_algorithm(is_file=args.file)

    save = numpy.copy(boards.pzl)

    if additional != '0' and additional != '1':
        print("[Error] Wrong input")
        exit(1)

    if user == '1' or user == '2' or user == '3':
        heuristic = manhattan_distance if user == '1' else linear_conflict if user == '2' else misplaced
        ida = IDAStar(heuristic, greedy=True if additional == "1" else False)
        try:
            result = ida.solve(boards.pzl, boards.slt)
        except RecursionError:
            print("This puzzle is too hard for Greedy search :(")
            exit(1)
        ida.show_result()

    elif user == '4':
        boards.addBorder()
        result = Astar(boards)
        print(result)

    else:
        print("[Error] Wrong input")
        exit(1)
