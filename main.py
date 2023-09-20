from Lab6.generate_and_test import generate_and_test
from csp import *
from search import *
from PracticeQs.SlidingPuzzleGraph import SlidingPuzzleGraph
from PracticeQs.SlidingPuzzleGraph import BFSFrontier
def main():
    if __name__ == ("__main__"):
        graph = SlidingPuzzleGraph([[1, ' ', 2],
                                    [6, 4, 3],
                                    [7, 8, 5]])

        solutions = generic_search(graph, BFSFrontier())
        print_actions(next(solutions))
if __name__ == ("__main__"):
    main()