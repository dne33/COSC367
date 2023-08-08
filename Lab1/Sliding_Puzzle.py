from collections import deque

from search import *
import copy
BLANK = ' '

class SlidingPuzzleGraph(Graph):

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state)  # the size of the puzzle
        # Find i and j such that state[i][j] == BLANK
        i = next((index for index, row in enumerate(state) if BLANK in row), None)
        j = state[i].index(BLANK)
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])  # or blank goes right
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the sequence always has one element."""
        return [self.starting_state]

    def is_goal(self, state):
        """Determine whether a given node (integer) is a goal."""
        n = len(state)
        # Check if the first element is ' '
        if state[0][0] != ' ':
            return False
        flat_list = [item for sublist in state for item in sublist]
        # Check if the rest of the elements are in order from 1 to n^2-1
        for i in enumerate(flat_list):
            if i[0] != 0:
                if i[0] != i[1]:
                    return False
        return True

    from collections import deque
    class BFSFrontier(Frontier):
        """This is an abstract class for frontier classes. It outlines the
        methods that must be implemented by a concrete subclass. Concrete
        subclasses determine the search strategy.

        """

        def __init__(self):
            self.container = deque([])

        def add(self, path):
            """Adds a new path to the frontier. A path is a sequence (tuple) of
            Arc objects. You should override this method.

            """
            self.container.appendleft(path)

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
            if len(self.container) > 0:
                return self.container.pop()
            else:
                raise StopIteration  # don't change this one

