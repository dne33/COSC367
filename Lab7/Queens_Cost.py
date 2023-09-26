def n_queens_cost(state):
    cost = 0
    for i in range(len(state)):  # Loop through each queen (i ranges from 0 to len(state) - 1)
        # Compare the current queen (i) with the remaining queens
        # (j ranges from i+1 to len(state) - 1)
        for j in range(i + 1, len(state)):
            if abs(state[i] - state[j]) == abs(i - j):  # Check if the queens threaten each other diagonally
                cost += 1
    return cost

print(n_queens_cost((1, 3, 2)))