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
