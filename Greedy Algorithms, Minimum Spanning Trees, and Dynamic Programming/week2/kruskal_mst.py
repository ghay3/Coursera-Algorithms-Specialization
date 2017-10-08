def minimum_spanning_tree(graph):
    import itertools
    vetices = list(graph.keys())
    v2uid = {v: uid for v, uid in zip(vetices, range(len(vetices)))}
    uf = UnionFind(len(vetices))
    edges = set()
    for v1, v2, weight in sorted(itertools.chain.from_iterable(graph.values()), key=lambda x: x[2]):
        uid1, uid2 = v2uid[v1], v2uid[v2]
        if not uf.is_connected(uid1, uid2):
            edges.add((v1, v2, weight))
            uf.connect(uid1, uid2)
            if uf.cnt == 1:
                break
    return edges


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


if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/File:Multiple_minimum_spanning_trees.svg
    g = {
        'a': [
            ('a', 'b', 1),
            ('a', 'd', 4),
            ('a', 'e', 3)
        ],
        'b': [
            ('a', 'b', 1),
            ('b', 'd', 4),
            ('b', 'e', 2)
        ],
        'c': [
            ('c', 'e', 4),
            ('c', 'f', 5)
        ],
        'd': [
            ('d', 'a', 4),
            ('d', 'e', 4),
            ('d', 'b', 4)
        ],
        'e': [
            ('a', 'e', 3),
            ('b', 'e', 2),
            ('c', 'e', 4),
            ('d', 'e', 4),
            ('f', 'e', 7)
        ],
        'f': [
            ('c', 'f', 5),
            ('e', 'f', 7)
        ]
    }
    print(minimum_spanning_tree(g))