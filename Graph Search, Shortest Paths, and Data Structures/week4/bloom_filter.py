class BloomFilter:

    def __init__(self, n, b, hash_funcs):
        self.n = n
        self.b = b
        self.hash_funcs = hash_funcs
        self.bits = [False for _ in range(n*b)]

    def add(self, key):
        for hash_func in self.hash_funcs:
            self.bits[hash_func(key, len(self.bits))] = True

    def has(self, key):
        return all([self.bits[hash_func(key, len(self.bits))] for hash_func in self.hash_funcs])


if __name__ == '__main__':
    import random

    k = 32
    hash_funcs = [lambda obj, length: (hash(str(obj) + s) % length)
                  for s in ['hash' + str(i) for i in range(32)]]
    bf = BloomFilter(100, 16, hash_funcs)
    st = set()
    for _ in range(100):
        num = random.randint(-1000, 1000)
        bf.add(num)
        st.add(num)

    assert all([bf.has(key) for key in st])