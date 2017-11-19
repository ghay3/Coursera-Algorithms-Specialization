import math


def shortest_path(graph):
    # get mapping key <-> idx
    idx2key = dict(enumerate(graph.keys()))
    key2idx = {key: idx for idx, key in idx2key.items()}

    # convert adjacent list to matrix with shortest edge
    n = len(key2idx)
    m = [[None for _ in range(n)] for _ in range(n)]
    for key_v, edges in graph.items():
        v = key2idx[key_v]
        for key_u, w in edges:
            u = key2idx[key_u]
            if m[v][u] is None or m[v][u] > w:
                m[v][u] = w

    dp = [[[math.inf for _ in range(n)] for _ in range(n)] for _ in range(n)]
    # base case when k = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j][0] = 0
            elif m[i][j]:
                dp[i][j][0] = m[i][j]

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                dp[i][j][k] = min(dp[i][j][k-1], dp[i][k][k-1] + dp[k][j][k-1])

    has_negative_cycle = any([dp[i][i][n-1] < 0 for i in range(n)])
    result = {
        key: {idx2key[i]: dp[idx][i][n-1] for i in range(n)}
        for key, idx in key2idx.items()}

    return not has_negative_cycle, result


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Dijkstra_Animation.gif
    g = {
        1: [(2, 7), (3, 9), (6, 14)],
        2: [(1, 7), (3, 10), (4, 15)],
        3: [(1, 9), (2, 10), (4, 11), (6, 2)],
        4: [(2, 15), (3, 11), (5, 6)],
        5: [(4, 6), (6, 9)],
        6: [(1, 14), (3, 2), (5, 9)]
    }
    has_result, result = shortest_path(g)
    print(has_result, result)