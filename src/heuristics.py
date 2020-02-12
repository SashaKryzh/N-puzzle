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


# TODO: linear conflict
def linear_conflict(board, goal):
    def calculate_conflicts(have, goal):
        # print(have)
        # print(goal)
        conflicts = 0
        for i in range(len(have)):
            i_pos = np.where(goal == have[i])[0]
            if have[i] != 0 and len(i_pos) > 0:
                for j in range(i):
                    j_pos = np.where(goal == have[j])
                    if have[j] != 0 and len(j_pos) > 0:
                        if (i > j) != (i_pos[0] > j_pos[0]):
                            conflicts += 1
        # print(conflicts)
        # print('---')
        return conflicts

    mandistance = manhattan_distance(board, goal)
    conflicts = 0
    for b_row, g_row in zip(board, goal):
        conflicts += calculate_conflicts(b_row, g_row)
    # print('++++++++++++++++')
    for b_col, g_col in zip(board.transpose(), goal.transpose()):
        conflicts += calculate_conflicts(b_col, g_col)
    return mandistance + (conflicts * 2)

# TODO: walking_distance or pattern_database
# def walking_distance(board, goal):

# board = np.array([
#     [4, 2, 5],
#     [1, 6, 0],
#     [8, 7, 3],
# ])
#
# # board = np.array([
# #     [1, 4, 3],
# #     [8, 0, 2],
# #     [7, 6, 5],
# # ])
#
# goal = np.array([
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5],
# ])
#
# print(manhattan_distance(board, goal))
# print(linear_conflict(board, goal))
