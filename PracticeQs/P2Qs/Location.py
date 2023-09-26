from search import Arc, Graph
from math import sqrt


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        raise NotImplementedError()  # replace this line with a correct code

    def outgoing_arcs(self, tail):
        x, y = self.location[tail]
        arcs = []
        for key, items in self.location.items():
            x1, y1 = items
            dist = sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))
            if key != tail and dist <= self.radius:


