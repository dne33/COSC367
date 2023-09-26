import random
import time


def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int or (type(object) == str and object in leaf_symbols):
        return True
    elif type(object) == list and len(object) == 3 and object[0] in function_symbols:
        return is_valid_expression(object[1], function_symbols, leaf_symbols) \
            and is_valid_expression(object[2], function_symbols, leaf_symbols)
    return False


def depth(expression):
    if type(expression) == str or type(expression) == int:
        return 0
    if type(expression) == list and len(expression) == 3:
        if 1 + depth(expression[1]) > 1 + depth(expression[2]):
            return 1 + depth(expression[1])
        else:
            return 1 + depth(expression[2])


def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str:
        return bindings[expression]
    elif type(expression) == list and len(expression) == 3:
        return (bindings[expression[0]])(evaluate(expression[1], bindings), evaluate(expression[2], bindings))


def random_expression(function_symbols, leaves, max_depth):
    if max_depth == random.randint(0, max_depth) or max_depth == 0:
        return random.choice(leaves)
    if random.choice([False, True]):
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth-1),
                    random_expression(function_symbols, leaves, max_depth-1)]

def generate_rest(initial_sequence, expression, length):
    new_list = []
    for i in range(length):
        bindings = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, 'i':len(initial_sequence), 'x':initial_sequence[-2], 'y':initial_sequence[-1]}
        evaluation = evaluate(expression, bindings)
        initial_sequence.append(evaluation)
        new_list.append(evaluation)
    return new_list

def predict_rest(sequence):
    function_symbols = ['+', '-', '*']
    leaves = list(range(-2, 3)) + ['x', 'y', 'i']
    max_depth = 3
    bindings = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, 'i': len(sequence),
                'x': 0, 'y': 0}
    used = []
    while True:
        found = True
        expression = random_expression(function_symbols, leaves, max_depth)

        for index in range(len(sequence)-2):
            bindings['x'] = sequence[index]
            bindings['y'] = sequence[index + 1]
            if evaluate(expression, bindings) != sequence[index + 2]:
                found = False
                break

        if found:
            return generate_rest(sequence.copy(), expression, 5)





from tests import *
def main():
    print_tests()



if __name__ == "__main__":
    main()
