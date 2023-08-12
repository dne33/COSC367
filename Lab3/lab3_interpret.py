import itertools

def interpretations(atoms):
    sorted_atoms = sorted(atoms)
    n = len(sorted_atoms)
    result = []
    value_combinations = itertools.product([False, True], repeat=n)
    for values in value_combinations:
        interpretation = dict(zip(sorted_atoms, values))
        result.append(interpretation)

    return result
