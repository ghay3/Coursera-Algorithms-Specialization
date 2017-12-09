import math


def knapsack(cap, values, weights):
    """O(n^2 * vmax) for integer values knapsack"""
    n = len(weights)
    vmax = max(values)

    # pad index
    weights = [None] + weights
    values = [None] + values

    dp = [[math.inf for _ in range(n * vmax)] for _ in range(n + 1)]

    # base case
    dp[0][0] = 0

    # solve dp
    for i in range(1, n + 1):
        for x in range(n * vmax):
            dp[i][x] = min(dp[i-1][x], weights[i] + dp[i-1][x-values[i]])

    x = n * vmax - 1
    while dp[n][x] > cap:
        x -= 1

    return x


def heuristic(cap, values, weights, epsilon=0.2):
    """heuristicly find a solution with value at least (1-epsilon) optimal solution"""
    n = len(values)
    vmax = max(values)

    m = epsilon * vmax / n
    values = [int(v // m) for v in values]

    return knapsack(cap, values, weights) * m


if __name__ == '__main__':
    import random

    v = [3, 2, 4, 4]
    w = [4, 3, 2, 3]
    print(knapsack(6, v, w))

    v = [random.randint(1, 1000) for _ in range(100)]
    w = [random.randint(1, 1000) for _ in range(100)]
    cap = 400
    exact_result = knapsack(cap, v, w)
    rough_result = heuristic(cap, v, w)
    ratio = rough_result / exact_result
    print('exact: {}, rough: {}, ratio: {}'.format(exact_result, rough_result, ratio))
