def max_value(tree):
    if type(tree) == int:
        return tree
    return max(min_value(i) for i in tree)


def min_value(tree):
    if type(tree) == int:
        return tree
    return min(max_value(i) for i in tree)


def max_action_value(game_tree):
    utility = max_value(game_tree)
    if type(game_tree) == int:
        return None, utility
    action, index = max((min_value(game_tree[i]), i) for i in range(len(game_tree)))
    return index, utility


def min_action_value(game_tree):
    utility = min_value(game_tree)
    if type(game_tree) == int:
        return (None, utility)
    action, index = min((max_value(game_tree[i]), i) for i in range(len(game_tree)))
    return (index, utility)


if __name__ == "__main__":
    game_tree = [2, [-3, 1], 4, 1]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    print()

    game_tree = [
        [[7, -5, 3, 1], [-5, 4, -10, 3], [-10, 6, 8, -5]],
        [[9, 2, -8, 1], [-1, -6, -10, 7], [-3, -2, -3, -2]],
        [[-5, -6, 5]],
    ]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    print()
    game_tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
