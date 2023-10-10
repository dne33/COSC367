from itertools import product


def interpretations(atoms):
    prod = product([True, False], atoms, repeat=len(atoms))
    result = []
    for i in prod:
        interpretation = dict(zip(prod, i))
        result.append(interpretation)
    print(result)

interpretations({"p", "q"})
