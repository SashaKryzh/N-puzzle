import numpy as np

from Node import Node
from heuristics import *


class IDAStar:

    def __init__(self, heuristic, greedy=False):
        self.heuristic = heuristic
        self.greedy = greedy

        self.FOUND = object()
        self.INFINITY = 9223372036854775807

        self.goal_board = None
        self.path = []

        self.opened = 1
        self.now_opened = 1
        self.max_in_memory = 1

    def solve(self, start_board, goal_board):
        self.goal_board = goal_board
        start_node = Node(start_board, goal_board, 0, self.heuristic, greedy=self.greedy)
        threshold = start_node.f
        while True:
            temp = self._search(start_node, threshold)
            if temp == self.FOUND:
                self.path.append(start_node)
                self.path.reverse()
                return self.opened, self.max_in_memory, self.now_opened, self.path
            if temp == self.INFINITY:
                return self.opened, self.max_in_memory, None, None
            threshold = temp

    def _search(self, n, threshold):
        if n.f > threshold:
            return n.f
        if n == self.goal_board:
            return self.FOUND
        minimum_cost = None
        for child in n.children:
            self.opened += 1
            self.now_opened += 1
            if self.now_opened > self.max_in_memory:
                self.max_in_memory = self.now_opened
            child_ida = self._search(child, threshold)
            if child_ida == self.FOUND:
                self.path.append(child)
                return self.FOUND
            if minimum_cost is None or (child_ida is not None and child_ida < minimum_cost):
                minimum_cost = child_ida
            self.now_opened -= 1
        return minimum_cost

    def show_result(self):
        for node in self.path:
            print(node)
        print('\nResults using IDA*')
        print('Complexity in time: ' + self.opened.__str__())
        print('Complexity in size: ' + self.max_in_memory.__str__())
        print('Number of moves required: ' + len(self.path).__str__())

# board = np.array([
#     [5,  1,  7,  3],
#     [9,  2, 11,  4],
#     [13,  6, 15,  8],
#     [0, 10, 14, 12],
# ])

# board = np.array([
#     [15, 14,  1,  6],
#     [9, 11,  4, 12],
#     [0, 10,  7,  3],
#     [13,  8, 5,  2],
# ])

# board = np.array([
#     [3, 2, 6],
#     [1, 4, 0],
#     [8, 7, 5],
# ])

# board = np.array([
#     [1, 3, 4],
#     [7, 0, 5],
#     [6, 8, 2],
# ])

# goal = np.array([
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5],
# ])

# goal = np.array([
#     [1,  2,  3,  4],
#     [12, 13, 14, 5],
#     [11, 0,  15, 6],
#     [10, 9,  8,  7],
# ])

# goal = np.array([
#     [1,  2,  3,  4],
#     [5, 6, 7, 8],
#     [9, 10,  11, 12],
#     [13, 14,  15,  0],
# ])

# ida = IDAStar(linear_conflict)
# result = ida.solve(board, goal)
# print(result)
# for node in result[3]:
#     print(node)
