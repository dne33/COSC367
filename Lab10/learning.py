def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        a = sum([weights[i] * input[i] for i in range(len(input))]) + bias
        return 1 if a >= 0 else 0

    return perceptron  # this line is fine


def update_weight_bias(weights, bias, training_example, learning_rate):
    perceptron = construct_perceptron(weights, bias)
    factor = learning_rate * (training_example[1] - perceptron(training_example[0]))
    percept_weight = [x * factor for x in training_example[0]]
    new_weight = [weights[i] + percept_weight[i] for i in range(len(weights))]
    new_bias = bias + factor
    return new_weight, new_bias


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    i = 0
    correct_values = False
    while i <= max_epochs and not correct_values:
        epoch_weight = weights
        epoch_bias = bias
        for training_example in training_examples:
            perceptron = construct_perceptron(weights, bias)
            if perceptron(training_example[0]) != training_example[1]:
                new_weight, new_bias = update_weight_bias(weights, bias, training_example, learning_rate)
                weights = new_weight
                bias = new_bias
        i += 1
        correct_values = (epoch_bias == bias and epoch_weight == weights)
    return tuple(weights), bias

if __name__ == "__main__":
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 0),
        ((1, 0), 0),
        ((1, 1), 1),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")

    perceptron = construct_perceptron(weights, bias)

    print(perceptron((0, 0)))
    print(perceptron((0, 1)))
    print(perceptron((1, 0)))
    print(perceptron((1, 1)))
    print(perceptron((2, 2)))
    print(perceptron((-3, -3)))
    print(perceptron((3, -1)))

    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 1), 0),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")