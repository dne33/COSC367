from search import Arc, Graph
import math

class RoutingGraph(Graph):
    def __init__(self, map_str):
        map_list = map_str.split("\n")
        map_list = map_list[:-1]
        map_list = [string.strip() for string in map_list]
        self.map_list = [list(string_list) for string_list in map_list]
        self.directions = [('N', -1, 0),
                           ('E', 0, 1),
                           ('S', 1, 0),
                           ('W', 0, -1)]
        self.irregular_nodes = ['X', '-', '|']
        self.goals = []
        self.portals = []
        self.fuel_stations = []
        for row_idx, row in enumerate(map_list):
            for col_idx, val in enumerate(row):
                if val == 'G':
                    self.goals.append((row_idx, col_idx, val))
                elif val == 'P':
                    self.portals.append((row_idx, col_idx, val))
                elif val == 'F':
                    self.fuel_stations.append((row_idx, col_idx, val))

    def starting_nodes(self):
        numeric_indices = [(row_idx, col_idx, int(val) if val.isdigit() else math.inf) for row_idx, row
                           in enumerate(self.map_list) for col_idx, val in enumerate(row) if val.isdigit() or val == 'S']
        return numeric_indices

    def is_goal(self, node):
        numeric_indices = self.goals
        node_row, node_column, letter = node
        fake_goal_node = node_row, node_column, 'G'
        return fake_goal_node in numeric_indices

    def outgoing_arcs(self, tail):
        arcs = []
        x_curr, y_curr, fuel = tail
        for direction, x, y in self.directions:
            if self.map_list[x+x_curr][y+y_curr] not in self.irregular_nodes and fuel > 0:
                arcs.append(Arc(tail=tail, head=(x+x_curr, y+y_curr, fuel-1), action=direction, cost=5))
        if self.map_list[x_curr][y_curr] == 'F' and fuel < 9:
            arcs.append(Arc(tail=tail, head=(x_curr, y_curr, 9), action='Fuel up', cost=15))
        elif self.map_list[x_curr][y_curr] == 'P':
            for row, col, letter in self.portals:
                if not (row == x_curr and col == y_curr):
                    arcs.append(Arc(tail=tail, head=(row, col, fuel), action='Teleport to ' + str((row, col)), cost=10))
        return arcs

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        # Manhattan distance
        cost_list = []
        x, y, _ = node
        for x_cost, y_cost, _ in self.goals:
            cost_list.append(abs(x-x_cost) + abs(y-y_cost))
        return min(cost_list)
def print_map(map_graph, frontier, solution):
    map_list = map_graph.map_list
    if solution:
        for arc in solution[1:-1]:
            x,y,_ = arc.head
            map_list[x][y] = '*'
        for arcs in frontier.explored:
            x, y, _ = arcs
            if map_list[x][y] == ' ':
                map_list[x][y] = '.'
    result = ""
    for row in map_list:
        result += ''.join(row) + '\n'
    print(result)

