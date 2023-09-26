# import any module as necessary
import itertools
def interpretations(atoms):
    sorted_atoms = sorted(atoms)
    n = len(atoms)
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

def models(knowledge):
    results = set()
    for keys in knowledge:
        for atom in atoms(keys):
            results.add(atom)
    results = sorted(results)
    interpretations1 = interpretations(results)
    return_list = []
    for interpretation in interpretations1:
        valid = True
        for formula in knowledge:
            if not value(formula, interpretation):
                valid = False
        if valid:
            return_list.append(interpretation)
    return return_list

knowledge_base = {
    lambda a, b: a and not b,
    lambda c, d: c or d
}

for interpretation in models(knowledge_base):
    print(interpretation)