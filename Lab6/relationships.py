from csp import Relation

# csp = CSP(
#    var_domains = {var:{0,1,2} for var in 'abcd'},
#    constraints = {
#       lambda a, b, c: a > b + c,
#       lambda c, d: c > d
#       }
#    )
relationsFirst = [
    Relation(
        header=['a', 'b', 'c'],
        tuples={(1, 0, 0), (2, 0, 0), (2, 0, 1), (2, 1, 0)}
    ),
    Relation(
        header=['c', 'd'],
        tuples={(1, 0), (2, 0), (2, 1)}
    )
]
# csp = CSP(
#    var_domains = {var:{-1,0,1} for var in 'abcd'},
#    constraints = {
#       lambda a, b: a == abs(b),
#       lambda c, d: c > d,
#       lambda a, b, c: a * b > c + 1
#       }
#    )

relations = [

    Relation(
        header=['a', 'b'],
        tuples={(0, 0), (1, 1), (1, -1)}
    ),
    Relation(
        header=['c', 'd'],
        tuples={(0, -1), (1, -1), (1, 0)}
    ),
    Relation(
        header=['a', 'b', 'c'],
        tuples={(1, 1, -1), (-1, -1, -1)}
    )

]

relations_after_elimination = [
    Relation(
        header=['c', 'd'],
        tuples={(0, -1), (1, -1), (1, 0)}
    ),
    Relation(
        header=['b', 'c'],
        tuples={(1, -1)}
    )
]
