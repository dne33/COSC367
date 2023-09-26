
def greedy_descent(initial_state, neighbours, cost):
    curr_state = initial_state, cost(initial_state)
    states = []

    # Initial neighbour search
    # saves all neighbours in a value, cost pair
    neighbour_list = []
    for x in neighbours(initial_state):
        neighbour_list.append((x, cost(x)))
    # Determines the smallest cost
    smallest = min(neighbour_list, key=lambda x: x[1])

    while smallest[1] < curr_state[1]:
        # print(states)
        neighbour_list = []
        states.append(curr_state[0])
        # make the current state the smallest
        curr_state = smallest
        # Search for new smallest
        for x in neighbours(smallest[0]):
            neighbour_list.append((x, cost(x)))
        # Determines the smallest cost
        if len(neighbour_list) == 0:
            break
        smallest = min(neighbour_list, key=lambda x: x[1])
    # Append the final current state
    states.append(curr_state[0])
    return states

def cost(x):
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)