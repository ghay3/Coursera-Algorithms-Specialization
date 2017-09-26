def topological_sort(graph):
    visited = {v: False for v in graph.keys()}
    order = []

    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs(w)
        order.insert(0, v)

    for v in graph.keys():
        if not visited[v]:
            dfs(v)
    return order


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Directed_acyclic_graph_2.svg
    g = {
        2: [],
        3: [8, 10],
        5: [11],
        7: [8, 11],
        8: [9],
        9: [],
        10: [],
        11: [2, 9, 10],
    }
    order = topological_sort(g)
    print(order)
