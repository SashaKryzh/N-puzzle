import numpy as np

from heuristics import manhattan_distance


class Node:

    def __init__(self, board, g, h):
        self.board = board
        self.g = g
        self.h = h

    @property
    def f(self):
        return self.g + self.h

    def children(self, heuristic, goal_board):
        def swap_to_copy(a, b):
            ret = self.board.copy()
            tmp = ret[b[0]][b[1]]
            ret[b[0]][b[1]] = 0
            ret[a[0]][a[1]] = tmp
            return ret

        children = []
        empty_index = np.where(self.board == 0)
        row, col = empty_index[0][0], empty_index[1][0]

        if row > 0:
            children.append(swap_to_copy((row, col), (row - 1, col)))
        if row < self.board.shape[1] - 1:
            children.append(swap_to_copy((row, col), (row + 1, col)))
        if col > 0:
            children.append(swap_to_copy((row, col), (row, col - 1)))
        if col < self.board.shape[0] - 1:
            children.append(swap_to_copy((row, col), (row, col + 1)))

        ret = [Node(x, self.g + 1, heuristic(x, goal_board)) for x in children]
        ret.sort()
        return ret

    def __eq__(self, other):
        if isinstance(other, np.ndarray):
            return np.array_equal(self.board, other)
        else:
            return np.array_equal(self.board, other.board)

    def __str__(self):
        s = "f = " + str(self.f) + "\n"
        return s + str(self.board)

    def __lt__(self, other):
        return self.f < other.f


# board = np.array([
#     [1, 2, 3],
#     [8, 4, 0],
#     [7, 6, 5],
# ])
#
# goal = np.array([
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5],
# ])
#
# node = Node(board, 0, 0)
# c = node.children(manhattan_distance, goal)
# print(c)
# for i in c:
#     print(i)
