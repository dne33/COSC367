import csv

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    spam_list = [int(x[-1]) for x in training_examples[1:]]
    # (count(spam=True) + pseudocount) / (count(spam) + pseudocount * |domain(spam)|)
    return (sum(spam_list)+pseudo_count)/(len(spam_list)+pseudo_count*len(set(spam_list)))
if __name__ == "__main__":
    prior = learn_prior("spam-labelled.csv")
    print(prior==0.255)

    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    print(format(prior, ".5f") == "0.25743")

    prior = learn_prior("spam-labelled.csv", pseudo_count=2)
    print(format(prior, ".5f") == "0.25980")

    prior = learn_prior("spam-labelled.csv", pseudo_count=10)
    print(format(prior, ".5f") == "0.27727")

    prior = learn_prior("spam-labelled.csv", pseudo_count=100)
    print(format(prior, ".5f") == "0.37750")

    prior = learn_prior("spam-labelled.csv", pseudo_count=1000)
    print(format(prior, ".5f") == "0.47773")

