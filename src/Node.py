import numpy as np

from heuristics import manhattan_distance


class Node:

    def __init__(self, board, goal_board, g, heuristic, move='Initial', greedy=False):
        self.__board = board
        self.__goal_board = goal_board
        self.__g = g if not greedy else 0
        self.__heuristic = heuristic
        self.__h = self.__heuristic(board, goal_board)
        self.__move_direction = move
        self.greedy = greedy

    @property
    def f(self):
        return self.__g + self.__h

    @property
    def children(self):
        def swap_to_copy(a, b, move):
            new_board = self.__board.copy()
            tmp = new_board[b[0]][b[1]]
            new_board[b[0]][b[1]] = 0
            new_board[a[0]][a[1]] = tmp
            return Node(new_board, self.__goal_board, self.__g + 1, self.__heuristic, move=move, greedy=self.greedy)

        children = []
        empty_index = np.where(self.__board == 0)
        row, col = empty_index[0][0], empty_index[1][0]

        if self.__move_direction != 'Down'  and row > 0:
            children.append(swap_to_copy((row, col), (row - 1, col), 'Up'))
        if self.__move_direction != 'Up'    and row < self.__board.shape[1] - 1:
            children.append(swap_to_copy((row, col), (row + 1, col), 'Down'))
        if self.__move_direction != 'Right' and col > 0:
            children.append(swap_to_copy((row, col), (row, col - 1), 'Left'))
        if self.__move_direction != 'Left'  and col < self.__board.shape[0] - 1:
            children.append(swap_to_copy((row, col), (row, col + 1), 'Right'))

        children.sort()
        return children

    def __eq__(self, other):
        if isinstance(other, np.ndarray):
            return np.array_equal(self.__board, other)
        else:
            return np.array_equal(self.__board, other.__board)

    def __str__(self):
        s = self.__move_direction + ' (f = ' + self.f.__str__() + ')\n'
        return s + str(self.__board)

    def __lt__(self, other):
        return self.f < other.f


# TESTS

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
# node = Node(board, goal, 0, manhattan_distance)
# c = node.children
# for i in c:
#     print(i)
