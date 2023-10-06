def posterior(prior, likelihood, observation):
    class_true = prior
    class_false = 1-prior
    for i, observed in enumerate(observation):
        class_true *= abs((not observed) - likelihood[i][True])
        class_false *= abs((not observed) - likelihood[i][False])
    normal = class_true + class_false
    return class_true/normal

def test():
    # Test 0
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, True, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true) == "P(C=False|observation) is approximately 0.00248")
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true) == "P(C=True |observation) is approximately 0.99752")

    # Test 1
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true) == "P(C=False|observation) is approximately 0.29845")
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true) == "P(C=True |observation) is approximately 0.70155")

    # Test 2
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true) == "P(C=False|observation) is approximately 0.99454")
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true) == "P(C=True |observation) is approximately 0.00546")

    # Test 3
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, False)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true) == "P(C=False|observation) is approximately 0.99987")
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true) == "P(C=True |observation) is approximately 0.00013")
if __name__ == "__main__":
    test()