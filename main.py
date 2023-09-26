from Lab6.generate_and_test import generate_and_test
from csp import *
from Lab6.cryptic_puz import *


def main():
    if __name__ == ("__main__"):
        new_csp = arc_consistent(cryptic_puzzle)
        solutions = []
        for solution in generate_and_test(new_csp):
            solutions.append(sorted((x, v) for x, v in solution.items()
                                    if x in "twofur"))
        print(len(solutions))
        solutions.sort()
        print(solutions[0])
        print(solutions[5])

if __name__ == ("__main__"):
    main()
