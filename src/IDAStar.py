import numpy as np

from Node import Node
from heuristics import manhattan_distance


class IDAStar:

    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.goal_board = None
        self.FOUND = object()
        self.INFINITY = 9223372036854775807
        self.path = []

    def solve(self, start_board, goal_board):
        self.goal_board = goal_board
        start_node = Node(start_board, 0, self.heuristic(start_board, goal_board))
        threshold = start_node.h

        self.path.append(start_node)

        while True:
            temp = self._search(start_node, threshold)
            if temp == self.FOUND:
                return self.path
            if temp == self.INFINITY:
                return None
            threshold = temp

    def _search(self, node, threshold):
        if node.f > threshold:
            return node.f
        if node == self.goal_board:
            return self.FOUND
        minimum_cost = self.INFINITY
        for child in node.children(self.heuristic, self.goal_board):
            self.path.append(child)
            child_ida = self._search(child, threshold)
            if child_ida == self.FOUND:
                return self.FOUND
            self.path.pop()
            if child_ida < minimum_cost:
                minimum_cost = child_ida
        return minimum_cost


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

ida = IDAStar(manhattan_distance)
path = ida.solve(board, goal)
for node in path:
    print(node)
