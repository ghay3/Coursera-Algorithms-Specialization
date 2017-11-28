import math


def shortest_path(graph, source):
    v2dist = {v: 0 if v == source else math.inf for v in graph.keys()}

    for i in range(len(v2dist)):
        for v, edges in graph.items():
            for u, w in edges:
                if v2dist[u] > v2dist[v] + w:
                    v2dist[u] = v2dist[v] + w

    # check negative cycle
    for v, edges in graph.items():
        for u, w in edges:
            if v2dist[u] > v2dist[v] + w:
                return False, None

    return True, v2dist


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
    has_result, v2dist = shortest_path(g, 1)
    print(has_result, v2dist)

