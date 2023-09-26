import itertools

def interpretations(atoms):
    n = len(atoms)
    result = []
    value_combinations = itertools.product([False, True], repeat=n)
    for values in value_combinations:
        interpretation = dict(zip(atoms, values))
        result.append(interpretation)

    return result
