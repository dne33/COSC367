from search import *
class FunkyNumericGraph(Graph):
    def __init__(self, starting_state):
        self.starting_state = starting_state

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        return node % 10 == 0

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.
        """
        return [self.starting_state]
    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        return [Arc(tail_node, tail_node-1 , action="1down", cost=1),
                  Arc(tail_node, tail_node+2 , action="2up", cost=1)]

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0)  # FIX THIS (return something instead)
        else:
            raise StopIteration  # don't change this one
