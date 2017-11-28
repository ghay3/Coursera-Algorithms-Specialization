import math


def johnson(graph: dict):
    graph[Ellipsis] = [(k, 0) for k in graph.keys()]
    has_result, v2weight_num = bellman_ford(graph, Ellipsis)

    if not has_result:
        return False, None
    print('has result')
    result = {}
    del graph[Ellipsis]
    for u in graph.keys():
        print('computing', u)
        v2dist = dijkstra_with_reweight(graph, u, v2weight_num)
        result[u] = {v: dist - v2weight_num[u] + v2weight_num[v] for v, dist in v2dist.items()}

    return True, result


def bellman_ford(graph, source):
    v2dist = {v: 0 if v == source else math.inf for v in graph.keys()}

    for i in range(len(v2dist)):
        for v, edges in graph.items():
            for u, w in edges:
                if v2dist[u] > v2dist[v] + w:
                    v2dist[u] = v2dist[v] + w

    # check negative cycle
    for v, edges in graph.items():
        for u, w in edges:
            if v2dist[u] > v2dist[v] + w:
                return False, None

    return True, v2dist


def dijkstra_with_reweight(graph, source, v2weight_num):
    pq = PriorityQueue()
    v2dist = {}

    pq.add(key=0, item=source)
    v2dist[source] = 0
    while not pq.is_empty():
        dist, v = pq.delete_min()
        v2dist[v] = dist
        for u, edge_dist in graph[v]:
            if u not in v2dist:
                cur_dist = dist + edge_dist + v2weight_num[v] - v2weight_num[u]
                if pq.has_item(u):
                    origin_dist, _ = pq.delete_item(u)
                    pq.add(key=min(cur_dist, origin_dist), item=u)
                else:
                    pq.add(key=cur_dist, item=u)
    return v2dist


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
    # https://en.wikipedia.org/wiki/File:Dijkstra_Animation.gif
    g = {
        1: [(2, 7), (3, 9), (6, 14)],
        2: [(1, 7), (3, 10), (4, 15)],
        3: [(1, 9), (2, 10), (4, 11), (6, 2)],
        4: [(2, 15), (3, 11), (5, 6)],
        5: [(4, 6), (6, 9)],
        6: [(1, 14), (3, 2), (5, 9)]
    }
    has_result, result = johnson(g)
    print(has_result, result)

