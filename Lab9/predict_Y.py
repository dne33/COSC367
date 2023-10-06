from numbers import Number
'''
X1  X2  X3  Y
T   T   F   F
T   F   F   F
T   T   F   F
T   F   F   T
F   F   F   T
F   T   F   T
F   F   F   F
'''

network = {
    'Y': {
        'Parents': [],
        'CPT': {
            # Note: domain(y) = set of outcomes in Y (True & False) |domain(y)| = length(domain(y))
            # (count(Y=True) + pseudocount) / (count(Y) + pseudocount * |domain(Y)|)
            (): (4+2)/(7 + 2*2),
        }
    },
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            # P(X1=True | Y=True)
            # (count(X1=True&Y=True) + pseudocount) / (count(Y=True) + pseudocount * |domain(X1)|)
            (True,): (1+2) / (4 + 2*2),
            # P(X1=True | Y=False)
            # (count(X1=True&Y=False) + pseudocount) / (count(Y=False) + pseudocount * |domain(X1)|)
            (False,): (3+2) / (3 + 2*2),
        }
    },
    'X2': {
        'Parents': ['Y'],
        'CPT': {
            # P(X2=True | Y=True)
            # (count(X2=True&Y=True) + pseudocount) / (count(Y=True) + pseudocount * |domain(X2)|)
            (True,): (1+2)/(4+2*2),
            # P(X2=True | Y=False)
            # (count(X2=True&Y=False) + pseudocount) / (count(Y=False) + pseudocount * |domain(X2)|)
            (False,): (2+2)/(3+2*2),
        }
    },
    'X3': {
        'Parents': ['Y'],
        'CPT': {
            # P(X3=True | Y=True)
            # (count(X3=True&Y=True) + pseudocount) / (count(Y=True) + pseudocount * |domain(X3)|)
            (True,): (0+2) / (4 + 2*2),
            # P(X3=True | Y=False)
            # (count(X3=True&Y=False) + pseudocount) / (count(Y=False) + pseudocount * |domain(X3)|)
            (False,): (0+2) / (3 + 2*2),
        }
    },
}
# Checking the overall type-correctness of the network
# without checking anything question-specific

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")
