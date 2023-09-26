from Assignment2 import *
def print_tests():
    # Comment any that you dont want to run out
    # If correct it will print true for each test case
    valid_test()
    print()
    depth_test()
    print()
    evaluate_test()
    print()
    random_test()
    print()
    rest_test()
    print()
    predict_test()
# Tests
def valid_test():
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == False)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == True)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == False)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == False)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == False)

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']
    print(is_valid_expression(expression, function_symbols, leaf_symbols) == False)


def depth_test():
    expression = 12
    print(depth(expression) == 0)
    expression = 'weight'
    print(depth(expression) == 0)
    expression = ['add', 12, 'x']
    print(depth(expression) == 1)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression) == 2)
    expression = ['add', ['add', 22, 'y'], ['add', 22, ['add', 22, 'y']]]
    print(depth(expression) == 3)


def evaluate_test():
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings) == 12)

    bindings = {'x': 5, 'y': 10, 'time': 15}
    expression = 'y'
    print(evaluate(expression, bindings) == 10)

    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings) == 17)

    import operator

    bindings = dict(x=5, y=10, blah=15, add=operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings) == 37)


def random_test():
    function_symbols = ['f', 'g', 'h']
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            print(False)
            break
    else:
        print(True)
    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]

    # Out of 10000 expressions, at least 1000 must be distinct
    seen = []
    for expression in expressions:
        if expression not in seen:
            seen.append(expression)
    print(len(seen) >= 1000)

    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                   for _ in range(10000)]

    # Out of 10000 expressions, there must be at least 100 expressions
    # of depth 0, 100 of depth 1, ..., and 100 of depth 4.


    # _check_diversity(expressions, max_depth)
    listy = [x for x in range(0, max_depth+1)]
    diction = dict()
    for x in listy:
        diction[x] = 0
    for expression in expressions:
        diction[depth(expression)] = diction[depth(expression)] + 1
    for values in diction.values():
        print(values >= 100)
def rest_test():
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [3, 4, 5, 6, 7])

    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i'
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate)==[3, 4, 5, 6])

    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [12, 14, 16, 18, 20])

    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [12, 14, 16, 18, 20])

    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [0, 1, 0, 1, 0, 1])

    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [1, 2, 3, 5, 8])

    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [367, 367, 367, 367, 367])

    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [-1, -1, -1, -1, -1])

    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate) == [])
def predict_test():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence == [0, 1, 2, 3, 4, 5, 6, 7] and the_rest == [8, 9, 10, 11, 12])

    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    the_rest = predict_rest(sequence)
    print(the_rest == [16, 18, 20, 22, 24])

    sequence = [31, 29, 27, 25, 23, 21]
    the_rest = predict_rest(sequence)
    print(the_rest == [19, 17, 15, 13, 11])

    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    the_rest = predict_rest(sequence)
    print(the_rest == [64, 81, 100, 121, 144])

    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    the_rest = predict_rest(sequence)
    print(the_rest == [51, 66, 83, 102, 123])

    sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    the_rest = predict_rest(sequence)
    print(the_rest == [21, 34, 55, 89, 144])

    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    the_rest = predict_rest(sequence)
    print(the_rest == [5, -4, 29, -13, 854])

    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    the_rest = predict_rest(sequence)
    print(the_rest == [-1055, 2547, -6149, 14845, -35839])