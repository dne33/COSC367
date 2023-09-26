import copy
import itertools

from csp import *


def arc_consistent(csp: CSP):
    csp = copy.deepcopy(csp)
    todo = {(x, c) for c in csp.constraints for x in scope(c)}  # to do := {<X, c> | c E C and X E scope(c)}
    while todo:  # while to do is not empty:
        x, c = todo.pop()  # select and remove path <X, c> from to do
        new_domain = set()
        ys = scope(c) - {x}  # {X, Y1, ..., Yk} - {X} -> {Y1, ..., Yk} (suppose scope of c is {X, Y1,..., Yk })
        for xval in csp.var_domains[x]:
            assignment = {x: xval}  # x E Dx
            for yval in itertools.product(*[csp.var_domains[y] for y in ys]):  # exists y1 E DY1 ,. . . , yk E DYk
                assignment.update(dict(zip(ys, yval)))
                if satisfies(assignment, c):  # s.th. c(X = x, Y1 = y1,..., Yk = yk )  = true
                    new_domain.add(xval)  # x
                    break
        if csp.var_domains[x] != new_domain:  # if NDX != DX :
            for c_prime in set(csp.constraints - {c}):
                if x in scope(c_prime):  # X E scope(c')
                    for z in scope(c_prime):  # Z E scope(c')
                        if x != z:  # / {X}
                            todo.add((z, c_prime))  # to do U <Z, c'>
            csp.var_domains[x] = new_domain  # DX := NDX
    return csp
