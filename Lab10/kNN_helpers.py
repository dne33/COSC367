import math
from collections import Counter


def euclidean_distance(v1, v2):
    return math.sqrt(sum([(v1[i] - v2[i]) ** 2 for i in range(len(v1))]))


def majority_element(labels):
    return Counter(labels).most_common(1)[0][0]


if __name__ == "__main__":
    print(euclidean_distance([0, 3, 1, -3, 4.5], [-2.1, 1, 8, 1, 1]) == 9.25526876973327)
    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]) == 0)
    print(majority_element("ababc") in "ab")
