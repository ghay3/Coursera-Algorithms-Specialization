import random
from collections import Counter, namedtuple
from copy import copy
from math import log, ceil

Edge = namedtuple('Edge', 'v1 v2')


# https://en.wikipedia.org/wiki/Karger%27s_algorithm
def karger_minimum_cut(V, E):
    n = len(V)
    return min([len(randomized_minimum_cut(V, E))
                for _ in range(n**2 * ceil(log(n)))])


def randomized_minimum_cut(V, E):
    V, E = UnionFind(len(V)), copy(E)
    while V.cnt > 2:
        e = random.choice(E)
        V, E = contract(V, E, e)
    return cut_edges(V, E)


def contract(V, E, e):
    if not V.is_connected(e.v1, e.v2):
        V.connect(e.v1, e.v2)
    return V, E


def cut_edges(V, E):
    _E = [e for e in E if not V.is_connected(e.v1, e.v2)]
    return _E


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
    # a circle
    n = 8
    V = range(n)
    E = [Edge(v1=i, v2=(i+1) % n) for i in range(n)]
    print(karger_minimum_cut(V, E))

    # https://en.wikipedia.org/wiki/File:Min_cut_example.svg
    n = 5
    V = range(n)
    E = [Edge(v1=i, v2=(i+1) % n) for i in range(n)]
    E += [Edge(1, 3), Edge(1, 4)]
    print(karger_minimum_cut(V, E))