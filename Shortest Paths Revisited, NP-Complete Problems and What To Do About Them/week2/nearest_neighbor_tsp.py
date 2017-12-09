import math


def nearest_neighbor(matrix, start):
    visited, n = {start}, len(matrix)
    distance = 0

    cur = start
    while len(visited) < n:
        min_idx, min_dist = None, math.inf
        for i in range(n):
            if i not in visited and matrix[cur][i] < min_dist:
                min_idx = i
                min_dist = matrix[cur][i]

        distance += min_dist
        cur = min_idx
        visited.add(cur)

    return distance + matrix[cur][start]
