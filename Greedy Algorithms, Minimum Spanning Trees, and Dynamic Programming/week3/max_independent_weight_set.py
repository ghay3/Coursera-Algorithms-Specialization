def max_independent_weight_set(weights):
    weights = [0] + weights
    wis = [0] * len(weights)
    wis[1] = weights[1]
    for i in range(2, len(weights)):
        if wis[i - 2] + weights[i] >= wis[i-1]:
            wis[i] = wis[i - 2] + weights[i]
        else:
            wis[i] = wis[i - 1]

    # reconstruct
    indices = []
    i = len(wis) - 1
    while i >= 1:
        if i == 1 or wis[i - 2] + weights[i] >= wis[i - 1]:
            indices.append(i)
            i -= 2
        else:
            i -= 1
    indices = [i - 1 for i in indices]

    return wis[-1], indices


if __name__ == '__main__':
    weights = [1, 4, 5, 4]
    max_weight, indices = max_independent_weight_set(weights)
    print(max_weight, indices)

    with open('t1.txt') as f:
        weights = [int(line.strip()) for line in f.readlines()]
        max_weight, indices = max_independent_weight_set(weights)
        print('weight:', max_weight)
        idx_set = set([i + 1 for i in indices])
        print(idx_set)
        to_check = [1, 2, 3, 4, 17, 117, 517, 997]
        print(''.join([str(int(i in idx_set)) for i in to_check]))