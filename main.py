from Assignment1.RoutingGraph import RoutingGraph
from Assignment1.RoutingGraph import print_map
from Assignment1.AStarFrontier import AStarFrontier
from search import *
def main():
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    |  S    |
    +-------+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +---------------+
    |    G          |
    |XXXXXXXXXXXX   |
    |           X   |
    |  XXXXXX   X   |
    |  X S  X   X   |
    |  X        X   |
    |  XXXXXXXXXX   |
    |               |
    +---------------+
    """

    map_graph = RoutingGraph(map_str)

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)

    print_map(map_graph, frontier, solution)

    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

if __name__ == ("__main__"):
    main()