import csv
def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    spam_list = [int(x[-1]) for x in training_examples[1:]]
    spam_len = len(spam_list)
    spam_true = sum(spam_list)
    spam_false = spam_len - spam_true
    prob_count = [[0,0], [0,0], [0,0],[0,0], [0,0],[0,0],[0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    for x in training_examples[1:]:
        for i, result in enumerate(x[:-1]):
            if int(result):
                prob_count[i][int(x[-1])] += 1
    return [(((x+pseudo_count)/(spam_false+pseudo_count*2)),((y+pseudo_count)/(spam_true+pseudo_count*2))) for [x,y] in prob_count]


likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood) == 12)
print([len(item) for item in likelihood] == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]) == "P(X1=True | Spam=False) = 0.35570")
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]) == "P(X1=False| Spam=False) = 0.64430")
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]) == "P(X1=True | Spam=True ) = 0.66667")
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]) == "P(X1=False| Spam=True ) = 0.33333")

likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]) == "P(X1=True | Spam=False) = 0.35762")
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]) == "P(X1=False| Spam=False) = 0.64238")
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]) == "P(X1=True | Spam=True ) = 0.66038")
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]) == "P(X1=False| Spam=True ) = 0.33962")