from search import *
from heapq import heappop, heappush
class AStarFrontier(Frontier):
    """This is an abstract class for frontier classes. It outlines the
    methods that must be implemented by a concrete subclass. Concrete
    subclasses determine the search strategy.
    """
    def __init__(self, map_graph):
        self.map_graph = map_graph
        self.frontier = []
        self.explored = []
        self.order = 0

    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.
        """
        if path[-1].head not in self.explored:
            heappush(self.frontier, (sum(x.cost for x in path) + self.order + self.map_graph.estimated_cost_to_goal(path[-1].head)*path[-1].cost, path))
            self.order += 1/1000000000000
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

        while len(self.frontier) > 0:
            path_tuple = heappop(self.frontier)[-1]
            state = path_tuple[-1].head
            if state not in self.explored:
                self.explored.append(state)
                return path_tuple
        else:
            raise StopIteration
