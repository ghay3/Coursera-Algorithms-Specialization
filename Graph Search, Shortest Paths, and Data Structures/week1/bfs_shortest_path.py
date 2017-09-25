from collections import deque
import math


def shortest_path(graph, source):
    visited = {v: v == source for v in graph.keys()}
    dist = {v: 0 if v == source else math.inf for v in graph.keys()}
    path = {source: None}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                dist[w] = dist[v] + 1
                path[w] = v
                queue.append(w)
    return dist, path


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Breadth-first-tree.svg
    g = {
        1: [2, 3, 4],
        2: [1, 5, 6],
        3: [],
        4: [1, 7, 8],
        5: [2, 9, 10],
        6: [],
        7: [4, 11, 12],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    }
    dist, path = shortest_path(g, 1)
    print(dist)
    print(path)
