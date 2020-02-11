import numpy as np


def manhattan_distance(board, goal):
    board_flat = board.ravel()
    goal_flat = goal.ravel()

    mandistance = 0
    for element in board_flat:
        distance = abs(np.where(goal_flat == element)[0][0] - np.where(board_flat == element)[0][0])
        x, y = distance // board.shape[0], distance % board.shape[0]
        mandistance += x + y
    return mandistance


board = np.array([
    [1, 2, 5],
    [3, 0, 6],
    [7, 4, 8],
])

# board = np.array([
#     [1, 4, 3],
#     [8, 0, 2],
#     [7, 6, 5],
# ])

goal = np.array([
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
])

print(manhattan_distance(board, goal))
