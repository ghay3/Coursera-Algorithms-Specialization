class PriorityQueue:
    """A minimum priority queue based on heap, accepte (key, item) and supports delete item, item should be hashable."""
    def __init__(self, records=None):
        if not records:
            self.records = [None]
            self.cnt = 0
            self.item2index = {}
        else:
            self.records = [None] + records
            self.cnt = len(records)
            self.item2index = {item: index + 1 for index, (key, item) in enumerate(records)}
            # heapify
            for k in range(self.cnt//2, 0, -1):
                self.sink(k)

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
    import random

    for _ in range(100):
        nums = list(range(100))
        random.shuffle(nums)

        # initialize priority queue
        records = [(num, num) for num in nums]
        pq = PriorityQueue(records)

        # delete 10 random items
        for i in range(10):
            num = random.choice(nums)
            nums.remove(num)
            pq.delete_item(num)

        algorithm_result = [pq.delete_min()[1] for _ in range(len(nums))]
        correct_result = sorted(nums)
        assert algorithm_result == correct_result

