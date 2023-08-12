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

def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """
    return {atom for atom in formula.__code__.co_varnames}


def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)

def models(kb):
    all_atoms = set().union(*(atoms(formula) for formula in kb))
    all_interpretations = interpretations(all_atoms)
    models_list = [interpretation for interpretation in all_interpretations if
                   all(value(formula, interpretation) for formula in kb)]

    return models_list
