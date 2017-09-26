def dfs(graph, source, func):
    visited = {v: False for v in graph.keys()}

    def dfs_recur(v):
        visited[v] = True
        func(v)
        for w in graph[v]:
            if not visited[w]:
                dfs_recur(w)
    dfs_recur(source)


def dfs2(graph, source, func):
    visited = {v: v == source for v in graph.keys()}
    stack = [source]
    func(source)
    while stack:
        for w in graph[stack[-1]]:
            if not visited[w]:
                visited[w] = True
                func(w)
                stack.append(w)
                break
        else:
            stack.pop()


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Depth-first-tree.svg
    g = {
        1: [2, 7, 8],
        2: [3, 6],
        3: [4, 5],
        4: [3],
        5: [3],
        6: [],
        7: [1],
        8: [1, 9, 12],
        9: [8, 10, 11],
        10: [9],
        11: [9],
        12: [12]
    }
    trace = []
    dfs(g, 1, lambda v: trace.append(v))
    assert trace == list(range(1, 13))

    trace = []
    dfs2(g, 1, lambda v: trace.append(v))
    assert trace == list(range(1, 13))

