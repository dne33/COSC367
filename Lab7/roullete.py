def roulette_wheel_select(population, fitness, r):
    sum_fitness = sum(fitness(i) for i in population)
    fitness_band = sum_fitness * r
    fit = 0
    for i in range(sum_fitness):
        fit += fitness(population[i])
        if fitness_band <= fit:
            return population[i]
    return population[-1]

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))