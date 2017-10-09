class UnionFind:
    def __init__(self, n, merge_method='by_size'):
        self.index = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.cnt = n
        self.merge = eval('self.' + merge_method)

    def is_connected(self, v, w):
        return self.root(v) == self.root(w)

    def root(self, v):
        while self.index[v] != v:
            self.index[v] = self.index[self.index[v]]
            v = self.index[v]
        return v

    def connect(self, v, w):
        vroot, wroot = self.root(v), self.root(w)
        if vroot != wroot:
            self.merge(vroot, wroot)
            self.cnt -= 1

    def by_size(self, vroot, wroot):
        if self.rank[vroot] < self.rank[wroot]:
            self.index[vroot] = wroot
            self.rank[wroot] += self.rank[vroot]
        else:
            self.index[wroot] = vroot
            self.rank[vroot] += self.rank[wroot]

    def by_height(self, vroot, wroot):
        if self.rank[vroot] < self.rank[wroot]:
            self.index[vroot] = wroot
        elif self.rank[vroot] > self.rank[wroot]:
            self.index[wroot] = vroot
        else:
            self.index[wroot] = vroot
            self.rank[vroot] += 1


if __name__ == '__main__':
    # 0 + https://en.wikipedia.org/wiki/File:Dsu_disjoint_sets_final.svg
    uf = UnionFind(9, 'by_height')
    uf.connect(1, 2)
    uf.connect(2, 5)
    uf.connect(5, 6)
    uf.connect(6, 8)
    uf.connect(3, 4)
    assert (uf.is_connected(1, 2))
    assert (uf.is_connected(1, 5))
    assert (uf.is_connected(1, 6))
    assert (uf.is_connected(1, 8))
    assert (uf.is_connected(3, 4))
    assert (uf.cnt == 4)