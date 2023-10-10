import math
from collections import Counter


def euclidean_distance(v1, v2):
    return math.sqrt(sum([(v1[i] - v2[i]) ** 2 for i in range(len(v1))]))


def majority_element(labels):
    return Counter(labels).most_common(1)[0][0]

def knn_predict(input, examples, distance, combine, k):
    neighbour_label = []
    curr_distance = -1
    consider = examples[:]
    consider.sort(key=lambda x: distance(input, x[0]))
    for example in consider:
        euc = distance(input, example[0])
        if len(neighbour_label) < k or euc == curr_distance:
            curr_distance = euc
            neighbour_label.append(example[1])
    return combine(neighbour_label)

if __name__ == "__main__":
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()
    # using knn for predicting numeric values

    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]


    def average(values):
        return sum(values) / len(values)


    distance = euclidean_distance
    combine = average

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()