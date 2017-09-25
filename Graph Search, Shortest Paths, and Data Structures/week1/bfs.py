from collections import deque


def bfs(graph, source, func):
    visited = {v: v == source for v in graph.keys()}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        func(v)
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


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
    trace = []
    bfs(g, 1, lambda v: trace.append(v))
    assert trace == list(range(1, 13))
