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

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    spam_list = [int(x[-1]) for x in training_examples[1:]]
    return (sum(spam_list)+pseudo_count)/(len(spam_list)+pseudo_count*len(set(spam_list)))

def posterior(prior, likelihood, observation):
    class_true = prior
    class_false = 1-prior
    for i, observed in enumerate(observation):
        class_true *= abs((not observed) - likelihood[i][True])
        class_false *= abs((not observed) - likelihood[i][False])
    normal = class_true + class_false
    return class_true/normal
def nb_classify(prior, likelihood, input_vector):
    prediction = posterior(prior, likelihood, input_vector)
    return ('Spam', prediction) if prediction >= 0.5 else ('Not Spam', 1-prediction)

prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector)
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector)
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))