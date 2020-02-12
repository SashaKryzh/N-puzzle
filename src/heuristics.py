import numpy as np


def manhattan_distance(board, goal):
    mandistance = 0
    for element in board.ravel():
        if element == 0:
            continue
        b_index = np.where(board == element)
        g_index = np.where(goal == element)
        mandistance += abs(g_index[0][0] - b_index[0][0]) + abs(g_index[1][0] - b_index[1][0])
    return mandistance

# TODO: 2 more heuristics
# def linear_conflict(board, goal):


# board = np.array([
#     [1, 2, 5],
#     [3, 0, 6],
#     [7, 4, 8],
# ])

# board = np.array([
#     [1, 4, 3],
#     [8, 0, 2],
#     [7, 6, 5],
# ])

# goal = np.array([
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5],
# ])

# print(manhattan_distance(board, goal))
