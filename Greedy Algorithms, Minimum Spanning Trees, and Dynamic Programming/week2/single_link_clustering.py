def get_cluster(graph, k):
    import itertools
    vetices = list(graph.keys())
    all_edges = sorted(itertools.chain.from_iterable(graph.values()), key=lambda x: x[2])

    v2uid = {v: uid for v, uid in zip(vetices, range(len(vetices)))}
    uf = UnionFind(len(vetices))

    chosen_edges = set()
    for v1, v2, weight in all_edges:
        uid1, uid2 = v2uid[v1], v2uid[v2]
        if not uf.is_connected(uid1, uid2):
            chosen_edges.add((v1, v2, weight))
            uf.connect(uid1, uid2)
            if uf.cnt == k:
                break

    max_margin = 0
    for v1, v2, weight in all_edges:
        uid1, uid2 = v2uid[v1], v2uid[v2]
        if not uf.is_connected(uid1, uid2):
            max_margin = weight
            break

    return chosen_edges, max_margin


class UnionFind:
    def __init__(self, n):
        self._index = list(range(n))
        self._size = [1 for _ in range(n)]
        self.cnt = n

    def is_connected(self, v, w):
        return self.root(v) == self.root(w)

    def root(self, v):
        while self._index[v] != v:
            self._index[v] = self._index[self._index[v]]
            v = self._index[v]
        return v

    def connect(self, v, w):
        vroot, wroot = self.root(v), self.root(w)
        if vroot != wroot:
            if self._size[vroot] < self._size[wroot]:
                self._index[vroot] = wroot
                self._size[wroot] += self._size[vroot]
            else:
                self._index[wroot] = vroot
                self._size[vroot] += self._size[wroot]
            self.cnt -= 1