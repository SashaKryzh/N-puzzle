from node import Node

class IDAStar:

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, start_board):
        start_node = Node(start_board, 0, self.heuristic)
        threshold = start_node.h
        while True:
            temp = self._search(start_node, threshold)
            if temp == self.goal:
                return temp
            if temp == iksdflk;sda
                return
            threshold = temp


    def _search(self, node, threshold):
        if node.f > threshold or node == self.goal:
            return node
        minimum_cost = 9223372036854775807
        for child in node.children:
            child_ida = self._search(child, threshold)
            if child_ida == self.goal:
                return child_ida
            if child_ida.f < minimum_cost:
                minimum_cost = child_ida.f
        node.f
        return node