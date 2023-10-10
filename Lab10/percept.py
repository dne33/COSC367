def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        a = sum([weights[i] * input[i] for i in range(len(input))]) + bias
        return 1 if a >= 0 else 0
    return perceptron  # this line is fine


if __name__ == "__main__":
    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)

    print(perceptron([1, 1]) == 0)
    print(perceptron([2, 1]) == 1)
    print(perceptron([3, 1]) == 1)
    print(perceptron([-1, -1]) == 1)
