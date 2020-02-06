import numpy as np


def manhattan_distance(board, goal):
    board_flat = board.ravel()
    goal_flat = goal.ravel()

    mandistance = 0
    for element in board.tolist():
        # distance = abs(np.where(goal_flat == element) - np.where(board_flat - element))
        # x, y = distance // board.shape[0], distance % board.shape[0]
        # mandistance += x + y
    return mandistance


board = np.array([
    [1, 2, 5],
    [3, 0, 6],
    [7, 4, 8],
])

goal = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
])


print(board)
print(goal)
# manhattan_distance(board, goal)

np.where
