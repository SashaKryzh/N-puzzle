import numpy as np

from Node import Node
from heuristics import manhattan_distance


# TODO: additional check if solvable
class IDAStar:

    def __init__(self, heuristic):
        self.heuristic = heuristic

        self.FOUND = object()
        self.INFINITY = 9223372036854775807

        self.goal_board = None
        self.path = []

        self.opened = 1
        self.now_opened = 1
        self.max_in_memory = 1

    def solve(self, start_board, goal_board):
        self.goal_board = goal_board
        start_node = Node(start_board, goal_board, 0, self.heuristic)
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
        minimum_cost = self.INFINITY
        for child in n.children:
            self.opened += 1
            self.now_opened += 1
            if self.now_opened > self.max_in_memory:
                self.max_in_memory = self.now_opened
            child_ida = self._search(child, threshold)
            if child_ida == self.FOUND:
                self.path.append(child)
                return self.FOUND
            if child_ida < minimum_cost:
                minimum_cost = child_ida
            self.now_opened -= 1
        return minimum_cost


# board = np.array([
#     [4, 1, 10, 8],
#     [13, 5, 14, 3],
#     [0, 7, 11, 9],
#     [2, 12, 6, 15],
# ])

board = np.array([
    [3, 2, 6],
    [1, 4, 0],
    [8, 7, 5],
])

# board = np.array([
#     [1, 3, 4],
#     [7, 0, 5],
#     [6, 8, 2],
# ])

goal = np.array([
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
])

# goal = np.array([
#     [1,  2,  3,  4],
#     [12, 13, 14, 5],
#     [11, 0,  15, 6],
#     [10, 9,  8,  7],
# ])

# goal = np.array([
#     [1,  2,  3,  4],
#     [12, 13, 14, 5],
#     [11, 0,  15, 6],
#     [10, 9,  8,  7],
# ])

ida = IDAStar(manhattan_distance)
result = ida.solve(board, goal)
print(result)
for node in result[3]:
    print(node)
