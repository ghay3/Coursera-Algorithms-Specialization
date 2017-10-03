class HashTable:

    def __init__(self, n=997):
        self.n = n
        self.buckets = [[] for _ in range(n)]

    def get_hash(self, key):
        return hash(key) % self.n

    def get(self, key):
        for k, v in self.buckets[self.get_hash(key)]:
            if k == key:
                return v
        else:
            return None

    def set(self, key, val):
        bucket_num = self.get_hash(key)
        for idx, (k, v) in enumerate(self.buckets[bucket_num]):
            if k == key:
                self.buckets[bucket_num][idx] = (key, val)
                break
        else:
            self.buckets[bucket_num].append((key, val))

    def delete(self, key):
        bucket_num = self.get_hash(key)
        self.buckets[bucket_num].remove((key, self.get(key)))


if __name__ == '__main__':
    import random
    ht = HashTable()
    dt = dict()
    for _ in range(1000):
        key, val = random.randint(-1000, 1000), random.randint(-1000, 1000)
        ht.set(key, val)
        dt[key] = val
        if random.randint(0, 1):
            ht.delete(key)
            del dt[key]

    for k, v in dt.items():
        assert ht.get(k) == v
