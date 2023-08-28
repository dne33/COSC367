from Lab6.generate_and_test import generate_and_test
from csp import *
def main():
    if __name__ == ("__main__"):
        simple_csp = CSP(
            var_domains={x: set(range(1, 5)) for x in 'abc'},
            constraints={
                lambda a, b: a < b,
                lambda b, c: b < c,
            })

        solutions = sorted(str(sorted(solution.items())) for solution
                           in generate_and_test(simple_csp))
        print("\n".join(solutions))
if __name__ == ("__main__"):
    main()