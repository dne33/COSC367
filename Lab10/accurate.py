def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        a = sum([weights[i] * input[i] for i in range(len(input))]) + bias
        return 1 if a >= 0 else 0
    return perceptron  # this line is fine

def accuracy(classifier, inputs, expected_outputs):
    return sum([classifier(inputs[i]) == expected_outputs[i] for i in range(len(inputs))])/len(inputs)
if __name__ == "__main__":
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))