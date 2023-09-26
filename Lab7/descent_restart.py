def greedy_descent(initial_state, neighbours, cost):
    curr_state = (initial_state, cost(initial_state))
    states = [initial_state]

    # Initial neighbour search
    # saves all neighbours in a value, cost pair
    neighbour_list = []
    for x in neighbours(initial_state):
        neighbour_list.append((x, cost(x)))
    # Determines the smallest cost
    if len(neighbour_list) == 0:
        return states
    smallest = min(neighbour_list, key=lambda x: x[1])

    while smallest[1] < curr_state[1]:
        # print(states)
        neighbour_list = []

        # make the current state the smallest

        # Search for new smallest
        for x in neighbours(smallest[0]):
            neighbour_list.append((x, cost(x)))
        # Determines the smallest cost
        if len(neighbour_list) == 0:
            break
        curr_state = smallest
        states.append(curr_state[0])
        smallest = min(neighbour_list, key=lambda x: x[1])
    # Append the final current state
    return states

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    global_min = False
    while not global_min:
        first_state = random_state()
        states = greedy_descent(first_state, neighbours, cost)
        for state in states:
            print(state)
            if cost(state) == 0:
                global_min = True
        if not global_min:
            print('RESTART')


    return None
def n_queens_neighbours(state):
    result = set()
    for index, i in enumerate(state):
        for index2, j in enumerate(state):
            state2 = list(state)
            if i != j:
                state2[index] = j
                state2[index2] = i
                result.add(tuple(state2))

    return sorted(list(result))

def n_queens_cost(state):
    cost = 0
    for i in range(len(state)):  # Loop through each queen (i ranges from 0 to len(state) - 1)
        # Compare the current queen (i) with the remaining queens
        # (j ranges from i+1 to len(state) - 1)
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):  # Check if the queens threaten each other diagonally
                cost += 1
    return cost
import random

N = 4
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)