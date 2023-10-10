weights = [-0.5, 0.5]
bias = -0.5
learning_rate = 0.5

examples = [
    ([1, 1],   0),    # index 0 (first example)
    ([2, 0],   1),
    ([1, -1],  0),
    ([-1, -1], 1),
    ([-2, 0],  0),
    ([-1, 1],  1),
]

'''
Consider a binary classification problem (i.e. there are two classes in the domain) 
where each object is represented by 2 numeric values (2 features). We are using a single perceptron as a classifier 
for this domain and want to learn its parameters. The weight update rule is w←w+ηx(t−y).

Weight <- Weight + learning_rate * example_val * (target - perceptron_out)
Bias <- Bias + learning_rate * (target - perceptron_out)
'''

# Answer the following with numeric values. Do not use fractions.
'''
Weight = Weight + learning_rate * example_val * (target - perceptron_out)
       = [-0.5, 0.5] + 0.5 * [1, 1] * (0 - 0)
       = [-0.5, 0.5] + [0, 0]
       = -0.5, 0.5]
Bias = Bias + learning_rate * (target - perceptron_out)
     = -0.5 + 0.5 * (0-0)
     = -0.5
After seeing the example at index 0, the value of the weight vector is [-0.5, 0.5] and the value of bias is -0.5
'''

'''
Weight = Weight + learning_rate * example_val * (target - perceptron_out)
       = [-0.5, 0.5] + 0.5 * [2, 0] * (1 - 0)
       = [-0.5, 0.5] + [1, 0]
       = [0.5, 0.5]
Bias = Bias + learning_rate * (target - perceptron_out)
     = -0.5 + 0.5 * (1-0)
     = 0
After seeing the example at index 1, the value of the weight vector is [0.5, 0.5] and the value of bias is 0
'''

'''
Weight = Weight + learning_rate * example_val * (target - perceptron_out)
       = [0.5, 0.5] + 0.5 * [1, -1] * (0 - 1)
       = [0.5, 0.5] + [-0.5, 0.5]
       = [0, 1]
Bias = Bias + learning_rate * (target - perceptron_out)
     = 0 + 0.5 * (0-1)
     = -0.5
After seeing the example at index 2, the value of the weight vector is [0, 1] and the value of bias is -0.5
'''