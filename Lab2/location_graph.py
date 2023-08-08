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
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        tail_loc = self.location[tail]
        arcs = []
        for key, loc in sorted(self.location.items()):
            euclid = sqrt((self.location[key][0] - tail_loc[0])**2 + (self.location[key][1] - tail_loc[1])**2)
            if euclid <= self.radius and key!=tail:
                arcs.append(Arc(tail=tail, head=key, action=tail+'->'+key, cost=euclid))
        return arcs