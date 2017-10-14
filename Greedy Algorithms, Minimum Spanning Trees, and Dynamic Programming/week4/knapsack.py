def knapsack(cap, values, weights):
    values = [0] + values
    weights = [0] + weights

    s = [[0] * (cap + 1) for _ in range(len(values))]
    for i in range(1, len(values)):
        for j in range(cap + 1):
            if weights[i] > j:
                s[i][j] = s[i - 1][j]
            else:
                s[i][j] = max(s[i - 1][j], s[i - 1][j - weights[i]] + values[i])
    return s[-1][-1]


def knapsack_recur(cap, values, weights):
    import functools

    values = [0] + values
    weights = [0] + weights

    @functools.lru_cache(maxsize=None)
    def solve(i, cap):
        if i == 0:
            return 0
        elif weights[i] > cap:
            return solve(i - 1, cap)
        else:
            return max(solve(i - 1, cap), solve(i - 1, cap - weights[i]) + values[i])

    return solve(len(values) - 1, cap)


if __name__ == '__main__':
    v = [3, 2, 4, 4]
    w = [4, 3, 2, 3]
    print(knapsack(6, v, w))
    print(knapsack_recur(6, v, w))