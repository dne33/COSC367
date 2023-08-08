from search import *
from heapq import *
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


class LCFSFrontier(Frontier):
    """This is an abstract class for frontier classes. It outlines the
    methods that must be implemented by a concrete subclass. Concrete
    subclasses determine the search strategy.

    """

    def __init__(self):
        self.frontier = []
        self.order = 1/1000000

    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """
        # get_total_cost = lambda x: sum(arc.cost for arc in path)
        # total_cost_path = get_total_cost(path)
        # index = bisect.bisect_right([get_total_cost(existing_path) for existing_path in self.frontier], total_cost_path)
        # self.frontier.insert(index, path)
        heappush(self.frontier, (sum(x.cost for x in path) + self.order, path))
        self.order += 1/1000000

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there is nothing to return this should raise a
        StopIteration exception.
        """
        if len(self.frontier) > 0:
            path_tuple = heappop(self.frontier)
            return path_tuple[1]
        else:
            raise StopIteration



