import itertools
import math
from collections import defaultdict


def traveling_salesman(matrix):
    nodes = set(range(len(matrix)))

    def subset2num(subset, exclude=None):
        return sum(1 << v for v in subset) - (0 if exclude is None else 1 << exclude)

    # choose a vertex as virtual source
    vs = 0
    rest_nodes = nodes - {vs}

    dp = defaultdict(lambda: math.inf)
    # base case for subset size = 1
    dp[(subset2num({vs}), vs)] = 0

    # solve dp
    for m in range(2, len(nodes) + 1):
        print(m)
        last_dp = dp
        dp = defaultdict(lambda: math.inf)
        for sub in itertools.combinations(rest_nodes, m - 1):
            for j in sub:
                num = subset2num(sub) + 1
                dp[(num, j)] = min(last_dp[(subset2num(sub, exclude=j) + 1, k)] + matrix[k][j]
                                   for k in itertools.chain([vs], sub) if k != j and matrix[k][j])

    return min(dp[(subset2num(nodes), j)] + matrix[j][vs] for j in rest_nodes if matrix[j][vs])


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Weighted_K4.svg
    matrix = [
        [None, 20, 42, 35],
        [20, None, 30, 34],
        [42, 30, None, 12],
        [35, 34, 12, None]
    ]
    result = traveling_salesman(matrix)
    print(result)
