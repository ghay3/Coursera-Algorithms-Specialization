def minimum_spanning_tree(graph):
    pq = PriorityQueue()
    edges = set()
    v2edge = {}
    v_remain = set(graph.keys())

    def eat_vertex(v):
        v_remain.remove(v)
        for u, w, weight in graph[v]:
            other = u if w == v else w
            if other in v_remain:
                if pq.has_item(other):
                    old_weight = pq.delete_item(other)[0]
                    pq.add(key=min(weight, old_weight), item=other)
                    if weight < old_weight:
                        v2edge[other] = (v, other, weight)
                else:
                    pq.add(key=weight, item=other)
                    v2edge[other] = (v, other, weight)

    eat_vertex(list(graph.keys())[0])
    while v_remain:
        weight, other = pq.delete_min()
        edges.add(v2edge[other])
        eat_vertex(other)

    return edges


class PriorityQueue:
    """A minimum priority queue based on heap, accepte (key, item) and supports delete item, item should be hashable."""
    def __init__(self):
        self.records = [None]
        self.cnt = 0
        self.item2index = {}

    def swim(self, k):
        while k > 1 and self.records[k][0] < self.records[k//2][0]:
            self.swap(k, k//2)
            k //= 2

    def sink(self, k):
        while k*2 <= self.cnt:
            j = k*2
            if j < self.cnt and self.records[j][0] > self.records[j+1][0]:
                j += 1

            if self.records[k][0] > self.records[j][0]:
                self.swap(k, j)
                k = j
            else:
                break

    def swap(self, k, j):
        self.item2index[self.records[k][1]] = j
        self.item2index[self.records[j][1]] = k
        self.records[k], self.records[j] = self.records[j], self.records[k]

    def add(self, key, item):
        self.records.append((key, item))
        self.cnt += 1
        self.item2index[item] = self.cnt
        self.swim(self.cnt)

    def delete_min(self):
        record = self.records[1]
        return self.delete_item(record[1])

    def delete_item(self, item):
        index = self.item2index[item]
        record = self.records[index]
        del self.item2index[item]

        if self.cnt == 1 or index == self.cnt:
            self.records.pop()
            self.cnt -= 1
        else:
            last_record = self.records.pop()
            self.records[index] = last_record
            self.item2index[last_record[1]] = index
            self.cnt -= 1
            self.swim(index)
            self.sink(index)

        return record

    def has_item(self, item):
        return item in self.item2index

    def is_empty(self):
        return self.cnt == 0


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


