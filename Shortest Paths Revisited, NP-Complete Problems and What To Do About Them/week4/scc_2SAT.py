def two_sat(n, clauses):
    """
    :param n: variable number
    :param clauses:
    a list of clause, each clause is represented by a 4-item tuple (idx1, negate?, idx2, negate?)
    "negate?" is either 0 or 1. For example, (2, 0, 5, 1) stands for  "v2 or (not v5)"
    index range is 1 ~ n
    :return: A list of variable values or None if not satisfiable
    """

    # build implication graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
        graph[-i] = []

    for clause in clauses:
        idx1, neg1, idx2, neg2 = clause
        var1 = -idx1 if neg1 else idx1
        var2 = -idx2 if neg2 else idx2
        graph[-var1].append(var2)
        graph[-var2].append(var1)

    # compute scc
    v2scc, cnt = strong_connected_component(graph)

    # check contradiction for vi and ~vi in same scc
    for i in range(1, n + 1):
        if v2scc[i] == v2scc[-i]:
            return None
    return True
    # construct solution
    vars = [None for _ in range(n + 1)]

    scc2v_set = {i: set() for i in range(1, cnt + 1)}
    for v, scc in v2scc.items():
        scc2v_set[scc].add(v)

    for scc in range(1, cnt + 1):
        for v in scc2v_set[scc]:
            idx, val = abs(v), v > 0
            if vars[idx] is None:
                vars[idx] = val

    return vars[1:]


def strong_connected_component(graph):
    r = reversed_graph(graph)
    order = get_dfs_reverse_post_order(r)

    v2scc, cnt = {}, 0
    visited = {v: False for v in graph}
    for v in order:
        if not visited[v]:
            cnt += 1
            dfs(v, graph, visited, lambda v: v2scc.setdefault(v, cnt))

    return v2scc, cnt


def dfs(source, graph, visited, post_func):
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
            dfs(v, graph, visited, lambda v: order.insert(0, v))
    return order


def reversed_graph(graph):
    r = {v: [] for v in graph.keys()}
    for v, others in graph.items():
        for w in others:
            r[w].append(v)
    return r


if __name__ == '__main__':
    # example:  (x1 v x2) ^ (~x1 v x3) ^ (x3 v x4) ^ (~x2 v ~x4)
    clauses = [
        (1, 0, 2, 0),
        (1, 1, 3, 0),
        (3, 0, 4, 0),
        (2, 1, 4, 1)
    ]
    result = two_sat(4, clauses)
    print(result)


