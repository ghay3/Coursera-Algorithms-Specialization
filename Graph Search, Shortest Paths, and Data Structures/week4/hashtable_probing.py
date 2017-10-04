import abc


class ProbeStrategy(abc.ABC):
    @abc.abstractmethod
    def get_sequence(self, key, n):
        return []


class LinearProbing(ProbeStrategy):
    def get_sequence(self, key, n):
        start = hash(key)
        i = 0
        while True:
            yield (start + i) % n
            i += 1


class QuadraticProbing(ProbeStrategy):
    def get_sequence(self, key, n):
        start = hash(key)
        i = 0
        while True:
            yield (start + i ** 2) % n
            i += 1


class DoubleHashing(ProbeStrategy):
    def get_sequence(self, key, n):
        start = hash(key)
        offset = (hash(key) * 701) % 997  # a dirty one here
        i = 0
        while True:
            yield (start + i * offset) % n
            i += 1


class HashTable:

    def __init__(self, n=997, prob_strategy: ProbeStrategy=DoubleHashing()):
        self.n = n
        self.prob_strategy = prob_strategy
        self.slots = [None for _ in range(n)]

    def get(self, key):
        for idx in self.prob_strategy.get_sequence(key, self.n):
            if self.slots[idx] is None:
                return None
            else:
                k, v = self.slots[idx]
                if k == key:
                    return v

    def set(self, key, val):
        for idx in self.prob_strategy.get_sequence(key, self.n):
            if self.slots[idx] is None or self.slots[idx][0] == key:
                self.slots[idx] = (key, val)
                break

    def delete(self, key):
        after_delete = False
        for idx in self.prob_strategy.get_sequence(key, self.n):
            if self.slots[idx] is None:
                break
            elif after_delete:
                k, v = self.slots[idx]
                self.slots[idx] = None
                self.set(k, v)
            else:
                k, v = self.slots[idx]
                if k == key:
                    self.slots[idx] = None
                    after_delete = True


if __name__ == '__main__':
    import random
    random.seed(1)

    lp = HashTable(prob_strategy=LinearProbing())
    qp = HashTable(prob_strategy=QuadraticProbing())
    dh = HashTable(prob_strategy=DoubleHashing())
    dt = dict()
    for _ in range(200):
        key, val = random.randint(-1000, 1000), random.randint(-1000, 1000)
        lp.set(key, val)
        qp.set(key, val)
        dh.set(key, val)
        dt[key] = val
        if random.randint(0, 1):
            lp.delete(key)
            qp.delete(key)
            dh.delete(key)
            del dt[key]

    for k, v in dt.items():
        assert lp.get(k) == v
        assert qp.get(k) == v
        assert dh.get(k) == v
