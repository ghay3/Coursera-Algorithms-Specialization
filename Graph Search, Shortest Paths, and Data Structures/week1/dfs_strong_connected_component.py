def strong_connected_component(graph):
    r = reversed_graph(graph)
    order = get_dfs_reverse_post_order(r)

    v2scc, cnt = {}, 0
    visited = {v: False for v in graph}
    for v in order:
        if not visited[v]:
            cnt += 1
            dfs2(v, graph, visited, lambda v: v2scc.setdefault(v, cnt))

    return v2scc, cnt


def dfs(v, graph, visited, post_func):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited, post_func)
    post_func(v)


def dfs2(source, graph, visited, post_func):
    stack = [source]
    while stack:
        for w in graph[stack[-1]]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)
                break
        else:
            v = stack.pop()
            post_func(v)


def get_dfs_reverse_post_order(graph):
    visited = {v: False for v in graph.keys()}
    order = []

    for v in graph.keys():
        if not visited[v]:
            dfs2(v, graph, visited, lambda v: order.insert(0, v))
    return order


def reversed_graph(graph):
    r = {v: [] for v in graph.keys()}
    for v, others in graph.items():
        for w in others:
            r[w].append(v)
    return r


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Scc.png
    g = {
        'a': ['b'],
        'b': ['c', 'e', 'f'],
        'c': ['d', 'g'],
        'd': ['c', 'h'],
        'e': ['a', 'f'],
        'f': ['g'],
        'g': ['f'],
        'h': ['d', 'h']
    }
    v2scc, cnt = strong_connected_component(g)
    print(v2scc)
    print(cnt)